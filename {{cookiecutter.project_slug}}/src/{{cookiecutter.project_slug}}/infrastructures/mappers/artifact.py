from dataclasses import dataclass
from datetime import datetime
from typing import final
from uuid import UUID

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactAdmissionNotificationDTO,
    ArtifactCatalogPublicationDTO,
    ArtifactDTO,
    EraDTO,
    MaterialDTO,
)
from {{cookiecutter.project_slug}}.application.interfaces.serialization import SerializationMapperProtocol


@final
@dataclass(frozen=True, slots=True)
class InfrastructureArtifactMapper(SerializationMapperProtocol):
    """Mapper for converting Application DTOs to
    dictionaries for external API communication.

    This mapper implements:
    - SerializationMapperProtocol: JSON serialization/deserialization
    for caching and external APIs
    """

    def to_dict(self, dto: ArtifactDTO) -> dict:
        """
        Converts an Application ArtifactDTO to a dictionary for JSON serialization
        (e.g., caching, external APIs).
        """
        return {
            "inventory_id": str(dto.inventory_id),
            "created_at": dto.created_at.isoformat(),
            "acquisition_date": dto.acquisition_date.isoformat(),
            "name": dto.name,
            "department": dto.department,
            "era": {"value": dto.era.value},
            "material": {"value": dto.material.value},
            "description": dto.description,
        }

    def from_dict(self, data: dict) -> ArtifactDTO:
        """
        Converts a dictionary from JSON deserialization to an Application ArtifactDTO.
        """
        return ArtifactDTO(
            inventory_id=UUID(data["inventory_id"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            acquisition_date=datetime.fromisoformat(data["acquisition_date"]),
            name=data["name"],
            department=data["department"],
            era=EraDTO(value=data["era"]["value"]),
            material=MaterialDTO(value=data["material"]["value"]),
            description=data.get("description"),
        )

    def to_admission_notification_dict(
        self, dto: ArtifactAdmissionNotificationDTO
    ) -> dict:
        """
        Converts an ArtifactAdmissionNotificationDTO to
        a dictionary for message broker communication.
        """
        return {
            "inventory_id": str(dto.inventory_id),
            "name": dto.name,
            "acquisition_date": dto.acquisition_date.isoformat(),
            "department": dto.department,
        }

    def to_catalog_publication_dict(
        self, dto: ArtifactCatalogPublicationDTO
    ) -> dict:
        """
        Converts an ArtifactCatalogPublicationDTO to a dictionary
        for external catalog API communication.
        """
        return {
            "inventory_id": str(dto.inventory_id),
            "name": dto.name,
            "era": {"value": dto.era.value},
            "material": {"value": dto.material.value},
            "description": dto.description,
        }
