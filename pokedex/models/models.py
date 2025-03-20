from typing import List, Optional #* For Relationships
from sqlmodel import SQLModel, Field, Relationship  #* Builders
#from sqlmodel import create_engine, Session #* Usage

class Pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1, le=1025) # 1025 max n° pokemon as of 13-03-2025
    name: str
    weight: Optional[float]   #Kg
    height: Optional[float]   #Meter
    description: Optional[str]
    abilities: List['AbilityCompatibility'] = Relationship(back_populates="pokemon")
    
#? Ability is actually 'Move'.. should i change api and db for that matter?
class Ability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1)
    name: str
    effect: str
    generation: int
    compatibility: List['AbilityCompatibility'] = Relationship(back_populates="ability")

    #FKs
    #! need to add _id in column name
    FK_category_id: Optional[int] = Field(foreign_key="abilitycategory.id")
    FK_type_id: Optional[int] = Field(foreign_key="abilitytype.id")

class AbilityCompatibility(SQLModel, table=True): #Many pokemons can have Many abilities
    id: Optional[int] = Field(default=None, primary_key=True)
    pokemon: Pokemon = Relationship(back_populates="abilities")
    ability: Ability = Relationship(back_populates="compatibility")

    #FKs
    FK_pokemon_id: int = Field(foreign_key="pokemon.id")
    FK_ability_id: int = Field(foreign_key="ability.id")

#!!! TYPE AND CATEGORY ARE INVERTED! NEED REWORK
class AbilityType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    color: str #hex color

class AbilityCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fotoPngUrl: str


#! new classes: need to add then in models/__init__.py