"""Utility functions for CLI interface."""

import json
import os
import re
import unicodedata
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from cmem.cmempy.dp.admin import get_prometheus_data
from cmem.cmempy.dp.proxy.graph import get_graphs_list
from cmem.cmempy.workspace.projects.project import get_projects
from prometheus_client import Metric
from prometheus_client.parser import text_string_to_metric_families

from cmem_cmemc.constants import NAMESPACES
from cmem_cmemc.context import ApplicationContext


def get_version() -> str:
    """Get the current version or SNAPSHOT."""
    return version("cmem-cmemc")


def extract_error_message(error: Exception) -> str:
    """Extract a message from an exception."""
    # exceptions with response is HTTPError
    message = type(error).__name__ + ": " + str(error) + "\n"
    try:
        # try to load Problem Details for HTTP API JSON
        details = json.loads(error.response.text)  # type: ignore[attr-defined]
        message += type(error).__name__ + ": "
        if "title" in details:
            message += details["title"] + ": "
        if "detail" in details:
            message += details["detail"]
    except (AttributeError, ValueError):
        # is not json or any other issue, output plain response text
        pass
    return message


def iri_to_qname(iri: str) -> str:
    """Return a qname for an IRI based on well known namespaces.

    In case of no matching namespace, the full IRI is returned.

    Args:
    ----
        iri: the IRI to transform

    Returns: string

    """
    for prefix, namespace in NAMESPACES.items():
        iri = iri.replace(namespace, prefix + ":")
    return iri


def read_rdf_graph_files(directory_path: str) -> list[tuple[str, str]]:
    """Read all files from directory_path and output as tuples.

    The tuple format is (filepath, graph_name),
    for example ("/tmp/rdf.nt", "http://example.com")
    """
    rdf_graphs = []
    for root, _, files in os.walk(directory_path):
        for _file in files:
            full_file_path = Path(root) / _file
            graph_file_name = _file + ".graph"
            full_graph_file_name_path = Path(root) / graph_file_name
            if not _file.endswith(".graph") and Path(full_graph_file_name_path).exists():
                graph_name = read_file_to_string(str(full_graph_file_name_path)).strip()
                rdf_graphs.append((str(full_file_path.resolve()), graph_name))
    return rdf_graphs


def read_file_to_string(file_path: str) -> str:
    """Read file to string."""
    with Path(file_path).open(mode="rb") as _file:
        return _file.read().decode("utf-8")


def get_graphs(writeable: bool = True, readonly: bool = True) -> list:
    """Retrieve list of accessible graphs from DP endpoint.

    readonly=True|writeable=True outputs all graphs
    readonly=False|writeable=True outputs only writeable graphs
    readonly=True|writeable=False outputs graphs without write access
    (but read access)
    """
    all_graphs = get_graphs_list()
    filtered_graphs = []
    for graph in all_graphs:
        if graph["writeable"] and writeable:
            filtered_graphs.append(graph)
        if not graph["writeable"] and readonly:
            filtered_graphs.append(graph)
    return filtered_graphs


def get_graphs_as_dict(writeable: bool = True, readonly: bool = True) -> dict:
    """Get the graph response as dict with IRI as main key."""
    graph_dict = {}
    for graph in get_graphs(writeable=writeable, readonly=readonly):
        graph_dict[graph["iri"]] = graph
    return graph_dict


