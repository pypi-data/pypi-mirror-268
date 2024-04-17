"""DataPlatform store commands for the cmem command line interface."""

import os
from pathlib import Path

import click
from click import UsageError
from cmem.cmempy.dp.admin import create_showcase_data, delete_bootstrap_data, import_bootstrap_data
from cmem.cmempy.dp.admin.backup import get_zip, post_zip

from cmem_cmemc import completion
from cmem_cmemc.commands import CmemcCommand, CmemcGroup
from cmem_cmemc.context import ApplicationContext


@click.command(cls=CmemcCommand, name="bootstrap")
@click.option(
    "--import",
    "import_",
    is_flag=True,
    help="Delete existing bootstrap data if present and import bootstrap "
    "data which was delivered with Corporate Memory.",
)
@click.option("--remove", is_flag=True, help="Delete existing bootstrap data if present.")
@click.pass_obj
def bootstrap_command(app: ApplicationContext, import_: bool, remove: bool) -> None:
    """Update/Import or remove bootstrap data.

    Use `--import` to import the bootstrap data needed for managing shapes and
    configuration objects. This will remove the old data first.

    Use `--remove` to delete bootstrap data.

    Note: The removal of existing bootstrap data will search for resources which are
    flagged with the isSystemResource property.
    """
    if import_ and remove or not import_ and not remove:
        raise UsageError("Either use the --import or the --remove option.")
    if import_:
        app.echo_info("Update or import bootstrap data ... ", nl=False)
        import_bootstrap_data()
        app.echo_success("done")
        return
    if remove:
        app.echo_info("Remove bootstrap data ... ", nl=False)
        delete_bootstrap_data()
        app.echo_success("done")
        return


@click.command(cls=CmemcCommand, name="showcase")
@click.option(
    "--scale",
    type=click.INT,
    default="10",
    show_default=True,
    help="The scale factor provides a way to set the target size of the "
    "scenario. A value of 10 results in around 40k triples, a value of "
    "50 in around 350k triples.",
)
@click.option(
    "--create",
    is_flag=True,
    help="Delete old showcase data if present and create new showcase data"
    "based on the given scale factor.",
)
@click.option("--delete", is_flag=True, help="Delete existing showcase data if present.")
@click.pass_obj
def showcase_command(app: ApplicationContext, scale: int, create: bool, delete: bool) -> None:
    """Create showcase data.

    This command creates a showcase scenario of multiple graphs including
    integration graphs, shapes, statement annotations, etc.

    Note: There is currently no deletion mechanism for the showcase data, and
    you need to remove the showcase graphs manually (or just remove all
    graphs).
    """
    if not delete and not create:
        raise ValueError("Either use the --create or the --delete flag.")
    if delete:
        raise NotImplementedError(
            "This feature is not implemented yet. " "Please delete the graphs manually."
        )
    if create:
        app.echo_info(f"Create showcase data with scale factor {scale} ... ", nl=False)
        create_showcase_data(scale_factor=scale)
        app.echo_success("done")


@click.command(cls=CmemcCommand, name="export")
@click.argument(
    "BACKUP_FILE",
    shell_complete=completion.graph_backup_files,
    required=True,
    type=click.Path(writable=True, allow_dash=False, dir_okay=False),
)
@click.option(
    "--overwrite",
    is_flag=True,
    help="Overwrite existing files. " "This is a dangerous option, so use it with care.",
)
@click.pass_obj
def export_command(app: ApplicationContext, backup_file: str, overwrite: bool) -> None:
    """Backup all knowledge graphs to a ZIP archive.

    The backup file is a ZIP archive containing all knowledge graphs (one
    Turtle file + configuration file per graph).

    This command will create lots of load on the server.
    It can take a long time to complete.
    """
    if Path(backup_file).exists() and overwrite is not True:
        raise ValueError(
            f"Export file {backup_file} already exists and --overwrite " "option is not used."
        )
    with get_zip() as request:
        request.raise_for_status()
        with Path(backup_file).open(mode="wb") as _:
            requested_size = 1024 * 1024
            byte_counter = 0
            overall_byte_counter = 0
            app.echo_info(f"Exporting graphs backup to {backup_file} ...", nl=False)
            for chunk in request.iter_content(chunk_size=requested_size):
                chunk_size = len(chunk)
                app.echo_debug(f"Got new chuck of {chunk_size} bytes.")
                byte_counter += chunk_size
                overall_byte_counter += chunk_size
                _.write(chunk)
                _.flush()
                os.fsync(_.fileno())
                if byte_counter > requested_size:
                    app.echo_info(".", nl=False)
                    byte_counter = 0
            app.echo_debug(f"Wrote {overall_byte_counter} bytes to {backup_file}.")
            app.echo_success(" done")


@click.command(cls=CmemcCommand, name="import")
@click.argument(
    "BACKUP_FILE",
    shell_complete=completion.graph_backup_files,
    required=True,
    type=click.Path(readable=True, exists=True, allow_dash=False, dir_okay=False),
)
@click.pass_obj
def import_command(app: ApplicationContext, backup_file: str) -> None:
    """Restore graphs from a ZIP archive.

    The backup file is a ZIP archive containing all knowledge graphs  (one
    Turtle file + configuration file per graph).

    The command will load a single backup ZIP archive into the triple store
    by replacing all graphs with the content of the Turtle files in the
    archive and deleting all graphs which are not in the archive.

    This command will create lots of load on the server.
    It can take a long time to complete.
    The backup file will be transferred to the server, then unzipped and
    imported graph by graph. After the initial transfer the network
    connection is not used anymore and may be closed by proxies.
    This does not mean that the import failed.
    """
    app.echo_info(f"Importing graphs backup from {backup_file} ...", nl=False)
    request = post_zip(backup_file)
    request.raise_for_status()
    app.echo_success(" done")


@click.group(cls=CmemcGroup)
def store() -> CmemcGroup:  # type: ignore[empty-body]
    """Import, export and bootstrap the knowledge graph store.

    This command group consist of commands to administrate the
    knowledge graph store as a whole.
    """


store.add_command(showcase_command)
store.add_command(bootstrap_command)
store.add_command(export_command)
store.add_command(import_command)
