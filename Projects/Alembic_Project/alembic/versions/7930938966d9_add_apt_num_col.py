"""add apt num col

Revision ID: 7930938966d9
Revises: bff03b40ca38
Create Date: 2022-09-19 11:22:43.288481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7930938966d9'
down_revision = 'bff03b40ca38'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade():
    op.drop_column("address", "apt_num")
