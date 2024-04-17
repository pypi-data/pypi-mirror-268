"""graph validation command group"""

import time
from datetime import UTC, datetime

import click
import requests
import timeago
from click import Context, UsageError
from click.shell_completion import CompletionItem
from cmem.cmempy.dp.shacl import validation
from requests import HTTPError
from rich.progress import Progress, SpinnerColumn, TaskID, TimeElapsedColumn

from cmem_cmemc import completion
from cmem_cmemc.commands import CmemcCommand, CmemcGroup
from cmem_cmemc.completion import _finalize_completion
from cmem_cmemc.context import ApplicationContext
from cmem_cmemc.exceptions import ServerError
from cmem_cmemc.object_list import (
    DirectListPropertyFilter,
    DirectValuePropertyFilter,
    ObjectList,
    compare_int_greater_than,
    transform_lower,
)
from cmem_cmemc.utils import struct_to_table


def get_sorted_validations_list(ctx: Context) -> list[dict]:  # noqa: ARG001
    """Get a sorted list of validation objects (aggregations)"""
    objects = validation.get_all_aggregations()
    return sorted(objects, key=lambda o: str(o.get("executionStarted", "SCHEDULED")))


validations_list = ObjectList(
    name="validation processes",
    get_objects=get_sorted_validations_list,
    filters=[
        DirectValuePropertyFilter(
            name="status",
            description="Filter list by current status of the process.",
            property_key="state",
            transform=transform_lower,
        ),
        DirectValuePropertyFilter(
            name="context-graph",
            description="Filter list by used data / context graph IRI.",
            property_key="contextGraphIri",
        ),
        DirectValuePropertyFilter(
            name="shape-graph",
            description="Filter list by used shape graph IRI.",
            property_key="shapeGraphIri",
        ),
        DirectValuePropertyFilter(
            name="more-resources-than",
            description="Filter list by the number of resources.",
            property_key="resourceCount",
            compare=compare_int_greater_than,
            fixed_completion=[
                CompletionItem("0"),
                CompletionItem("100"),
                CompletionItem("500"),
            ],
        ),
        DirectValuePropertyFilter(
            name="more-violations-than",
            description="Filter list by the number of violations.",
            property_key="violationsCount",
            compare=compare_int_greater_than,
            fixed_completion=[
                CompletionItem("0"),
                CompletionItem("100"),
                CompletionItem("500"),
            ],
        ),
        DirectValuePropertyFilter(
            name="more-violated-resources-than",
            description="Filter list by the number of violated resources.",
            property_key="resourcesWithViolationsCount",
            compare=compare_int_greater_than,
            fixed_completion=[
                CompletionItem("0"),
                CompletionItem("100"),
                CompletionItem("500"),
            ],
        ),
    ],
)


def get_violations_list(ctx: Context) -> list[dict]:
    """Get a list of violations"""
    try:
        # sometimes process_id is in params, sometimes in args !?
        process_id = ctx.params.get("process_id", None)
        if not process_id:
            process_id = ctx.args[0]
    except IndexError:
        return []  # process_id not given
    violations: list[dict] = []  # create a new object which better matches object_list needs
    for result in validation.get(batch_id=process_id)["results"]:
        resource_iri = result["resourceIri"]
        node_shapes = result["nodeShapes"]
        for _ in result["violations"]:
            _["resourceIri"] = resource_iri
            _["nodeShapes"] = node_shapes
            _["constraintName"] = _["reportEntryConstraintMessageTemplate"]["constraintName"]
            violations.append(_)
    return violations


violations_list = ObjectList(
    name="violations",
    get_objects=get_violations_list,
    filters=[
        DirectValuePropertyFilter(
            name="constraint",
            description="Filter list by constraint name.",
            property_key="constraintName",
        ),
        DirectValuePropertyFilter(
            name="severity", description="Filter list by severity.", property_key="severity"
        ),
        DirectValuePropertyFilter(
            name="resource", description="Filter list by resource IRI.", property_key="resourceIri"
        ),
        DirectListPropertyFilter(
            name="node-shape",
            description="Filter list by node shape IRI.",
            property_key="nodeShapes",
        ),
        DirectValuePropertyFilter(
            name="property-shape",
            description="Filter list by property shape IRI.",
            property_key="source",
        ),
    ],
)


