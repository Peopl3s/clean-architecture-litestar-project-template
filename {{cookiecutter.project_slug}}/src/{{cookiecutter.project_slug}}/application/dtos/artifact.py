from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Literal, final
from uuid import UUID


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MaterialDTO:
    """Data Transfer Object for Material."""
    value: Literal[
        "ceramic",
        "metal",
        "stone",
        "glass",
        "bone",
        "wood",
        "textile",
        "other",
    ]


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class EraDTO:
    """Data Transfer Object for Era."""
    value: Literal[
        "paleolithic",
        "neolithic",
        "bronze_age",
        "iron_age",
        "antiquity",
        "middle_ages",
        "modern",
    ]


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArtifactDTO:
    """Application DTO for transferring artifact data between layers.

    Note: This DTO does NOT perform business validation.
    Business rules are enforced by the Domain Entity (ArtifactEntity).
    DTOs are simple data carriers for inter-layer communication.
    """
    inventory_id: UUID
    acquisition_date: datetime
    name: str
    department: str
    era: EraDTO
    material: MaterialDTO
    description: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArtifactAdmissionNotificationDTO:
    """DTO for artifact admission notifications."""
    inventory_id: UUID
    name: str
    acquisition_date: datetime
    department: str


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArtifactCatalogPublicationDTO:
    """DTO for publishing artifacts to the catalog."""
    inventory_id: UUID
    name: str
    era: EraDTO
    material: MaterialDTO
    description: str | None = None
