"""initial migration

Revision ID: 737c3c46bc9a
Revises: 35bfd79c7ef8
Create Date: 2024-04-18 22:08:42.474493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '737c3c46bc9a'
down_revision: Union[str, None] = '35bfd79c7ef8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
