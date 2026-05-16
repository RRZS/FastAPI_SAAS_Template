"""Lead Table

Revision ID: c1a2b3d4e5f6
Revises: 80f9e1cc8879
Create Date: 2026-05-16 00:00:00.000000

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c1a2b3d4e5f6"
down_revision = "80f9e1cc8879"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "lead",
        sa.Column("id", sa.Integer),
        sa.Column("org_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("message", sa.String(), nullable=True),
        sa.Column("source", sa.String(), nullable=False, server_default=sa.text("'web'")),
        sa.Column("status", sa.String(), nullable=False, server_default=sa.text("'new'")),
        sa.Column("contacted_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column(
            "date_created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.Column(
            "date_updated", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["org_id"], ["organization.id"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_constraint("lead_org_id_fkey", table_name="lead")
    op.drop_table("lead")
