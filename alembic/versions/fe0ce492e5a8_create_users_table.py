"""create users table
Revision ID: fe0ce492e5a8
Revises: 06ef2e615869
Create Date: 2023-09-20 14:51:07.519145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe0ce492e5a8'
down_revision: Union[str, None] = '06ef2e615869'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('Users',
                    sa.Column('id',sa.Integer,primary_key=True,nullable=False),
                    sa.Column('email',sa.String(255),nullable=False,unique=True),
                    sa.Column('password',sa.String,nullable=False),
                    sa.Column('created_at',sa.DATETIME,nullable=False,server_default=sa.text('getutcdate()')))


def downgrade():
    op.drop_table("Users")
