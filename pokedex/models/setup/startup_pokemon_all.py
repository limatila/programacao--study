#* Continuing from startup_inserts.py work...
# Using pypokedex package: https://github.com/arnavb/pypokedex

from sqlmodel import Session, select
import pypokedex as pk
from pypokedex.exceptions import PyPokedexError

from pokedex.models import Pokemon
from pokedex.dependencies import get_engine, DB_ENGINE_CHOICE

def update_startup_null_descriptions(engine = get_engine(DB_ENGINE_CHOICE)):
    with Session(engine) as session:
        for i in range(5):
            if i == 0: continue

            selectIterationStatement = select(Pokemon).where(Pokemon.id == i)

            PokeFromDB = session.exec(selectIterationStatement).one_or_none()
            currentPokeFromPK = pk.get(dex=i)
            currentDescriptionFromPK = currentPokeFromPK.get_descriptions()['red'].replace('\n', ' ') #getting and sanitizing breaklines 
            #? You can change 'red' to any pokemon game you wish (if it's available), see pypokedex docs

            #Update
            PokeFromDB.weight = currentPokeFromPK.weight / 10 #pypokedex delivers in Kg*10
            PokeFromDB.height = currentPokeFromPK.height / 10 #pypokedex delivers in m*10
            PokeFromDB.description = currentDescriptionFromPK

            session.add(PokeFromDB)
            session.commit()

#! long process of getting all of them! sit and wait. (should be replaced around other methods...)
last_iteration_count: int = 0
def insert_all_pokemons(engine = get_engine(DB_ENGINE_CHOICE), skip_startup_inserts: bool = False):
    global last_iteration_count
    first_index: int = 1
    if skip_startup_inserts == True:
        first_index = 5
    if last_iteration_count != 0: #This means that an error has ocurred and the function has been runned again
        first_index = last_iteration_count

    with Session(engine) as session: 
        for i in range(first_index, 1026):
            last_iteration_count = i

            try:
                if i == 0: continue #minimum of 1 to id
                
                print("starting insert: ", i)
                currentPokemon = pk.get(dex=i)
                
                #Sanitizing description
                currentDescriptionArray = currentPokemon.get_descriptions()
                currentDescription = currentDescriptionArray.get( list(currentDescriptionArray.keys())[0] ) #First available description
                currentDescription = currentDescription.replace('\n', ' ')

                session.add(Pokemon(id=i, name=currentPokemon.name.title(), weight=(currentPokemon.weight / 10), height=(currentPokemon.height / 10),
                                    description=currentDescription)
                                )
                
                #Batched commit
                if i %25 == 0:
                    session.commit()
            except PyPokedexError as err:
                insert_all_pokemons(skip_startup_inserts=skip_startup_inserts)

        #Last check
        session.commit()
        last_iteration_count = 0 #returning to ideal state (no error prone)

if __name__ == "__main__":
    #Update weight, height, description, pokemons 1 - 4
    update_startup_null_descriptions()

    #Insert pokemons 5 - 1025 (dictated by parameter)
    insert_all_pokemons(skip_startup_inserts=True) 