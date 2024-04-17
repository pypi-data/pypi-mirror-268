"""access control"""

import click
import requests.exceptions
from click import Option, UsageError
from cmem.cmempy.dp.authorization.conditions import (
    create_access_condition,
    delete_access_condition,
    fetch_all_acls,
    get_access_condition_by_iri,
    review_graph_rights,
    update_access_condition,
)
from cmem.cmempy.keycloak.user import get_user_by_username, user_groups

from cmem_cmemc import completion
from cmem_cmemc.commands import CmemcCommand, CmemcGroup
from cmem_cmemc.constants import NS_ACL, NS_GROUP, NS_USER
from cmem_cmemc.context import ApplicationContext
from cmem_cmemc.utils import convert_iri_to_qname, convert_qname_to_iri, struct_to_table

# option descriptions
HELP_TEXTS = {
    "name": "A short name or label.",
    "id": "An optional ID (will be an UUID otherwise).",
    "description": "An optional description.",
    "user": "A specific user account required by the access condition.",
    "group": "A membership in a user group required by the access condition",
    "read_graph": "Grants read access to a graph.",
    "write_graph": "Grants write access to a graph (includes read access).",
    "action": "Grants usage permissions to an action / functionality.",
}

PUBLIC_USER_URI = "urn:elds-backend-anonymous-user"
PUBLIC_GROUP_URI = "urn:elds-backend-public-group"

KNOWN_ACCESS_CONDITION_URLS = [PUBLIC_USER_URI, PUBLIC_GROUP_URI]


def _list_to_acl_url(ctx: ApplicationContext, param: Option, value: list) -> list:
    """Option callback which returns a URI for a list of strings.

    or list of URIs, if a tuple comes from click
    or not, if it is already a known URI .... or None
    """
    return [_value_to_acl_url(ctx, param, _) for _ in value]


def _value_to_acl_url(
    ctx: ApplicationContext,  # noqa: ARG001
    param: Option,
    value: str | None,
) -> str | None:
    """Option callback which returns a URI for a string.

    or not, if it is already a known URI .... or None
    """
    if value in KNOWN_ACCESS_CONDITION_URLS:
        return value
    if value == "":
        return ""
    if value is None:
        return None
    match param.name:
        case "groups":
            return f"{NS_GROUP}{value}"
        case "user":
            return f"{NS_USER}{value}"
    return f"{NS_ACL}{value}"


def generate_acl_name(user: str | None, groups: list[str]) -> str:
    """Create an access condition name based on user and group assignments."""
    if len(groups) > 0:
        group_term = "groups" if len(groups) > 1 else "group"
        groups_labels = ", ".join(
            [convert_iri_to_qname(iri=_, default_ns=NS_GROUP)[1:] for _ in groups]
        )
        if user:
            return (
                f"Condition for user {convert_iri_to_qname(iri=user, default_ns=NS_USER)[1:]} "
                f"and {group_term} {groups_labels}"
            )
        return f"Condition for {group_term} {groups_labels}"
    if user:
        return f"Condition for user: {convert_iri_to_qname(iri=user, default_ns=NS_USER)[1:]}"
    return "Condition for ALL users"


@click.command(cls=CmemcCommand, name="list")
@click.option("--raw", is_flag=True, help="Outputs raw JSON.")
@click.option(
    "--id-only",
    is_flag=True,
    help="Lists only URIs. This is useful for piping the IDs into other commands.",
)
@click.pass_obj
def list_command(app: ApplicationContext, raw: bool, id_only: bool) -> None:
    """List access conditions.

    This command retrieves and lists all access conditions, which are manageable
    by the current account.
    """
    acls = fetch_all_acls()
    if raw:
        app.echo_info_json(acls)
        return
    if id_only:
        for graph in acls:
            app.echo_info(convert_iri_to_qname(iri=graph.get("iri"), default_ns=NS_ACL))
        return
    table = [
        (convert_iri_to_qname(iri=_.get("iri"), default_ns=NS_ACL), _.get("name", "-"))
        for _ in acls
    ]
    app.echo_info_table(table, headers=["URI", "Name"], sort_column=0)


