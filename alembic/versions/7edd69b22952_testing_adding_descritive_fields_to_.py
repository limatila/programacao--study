"""Testing: adding descritive fields to Pokemon

Revision ID: 7edd69b22952
Revises: 
Create Date: 2025-03-13 21:54:16.345088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7edd69b22952'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('weight', sa.Float(), nullable=True))
    op.add_column('pokemon', sa.Column('height', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemon', 'height')
    op.drop_column('pokemon', 'weight')
    # ### end Alembic commands ###
