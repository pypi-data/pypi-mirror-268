"""Implementation of mcli describe run"""
from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generator, List, Optional, TypeVar

from rich.table import Table

from mcli.api.exceptions import cli_error_handler
from mcli.api.model.run import Node, Run, RunLifecycle, RunStatus
from mcli.cli.common.run_filters import get_runs_with_filters
from mcli.cli.m_get.display import MCLIDisplayItem, MCLIGetDisplay, OutputDisplay, create_vertical_display_table
from mcli.cli.m_update.m_update import get_expiration_date
from mcli.models.run_config import ComputeConfig
from mcli.utils.utils_date import format_timestamp
from mcli.utils.utils_logging import FormatString, console, format_string

logger = logging.getLogger(__name__)


# Displays
class MCLIDescribeRunDetailsDisplay(MCLIGetDisplay):
    """ Vertical table view of run details """

    def __init__(self, models: List[Run]):
        self.models = sorted(models, key=lambda x: x.created_at, reverse=True)
        self.include_reason_in_display = any(m.reason for m in models)

    @property
    def index_label(self) -> str:
        return ""

    def create_custom_table(self, data: List[Dict[str, str]]) -> Optional[Table]:
        if not self.include_reason_in_display:
            del data[0]['Reason']
        return create_vertical_display_table(data=data[0])

    def get_max_duration(self, run: Run) -> Optional[str]:
        max_duration_seconds = run.max_duration_seconds
        if max_duration_seconds is None:
            return None

        display_time = f"{max_duration_seconds} second{'' if max_duration_seconds == 1 else 's'}"
        if run.started_at:
            display_time += f" (expires {get_expiration_date(run.started_at, max_duration_seconds)})"

        return display_time

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for model in self.models:
            display_config = {
                'Run Name': model.name,
                'Parent Run Name': model.submitted_config.parent_name if model.submitted_config else None,
                'Run ID': model.run_uid,
                'Last Resumption ID': model.last_resumption_id,
                'User': model.created_by,
                'Cluster': model.cluster,
                'Image': model.image,
                'Priority': model.priority.lower().capitalize(),
                'Status': model.status.name.lower().capitalize(),
                'Preemptible': model.preemptible,
                'Reason': model.reason,
                'Watchdog': model.retry_on_system_failure,
                'Max Retries': model.max_retries if model.max_retries else 0,
            }

            if not model.image:
                del display_config['Image']

            if not display_config['Parent Run Name']:
                # Sort of hacky, but delete afterwards to preserve order
                del display_config['Parent Run Name']

            max_duration = self.get_max_duration(model)
            if max_duration:
                display_config["Max Duration"] = max_duration

            item = MCLIDisplayItem(display_config)
            yield item


def format_lifecycle_event(run: Run, event: RunLifecycle) -> str:
    # TODO: move lifecycle event parsing to MAPI
    if event.status == RunStatus.COMPLETED:
        return 'Run completed successfully'
    elif event.status == RunStatus.FAILED:
        failed_with = ''
        if event.reason:
            failed_with = f' with exit code {event.reason}'
        log_tail = ''
        if event.resumption_index < run.resumption_count - 1:
            # add resumption flag to the log command if not the latest resumption
            log_tail = f' --resumption {event.resumption_index}'

        return f'Run failed{failed_with}\n' + \
            f'See logs with [blue]mcli logs {run.name}{log_tail}'
    elif event.status == RunStatus.STOPPED:
        if event.reason == 'Preempted':
            return 'Run was preempted'
        elif event.reason == 'Node Failure':
            return 'Run was stopped due to node failure'
        else:
            return "Run stopped"
    elif event.status == RunStatus.RUNNING:
        if event.resumption_index == 0:
            return 'Run started'
        else:
            return 'Run resumed'
    elif event.status == RunStatus.PENDING:
        if event.resumption_index == 0:
            return 'Run created'
        else:
            return 'Run placed back in the scheduling queue'
    # We don't want to inundate the user with all Run Statuses,
    # so let's hide other statuses for now
    return ''


# TODO: replace lifecycle events with run events
def format_event_log(run: Run) -> Table:
    grid = Table(expand=False, padding=(0, 2, 0, 2))
    grid.add_column(header='Time', justify='left')
    grid.add_column(header='Resumption', justify='left')
    grid.add_column(header='Event', justify='left')

    lifecycle = sorted(run.lifecycle, key=lambda x: (x.resumption_index, x.started_at))
    current_attempt = 0
    for event in lifecycle:
        if event.resumption_index != current_attempt:
            grid.add_section()
            current_attempt = event.resumption_index
        text = format_lifecycle_event(run=run, event=event)
        if len(text) > 0:
            grid.add_row(format_timestamp(event.started_at), str(event.resumption_index), text)
    return grid


