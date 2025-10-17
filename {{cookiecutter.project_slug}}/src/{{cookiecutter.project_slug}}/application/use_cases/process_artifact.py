from dataclasses import dataclass
from typing import TYPE_CHECKING, final

import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.application.exceptions import ArtifactNotFoundError
from {{cookiecutter.project_slug}}.application.use_cases.fetch_artifact_from_museum_api import (
    FetchArtifactFromMuseumAPIUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.get_artifact_from_cache import (
    GetArtifactFromCacheUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.get_artifact_from_repo import (
    GetArtifactFromRepoUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.publish_artifact_to_broker import (
    PublishArtifactToBrokerUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.publish_artifact_to_catalog import (
    PublishArtifactToCatalogUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.save_artifact_to_cache import (
    SaveArtifactToCacheUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.save_artifact_to_repo import (
    SaveArtifactToRepoUseCase,
)

if TYPE_CHECKING:
    from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProcessArtifactUseCase:
    """
    Use case for processing an artifact, including fetching from cache, repository,
    or external API, saving, and publishing.
    """

    get_artifact_from_cache_use_case: GetArtifactFromCacheUseCase
    get_artifact_from_repo_use_case: GetArtifactFromRepoUseCase
    fetch_artifact_from_museum_api_use_case: FetchArtifactFromMuseumAPIUseCase
    save_artifact_to_repo_use_case: SaveArtifactToRepoUseCase
    save_artifact_to_cache_use_case: SaveArtifactToCacheUseCase
    publish_artifact_to_broker_use_case: PublishArtifactToBrokerUseCase
    publish_artifact_to_catalog_use_case: PublishArtifactToCatalogUseCase

    async def __call__(self, inventory_id: str) -> ArtifactDTO:
        """
        Executes the artifact processing flow.

        Args:
            inventory_id: The ID of the artifact to process.

        Returns:
            An ArtifactDTO representing the processed artifact.
        """
        if artifact_dto := await self.get_artifact_from_cache_use_case(inventory_id):
            return artifact_dto

        if artifact_dto := await self.get_artifact_from_repo_use_case(inventory_id):
            await self.save_artifact_to_cache_use_case(inventory_id, artifact_dto)
            return artifact_dto

        artifact_dto = await self.fetch_artifact_from_museum_api_use_case(inventory_id)
        await self.save_artifact_to_repo_use_case(artifact_dto)
        await self.save_artifact_to_cache_use_case(inventory_id, artifact_dto)

        try:
            await self.publish_artifact_to_broker_use_case(artifact_dto)
        except Exception:
            logger.warning(
                "Failed to publish artifact notification to message broker (non-critical)",
                inventory_id=inventory_id,
            )

        try:
            await self.publish_artifact_to_catalog_use_case(artifact_dto)
        except Exception:
            logger.warning(
                "Failed to publish artifact to public catalog (non-critical)",
                inventory_id=inventory_id,
            )

        logger.info(
            "Artifact successfully fetched and processed",
            inventory_id=inventory_id,
        )
        return artifact_dto
