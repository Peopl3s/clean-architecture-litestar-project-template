from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import DateTime, Index, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, registry

mapper_registry = registry()


@mapper_registry.mapped
class ArtifactModel:
    """
    SQLAlchemy model for storing artifact data.

    Maps to the 'artifacts' table in the database.
    """
    __tablename__ = "artifacts"
    __table_args__ = (
        Index("ix_artifacts_name", "name"),
        Index("ix_artifacts_department", "department"),
    )

    def __init__(
            self,
            *,
            inventory_id: UUID,
            created_at: datetime,
            acquisition_date: datetime,
            name: str,
            department: str,
            era: str,
            material: str,
            description: str | None = None,
    ) -> None:
        """
        Initializes a new ArtifactModel instance.

        Args:
            inventory_id: Unique identifier for the artifact.
            created_at: Timestamp when the artifact record was created.
            acquisition_date: Date when the artifact was acquired.
            name: Name of the artifact.
            department: Department where the artifact is located.
            era: Historical era of the artifact.
            material: Primary material of the artifact.
            description: Optional description of the artifact.
        """
        self.inventory_id = inventory_id
        self.created_at = created_at
        self.acquisition_date = acquisition_date
        self.name = name
        self.department = department
        self.era = era
        self.material = material
        self.description = description

    inventory_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
        server_default=func.now(),
    )
    acquisition_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    department: Mapped[str] = mapped_column(String(length=255), nullable=False)
    era: Mapped[str] = mapped_column(String(length=50), nullable=False)
    material: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        """
        Returns a string representation of the ArtifactModel.
        """
        return (
            f"<ArtifactModel(inventory_id={self.inventory_id!s}, "
            f"name={self.name!r}, department={self.department!r})>"
        )
