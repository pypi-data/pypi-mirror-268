"""
Status factory module.
"""
from __future__ import annotations

import typing

from digitalhub_core.entities._base.status import State
from digitalhub_core.utils.import_utils import (
    check_layer_existence,
    check_module_existence_by_framework,
    import_class,
    import_registry,
)

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.status import Status


def build_status(
    kind: str,
    layer_digitalhub: str | None = None,
    framework_runtime: str | None = None,
    **kwargs,
) -> Status:
    """
    Build entity status object.

    Parameters
    ----------
    kind : str
        The type of status to build.
    layer_digitalhub : str
        Layer name (e.g. "digitalhub_core") where the status is defined.
    framework_runtime : str
        Framework name (e.g. "mlrun", "nefertem") where the status is defined.
        This referes to the module where the status is defined. The import
        function will search in different layers.

    Returns
    -------
    Status
        Status object.
    """
    # Raise error if both layer and framework are not provided or if both are provided.
    # This is because we need some information where to search for the status class.
    if (layer_digitalhub is None) == (framework_runtime is None):
        raise ValueError("Either layer or framework must be provided, but not both.")

    # If layer is not provided, try to import from runtime, otherwise search by layer.
    if framework_runtime is not None:
        layer_digitalhub = check_module_existence_by_framework(framework_runtime)
    else:
        check_layer_existence(layer_digitalhub)

    # Import registry
    # Note that this requires the creation of a registry whenever a new status entity is created.
    module_to_import = f"{layer_digitalhub}.entities.registries"
    registry = import_registry(module_to_import, "status_registry")
    class_status = _import_class(registry, kind)

    kwargs = parse_arguments(**kwargs)
    return class_status(**kwargs)


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
        Keyword arguments with default values.
    """
    state = kwargs.get("state")
    if state is None:
        kwargs["state"] = State.CREATED.value
    else:
        if kwargs["state"] not in State.__members__:
            raise ValueError(f"Invalid state: {state}")
    return kwargs


def _import_class(registry: dict, kind: str) -> Status:
    """
    Import status class from registry.

    Parameters
    ----------
    registry : dict
        Registry.
    kind : str
        Entity kind.

    Returns
    -------
    Status
        Status class.
    """
    try:
        module_and_class = registry[kind]
    except KeyError:
        raise ValueError(f"Status {kind} not found in registry.")

    try:
        module = module_and_class["module"]
        status_class = module_and_class["status_class"]
    except KeyError:
        raise ValueError("Malformed registration.")

    return import_class(module, status_class)
