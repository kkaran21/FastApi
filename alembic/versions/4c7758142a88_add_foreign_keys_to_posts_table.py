"""add foreign keys to posts table

Revision ID: 4c7758142a88
Revises: fe0ce492e5a8
Create Date: 2023-09-20 14:51:49.833887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c7758142a88'
down_revision: Union[str, None] = 'fe0ce492e5a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts",sa.Column('owner_id',sa.Integer,nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="Users",
                          local_cols=['owner_id',],remote_cols=['id'],ondelete="CASCADE")
    pass



def downgrade() -> None:
    op.drop_constraint(constraint_name="posts_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