def convert_uri_to_filename(value: str, allow_unicode: bool = False) -> str:
    """Convert URI to unix friendly filename.

    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert / to underscore. Convert to lowercase.
    Also strip leading and trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"\.", "_", value.lower())
    value = re.sub(r"/", "_", value.lower())
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def struct_to_table(
    source: str | bool | float | list | dict, table: list | None = None, prefix: str = ""
) -> list:
    """Prepare flat key/value table from a deep structure.

    This function takes structure and creates a flat table out of it,
    key by key, value by value. For each level deeper it prefixes the
    father keys.

    Example input:  {'k1': '1', 'k2': {'k3': '3', 'k4': '4'}}
    Example output: [['k1', '1'], ['k2:k3', '3'], ['k2:k4', '4']]

    Args:
    ----
        source (any): The structure which is transformed into a flat table.
        table (list): The table where the key/value rows will be appended.
        prefix (str): A prefix which is used to indicate the level.

    Returns:
    -------
        The input table extended with rows from the input source.

    """
    if table is None:
        table = []
    if type(source) in (str, bool, int, float):
        table.append([prefix, source])
        return table
    if isinstance(source, dict):
        if len(prefix) != 0:
            prefix = prefix + "."
        for key in source:
            table = struct_to_table(source[key], table, prefix + key)
        return table
    if isinstance(source, list):
        for value in source:
            table = struct_to_table(value, table, prefix)
        return table
    return table


def split_task_id(task_id: str) -> tuple[str, str]:
    """Validate and split cmemc task ID.

    Args:
    ----
        task_id (str): The task ID in the workspace.

    Raises:
    ------
        ValueError: in case the task ID is not splittable

    """
    try:
        project_part = task_id.split(":")[0]
        task_part = task_id.split(":")[1]
    except IndexError as error:
        raise ValueError(f"{task_id} is not a valid task ID.") from error
    return project_part, task_part


def metric_get_labels(family: Metric, clean: bool = True) -> dict[str, list[str]]:
    """Get the labels of a metric family.

    clean: remove keys with only one dimension
    family: the metric family

    Returns: labels as dict
    """
    labels: dict[str, list[str]] = {}
    # build tree structure
    for sample in family.samples:
        for label in sample.labels:
            value = sample.labels[label]
            if label not in labels:
                labels[label] = []
            if value not in labels[label]:
                labels[label].append(value)
    if clean:
        labels = dict(filter(lambda elem: len(elem[1]) > 1, labels.items()))
    return labels


def metrics_get_dict(job_id: str = "DP") -> dict[str, Metric]:
    """Get metrics data as dict."""
    data = {}
    if job_id == "DP":
        for family in text_string_to_metric_families(get_prometheus_data().text):
            data[family.name] = family
        return data
    raise ValueError(f"job name {job_id} unknown.")


def metrics_get_family(job_id: str, metric_id: str) -> Metric:
    """Get family data.

    This function returns a dictionary of metric families.
    """
    try:
        return metrics_get_dict(job_id=job_id)[metric_id]
    except KeyError as error:
        raise ValueError(f"The job {job_id} does not have a metric {metric_id}.") from error


def check_or_select_project(app: ApplicationContext, project_id: str | None = None) -> str:
    """Check for given project, select the first one if there is only one.

    Args:
    ----
        app (ApplicationContext): the click cli app context.
        project_id (str): The project ID.

    Raises:
    ------
        ValueError: if no projects available.
        ValueError: if more than one project is.

    Returns:
    -------
        Maybe project_id if there was no project_id before.

    """
    if project_id is not None:
        return project_id

    projects = get_projects()
    if len(projects) == 1:
        project_name = str(projects[0]["name"])
        app.echo_warning(
            "Missing project (--project) - since there is only one project, "
            f"this is selected: {project_name}"
        )
        return project_name

    if len(projects) == 0:
        raise ValueError(
            "There are no projects available. "
            "Please create a project with 'cmemc project create'."
        )

    # more than one project
    raise ValueError(
        "There is more than one project available so you need to "
        "specify the project with '--project'."
    )


@dataclass
class PublishedPackage:
    """Represents a published package from pypi.org."""

    name: str
    description: str
    version: str
    published: str


def get_published_packages() -> list[PublishedPackage]:
    """Get a scraped list of plugin packages scraped from pypi.org."""
    url = "https://pypi.org/search/?q=%22cmem-plugin-%22"
    soup = BeautifulSoup(requests.get(url, timeout=5).content, "html.parser")
    packages = []
    snippets = soup.find_all("a", class_="package-snippet")
    for _ in snippets:
        name = _.findChildren(class_="package-snippet__name")[0].getText()
        if name == "cmem-plugin-base":
            continue
        if not name.startswith("cmem-plugin-"):
            continue
        description = _.findChildren(class_="package-snippet__description")[0].getText()
        package_version = _.findChildren(class_="package-snippet__version")[0].getText()
        published = _.findChildren(name="time")[0].attrs["datetime"]
        packages.append(
            PublishedPackage(
                name=name, description=description, version=package_version, published=published
            )
        )
    return packages


def convert_iri_to_qname(iri: str, default_ns: str) -> str:
    """Convert IRI to a QName based on the default namespace.

    If the IRI does not match the default namespace, the method returns the full IRI.
    """
    if iri.startswith(default_ns):
        return iri.replace(default_ns, ":")
    return iri


def convert_qname_to_iri(qname: str, default_ns: str) -> str:
    """Convert a QName to an IRI based on the default namespace.

    If the QName does not match the default namespace, the method returns the full IRI.
    """
    if qname.startswith(":"):
        return default_ns + qname[1:]

    return qname
