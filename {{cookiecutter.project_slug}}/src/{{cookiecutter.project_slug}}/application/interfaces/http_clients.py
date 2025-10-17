from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactCatalogPublicationDTO, ArtifactDTO


class ExternalMuseumAPIProtocol(Protocol):
    """
    Protocol for interacting with an external museum API.
    """

    @abstractmethod
    async def fetch_artifact(self, inventory_id: str | UUID) -> ArtifactDTO:
        """
        Fetches an artifact from the external museum API.

        Args:
            inventory_id: The ID of the artifact to fetch.

        Returns:
            An ArtifactDTO object.
        """
        ...


class PublicCatalogAPIProtocol(Protocol):
    """
    Protocol for interacting with a public catalog API.
    """

    @abstractmethod
    async def publish_artifact(
        self, artifact: ArtifactCatalogPublicationDTO
    ) -> str:
        """
        Publishes an artifact to the public catalog API.

        Args:
            artifact: The ArtifactCatalogPublicationDTO to publish.

        Returns:
            A string representing the publication status or ID.
        """
        ...
