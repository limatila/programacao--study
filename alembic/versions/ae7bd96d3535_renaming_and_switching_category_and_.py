"""Renaming and switching: category and type of abilities

Revision ID: ae7bd96d3535
Revises: 6f45a1c900dc
Create Date: 2025-03-19 13:45:05.639341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ae7bd96d3535'
down_revision: Union[str, None] = '6f45a1c900dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###

    #changing name of table
    op.rename_table('abilitycategory', 'temp_ability_table')
    op.rename_table('abilitytype', 'abilitycategory') #First swap
    op.rename_table('temp_ability_table', 'abilitytype') #Second swap

    #_id change in Ability model
    op.alter_column('ability', 'FK_category', new_column_name="FK_category_id")
    op.alter_column('ability', 'FK_type', new_column_name="FK_type_id")

    #Updating constraint names
    op.drop_constraint('ability_FK_type_fkey', 'ability', type_='foreignkey')
    op.drop_constraint('ability_FK_category_1_fkey', 'ability', type_='foreignkey')
    op.create_foreign_key(None, 'ability', 'abilitytype', ['FK_type_id'], ['id'])
    op.create_foreign_key(None, 'ability', 'abilitycategory', ['FK_category_id'], ['id'])

    #!wrong bellow, should not modify data structure, only names:
    # op.add_column('abilitycategory', sa.Column('fotoPngUrl', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # op.drop_column('abilitycategory', 'color')
    # op.add_column('abilitytype', sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # op.drop_column('abilitytype', 'fotoPngUrl')

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###

    #!wrong bellow, should not modify data structure, only names:
    # op.add_column('abilitytype', sa.Column('fotoPngUrl', sa.VARCHAR(), autoincrement=False, nullable=False))
    # op.drop_column('abilitytype', 'color')
    # op.add_column('abilitycategory', sa.Column('color', sa.VARCHAR(), autoincrement=False, nullable=False))
    # op.drop_column('abilitycategory', 'fotoPngUrl')
    
    op.rename_table('abilitycategory', 'temp_ability_table')
    op.rename_table('abilitytype', 'abilitycategory') #First swap
    op.rename_table('temp_ability_table', 'abilitytype') #Second swap

    op.alter_column('ability', 'FK_category_id', new_column_name="FK_category")
    op.alter_column('ability', 'FK_type_id', new_column_name="FK_type")

    op.drop_constraint(None, 'ability', type_='foreignkey')
    op.drop_constraint(None, 'ability', type_='foreignkey')
    op.create_foreign_key('ability_FK_category_1_fkey', 'ability', 'abilitycategory', ['FK_category'], ['id'])
    op.create_foreign_key('ability_FK_type_fkey', 'ability', 'abilitytype', ['FK_type'], ['id'])

    # ### end Alembic commands ###
