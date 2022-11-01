"""add superuser column

Revision ID: c7025892455f
Revises: d6553c0e950b
Create Date: 2019-10-24 12:04:33.969241

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c7025892455f"
down_revision = "d6553c0e950b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "superuser",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "superuser")
    # ### end Alembic commands ###
