"""add image column in posts table

Revision ID: b70df45df41c
Revises: b9a2e9566b43
Create Date: 2023-09-23 17:51:38.406757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b70df45df41c'
down_revision: Union[str, None] = 'b9a2e9566b43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('images',sa.String))


def downgrade() -> None:
    op.drop_column("posts","images")