@click.command(cls=CmemcCommand, name="inspect")
@click.argument("access_condition_id", type=click.STRING, shell_complete=completion.acl_ids)
@click.option("--raw", is_flag=True, help="Outputs raw JSON.")
@click.pass_obj
def inspect_command(app: ApplicationContext, access_condition_id: str, raw: bool) -> None:
    """Inspect an access condition.

    Note: access conditions can be listed by using the `acl list` command.
    """
    iri = convert_qname_to_iri(qname=access_condition_id, default_ns=NS_ACL)
    access_condition = get_access_condition_by_iri(iri).json()

    if raw:
        app.echo_info_json(access_condition)
        return

    table = struct_to_table(access_condition)
    app.echo_info_table(table, headers=["Key", "Value"], sort_column=0)


@click.command(cls=CmemcCommand, name="create")
@click.option(
    "--name",
    "name",
    type=click.STRING,
    help=HELP_TEXTS["name"],
)
@click.option(
    "--id",
    "id_",
    type=click.STRING,
    help=HELP_TEXTS["id"],
)
@click.option(
    "--description",
    "description",
    type=click.STRING,
    help=HELP_TEXTS["description"],
)
@click.option(
    "--user",
    type=click.STRING,
    shell_complete=completion.acl_users,
    help=HELP_TEXTS["user"],
    callback=_value_to_acl_url,
)
@click.option(
    "--group",
    "groups",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.acl_groups,
    help=HELP_TEXTS["group"],
    callback=_list_to_acl_url,
)
@click.option(
    "--read-graph",
    "read_graphs",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.graph_uris_with_all_graph_uri,
    help=HELP_TEXTS["read_graph"],
)
@click.option(
    "--write-graph",
    "write_graphs",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.graph_uris_with_all_graph_uri,
    help=HELP_TEXTS["write_graph"],
)
@click.option(
    "--action",
    "actions",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.acl_actions,
    help=HELP_TEXTS["action"],
)
@click.pass_obj
# pylint: disable-msg=too-many-arguments
def create_command(  # noqa: PLR0913
    app: ApplicationContext,
    name: str,
    id_: str,
    description: str,
    user: str,
    groups: list[str],
    read_graphs: tuple[str],
    write_graphs: tuple[str],
    actions: tuple[str],
) -> None:
    """Create an access condition."""
    if not read_graphs and not write_graphs and not actions:
        raise click.UsageError(
            "Missing access / usage grant. Use at least one of the following options: "
            "--read-graph, --write-graph or --action."
        )
    if not user and not groups:
        app.echo_warning(
            "Access conditions without a user and without a group assignment " "affect ALL users."
        )

    if not name:
        name = generate_acl_name(user=user, groups=groups)

    if not description:
        description = "This access condition was created with cmemc."

    app.echo_info(
        f"Creating access condition '{name}' ... ",
        nl=False,
    )
    create_access_condition(
        name=name,
        static_id=id_,
        description=description,
        user=user,
        groups=groups,
        read_graphs=list(read_graphs),
        write_graphs=list(write_graphs),
        actions=list(actions),
    )
    app.echo_success("done")


@click.command(cls=CmemcCommand, name="update")
@click.argument(
    "access_condition_id",
    nargs=1,
    required=True,
    type=click.STRING,
    shell_complete=completion.acl_ids,
)
@click.option(
    "--name",
    "name",
    type=click.STRING,
    help=HELP_TEXTS["name"],
)
@click.option(
    "--description",
    "description",
    type=click.STRING,
    help=HELP_TEXTS["description"],
)
@click.option(
    "--user",
    type=click.STRING,
    shell_complete=completion.acl_users,
    help=HELP_TEXTS["user"],
    callback=_value_to_acl_url,
)
@click.option(
    "--group",
    "groups",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.acl_groups,
    help=HELP_TEXTS["group"],
    callback=_list_to_acl_url,
)
@click.option(
    "--read-graph",
    "read_graphs",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.graph_uris_with_all_graph_uri,
    help=HELP_TEXTS["read_graph"],
)
@click.option(
    "--write-graph",
    "write_graphs",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.graph_uris_with_all_graph_uri,
    help=HELP_TEXTS["write_graph"],
)
@click.option(
    "--action",
    "actions",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.acl_actions,
    help=HELP_TEXTS["action"],
)
@click.pass_obj
# pylint: disable-msg=too-many-arguments
def update_command(  # noqa: PLR0913
    app: ApplicationContext,
    access_condition_id: str,
    name: str,
    description: str,
    user: str,
    groups: list[str],
    read_graphs: tuple[str],
    write_graphs: tuple[str],
    actions: tuple[str],
) -> None:
    """Update an access condition.

    Given an access condition URL, you can change specific options
    to new values.
    """
    iri = convert_qname_to_iri(qname=access_condition_id, default_ns=NS_ACL)
    payload = get_access_condition_by_iri(iri=iri).json()
    app.echo_info(
        f"Updating access condition {payload['name']} ... ",
        nl=False,
    )

    update_access_condition(
        iri=iri,
        name=name,
        description=description,
        user=user,
        groups=groups,
        read_graphs=read_graphs,
        write_graphs=write_graphs,
        actions=actions,
    )
    app.echo_success("done")


