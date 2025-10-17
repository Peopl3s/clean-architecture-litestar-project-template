from dataclasses import dataclass
from typing import final

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO
from {{cookiecutter.project_slug}}.presentation.api.rest.v1.schemas.responses import (
    ArtifactResponseSchema,
    EraResponseSchema,
    MaterialResponseSchema,
)


@final
@dataclass(frozen=True, slots=True)
class ArtifactPresentationMapper:
    """Mapper for converting Application DTOs to Presentation Response models.

    This mapper isolates the Presentation layer from direct dependencies on Application DTOs,
    following Clean Architecture principles.
    """

    def to_response(self, dto: ArtifactDTO) -> ArtifactResponseSchema:
        """Convert Application DTO to API Response model."""
        return ArtifactResponseSchema(
            inventory_id=dto.inventory_id,
            created_at=dto.created_at,
            acquisition_date=dto.acquisition_date,
            name=dto.name,
            department=dto.department,
            era=EraResponseSchema(value=dto.era.value),
            material=MaterialResponseSchema(value=dto.material.value),
            description=dto.description,
        )
