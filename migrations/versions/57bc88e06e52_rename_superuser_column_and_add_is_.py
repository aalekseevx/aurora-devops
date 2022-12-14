"""Rename superuser column and add is_official for chats

Revision ID: 57bc88e06e52
Revises: c7025892455f
Create Date: 2019-10-24 22:14:57.104716

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "57bc88e06e52"
down_revision = "c7025892455f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chats",
        sa.Column(
            "is_official",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=True,
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "is_superuser",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=True,
        ),
    )
    op.drop_column("users", "superuser")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "superuser",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("users", "is_superuser")
    op.drop_column("chats", "is_official")
    # ### end Alembic commands ###