@click.command(cls=CmemcCommand, name="delete")
@click.option(
    "-a",
    "--all",
    "all_",
    is_flag=True,
    help="Delete all access conditions. " "This is a dangerous option, so use it with care.",
)
@click.argument(
    "access_condition_ids",
    nargs=-1,
    type=click.STRING,
    shell_complete=completion.acl_ids,
)
@click.pass_obj
def delete_command(app: ApplicationContext, all_: bool, access_condition_ids: list[str]) -> None:
    """Delete access conditions.

    This command deletes existing access conditions from the account.

    Note: Access conditions can be listed by using the `cmemc admin acs list` command.
    """
    if access_condition_ids == () and not all_:
        raise click.UsageError(
            "Either specify at least one access condition ID,"
            " or use the --all option to delete all access conditions."
        )
    if all_:
        access_condition_ids = [_["iri"] for _ in fetch_all_acls()]

    count = len(access_condition_ids)
    for index, _ in enumerate(access_condition_ids, 1):
        app.echo_info(f"Delete access condition {index}/{count}: {_} ... ", nl=False)
        delete_access_condition(iri=convert_qname_to_iri(qname=_, default_ns=NS_ACL))
        app.echo_success("done")


@click.command(name="review")
@click.option("--raw", is_flag=True, help="Outputs raw JSON.")
@click.argument("user", type=click.STRING, shell_complete=completion.acl_users)
@click.option(
    "--group",
    "groups",
    type=click.STRING,
    multiple=True,
    shell_complete=completion.acl_groups,
    callback=_list_to_acl_url,
    help="Add groups to the review request (what-if-scenario).",
)
@click.pass_obj
def review_command(app: ApplicationContext, raw: bool, user: str, groups: list[str] | None) -> None:
    """Review grants for a given account.

    This command has two working modes: (1) You can review the access conditions
    of an actual account - this needs access to keycloak and the access condition API,
    (2) You can review the access conditions of an imaginary account with a set of
    freely added groups (what-if-scenario) - this only needs access to the access
    condition API.

    The output of the command is a list of grants the account has based on your input
    and all access conditions loaded in the store. In addition to that, some metadata
    of the account is shown.
    """
    if not groups:
        app.echo_debug("Trying to fetch groups from keycloak.")
        keycloak_user = get_user_by_username(username=user)
        if not keycloak_user:
            raise UsageError(
                "Unknown User or no access to get user info.\n"
                "Use the --group option to assign groups manually (what-if-scenario)."
            )
        try:
            keycloak_user_groups = user_groups(user_id=keycloak_user[0]["id"])
            groups = [f"{NS_GROUP}{_['name']}" for _ in keycloak_user_groups]
        except requests.exceptions.HTTPError as error:
            raise UsageError(
                f"You do not have the permission to retrieve the groups for user {user}"
                " from Keycloak.\n"
                "Use the --group option to assign groups manually (what-if-scenario)."
            ) from error
    app.echo_debug(f"Got groups: {groups}")
    review_info: dict = review_graph_rights(
        account_iri=f"{NS_USER}{user}", group_iris=groups
    ).json()
    review_info["groupIri"] = groups
    if raw:
        app.echo_info_json(review_info)
        return
    table = struct_to_table(review_info)
    app.echo_info_table(table, headers=["Key", "Value"], sort_column=0)


@click.group(cls=CmemcGroup)
def acl() -> CmemcGroup:  # type: ignore[empty-body]
    """List, create, delete and modify and review access conditions.

    With this command group, you can manage and inspect access conditions
    in eccenca Corporate Memory. Access conditions are identified by a URL.
    They grant access to knowledge graphs or actions to user or groups.
    """


acl.add_command(list_command)
acl.add_command(inspect_command)
acl.add_command(create_command)
acl.add_command(update_command)
acl.add_command(delete_command)
acl.add_command(review_command)
