from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity


class ArtifactRepositoryProtocol(Protocol):
    """
    Protocol for an artifact repository.
    Defines methods for retrieving and saving artifact entities.
    """

    @abstractmethod
    async def get_by_inventory_id(
        self, inventory_id: str | UUID
    ) -> ArtifactEntity | None:
        """
        Retrieves an artifact by its inventory ID.

        Args:
            inventory_id: The unique identifier of the artifact.

        Returns:
            The ArtifactEntity if found, otherwise None.
        """
        ...

    @abstractmethod
    async def save(self, artifact: ArtifactEntity) -> None:
        """
        Saves a new artifact or updates an existing one.

        Args:
            artifact: The ArtifactEntity to save.
        """
        ...
