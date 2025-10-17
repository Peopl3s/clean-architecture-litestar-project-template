from dataclasses import dataclass
from typing import final

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactAdmissionNotificationDTO,
    ArtifactCatalogPublicationDTO,
    ArtifactDTO,
    EraDTO,
    MaterialDTO,
)
from {{cookiecutter.project_slug}}.application.interfaces.mappers import DtoEntityMapperProtocol
from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era
from {{cookiecutter.project_slug}}.domain.value_objects.material import Material


@final
@dataclass(frozen=True, slots=True)
class ArtifactMapper(DtoEntityMapperProtocol):
    """Mapper for converting between Domain Entities and Application DTOs.

    This mapper is part of the Application layer and handles conversions between:
    - Domain Entities (business logic)
    - Application DTOs (use case data transfer)

    It does NOT handle infrastructure concerns like JSON serialization.
    """

    def to_dto(self, entity: ArtifactEntity) -> ArtifactDTO:
        """Convert Domain Entity to Application DTO."""
        return ArtifactDTO(
            inventory_id=entity.inventory_id,
            created_at=entity.created_at,
            acquisition_date=entity.acquisition_date,
            name=entity.name,
            department=entity.department,
            era=EraDTO(value=entity.era.value),
            material=MaterialDTO(value=entity.material.value),
            description=entity.description,
        )

    def to_entity(self, dto: ArtifactDTO) -> ArtifactEntity:
        """Convert Application DTO to Domain Entity."""
        return ArtifactEntity(
            inventory_id=dto.inventory_id,
            name=dto.name,
            acquisition_date=dto.acquisition_date,
            department=dto.department,
            era=Era(value=dto.era.value),
            material=Material(value=dto.material.value),
            description=dto.description,
        )

    def to_notification_dto(
        self, entity: ArtifactEntity
    ) -> ArtifactAdmissionNotificationDTO:
        """Convert Domain Entity to Notification DTO for message broker."""
        return ArtifactAdmissionNotificationDTO(
            inventory_id=entity.inventory_id,
            name=entity.name,
            acquisition_date=entity.acquisition_date,
            department=entity.department,
        )

    def to_publication_dto(
        self, entity: ArtifactEntity
    ) -> ArtifactCatalogPublicationDTO:
        """Convert Domain Entity to Publication DTO for external catalog API."""
        return ArtifactCatalogPublicationDTO(
            inventory_id=entity.inventory_id,
            name=entity.name,
            era=EraDTO(value=entity.era.value),
            material=MaterialDTO(value=entity.material.value),
            description=entity.description,
        )
