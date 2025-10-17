from dataclasses import dataclass
from typing import final
from uuid import UUID

import httpx
import stamina
import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactCatalogPublicationDTO,
    ArtifactDTO,
)
from {{cookiecutter.project_slug}}.application.exceptions import ArtifactNotFoundError
from {{cookiecutter.project_slug}}.application.interfaces.http_clients import (
    ExternalMuseumAPIProtocol,
    PublicCatalogAPIProtocol,
)
from {{cookiecutter.project_slug}}.infrastructures.mappers.artifact import InfrastructureArtifactMapper

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ExternalMuseumAPIClient(ExternalMuseumAPIProtocol):
    """
    Client for interacting with an external museum API to fetch artifact data.
    """
    base_url: str
    client: httpx.AsyncClient
    mapper: InfrastructureArtifactMapper

    @stamina.retry(
        on=(httpx.HTTPError, httpx.RequestError),
        attempts=3,
        wait_initial=0.5,
        wait_jitter=1.0,
    )
    async def fetch_artifact(self, inventory_id: str | UUID) -> ArtifactDTO:
        """
        Fetches an artifact from the external museum API.

        Args:
            inventory_id: The ID of the artifact to fetch.

        Returns:
            An ArtifactDTO object if found.

        Raises:
            ArtifactNotFoundError: If the artifact is not found (404).
            httpx.HTTPStatusError: For other HTTP errors.
            httpx.RequestError: For network-related errors.
            ValueError: If data validation fails.
            Exception: For any other unexpected errors.
        """
        inventory_id_str = (
            str(inventory_id) if isinstance(inventory_id, UUID) else inventory_id
        )
        url = f"{self.base_url}/artifacts/{inventory_id_str}"
        logger.debug("Fetching artifact from URL", url=url)

        try:
            response = await self.client.get(url)
            if response.status_code == 404:
                logger.warning("Artifact not found (404)", inventory_id=inventory_id_str)
                raise ArtifactNotFoundError(
                    f"Artifact {inventory_id_str} not found in external service"
                )

            response.raise_for_status()
            data = response.json()

            logger.debug("Successfully fetched artifact", data=data)

            return self.mapper.from_dict(data)

        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            logger.exception(
                "HTTP error while fetching artifact",
                inventory_id=inventory_id_str,
                error=str(e),
            )
            raise
        except ValueError as e:
            logger.exception(
                "Data validation error for artifact",
                inventory_id=inventory_id_str,
                error=str(e),
            )
            raise
        except Exception as e:
            logger.exception(
                "Unexpected error while fetching artifact",
                inventory_id=inventory_id_str,
                error=str(e),
            )
            raise


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PublicCatalogAPIClient(PublicCatalogAPIProtocol):
    """
    Client for interacting with a public catalog API to publish artifact data.
    """
    base_url: str
    client: httpx.AsyncClient
    mapper: InfrastructureArtifactMapper

    @stamina.retry(
        on=(httpx.HTTPError, httpx.RequestError),
        attempts=3,
        wait_initial=1.0,
        wait_jitter=1.0,
    )
    async def publish_artifact(self, artifact: ArtifactCatalogPublicationDTO) -> str:
        """
        Publishes an artifact to the public catalog API.

        Args:
            artifact: The ArtifactCatalogPublicationDTO to publish.

        Returns:
            A string representing the public ID of the published artifact.

        Raises:
            httpx.HTTPStatusError: For HTTP errors during publication.
            httpx.RequestError: For network-related errors.
            ValueError: If the response data is missing the 'public_id'.
            Exception: For any other unexpected errors.
        """
        payload = self.mapper.to_catalog_publication_dict(artifact)

        url = f"{self.base_url}/items"
        logger.debug("Publishing artifact to URL", url=url, payload=payload)

        try:
            response = await self.client.post(
                url, json=payload, timeout=httpx.Timeout(10.0)
            )
            response.raise_for_status()
            data = response.json()
        except (httpx.HTTPStatusError, httpx.RequestError) as e:
            logger.exception("Error during HTTP request", url=url, error=str(e))
            raise
        except Exception as e:
            logger.exception("Unexpected error during publishing artifact", error=str(e))
            raise Exception("Failed to publish artifact to catalog: %s", e) from e

        public_id = str(data.get("public_id", ""))
        if not public_id:
            logger.exception("Response JSON missing 'public_id' field", data=data)
            raise ValueError("Invalid response data: missing 'public_id'")

        logger.debug("Successfully published artifact", public_id=public_id)
        return public_id
