"""add auto genereted votes table

Revision ID: b9a2e9566b43
Revises: 4c7758142a88
Create Date: 2023-09-20 15:34:27.451405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9a2e9566b43'
down_revision: Union[str, None] = '4c7758142a88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('postid', sa.Integer(), nullable=False),
    sa.Column('likedby_userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['likedby_userid'], ['Users.id'], ondelete='NO ACTION'),
    sa.ForeignKeyConstraint(['postid'], ['posts.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('postid', 'likedby_userid')
    )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'content')
    op.drop_table('votes')
    # ### end Alembic commands ###
