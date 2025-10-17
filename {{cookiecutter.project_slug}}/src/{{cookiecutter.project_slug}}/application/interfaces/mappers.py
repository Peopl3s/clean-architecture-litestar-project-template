from abc import abstractmethod
from typing import Protocol

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactAdmissionNotificationDTO,
    ArtifactCatalogPublicationDTO,
    ArtifactDTO,
)
from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity


class DtoEntityMapperProtocol(Protocol):
    """Protocol for Application layer mapper (Domain Entity <-> Application DTO)."""

    @abstractmethod
    def to_dto(self, entity: ArtifactEntity) -> ArtifactDTO:
        """Converts a Domain Entity to an Application DTO."""
        ...

    @abstractmethod
    def to_entity(self, dto: ArtifactDTO) -> ArtifactEntity:
        """Converts an Application DTO to a Domain Entity."""
        ...

    @abstractmethod
    def to_notification_dto(
        self, entity: ArtifactEntity
    ) -> ArtifactAdmissionNotificationDTO:
        """Converts a Domain Entity to an ArtifactAdmissionNotificationDTO."""
        ...

    @abstractmethod
    def to_publication_dto(
        self, entity: ArtifactEntity
    ) -> ArtifactCatalogPublicationDTO:
        """Converts a Domain Entity to an ArtifactCatalogPublicationDTO."""
        ...
