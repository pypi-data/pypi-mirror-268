"""
Spec factory entity.
"""
from __future__ import annotations

import typing

from digitalhub_core.utils.import_utils import (
    check_layer_existence,
    check_module_existence_by_framework,
    import_class,
    import_registry,
)

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.spec import Spec, SpecParams


def build_spec(
    kind: str,
    layer_digitalhub: str | None = None,
    framework_runtime: str | None = None,
    validate: bool = True,
    **kwargs,
) -> Spec:
    """
    Build entity spec object.

    Parameters
    ----------
    kind : str
        The type of spec to build.
    layer_digitalhub : str
        Layer name (e.g. "digitalhub_core") where the spec is defined.
    framework_runtime : str
        Framework name (e.g. "mlrun", "nefertem") where the spec is defined.
        This referes to the module where the spec is defined. The import
        function will search in different layers.
    validate : bool
        Flag to determine if arguments validation against a pydantic schema must be ignored.

    Returns
    -------
    Spec
        Spec object.
    """
    # Raise error if both layer and framework are not provided or if both are provided.
    # This is because we need some information where to search for the spec class.
    if (layer_digitalhub is None) == (framework_runtime is None):
        raise ValueError("Either layer or framework must be provided, but not both.")

    # If layer is not provided, try to import from runtime, otherwise search by layer.
    if framework_runtime is not None:
        layer_digitalhub = check_module_existence_by_framework(framework_runtime)
    else:
        check_layer_existence(layer_digitalhub)

    # Import registry
    # Note that this requires the creation of a registry whenever a new spec entity is created.
    module_to_import = f"{layer_digitalhub}.entities.registries"
    registry = import_registry(module_to_import, "spec_registry")

    # Import classes
    class_spec, class_params = _import_classes(registry, kind)

    # Validate arguments
    if validate:
        kwargs = class_params(**kwargs).dict(by_alias=True, exclude_none=True)

    return class_spec(**kwargs)


def _import_classes(registry: dict[str, dict[str, str]], kind: str) -> tuple[Spec, SpecParams]:
    """
    Import spec and params classes from registry.

    Parameters
    ----------
    registry : dict
        Registry.
    kind : str
        Entity kind.

    Returns
    -------
    tuple
        Spec class and params class.
    """
    try:
        module_and_class = registry[kind]
    except KeyError:
        raise ValueError(f"Spec {kind} not found in registry.")

    try:
        module = module_and_class["module"]
        spec_class = module_and_class["spec_class"]
        param_class = module_and_class["spec_params"]
    except KeyError:
        raise ValueError("Malformed registration.")

    return import_class(module, spec_class), import_class(module, param_class)
