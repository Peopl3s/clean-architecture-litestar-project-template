from dataclasses import dataclass
from typing import TYPE_CHECKING, final

import structlog

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.application.exceptions import FailedPublishArtifactMessageBrokerException
from {{cookiecutter.project_slug}}.application.interfaces.mappers import DtoEntityMapperProtocol
from {{cookiecutter.project_slug}}.application.interfaces.message_broker import MessageBrokerPublisherProtocol

if TYPE_CHECKING:
    from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PublishArtifactToBrokerUseCase:
    """
    Use case for publishing an artifact to a message broker.
    """

    message_broker: MessageBrokerPublisherProtocol
    artifact_mapper: DtoEntityMapperProtocol

    async def __call__(self, artifact_dto: ArtifactDTO) -> None:
        """
        Executes the use case to publish an artifact to the message broker.

        Args:
            artifact_dto: The ArtifactDTO to publish.

        Raises:
            FailedPublishArtifactMessageBrokerException: If publishing to the message broker fails.
        """
        try:
            notification_dto = self.artifact_mapper.to_notification_dto(artifact_dto)
            await self.message_broker.publish_new_artifact(notification_dto)
            logger.info(
                "Published new artifact event to message broker",
                inventory_id=artifact_dto.inventory_id,
            )
        except Exception as e:
            logger.warning(
                "Failed to publish artifact notification to message broker (non-critical)",
                inventory_id=artifact_dto.inventory_id,
                error=str(e),
            )
            raise FailedPublishArtifactMessageBrokerException(
                "Failed to publish message to broker", str(e)
            ) from e
