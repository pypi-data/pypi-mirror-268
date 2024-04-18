"""
Module for performing operations on runs.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.runs.entity import run_from_dict, run_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.runs.entity import Run


ENTITY_TYPE = "runs"


def create_run(**kwargs) -> Run:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Run
       Object instance.
    """
    return run_from_parameters(**kwargs)


def create_run_from_dict(obj: dict) -> Run:
    """
    Create a new Run instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Run
        Run object.
    """
    check_context(obj.get("project"))
    return run_from_dict(obj)


def new_run(
    project: str,
    task: str,
    kind: str,
    uuid: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    inputs: dict | None = None,
    outputs: list | None = None,
    parameters: dict | None = None,
    values: list | None = None,
    local_execution: bool = False,
    **kwargs,
) -> Run:
    """
    Create run.

    Parameters
    ----------
    project : str
        Project name.
    task : str
        Name of the task associated with the run.
    kind : str
        Kind of the object.
    uuid : str
        ID of the object in form of UUID.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    inputs : dict
        Inputs of the run.
    outputs : list
        Outputs of the run.
    parameters : dict
        Parameters of the run.
    values : list
        Values of the run.
    local_execution : bool
        Flag to determine if object has local execution.
    embedded : bool
        Flag to determine if object must be embedded in project.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Run
        Run object.
    """
    obj = create_run(
        project=project,
        task=task,
        kind=kind,
        uuid=uuid,
        source=source,
        labels=labels,
        inputs=inputs,
        outputs=outputs,
        parameters=parameters,
        values=values,
        local_execution=local_execution,
        **kwargs,
    )
    obj.save()
    return obj


def get_run(project: str, entity_id: str, **kwargs) -> Run:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    Run
        Object instance.
    """
    api = api_ctx_read(project, ENTITY_TYPE, entity_id)
    obj = get_context(project).read_object(api, **kwargs)
    return create_run_from_dict(obj)


def import_run(file: str) -> Run:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Run
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_run_from_dict(obj)


def delete_run(project: str, entity_id: str, cascade: bool = True, **kwargs) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    params = kwargs.get("params", {})
    if params is None or not params:
        kwargs["params"] = {}
        kwargs["params"]["cascade"] = str(cascade).lower()
    api = api_ctx_delete(project, ENTITY_TYPE, entity_id)
    return get_context(project).delete_object(api, **kwargs)


def update_run(entity: Run, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Run
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(include_all_non_private=True), **kwargs)


def list_runs(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of runs dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
