"""create address_id to users

Revision ID: bff03b40ca38
Revises: f0ae74ff1b24
Create Date: 2022-09-19 08:59:41.922499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bff03b40ca38'
down_revision = 'f0ae74ff1b24'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'address_id')