def _get_batch_validation_option(validation_: dict) -> tuple[str, str]:
    """Get a completion option of a single batch validation"""
    id_ = validation_["id"]
    state = validation_["state"]
    graph = validation_["contextGraphIri"]
    stamp = datetime.fromtimestamp(validation_["executionStarted"] / 1000, tz=UTC)
    time_ago = timeago.format(stamp, datetime.now(tz=UTC))
    resources = _get_resource_count(validation_)
    violations = _get_violation_count(validation_)
    return (
        id_,
        f"{state} - {time_ago}, {resources} resources, {violations} violations ({graph})",
    )


def _complete_all_batch_validations(
    ctx: click.Context,  # noqa: ARG001
    param: click.Argument,  # noqa: ARG001
    incomplete: str,
) -> list[CompletionItem]:
    """Provide completion for batch validation"""
    options = [_get_batch_validation_option(_) for _ in validation.get_all_aggregations()]
    return _finalize_completion(candidates=options, incomplete=incomplete)


def _complete_running_batch_validations(
    ctx: click.Context,  # noqa: ARG001
    param: click.Argument,  # noqa: ARG001
    incomplete: str,
) -> list[CompletionItem]:
    """Provide completion for running batch validation"""
    options = [
        _get_batch_validation_option(_)
        for _ in validation.get_all_aggregations()
        if _["state"] == validation.STATUS_RUNNING
    ]
    return _finalize_completion(candidates=options, incomplete=incomplete)


def show_process_summary(app: ApplicationContext, process_id: str) -> None:
    """Show summary of the validation process"""
    app.echo_info_table(
        struct_to_table(validation.get_aggregation(batch_id=process_id)),
        headers=["Key", "Value"],
        sort_column=0,
        caption="Validation Summary",
    )


def show_violated_resources(app: ApplicationContext, data: list[dict]) -> None:
    """Show violated resource IRIs of a validation process"""
    messages = sorted({_["resourceIri"] for _ in data})
    app.echo_info(message=messages)


def _wait_for_process_completion(
    app: ApplicationContext, process_id: str, polling_interval: int, use_rich: bool = False
) -> str:
    class State:
        """State of a validation process"""

        id_: str
        data: dict
        status: str
        completed: int
        total: int

        def __init__(self, id_: str):
            self.id_ = id_
            self.refresh()

        def refresh(self) -> None:
            self.data = validation.get_aggregation(batch_id=self.id_)
            self.status = self.data.get("state", "UNKNOWN")
            self.completed = self.data.get("resourceProcessedCount", 0)
            self.total = self.data.get("resourceCount", 0)
            app.echo_debug(f"Process {self.id_} has status {self.status}.")

    state = State(id_=process_id)
    progress: Progress | None = None
    task: TaskID | None = None
    if use_rich:
        progress = Progress(
            SpinnerColumn(),
            *Progress.get_default_columns(),
            TimeElapsedColumn(),
            transient=True,
            console=app.console,
        )
        progress.__enter__()  # simulate context manager (with:)
        task = progress.add_task(f"{state.status.capitalize()} ... ", total=state.total)
    while True:
        time.sleep(polling_interval)
        state.refresh()
        if progress is not None and task is not None:
            progress.update(
                task_id=task,
                completed=state.completed,
                description=f"{state.status.capitalize()} ... {state.completed} / {state.total}",
            )
        if state.status in (validation.STATUS_SCHEDULED, validation.STATUS_RUNNING):
            # when reported as running or scheduled, start another loop
            continue
        # when reported as finished, error or cancelled break out
        break
    if progress is not None and task is not None:
        progress.stop()
        progress.__exit__(None, None, None)
    if state.status == validation.STATUS_CANCELLED:
        raise ServerError("Process was cancelled.")
    if state.status == validation.STATUS_ERROR:
        error_message = state.data.get("error", "")
        raise ServerError(f"Process ended with error: {error_message}")
    return state.status


def _get_violation_table(violations: list[dict]) -> tuple[list, list]:
    """Get violation table from batch validation result"""
    table = []
    for violation in violations:
        resource_iri: str = str(violation.get("resourceIri"))
        path = violation.get("path", None)
        constraint_name = violation.get("constraintName", "UNKNOWN")
        node_shapes = violation.get("nodeShapes", [])
        text = violation["messages"][0]["value"]  # default: use the text of the first message
        for message in violation["messages"]:
            # look for en non non-lang messages to use
            if message["lang"] == "" or message["lang"] == "en":
                text = str(message["value"])
                break
        cell = ""
        if path is not None:
            cell = f"Path: {path}"
        if len(node_shapes) == 1:
            cell = f"{cell}\nNodeShape: {node_shapes[0]}"
        if len(node_shapes) > 1:
            cell = f"{cell}\nNodeShapes:"
            for node_shape in node_shapes:
                cell = f"{cell}\n - {node_shape}"
        cell = f"{cell}\nMessage: {text}"
        row = [resource_iri, constraint_name, cell]
        table.append(row)
    return table, ["Resource IRI", "Constraint", "Details"]


