"""
Import utils module.
"""
from __future__ import annotations

import importlib
import importlib.metadata


def check_module_existence_by_framework(framework: str) -> str:
    """
    Try to import registry from implemented module.

    Parameters
    ----------
    framework : str
        Framework name.

    Returns
    -------
    str
        Valid module name.
    """
    # Cycle over digitalhub layers modules (core, data, ml, ai).
    for layer in ["core", "data", "ml", "ai"]:
        # Try to import module
        module_name = f"digitalhub_{layer}_{framework}"
        try:
            importlib.metadata.distribution(module_name)
            return module_name
        except importlib.metadata.PackageNotFoundError:
            continue
    # If no module is found raise error
    else:
        raise ModuleNotFoundError(f"Module not found in digitalhub layers core, data, ml, ai for framework {framework}")


def check_layer_existence(layer: str) -> None:
    """
    Check if layer exists.

    Parameters
    ----------
    layer : str
        Layer name.

    Returns
    -------
    None
    """
    try:
        importlib.metadata.distribution(layer)
    except importlib.metadata.PackageNotFoundError:
        raise ModuleNotFoundError(f"Layer {layer} not found.")


def import_registry(module_to_import: str, registry: str) -> dict:
    """
    Import registry from implemented module.

    Parameters
    ----------
    module_to_import : str
        Module name.
    registry : str
        Registry name.

    Returns
    -------
    dict
        Registry.
    """
    module = importlib.import_module(module_to_import)
    try:
        return getattr(module, registry)
    except AttributeError:
        raise ModuleNotFoundError(f"Module {module_to_import} has no '{registry}'.")


def import_class(module_to_import: str, class_name: str) -> type:
    """
    Import class from implemented module.

    Parameters
    ----------
    module_to_import : str
        Module name.
    class_name : str
        Class name.

    Returns
    -------
    type
        Class.
    """
    module = importlib.import_module(module_to_import)
    try:
        return getattr(module, class_name)
    except AttributeError:
        raise ModuleNotFoundError(f"Module {module_to_import} has no '{class_name}' class.")
