"""
Base Runtime module.
"""
from __future__ import annotations

from abc import abstractmethod
from typing import Any, Callable

from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.logger import LOGGER


class Runtime:
    """
    Base Runtime class.

    Runtimes are the entities responsible for the actual execution
    of a given run. They are highly specialized components which
    can translate the representation of a given execution as expressed
    in the run into an actual execution operation performed via
    libraries, code, external tools etc.
    """

    ##################################
    # Abstract methods
    ##################################

    # This attribute is a list of allowed actions (tasks)
    # MUST BE explicitly extended in the subclass.
    allowed_actions = []

    def __init__(self) -> None:
        """
        Constructor.
        """
        if not self.allowed_actions:
            raise EntityError(
                "'allowed_actions' attribute must be extended in the subclass with the list of allowed actions."
            )

    @abstractmethod
    def build(self, executable: dict, task: dict, run: dict) -> dict:
        """
        Build run spec.
        """

    @abstractmethod
    def run(self, run: dict) -> dict:
        """
        Execute run task.
        """

    @staticmethod
    @abstractmethod
    def _get_executable(action: str) -> Callable:
        """
        Get executable from action.
        """

    ##################################
    # Private methods
    ##################################

    def _validate_task(self, run: dict) -> str:
        """
        Check if task is allowed. This presumes that the
        runtime holds a list of allowed actions in the self.allowed_actions
        attribute.

        Parameters
        ----------
        run : dict
            Run object dictionary.

        Returns
        -------
        str
            Action to execute.
        """
        action = self._get_action(run)
        if action not in self.allowed_actions:
            msg = f"Task {action} not allowed for {self.__class__.__name__} runtime."
            LOGGER.error(msg)
            raise EntityError(msg)
        return action

    @staticmethod
    def _get_action(run: dict) -> str:
        """
        Get action to execute from run.

        The run object stores in its spec the identifier of the task
        it is associated with. The task string is derived from the
        function string, and has the following format:

        <function-kind>+<task-action>://<project-name>/<function-name>:<function-id>

        Parameters
        ----------
        run : dict
            Run object dictionary.

        Returns
        -------
        str
            Action to execute.

        Raises
        ------
        RuntimeError
            If malformed run spec.

        Examples
        --------
        >>> run = {"spec": {"task": fnckind+action://project/function:uuid4}}
        >>> Runtime._get_action(run)
        'action'
        """
        try:
            return run["spec"]["task"].split(":")[0].split("+")[1]
        except (KeyError, IndexError):
            msg = "Malformed run spec."
            LOGGER.exception(msg)
            raise RuntimeError(msg)

    @staticmethod
    def _execute(func: Callable, *args, **kwargs) -> Any:
        """
        Execute function.

        Parameters
        ----------
        func : Callable
            Function to execute.
        *args
            Function arguments.
        **kwargs
            Function keyword arguments.

        Returns
        -------
        Any
            Function result.
        """
        try:
            return func(*args, **kwargs)
        except Exception:
            msg = "Something got wrong during function execution."
            LOGGER.exception(msg)
            raise RuntimeError(msg)
