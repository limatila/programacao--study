from typing import List, Optional #For Relationships
from sqlmodel import SQLModel, Field, Relationship  #Builders
from sqlmodel import create_engine, Session #Usage

#* Connections
sqlite_filename: str = "data.db"
pgsql_heading: dict[str, str] = {
    "user": "root",
    "password": "3223",
    "adress": "127.0.0.1:8089", 
    "db": "pokedex_data"
}

#* Engines: for usage
def get_engine(engineChoice: str  = "sqlite3" ):
    match(engineChoice):
        case "pgsql":
            return create_engine(f"postgresql://{pgsql_heading['user']}:{pgsql_heading['password']}" +
                                 f"@{pgsql_heading['adress']}/{pgsql_heading['db']}",
                                 echo=True, pool_pre_ping=True)
        case "sqlite" | "sqlite3":
            return create_engine(f"sqlite:///{sqlite_filename}")
        case _:
            raise Exception("Not a valid choice of engine, please select between \"sqlite\" and \"pgsql\".")

engine = get_engine("pgsql")

class Pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1, le=1025) # 1025 max n° pokemon as of 13-03-2025
    name: str
    weight: Optional[float]   #Kg
    height: Optional[float]   #Meter
    description: Optional[str]
    abilities: List['AbilityCompatibility'] = Relationship(back_populates="pokemon")
    
class Ability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, ge=1)
    name: str
    effect: str
    generation: int
    compatibility: List['AbilityCompatibility'] = Relationship(back_populates="ability")

    #FKs
    FK_category: int = Field(foreign_key="abilitycategory.id")
    FK_type: Optional[int] = Field(foreign_key="abilitytype.id")

class AbilityCompatibility(SQLModel, table=True): #Many pokemons can have Many abilities
    id: Optional[int] = Field(default=None, primary_key=True)
    pokemon: Pokemon = Relationship(back_populates="abilities")
    ability: Ability = Relationship(back_populates="compatibility")

    #FKs
    FK_pokemon_id: int = Field(foreign_key="pokemon.id")
    FK_ability_id: int = Field(foreign_key="ability.id")

class AbilityCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    color: str #hex color

class AbilityType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    fotoPngUrl: str

#! new classes: need to add then in models/__init__.py

if __name__ == "__main__":
    #* Migration: AVAILABLE FIRST TIME ONLY!
    # SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        newPokemon_1 = Pokemon(name="squirtle")
        newPokemon_2 = Pokemon(name="charizard")

        session.add_all([newPokemon_1, newPokemon_2])
        session.commit()