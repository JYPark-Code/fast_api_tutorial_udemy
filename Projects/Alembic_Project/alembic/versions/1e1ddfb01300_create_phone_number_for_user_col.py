"""create phone number for user col

Revision ID: 1e1ddfb01300
Revises: 
Create Date: 2022-09-19 08:34:58.323638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e1ddfb01300'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
