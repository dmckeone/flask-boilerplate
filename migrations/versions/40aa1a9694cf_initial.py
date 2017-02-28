"""
Create initial structure

Revision ID: 40aa1a9694cf
Revises: None
Create Date: 2016-03-22 00:08:31.860252
"""

# revision identifiers, used by Alembic.
revision = '40aa1a9694cf'
down_revision = None

from alembic import op
from sqlalchemy import Column, Integer, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB

def upgrade():
    op.create_table('document',
        Column('id', Integer(), nullable=False),
        Column('data', JSONB()),
        PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('document')
