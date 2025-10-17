"""Database mapper for converting between Domain Entities and SQLAlchemy Models.

This mapper is responsible for the conversion logic between the domain layer
and the database persistence layer, following the Single Responsibility Principle.
"""

from dataclasses import dataclass
from typing import final

from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era
from {{cookiecutter.project_slug}}.domain.value_objects.material import Material
from {{cookiecutter.project_slug}}.infrastructures.db.models.artifact import ArtifactModel


@final
@dataclass(frozen=True, slots=True)
class ArtifactDBMapper:
    """
    Mapper for converting between ArtifactEntity (Domain) and ArtifactModel (SQLAlchemy).

    This class provides methods for bidirectional mapping, ensuring separation of concerns
    between the domain logic and database persistence.
    """

    def to_entity(self, model: ArtifactModel) -> ArtifactEntity:
        """
        Converts an SQLAlchemy ArtifactModel to a Domain ArtifactEntity.

        Args:
            model: The SQLAlchemy ArtifactModel instance.

        Returns:
            An ArtifactEntity instance.
        """
        return ArtifactEntity(
            inventory_id=model.inventory_id,
            created_at=model.created_at,
            acquisition_date=model.acquisition_date,
            name=model.name,
            department=model.department,
            era=Era(value=model.era),
            material=Material(value=model.material),
            description=model.description,
        )

    def to_model(self, entity: ArtifactEntity) -> ArtifactModel:
        """
        Converts a Domain ArtifactEntity to an SQLAlchemy ArtifactModel.

        Args:
            entity: The Domain ArtifactEntity instance.

        Returns:
            An SQLAlchemy ArtifactModel instance.
        """
        return ArtifactModel(
            inventory_id=entity.inventory_id,
            created_at=entity.created_at,
            acquisition_date=entity.acquisition_date,
            name=entity.name,
            department=entity.department,
            era=str(entity.era),
            material=str(entity.material),
            description=entity.description,
        )

    def update_model_from_entity(
        self, model: ArtifactModel, entity: ArtifactEntity
    ) -> None:
        """
        Updates an existing SQLAlchemy ArtifactModel with data from a Domain ArtifactEntity.

        This method is used for updating database records based on changes in the domain entity.

        Args:
            model: The existing SQLAlchemy ArtifactModel to update.
            entity: The Domain ArtifactEntity containing the new data.
        """
        model.name = entity.name
        model.era = str(entity.era)
        model.material = str(entity.material)
        model.description = entity.description
        model.acquisition_date = entity.acquisition_date
        model.department = entity.department
