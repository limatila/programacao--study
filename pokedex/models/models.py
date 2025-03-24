from sqlmodel import SQLModel, Field, Relationship  #* Builders
#from sqlmodel import create_engine, Session #* Usage
from sqlalchemy import UniqueConstraint #* Additionals
from typing import List, Optional #* For NOT NULL definition and Relationships
from pokedex.dependencies.config import MAX_POKEMON_NATIONAL_ID

class Pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1, le=MAX_POKEMON_NATIONAL_ID)
    name: str
    weight: Optional[float]   #Kg
    height: Optional[float]   #Meter
    description: Optional[str]

    #Relationships
    abilities: List['AbilityCompatibility'] = Relationship(back_populates="pokemons") #? needs to be mirrored with the anottated class

    #other constraints
    __table_args__ = (UniqueConstraint("name"), )

class Ability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1)
    name: str
    effect: str
    generation: int

    #FKs
    FK_category_id: Optional[int] = Field(foreign_key="abilitycategory.id")
    FK_type_id: Optional[int] = Field(foreign_key="abilitytype.id")

    #Relationships - needed for .joins
    compatibilitys: List['AbilityCompatibility'] = Relationship(back_populates="abilities")
    type: Optional['AbilityType'] = Relationship(back_populates="abilities")
    category: Optional['AbilityCategory'] = Relationship(back_populates="abilities")

    #other constraints
    __table_args__ = (UniqueConstraint("name"), )

class AbilityCompatibility(SQLModel, table=True): #Many pokemons can have Many abilities
    id: Optional[int] = Field(default=None, primary_key=True)
    pokemons: Pokemon = Relationship(back_populates="abilities")
    abilities: Ability = Relationship(back_populates="compatibilitys")

    #FKs
    FK_pokemon_id: int = Field(foreign_key="pokemon.id")
    FK_ability_id: int = Field(foreign_key="ability.id")

class AbilityType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    color: str #hex color

    #Relationships
    abilities: List[Ability] = Relationship(back_populates="type")

    #other constraints
    __table_args__ = (UniqueConstraint("name"), )

class AbilityCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fotoPngUrl: str

    #Relationships
    abilities: List[Ability] = Relationship(back_populates="category")

    #other constraints
    __table_args__ = (UniqueConstraint("name"), )

#! new classes: need to add then in models/__init__.py


if __name__ == "__main__":
    from pokedex.dependencies import get_engine, DB_ENGINE_CHOICE
    SQLModel.metadata.create_all(get_engine(DB_ENGINE_CHOICE))
