"""
Module for performing operations on tasks.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.tasks.entity import task_from_dict, task_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.tasks.entity import Task


ENTITY_TYPE = "tasks"


def create_task(**kwargs) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Task
       Object instance.
    """
    return task_from_parameters(**kwargs)


def create_task_from_dict(obj: dict) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    obj : dict
        Object dictionary.

    Returns
    -------
    Task
       Object instance.
    """
    check_context(obj.get("project"))
    return task_from_dict(obj)


def new_task(
    project: str,
    kind: str,
    uuid: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    function: str | None = "",
    node_selector: list[dict] | None = None,
    volumes: list[dict] | None = None,
    resources: list[dict] | None = None,
    affinity: dict | None = None,
    tolerations: list[dict] | None = None,

    env: list[dict] | None = None,
    secrets: list[str] | None = None,
    backoff_limit: int | None = None,
    schedule: str | None = None,
    replicas: int | None = None,
    **kwargs,
) -> Task:
    """
    Create a new object instance.

    Parameters
    ----------
    project : str
        Project name.
    kind : str
        Kind of the object.
    uuid : str
        ID of the object in form of UUID.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    function : str
        The function string identifying the function.
    node_selector : list[NodeSelector]
        The node selector of the task.
    volumes : list[Volume]
        The volumes of the task.
    resources : list[Resource]
        Kubernetes resources for the task.
    affinity : Affinity
        The affinity of the task.
    tolerations : list[Toleration]
        The tolerations of the task.
    env : list[Env]
        The env variables of the task.
    secrets : list[str]
        The secrets of the task.
    backoff_limit : int
        The backoff limit of the task.
    schedule : str
        The schedule of the task.
    replicas : int
        The replicas of the task.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Task
       Object instance.
    """
    obj = create_task(
        project=project,
        kind=kind,
        uuid=uuid,
        source=source,
        labels=labels,
        function=function,
        node_selector=node_selector,
        volumes=volumes,
        resources=resources,
        affinity=affinity,
        tolerations=tolerations,
        env=env,
        secrets=secrets,
        backoff_limit=backoff_limit,
        schedule=schedule,
        replicas=replicas,
        **kwargs,
    )
    obj.save()
    return obj


def get_task(project: str, entity_id: str, **kwargs) -> Task:
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
    Task
        Object instance.
    """
    api = api_ctx_read(project, ENTITY_TYPE, entity_id)
    obj = get_context(project).read_object(api, **kwargs)
    return create_task_from_dict(obj)


def import_task(file: str) -> Task:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Task
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_task_from_dict(obj)


def delete_task(project: str, entity_id: str, cascade: bool = True, **kwargs) -> dict:
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


def update_task(entity: Task, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Task
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_tasks(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of tasks dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
