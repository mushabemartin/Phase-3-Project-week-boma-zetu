"""Updated ResidentialProperty model removed price_per_sqf column

Revision ID: a47e8199cfe0
Revises: 88ec72ab0c6b
Create Date: 2023-09-06 16:41:06.863715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a47e8199cfe0'
down_revision: Union[str, None] = '88ec72ab0c6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
