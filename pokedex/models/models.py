from typing import List, Optional #For Relationships
from sqlmodel import SQLModel, Field, Relationship  #Builders
from sqlmodel import create_engine, Session #Usage

#* Connections
sqlite_filename: str = "data.db"
pgsql_heading: dict[str, str] = {
    "user": "root",
    "password": "3223",
    "adress": "localhost", 
    "port": "8089",
    "db": "pokedex"
}

#* Engines: for usage
# pgsql_engine = create_engine(f"postgresql://{pgsql_heading['user']}:{pgsql_heading['password']}" +
#                              f"@{pgsql_heading['adress']}:{pgsql_heading['port']}/{pgsql_heading['db']}")
sqlite_engine = create_engine(f"sqlite:///{sqlite_filename}")

class Pokemon(SQLModel, table=True):
    id: int = Field(primary_key=True, nullable=False)
    name: str
    
class Ability(SQLModel, table=True):
    id: int = Field(primary_key=True, nullable=False, ge=1)
    name: str
    effect: str
    generation: int
    categories: List['AbilityCategory'] = Relationship(back_populates="name")

class AbilityCategory(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    color: str #hex

class AbilityCompatibility(SQLModel, table=True): #Many pokemons can have Many abilities
    id: int = Field(primary_key=True)
    pokemon: Pokemon = Relationship( back_populates="Pokemon" ) #!!!!! what da hel !!!!!
    ability: Ability = Relationship( back_populates="Ability" )

#* Migration: FIRST TIME ONLY!
# SQLModel.metadata.create_all(pgsql_engine)
SQLModel.metadata.create_all(sqlite_engine)

if __name__ == "__main__":
    with Session(sqlite_engine) as session:
        newPokemon_1 = Pokemon(id=1, name="squirtle")
        newPokemon_2 = Pokemon(id=2, name="charizard")

        session.add_all([newPokemon_1, newPokemon_2])
        session.commit()