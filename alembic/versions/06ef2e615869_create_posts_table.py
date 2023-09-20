"""create posts table

Revision ID: 06ef2e615869
Revises: 
Create Date: 2023-09-20 14:36:05.445519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06ef2e615869'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer,primary_key=True,nullable=False),
                    sa.Column('title',sa.String,nullable=False),
                    sa.Column('published',sa.Boolean,nullable=False,server_default='True'),
                    sa.Column('created_at',sa.DATETIME,nullable=False,server_default=sa.text('getutcdate()')))


def downgrade():
    op.drop_table("posts")
