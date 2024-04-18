"""
Artifact operations module.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.artifacts.entity import artifact_from_dict, artifact_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.generic_utils import parse_entity_key
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact


ENTITY_TYPE = "artifacts"


def create_artifact(**kwargs) -> Artifact:
    """
    Create a new artifact with the provided parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Artifact
        Object instance.
    """
    return artifact_from_parameters(**kwargs)


def create_artifact_from_dict(obj: dict) -> Artifact:
    """
    Create a new Artifact instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Artifact
        Artifact object.
    """
    check_context(obj.get("project"))
    return artifact_from_dict(obj)


def new_artifact(
    project: str,
    name: str,
    kind: str,
    path: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    src_path: str | None = None,
    **kwargs,
) -> Artifact:
    """
    Create an instance of the Artifact class with the provided parameters.

    Parameters
    ----------
    project : str
        Project name.
    name : str
        Name that identifies the object.
    kind : str
        Kind of the object.
    path : str
        Destination path of the artifact.
    uuid : str
        ID of the object in form of UUID.
    description : str
        Description of the object.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    src_path : str
        Path to the artifact on local file system.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Artifact
       Object instance.
    """
    obj = create_artifact(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        path=path,
        src_path=src_path,
        **kwargs,
    )
    obj.save()
    return obj


def get_artifact(project: str, entity_name: str | None = None, entity_id: str | None = None, **kwargs) -> Artifact:
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
    Artifact
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
    return create_artifact_from_dict(obj)


def get_artifact_from_key(key: str) -> Artifact:
    """
    Get artifact from key.

    Parameters
    ----------
    key : str
        Key of the artifact.
        It's format is store://<project>/artifacts/<kind>/<name>:<uuid>.
    """
    project, _, _, _, uuid = parse_entity_key(key)
    return get_artifact(project, entity_id=uuid)


def import_artifact(file: str) -> Artifact:
    """
    Import an Artifact object from a file using the specified file path.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Artifact
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_artifact_from_dict(obj)


def delete_artifact(
    project: str,
    entity_name: str | None = None,
    entity_id: str | None = None,
    delete_all_versions: bool = False,
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


def update_artifact(entity: Artifact, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Artifact
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity_id=entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_artifacts(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of artifacts dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