class MCLIDescribeRunMetadataDisplay(MCLIGetDisplay):
    """ Vertical table view of run metadata """

    def __init__(self, metadata: Dict[str, Any]):
        self.metadata = metadata

    @property
    def index_label(self) -> str:
        return "Key"

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for k in sorted(self.metadata.keys()):
            item = MCLIDisplayItem({
                'Key': k,
                'Value': self.metadata[k],
            })
            yield item


def format_status(status: str) -> str:
    status = status.lower().capitalize()

    if status == 'Failed':
        return f'[red]{status}[/]'

    if status == 'Stopped':
        return f'[bright_black]{status}[/]'

    return status


class MCLIDescribeRunNodeDisplay(MCLIGetDisplay):
    """ Horizontal table view of run node """

    def __init__(self, nodes: List[Node]):
        self.nodes = sorted(nodes, key=lambda x: x.rank)

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for n in self.nodes:
            yield MCLIDisplayItem({
                'Rank': n.rank,
                'Node Name': n.name,
                'Status': format_status(n.status),
                'Reason': n.reason or '',
            })

    @property
    def index_label(self) -> str:
        return 'Rank'


T = TypeVar('T')


def compute_or_deprecated(compute: ComputeConfig, key: str, deprecated: T) -> Optional[T]:
    from_compute = compute.get(key, None)
    if from_compute is not None:
        return from_compute
    return deprecated


@dataclass
class DescribeComputeRequests():
    """Describer for compute requests"""
    cluster: Optional[str] = None
    gpu_type: Optional[str] = None
    gpus: Optional[int] = None
    cpus: Optional[int] = None
    nodes: Optional[int] = None

    # TODO: add instance type

    @property
    def display_names(self) -> Dict[str, str]:
        # Return display name mapping for table
        return {
            'cluster': 'Cluster',
            'gpu_type': 'GPU Type',
            'gpus': 'GPUs',
            'cpus': 'CPUs',
            'nodes': 'Nodes',
        }

    @classmethod
    def from_run(cls, run: Run) -> DescribeComputeRequests:
        return DescribeComputeRequests(
            cluster=run.cluster,
            gpu_type=run.gpu_type,
            gpus=run.gpus,
            cpus=run.cpus,
            nodes=run.node_count,
        )

    def to_table(self) -> Table:
        data = {self.display_names.get(k, k.capitalize()): str(v) for k, v in asdict(self).items() if v is not None}
        return create_vertical_display_table(data=data)


@cli_error_handler("mcli describe run")
def describe_run(
    run_name: Optional[str],
    output: OutputDisplay = OutputDisplay.TABLE,
    no_yaml: bool = False,
    yaml_only: bool = False,
    **kwargs,
):
    """
    Fetches more details of a Run
    """
    del kwargs

    latest = not run_name
    name_filter = [run_name] if run_name else []

    runs = get_runs_with_filters(
        name_filter=name_filter,
        latest=latest,
        include_details=True,
        include_deleted=True,
    )

    if len(runs) == 0:
        print(f'No runs found with name: {run_name}')
        return
    run = runs[0]
    if not yaml_only:
        # Run details section
        print(format_string('Run Details', FormatString.BOLD))
        details_display = MCLIDescribeRunDetailsDisplay([run])
        details_display.print(output)
        print()

        # Compute requests section
        print(format_string('Compute Requests', FormatString.BOLD))
        compute_display = DescribeComputeRequests.from_run(run)
        console.print(compute_display.to_table())
        print()

        if run.metadata:
            print(format_string('Run Metadata', FormatString.BOLD))
            metadata_display = MCLIDescribeRunMetadataDisplay(run.metadata)
            metadata_display.print(output, markup=False)
            print()

        if run.nodes:
            print(format_string('Run Nodes', FormatString.BOLD))
            node_display = MCLIDescribeRunNodeDisplay(run.nodes)
            node_display.print(output)
            print()

        # Run event log section
        print(format_string('Run Event Log', FormatString.BOLD))
        console.print(format_event_log(run))
        print()

    if no_yaml or run.submitted_config is None:
        # Stop here and skip printing yaml
        return

    if not yaml_only:
        # Skip printing the header if --yaml-only is set
        # This will allow users to directly pipe the output to a file if they like
        print(format_string('Submitted Run Configuration', FormatString.BOLD))
    print(run.submitted_config)
