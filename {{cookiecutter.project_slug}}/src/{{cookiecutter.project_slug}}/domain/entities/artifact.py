from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import final
from uuid import UUID

from {{cookiecutter.project_slug}}.domain.exceptions import DomainValidationError
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era
from {{cookiecutter.project_slug}}.domain.value_objects.material import Material


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArtifactEntity:
    """Domain Entity representing an artifact with business invariants.

    This entity enforces business rules and maintains data integrity
    at the domain level, ensuring that invalid artifacts cannot exist.
    """
    inventory_id: UUID
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    acquisition_date: datetime
    name: str
    department: str
    era: Era
    material: Material
    description: str | None = None

    def __post_init__(self) -> None:
        """
        Validates business invariants of the ArtifactEntity.

        Domain entities must protect their invariants and ensure
        that invalid state cannot exist in the domain model.

        Raises:
            DomainValidationError: If any business invariant is violated.
        """
        if self.acquisition_date > datetime.now(UTC):
            raise DomainValidationError("Acquisition date cannot be in the future")
        if self.acquisition_date > self.created_at:
            raise DomainValidationError("Acquisition date cannot be later than created_at")
        if len(self.name) < 2 or len(self.name) > 100:
            raise DomainValidationError("Name must be between 2 and 100 characters")
        if len(self.department) < 2 or len(self.department) > 100:
            raise DomainValidationError("Department must be between 2 and 100 characters")
        if self.description is not None and len(self.description) > 1000:
            raise DomainValidationError("Description must be at most 1000 characters")
