from __future__ import annotations

import importlib
import importlib.metadata
import re
import subprocess
import sys
from types import ModuleType


def import_module(package: str) -> ModuleType:
    """
    Import modules from package name.

    Parameters
    ----------
    package : str
        Package name.

    Returns
    -------
    ModuleType
        Module.
    """
    try:
        return importlib.import_module(package)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Package {package} not found.")
    except Exception as e:
        raise e


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
    module = import_module(module_to_import)
    try:
        return getattr(module, class_name)
    except AttributeError:
        raise ModuleNotFoundError(f"Module {module_to_import} has no '{class_name}' class.")


def list_runtimes() -> list[str]:
    """
    List installed runtimes for digitalhub.

    Returns
    -------
    list
        List of installed runtimes names.
    """
    pattern = r"digitalhub-.*-.*"

    try:
        pip_output = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
        installed_packages = [r.decode().split("==")[0] for r in pip_output.split()]
        return [x.replace("-", "_") for x in installed_packages if re.match(pattern, x)]
    except Exception:
        raise RuntimeError("Error listing installed runtimes.")


def register_runtimes_entities() -> None:
    """
    Register runtimes and related entities into registry.

    Returns
    -------
    None
    """
    for package in list_runtimes():
        import_module(package)


def register_layer_entities() -> None:
    """
    Register layer and related entities into registry.

    Returns
    -------
    None
    """
    for layer in ["core", "data", "ml", "ai"]:
        # Check if package exists
        package = f"digitalhub_{layer}"
        try:
            importlib.metadata.distribution(package)
        except importlib.metadata.PackageNotFoundError:
            # Return because the layers are pyramidal from
            # core to ai
            return

        # Try ot import registry from entities.registries module
        try:
            import_module(f"{package}.entities.registries")
        except Exception:
            pass
