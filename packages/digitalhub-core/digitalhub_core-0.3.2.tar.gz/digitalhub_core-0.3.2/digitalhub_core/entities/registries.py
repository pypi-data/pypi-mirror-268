from __future__ import annotations

from digitalhub_core.entities._base.metadata import MetadataRegistry
from digitalhub_core.entities._base.spec import SpecRegistry
from digitalhub_core.entities._base.status import StatusRegistry

metadata_registry = MetadataRegistry()
spec_registry = SpecRegistry()
status_registry = StatusRegistry()

for i in [
    "artifact",
    "project",
    "secret",
    "service",
    "workflow",
]:
    root = f"digitalhub_core.entities.{i}s"
    metadata_registry.register(i, f"{root}.metadata", f"{i.title()}Metadata")
    spec_registry.register(i, f"{root}.spec", f"{i.title()}Spec", f"{i.title()}Params")
    status_registry.register(i, f"{root}.status", f"{i.title()}Status")
