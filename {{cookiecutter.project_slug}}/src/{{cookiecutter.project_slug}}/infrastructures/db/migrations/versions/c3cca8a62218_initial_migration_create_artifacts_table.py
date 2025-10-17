"""Initial migration: create artifacts table

Revision ID: c3cca8a62218
Revises:
Create Date: 2025-09-25 06:39:37.872475

"""

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c3cca8a62218"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Create artifacts table
    op.create_table(
        "artifacts",
        sa.Column("inventory_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("acquisition_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("department", sa.String(length=255), nullable=False),
        sa.Column("era", sa.String(length=50), nullable=False),
        sa.Column("material", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("inventory_id"),
    )

    # Create indexes
    op.create_index("ix_artifacts_name", "artifacts", ["name"])
    op.create_index("ix_artifacts_department", "artifacts", ["department"])


def downgrade() -> None:
    # Drop indexes
    op.drop_index("ix_artifacts_department", table_name="artifacts")
    op.drop_index("ix_artifacts_name", table_name="artifacts")

    # Drop table
    op.drop_table("artifacts")
