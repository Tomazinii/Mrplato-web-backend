"""alter activity time field

Revision ID: 2ec0bd0874c7
Revises: 3172221d2fdb
Create Date: 2024-03-09 21:53:43.543780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ec0bd0874c7'
down_revision: Union[str, None] = '3172221d2fdb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('activity', 'time', type_=sa.DateTime(timezone=True))

def downgrade():
    op.alter_column('activity', 'time', type_=sa.DateTime())
