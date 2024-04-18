"""
Runtime factory entity.
"""
from __future__ import annotations

import typing

from digitalhub_core.registry.import_utils import import_class
from digitalhub_core.registry.registry import registry

if typing.TYPE_CHECKING:
    from digitalhub_core.registry.models import RegistryEntry
    from digitalhub_core.runtimes.base import Runtime


def build_runtime(kind: str) -> Runtime:
    """
    Build runtime object.

    Parameters
    ----------
    kind : str
        The type of runtime to build.

    Returns
    -------
    Runtime
        Runtime object.
    """
    infos: RegistryEntry = getattr(registry, kind)
    runtime = import_class(infos.runtime.module, infos.runtime.class_name)
    return runtime()
