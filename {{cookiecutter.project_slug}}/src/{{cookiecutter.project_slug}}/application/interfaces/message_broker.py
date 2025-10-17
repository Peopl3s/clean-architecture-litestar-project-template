from abc import abstractmethod
from typing import Protocol

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactAdmissionNotificationDTO


class MessageBrokerPublisherProtocol(Protocol):
    """
    Protocol for publishing messages to a message broker.
    """

    @abstractmethod
    async def publish_new_artifact(
        self, artifact: ArtifactAdmissionNotificationDTO
    ) -> None:
        """
        Publishes a new artifact admission notification to the message broker.

        Args:
            artifact: The ArtifactAdmissionNotificationDTO to publish.
        """
        ...
