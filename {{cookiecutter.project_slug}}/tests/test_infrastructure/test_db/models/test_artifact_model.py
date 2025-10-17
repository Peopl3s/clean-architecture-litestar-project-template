from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import DateTime, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, registry

from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era
from {{cookiecutter.project_slug}}.domain.value_objects.material import Material

test_mapper_registry = registry()


@test_mapper_registry.mapped
class TestArtifactModel:
    """SQLite-compatible artifact model for testing"""
    __tablename__ = "artifacts"
    __table_args__ = (
        Index("ix_artifacts_name", "name"),
        Index("ix_artifacts_department", "department"),
    )

    def __init__(
            self,
            *,
            inventory_id: str | UUID,
            created_at: datetime,
            acquisition_date: datetime,
            name: str,
            department: str,
            era: str,
            material: str,
            description: str | None = None,
    ) -> None:
        self.inventory_id = str(inventory_id) if isinstance(inventory_id, UUID) else inventory_id
        self.created_at = created_at
        self.acquisition_date = acquisition_date
        self.name = name
        self.department = department
        self.era = era
        self.material = material
        self.description = description

    inventory_id: Mapped[str] = mapped_column(
        String(length=36),
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
        return (
            f"<TestArtifactModel(inventory_id={self.inventory_id!s}, "
            f"name={self.name!r}, department={self.department!r})>"
        )

    def to_dataclass(self) -> ArtifactEntity:
        return ArtifactEntity(
            inventory_id=UUID(self.inventory_id),
            created_at=self.created_at,
            acquisition_date=self.acquisition_date,
            name=self.name,
            department=self.department,
            era=Era(value=self.era),
            material=Material(value=self.material),
            description=self.description,
        )

    @classmethod
    def from_dataclass(
        cls: type["TestArtifactModel"], artifact: ArtifactEntity
    ) -> "TestArtifactModel":
        return cls(
            inventory_id=str(artifact.inventory_id),
            created_at=artifact.created_at,
            acquisition_date=artifact.acquisition_date,
            name=artifact.name,
            department=artifact.department,
            era=str(artifact.era),
            material=str(artifact.material),
            description=artifact.description,
        )
