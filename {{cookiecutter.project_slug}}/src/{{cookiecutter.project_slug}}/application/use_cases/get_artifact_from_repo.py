from dataclasses import dataclass
from typing import TYPE_CHECKING, final

import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.application.interfaces.mappers import DtoEntityMapperProtocol
from {{cookiecutter.project_slug}}.application.interfaces.repositories import ArtifactRepositoryProtocol
from {{cookiecutter.project_slug}}.application.interfaces.uow import UnitOfWorkProtocol

if TYPE_CHECKING:
    from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetArtifactFromRepoUseCase:
    """
    Use case for retrieving an artifact from the repository.
    """

    uow: UnitOfWorkProtocol
    artifact_mapper: DtoEntityMapperProtocol

    async def __call__(self, inventory_id: str) -> ArtifactDTO | None:
        """
        Executes the use case to get an artifact from the repository.

        Args:
            inventory_id: The ID of the artifact to retrieve.

        Returns:
            An ArtifactDTO if found in the repository, otherwise None.
        """
        async with self.uow:
            artifact_entity: (
                ArtifactEntity | None
            ) = await self.uow.repository.get_by_inventory_id(inventory_id)
            if artifact_entity:
                logger.info("Artifact found in repository", inventory_id=inventory_id)
                return self.artifact_mapper.to_dto(artifact_entity)
            logger.info("Artifact not found in repository", inventory_id=inventory_id)
            return None
