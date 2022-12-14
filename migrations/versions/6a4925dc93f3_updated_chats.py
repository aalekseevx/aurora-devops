"""updated chats

Revision ID: 6a4925dc93f3
Revises: 57bc88e06e52
Create Date: 2021-01-30 20:54:47.102016

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6a4925dc93f3"
down_revision = "57bc88e06e52"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chats", sa.Column("desired_kp", sa.Integer(), nullable=True)
    )
    op.add_column(
        "chats", sa.Column("geonames_data", sa.Text(), nullable=True)
    )
    op.add_column("chats", sa.Column("latitude", sa.Float(), nullable=True))
    op.add_column("chats", sa.Column("longitude", sa.Float(), nullable=True))
    op.add_column(
        "chats",
        sa.Column(
            "mute",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )
    op.add_column(
        "chats",
        sa.Column(
            "subscribe",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )
    op.add_column("chats", sa.Column("user_info", sa.Text(), nullable=True))
    op.add_column("chats", sa.Column("weather_info", sa.Text(), nullable=True))
    op.drop_column("chats", "type")
    op.drop_column("chats", "join_filter")
    op.drop_column("chats", "is_official")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chats",
        sa.Column(
            "is_official",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "chats",
        sa.Column(
            "join_filter",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "chats",
        sa.Column("type", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("chats", "weather_info")
    op.drop_column("chats", "user_info")
    op.drop_column("chats", "subscribe")
    op.drop_column("chats", "mute")
    op.drop_column("chats", "longitude")
    op.drop_column("chats", "latitude")
    op.drop_column("chats", "geonames_data")
    op.drop_column("chats", "desired_kp")
    # ### end Alembic commands ###
