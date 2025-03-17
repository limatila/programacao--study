from fastapi import FastAPI, Depends #TODO - , HTTPException, status
from sqlmodel import select, Session
from sqlalchemy.sql import func #func for db functions

from pokedex.models import Pokemon, Ability, AbilityCategory, AbilityType, AbilityCompatibility #And many more if wanted for the apis.
from pokedex.dependencies.connections import get_db_session_dependency

API_VERSION = "v1"
app = FastAPI()

#Pattern: vNumber/method/model/etc...
BASE_URLS: dict[str, str] = {
    "get": f"/{API_VERSION}/get",
    "post": f"/{API_VERSION}/post",
    "delete": f"/{API_VERSION}/delete",
}

#* Getters
#TODO: sanitize of request and output
#models.Pokemons
@app.get(BASE_URLS['get'] + '/pokemon/id/{id_inserted}')
def get_pokemon_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Pokemon).where(Pokemon.id == id_inserted)
    queryResult = session.exec(statement).one()

    return queryResult

@app.get(BASE_URLS['get'] + '/pokemon/name/{name_inserted}')
def get_pokemon_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one()

    return queryResult

#models.Abilities
@app.get(BASE_URLS['get'] + '/ability/id/{id_inserted}')
def get_ability_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(Ability.id == id_inserted)
    queryResult = session.exec(statement).one()

    #! not finished
    return queryResult

@app.get(BASE_URLS['get'] + '/ability/name/{name_inserted}')
def get_ability_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(func.lower(Ability.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one()

    #! Temporary -- move to decorator
    if queryResult.FK_type:
        statement = select(AbilityType).where(AbilityType.id == queryResult.FK_type)
        TypeResult = session.exec(statement).one()
    if queryResult.FK_category:
        statement = select(AbilityCategory).where(AbilityCategory.id == queryResult.FK_category)
        CategoryResult = session.exec(statement).one()

    return { #! Temporary
            "id": queryResult.id,
            "name": queryResult.name,
            "effect": queryResult.effect,
            "generation": queryResult.generation,
            "AbilityType": TypeResult.name,
            "AbilityCategory": CategoryResult.name
        }

#models.AbilityCompatibilities
@app.get(BASE_URLS['get'] + '/abilitycompatibility/')
def get_ability_by_id(pokemon: str, ability: str, session: Session = Depends(get_db_session_dependency)):   
    if pokemon and ability:
        selectPokeId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        pokemon_id = session.exec(selectPokeId).first().id
        ability_id = session.exec(selectAbilityId).first().id
    # else:
    #     return HTTPException
    
    compatibilityStatement = (
            select(Ability) \
            .where(AbilityCompatibility.FK_pokemon_id == pokemon_id) \
            .where(AbilityCompatibility.FK_ability_id == ability_id)
        )
    queryResult = session.exec(compatibilityStatement).all()

    if queryResult:
        return {
            "isCompatible": True,
            "pokemon_id": pokemon_id,
            "ability_id": ability_id
        }


#* Puts
#models.AbilityTypes
#models.AbilityCompatibility

#* Posts
#models.AbilityTypes
#models.AbilityCategories

#* Deletes
#models.Pokemon
#models.AbilityCompatibility