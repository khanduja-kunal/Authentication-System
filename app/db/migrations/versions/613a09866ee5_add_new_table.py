"""Add new table

Revision ID: 613a09866ee5
Revises: 5bb774423ff7
Create Date: 2025-05-08 11:09:53.999516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '613a09866ee5'
down_revision: Union[str, None] = '5bb774423ff7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklisted_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('blacklisted_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_blacklisted_tokens_id'), 'blacklisted_tokens', ['id'], unique=False)
    op.add_column('users', sa.Column('profile_picture', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_picture')
    op.drop_index(op.f('ix_blacklisted_tokens_id'), table_name='blacklisted_tokens')
    op.drop_table('blacklisted_tokens')
    # ### end Alembic commands ###
