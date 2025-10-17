from dataclasses import dataclass
from typing import TYPE_CHECKING, final

import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.application.interfaces.cache import CacheProtocol
from {{cookiecutter.project_slug}}.application.interfaces.serialization import SerializationMapperProtocol

if TYPE_CHECKING:
    from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetArtifactFromCacheUseCase:
    """
    Use case for retrieving an artifact from the cache.
    """

    cache_client: CacheProtocol
    serialization_mapper: SerializationMapperProtocol

    async def __call__(self, inventory_id: str) -> ArtifactDTO | None:
        """
        Executes the use case to get an artifact from the cache.

        Args:
            inventory_id: The ID of the artifact to retrieve.

        Returns:
            An ArtifactDTO if found in cache, otherwise None.
        """
        cached_artifact_data: dict | None = await self.cache_client.get(inventory_id)
        if cached_artifact_data:
            logger.info("Artifact found in cache", inventory_id=inventory_id)
            return self.serialization_mapper.from_dict(cached_artifact_data)
        logger.info("Artifact not found in cache", inventory_id=inventory_id)
        return None
