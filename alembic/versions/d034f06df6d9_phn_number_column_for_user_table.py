""" phn number column for user table

Revision ID: d034f06df6d9
Revises: 
Create Date: 2026-10-10 18:37:10.536525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd034f06df6d9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable = True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')

