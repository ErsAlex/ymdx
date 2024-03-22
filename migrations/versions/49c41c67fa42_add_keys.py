"""add_keys

Revision ID: 49c41c67fa42
Revises: 905c097fb6c3
Create Date: 2024-03-21 12:35:04.457159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49c41c67fa42'
down_revision: Union[str, None] = '905c097fb6c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kv_keys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('key_type', sa.Enum('AUTH_KEY', 'PASS_RESET_KEY', name='keytype'), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('kv_users', sa.Column('is_authenticated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kv_users', 'is_authenticated')
    op.drop_table('kv_keys')
    # ### end Alembic commands ###
