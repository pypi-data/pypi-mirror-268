"""
Task specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class TaskSpec(Spec):
    """Task specification."""

    def __init__(self, function: str) -> None:
        """
        Constructor.
        """
        self.function = function


class TaskParams(SpecParams):
    """
    Base task model.
    """

    function: str
    """Function string."""
