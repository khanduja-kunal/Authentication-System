"""Add created_at to OTP and index

Revision ID: 5bb774423ff7
Revises: b0424e1edaa9
Create Date: 2025-05-05 16:20:55.443425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5bb774423ff7'
down_revision: Union[str, None] = 'b0424e1edaa9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('otps', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.create_index('ix_otp_email_purpose_created', 'otps', ['email', 'purpose', 'created_at'], unique=False)
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_index('ix_otp_email_purpose_created', table_name='otps')
    op.drop_column('otps', 'created_at')
    # ### end Alembic commands ###
