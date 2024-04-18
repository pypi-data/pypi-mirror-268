from __future__ import annotations

from pydantic import BaseModel


class RuntimeEntry(BaseModel):
    """
    Model for Runtime entry.
    """

    module: str
    """Module path."""

    class_name: str
    """Class name."""


class SpecEntry(BaseModel):
    """
    Model for Spec entry.
    """

    module: str
    """Module path."""

    class_name: str
    """Class name."""

    parameters_validator: str
    """Class name of the parameter validator."""


class StatusEntry(BaseModel):
    """
    Model for Status entry.
    """

    module: str
    """Module path."""

    class_name: str
    """Class name."""


class MetadataEntry(BaseModel):
    """
    Model for Metadata entry.
    """

    module: str
    """Module path."""

    class_name: str
    """Class name."""


class RegistryEntry(BaseModel):
    entity_type: str
    """Entity type."""

    spec: SpecEntry
    """Spec infos."""

    status: StatusEntry
    """Status infos."""

    metadata: MetadataEntry
    """Metadata infos."""

    runtime: RuntimeEntry = None
    """Runtime infos."""
