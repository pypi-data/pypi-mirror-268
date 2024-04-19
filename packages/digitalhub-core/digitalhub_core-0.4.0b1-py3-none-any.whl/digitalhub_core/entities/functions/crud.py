"""
Module for performing operations on functions.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.functions.entity import function_from_dict, function_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.functions.entity import Function

ENTITY_TYPE = "functions"


def create_function(**kwargs) -> Function:
    """
    Create a new object instance.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Function
       Object instance.
    """
    return function_from_parameters(**kwargs)


def create_function_from_dict(obj: dict) -> Function:
    """
    Create a new Function instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create the Function from.

    Returns
    -------
    Function
        Function object.
    """
    check_context(obj.get("project"))
    return function_from_dict(obj)


def new_function(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    git_source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    **kwargs,
) -> Function:
    """
    Create a new Function instance and persist it to the backend.

    Parameters
    ----------
    project : str
        Project name.
    name : str
        Name that identifies the object.
    kind : str
        Kind of the object.
    uuid : str
        ID of the object in form of UUID.
    description : str
        Description of the object.
    git_source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Function
       Object instance.
    """
    obj = create_function(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        git_source=git_source,
        labels=labels,
        embedded=embedded,
        **kwargs,
    )
    obj.save()
    return obj


def get_function(project: str, entity_name: str | None = None, entity_id: str | None = None, **kwargs) -> Function:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_name : str
        Entity name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    Function
        Object instance.
    """
    if (entity_id is None) and (entity_name is None):
        raise ValueError("Either entity_name or entity_id must be provided.")

    context = get_context(project)

    if entity_name is not None:
        params = kwargs.get("params", {})
        if params is None or not params:
            kwargs["params"] = {}

        api = api_ctx_list(project, ENTITY_TYPE)
        kwargs["params"]["name"] = entity_name
        obj = context.list_objects(api, **kwargs)[0]
    else:
        api = api_ctx_read(project, ENTITY_TYPE, entity_id)
        obj = context.read_object(api, **kwargs)
    return create_function_from_dict(obj)


def import_function(file: str) -> Function:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Function
        Object instance.
    """
    obj = read_yaml(file)
    if isinstance(obj, list):
        func_dict = obj[0]
        task_dicts = obj[1:]
    else:
        func_dict = obj
        task_dicts = []
    check_context(func_dict.get("project"))
    func = create_function_from_dict(func_dict)
    func.import_tasks(task_dicts)
    return func


def delete_function(
    project: str,
    entity_name: str | None = None,
    entity_id: str | None = None,
    delete_all_versions: bool = False,
    cascade: bool = True,
    **kwargs,
) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_name : str
        Entity name.
    entity_id : str
        Entity ID.
    delete_all_versions : bool
        Delete all versions of the named entity. Entity name is required.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    if (entity_id is None) and (entity_name is None):
        raise ValueError("Either entity_name or entity_id must be provided.")

    context = get_context(project)

    params = kwargs.get("params", {})
    if params is None or not params:
        kwargs["params"] = {}
        kwargs["params"]["cascade"] = str(cascade).lower()

    if entity_id is not None:
        api = api_ctx_delete(project, ENTITY_TYPE, entity_id)
    else:
        kwargs["params"]["name"] = entity_name
        api = api_ctx_list(project, ENTITY_TYPE)
        if delete_all_versions:
            return context.delete_object(api, **kwargs)
        obj = context.list_objects(api, **kwargs)[0]
        entity_id = obj["id"]

    api = api_ctx_delete(project, ENTITY_TYPE, entity_id)
    return context.delete_object(api, **kwargs)


def update_function(entity: Function, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Function
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity_id=entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_functions(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of functions dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
