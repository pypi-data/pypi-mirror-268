"""
Metadata factory module.
"""
from __future__ import annotations

import typing

from digitalhub_core.utils.generic_utils import get_timestamp
from digitalhub_core.utils.import_utils import (
    check_layer_existence,
    check_module_existence_by_framework,
    import_class,
    import_registry,
)

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.metadata import Metadata


def build_metadata(
    kind: str,
    layer_digitalhub: str | None = None,
    framework_runtime: str | None = None,
    **kwargs,
) -> Metadata:
    """
    Build entity metadata object.

    Parameters
    ----------
    kind : str
        The type of metadata to build.
    layer_digitalhub : str
        Layer name (e.g. "digitalhub_core") where the metadata is defined.
    framework_runtime : str
        Framework name (e.g. "mlrun", "nefertem") where the metadata is defined.
        This referes to the module where the metadata is defined. The import
        function will search in different layers.

    Returns
    -------
    Metadata
        Metadata object.
    """
    # Raise error if both layer and framework are not provided or if both are provided.
    # This is because we need some information where to search for the metadata class.
    if (layer_digitalhub is None) == (framework_runtime is None):
        raise ValueError("Either layer or framework must be provided, but not both.")

    # If layer is not provided, try to import from runtime, otherwise search by layer.
    if framework_runtime is not None:
        layer_digitalhub = check_module_existence_by_framework(framework_runtime)
    else:
        check_layer_existence(layer_digitalhub)

    # Import registry
    # Note that this requires the creation of a registry whenever a new metadata entity is created.
    module_to_import = f"{layer_digitalhub}.entities.registries"
    registry = import_registry(module_to_import, "metadata_registry")
    class_metadata = _import_class(registry, kind)

    kwargs = parse_arguments(**kwargs)
    return class_metadata(**kwargs)


def parse_arguments(**kwargs) -> dict:
    """
    Parse keyword arguments and add default values if necessary.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    dict
        A dictionary containing the entity metadata attributes.
    """
    if "created" not in kwargs or kwargs["created"] is None:
        kwargs["created"] = get_timestamp()
    if "updated" not in kwargs or kwargs["updated"] is None:
        kwargs["updated"] = kwargs["created"]
    return kwargs


def _import_class(registry: dict, kind: str) -> Metadata:
    """
    Import metadata class from registry.

    Parameters
    ----------
    registry : dict
        Registry.
    kind : str
        Entity kind.

    Returns
    -------
    Metadata
        Metadata class.
    """
    try:
        module_and_class = registry[kind]
    except KeyError:
        raise ValueError(f"Metadata {kind} not found in registry.")

    try:
        module = module_and_class["module"]
        metadata_class = module_and_class["metadata_class"]
    except KeyError:
        raise ValueError("Malformed registration.")

    return import_class(module, metadata_class)
