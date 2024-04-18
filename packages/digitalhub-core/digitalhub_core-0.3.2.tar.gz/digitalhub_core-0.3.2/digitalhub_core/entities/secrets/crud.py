"""
Secret operations module.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.entities.secrets.entity import secret_from_dict, secret_from_parameters
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.io_utils import read_yaml

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.secrets.entity import Secret


ENTITY_TYPE = "secrets"


def create_secret(**kwargs) -> Secret:
    """
    Create a new Secret instance with the specified parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Secret
        An instance of the created secret.
    """
    return secret_from_parameters(**kwargs)


def create_secret_from_dict(obj: dict) -> Secret:
    """
    Create a new Secret instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Secret
        Secret object.
    """
    check_context(obj.get("project"))
    return secret_from_dict(obj)


def new_secret(
    project: str,
    name: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    secret_value: str | None = None,
    **kwargs,
) -> Secret:
    """
    Create a new Secret instance with the specified parameters.

    Parameters
    ----------
    project : str
        A string representing the project associated with this secret.
    name : str
        The name of the secret.
    uuid : str
        ID of the object in form of UUID.
    description : str
        A description of the secret.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    secret_value : str
        Value of the secret.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Secret
        An instance of the created secret.
    """
    if secret_value is None:
        raise ValueError("secret_value must be provided.")

    obj = create_secret(
        project=project,
        name=name,
        kind="secret",
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        **kwargs,
    )
    obj.save()
    obj.set_secret_value(value=secret_value)
    return obj


def get_secret(project: str, entity_name: str | None = None, entity_id: str | None = None, **kwargs) -> Secret:
    """
    Retrieves secret details from backend.

    Parameters
    ----------

    project : str
        Project name.
    name : str
        The name of the secret.
    uuid : str
        ID of the object in form of UUID.

    Returns
    -------
    Secret
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
    return create_secret_from_dict(obj)


def import_secret(file: str) -> Secret:
    """
    Import an Secret object from a file using the specified file path.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Secret
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_secret_from_dict(obj)


def delete_secret(
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


def update_secret(entity: Secret, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Secret
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity_id=entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_secrets(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of secrets dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
