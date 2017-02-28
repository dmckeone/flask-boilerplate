"""
Create users table

Revision ID: 2a55de3a35ee
Revises: 40aa1a9694cf
Create Date: 2017-02-28 08:19:35.762706

"""

# revision identifiers, used by Alembic.
revision = '2a55de3a35ee'
down_revision = '40aa1a9694cf'

from alembic import op
from sqlalchemy import Column, Integer, Unicode, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB


def upgrade():
    op.create_table('users',
        Column('id', Integer(), nullable=False),
        Column('first_name', Unicode()),
        Column('last_name', Unicode()),
        Column('data', JSONB()),
        PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
