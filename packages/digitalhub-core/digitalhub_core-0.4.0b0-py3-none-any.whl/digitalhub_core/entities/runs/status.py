"""
RunStatus class module.
"""
from __future__ import annotations

import typing

from digitalhub_core.entities._base.status import Status
from digitalhub_core.entities.artifacts.crud import get_artifact_from_key
from digitalhub_core.utils.generic_utils import parse_entity_key

if typing.TYPE_CHECKING:
    from digitalhub_core.entities._base.entity import Entity

ENTITY_FUNC = {
    "artifacts": get_artifact_from_key,
}


class RunStatus(Status):
    """
    Status class for run entities.
    """

    def __init__(
        self,
        state: str,
        message: str | None = None,
        outputs: list | None = None,
        results: dict | None = None,
    ) -> None:
        """
        Constructor.
        """
        super().__init__(state, message)
        self.outputs = outputs
        self.results = results

    def get_results(self) -> dict:
        """
        Get results.

        Returns
        -------
        dict
            The results.
        """
        return self.results if self.results is not None else {}

    def get_outputs(self, as_key: bool = False, as_dict: bool = False) -> list[dict[str, str | dict | Entity]]:
        """
        Get outputs.

        Parameters
        ----------
        as_key : bool
            If True, return outputs as keys.
        as_dict : bool
            If True, return outputs as dictionaries.

        Returns
        -------
        list[dict[str, str | dict | Entity]]
            The outputs.
        """
        outputs = []
        if self.outputs is None:
            return outputs

        for i in self.outputs:
            for parameter, key in i.items():
                entity_type = self._get_entity_type(key)
                entity = ENTITY_FUNC[entity_type](key)
                if as_key:
                    entity = entity.key
                if as_dict:
                    entity = entity.to_dict()
                outputs.append({parameter: entity})

        return outputs

    @staticmethod
    def _get_entity_type(key: str) -> str:
        """
        Get entity type.

        Parameters
        ----------
        key : str
            The key of the entity.

        Returns
        -------
        str
            The entity type.
        """
        _, entity_type, _, _, _ = parse_entity_key(key)
        return entity_type

    def get_values(self, values_list: list) -> list:
        """
        Get values.

        Parameters
        ----------
        values_list : list
            The values list to search in.

        Returns
        -------
        list
            The values.
        """
        return {k: v for k, v in self.get_results().items() if k in values_list}
