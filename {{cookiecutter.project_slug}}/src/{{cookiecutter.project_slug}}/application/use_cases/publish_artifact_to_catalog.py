from dataclasses import dataclass
from typing import TYPE_CHECKING, final

import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.application.exceptions import FailedPublishArtifactInCatalogException
from {{cookiecutter.project_slug}}.application.interfaces.http_clients import PublicCatalogAPIProtocol
from {{cookiecutter.project_slug}}.application.interfaces.mappers import DtoEntityMapperProtocol

if TYPE_CHECKING:
    from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PublishArtifactToCatalogUseCase:
    """
    Use case for publishing an artifact to a public catalog.
    """

    catalog_api_client: PublicCatalogAPIProtocol
    artifact_mapper: DtoEntityMapperProtocol

    async def __call__(self, artifact_dto: ArtifactDTO) -> None:
        """
        Executes the use case to publish an artifact to the public catalog.

        Args:
            artifact_dto: The ArtifactDTO to publish.

        Raises:
            FailedPublishArtifactInCatalogException: If publishing to the catalog fails.
        """
        try:
            publication_dto = self.artifact_mapper.to_publication_dto(artifact_dto)
            public_id: str = await self.catalog_api_client.publish_artifact(
                publication_dto
            )
            logger.info(
                "Artifact published to public catalog",
                inventory_id=artifact_dto.inventory_id,
                public_id=public_id,
            )
        except Exception as e:
            logger.exception(
                "Failed to publish artifact to catalog",
                inventory_id=artifact_dto.inventory_id,
                error=str(e),
            )
            raise FailedPublishArtifactInCatalogException(
                "Could not publish artifact to catalog", str(e)
            ) from e