def _get_resource_count(batch_validation: dict) -> str:
    """Get resource count from validation report"""
    resource_count = str(batch_validation.get("resourceCount", "-"))
    processed_count = str(batch_validation.get("resourceProcessedCount", "-"))
    if resource_count == processed_count:
        return resource_count
    return f"{processed_count} / {resource_count}"


def _get_violation_count(process_data: dict) -> str:
    """Get violation count from validation report"""
    if process_data.get("executionStarted") is None:
        return "-"
    resources = str(process_data.get("resourcesWithViolationsCount", "0"))
    violations = str(process_data.get("violationsCount", "0"))
    if violations == "0":
        return "0"
    return f"{violations} ({resources} Resources)"


@click.command(cls=CmemcCommand, name="execute")
@click.argument("iri", type=click.STRING, shell_complete=completion.graph_uris)
@click.option(
    "--shape-graph",
    shell_complete=completion.graph_uris,
    default="https://vocab.eccenca.com/shacl/",
    show_default=True,
    help="The shape catalog used for validation.",
)
@click.option(
    "--id-only",
    is_flag=True,
    help="Return the validation process identifier only. "
    "This is useful for piping the ID into other commands.",
)
@click.option(
    "--wait",
    is_flag=True,
    help="Wait until the process is finished. When using this option without the "
    "`--id-only` flag, it will enable a progress bar and a summary view.",
)
@click.option(
    "--polling-interval",
    type=click.IntRange(min=1),
    show_default=True,
    default=1,
    help="How many seconds to wait between status polls. Status polls are"
    " cheap, so a higher polling interval is most likely not needed.",
)
@click.pass_obj
def execute_command(  # noqa: PLR0913
    app: ApplicationContext,
    iri: str,
    shape_graph: str,
    id_only: bool,
    wait: bool,
    polling_interval: int,
) -> None:
    """Start a new validation process.

    Validation is performed on all typed resources of a data / context graph (IRI).
    Each resource is validated against all applicable node shapes from a
    selected shape catalog graph (and its sub-graphs).
    """
    process_id = validation.start(context_graph=iri, shape_graph=shape_graph)
    if wait:
        _wait_for_process_completion(
            app=app, process_id=process_id, use_rich=not id_only, polling_interval=polling_interval
        )
    if id_only:
        app.echo_info(process_id)
        return
    show_process_summary(process_id=process_id, app=app)


@click.command(cls=CmemcCommand, name="list")
@click.option(
    "--filter",
    "filter_",
    type=(str, str),
    multiple=True,
    help=validations_list.get_filter_help_text(),
    shell_complete=validations_list.complete_values,
)
@click.option(
    "--id-only",
    is_flag=True,
    help="List validation process identifier only. "
    "This is useful for piping the IDs into other commands.",
)
@click.option("--raw", is_flag=True, help="Outputs raw JSON of the validation list.")
@click.pass_context
def list_command(ctx: Context, filter_: tuple[tuple[str, str]], id_only: bool, raw: bool) -> None:
    """List running and finished validation processes.

    This command provides a filterable table or identifier list of validation
    processes. The command operates on the process summary and provides some statistics.

    Note: Detailed information on the found violations can be listed with the
    `graph validation inspect` command.
    """
    validations = validations_list.apply_filters(ctx=ctx, filter_=filter_)
    app: ApplicationContext = ctx.obj

    if raw:
        app.echo_info_json(validations)
        return

    if id_only:
        for _ in validations:
            app.echo_info(_["id"])
        return

    if len(validations) == 0:
        app.echo_warning(
            "No validation processes found. "
            "Use `graph validation execute` to start a new validation process."
        )
        return

    # output a user table
    table = []
    for _ in validations:
        if "executionStarted" in _ and _["executionStarted"] is not None:
            stamp = datetime.fromtimestamp(_["executionStarted"] / 1000, tz=UTC)
            time_ago = timeago.format(stamp, datetime.now(tz=UTC))
        else:
            time_ago = f"{_['state']}"
        row = [
            _["id"],
            _["state"],
            time_ago,
            _["contextGraphIri"],
            _get_resource_count(_),
            _get_violation_count(_),
        ]
        table.append(row)
    app.echo_info_table(
        table, headers=["ID", "Status", "Started", "Graph", "Resources", "Violations"]
    )


