from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MaterialResponseSchema(BaseModel):
    """Schema for material response."""
    
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
    value: str


class EraResponseSchema(BaseModel):
    """Schema for era response."""
    
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
    value: str


class ArtifactResponseSchema(BaseModel):
    """Schema for artifact response."""
    
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        from_attributes=True,
    )

    inventory_id: UUID = Field(..., description="Unique identifier of the artifact")
    created_at: datetime = Field(
        description="Timestamp when the artifact record was created (UTC)",
    )
    acquisition_date: datetime = Field(
        ..., description="Date when the artifact was acquired"
    )
    name: str = Field(..., description="Name of the artifact")
    department: str = Field(
        ...,
        description="Department responsible for the artifact",
    )
    era: EraResponseSchema = Field(..., description="Historical era of the artifact")
    material: MaterialResponseSchema = Field(..., description="Material of the artifact")
    description: str | None = Field(
        None, description="Optional description of the artifact"
    )