@click.command(cls=CmemcCommand, name="inspect")
@click.argument("process_id", type=click.STRING, shell_complete=_complete_all_batch_validations)
@click.option(
    "--filter",
    "filter_",
    type=(str, str),
    multiple=True,
    help=violations_list.get_filter_help_text(),
    shell_complete=violations_list.complete_values,
)
@click.option(
    "--id-only",
    is_flag=True,
    help="Return violated resource identifier only. "
    "This is useful for piping the ID into other commands.",
)
@click.option(
    "--summary",
    is_flag=True,
    help="Outputs the summary of the graph validation "
    "instead of the violations list (not filterable).",
)
@click.option("--raw", is_flag=True, help="Outputs raw JSON of the validation result.")
@click.pass_context
def inspect_command(  # noqa: PLR0913
    ctx: Context,
    process_id: str,
    filter_: tuple[tuple[str, str]],
    id_only: bool,
    summary: bool,
    raw: bool,
) -> None:
    """List and inspect errors found with a validation process.

    This command provides detailed information on the found violations of
    a validation process.

    Use the `--filter` option to limit the output based on different criteria such as
    constraint name (`constraint`), origin node shape of the rule (`node-shape`), or
    the validated resource (`resource`).

    Note: Validation processes IDs can be listed with the `graph validation list`
    command, or by utilizing the tab completion of this command.
    """
    app: ApplicationContext = ctx.obj
    if process_id not in [_["id"] for _ in validation.get_all_aggregations()]:
        raise UsageError(f"Validation process with ID '{process_id}' is not known (anymore).")

    if summary:
        if raw:
            app.echo_info_json(validation.get_aggregation(batch_id=process_id))
        else:
            show_process_summary(app=app, process_id=process_id)
        return

    data = violations_list.apply_filters(ctx=ctx, filter_=filter_)

    if id_only:
        show_violated_resources(app=app, data=data)
        return

    if raw:
        app.echo_info_json(data)
        return

    if len(data) == 0 and len(filter_) == 0:
        app.echo_warning(
            "The given validation process does not have any violations - "
            "I will show the summary instead."
        )
        show_process_summary(app=app, process_id=process_id)
    else:
        messages_table, messages_header = _get_violation_table(violations=data)
        if len(messages_table) > 0:
            app.echo_info("")
            app.echo_info_table(messages_table, headers=messages_header, sort_column=0)


@click.command(cls=CmemcCommand, name="cancel")
@click.argument("process_id", type=click.STRING, shell_complete=_complete_running_batch_validations)
@click.pass_obj
def cancel_command(app: ApplicationContext, process_id: str) -> None:
    """Cancel a running validation process.

    Note: In order to get the process IDs of all currently running validation
    processes, use the `graph validation list` command with the option
    `--filter status running`, or utilize the tab completion of this command.
    """
    try:
        graph_validation = validation.get_aggregation(process_id)
    except HTTPError as error:
        if error.response is not None and error.response.status_code == requests.codes.not_found:
            raise click.UsageError(
                f"Graph validation process with ID {process_id} does not exist."
            ) from error
    else:
        if graph_validation["state"] != validation.STATUS_RUNNING:
            raise click.UsageError(
                f"Graph validation process with ID {process_id} is not a running anymore."
            )
    app.echo_info(f"Graph validation process with ID {process_id} ... ", nl=False)
    validation.cancel(batch_id=process_id)
    app.echo_success("cancelled")


@click.group(cls=CmemcGroup, name="validation")
def validation_group() -> CmemcGroup:  # type: ignore[empty-body]
    """Validate resources in a graph.

    This command group is dedicated to the management of resource validation processes.
    A validation process verifies, that resources in a specific graph are valid according
    to the node shapes in a shape catalog graph.

    Note: Validation processes are identified with a random ID and can be listed with
    the `graph validation list` command. To start or cancel validation processes,
    use the `graph validation execute` and `graph validation cancel` command.
    To inspect the found violations of a validation process, use the
    `graph validation inspect` command.
    """


validation_group.add_command(execute_command)
validation_group.add_command(list_command)
validation_group.add_command(inspect_command)
validation_group.add_command(cancel_command)
