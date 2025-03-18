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
    queryResult = session.exec(statement).one_or_none()

    return queryResult

@app.get(BASE_URLS['get'] + '/pokemon/name/{name_inserted}')
def get_pokemon_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one_or_none()

    return queryResult

#models.Abilities
@app.get(BASE_URLS['get'] + '/ability/id/{id_inserted}')
def get_ability_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(Ability.id == id_inserted)
    queryResult = session.exec(statement).one_or_none()

    #! not finished -- add decorator
    return queryResult

@app.get(BASE_URLS['get'] + '/ability/name/{name_inserted}')
def get_ability_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(func.lower(Ability.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one_or_none()

    #! Temporary -- move to decorator
    if queryResult.FK_type:
        statement = select(AbilityType).where(AbilityType.id == queryResult.FK_type)
        TypeResult = session.exec(statement).one_or_none()
    if queryResult.FK_category:
        statement = select(AbilityCategory).where(AbilityCategory.id == queryResult.FK_category)
        CategoryResult = session.exec(statement).one_or_none()

    return { 
            "id": queryResult.id,
            "name": queryResult.name,
            "effect": queryResult.effect,
            "generation": queryResult.generation,
            "AbilityType": TypeResult.name,
            "AbilityCategory": CategoryResult.name
        } #! Temporary

#models.AbilityCompatibilities
@app.get(BASE_URLS['get'] + '/abilitycompatibility/') #to be used with ?pokemon=[name]&ability=[name]
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


#* Posts
#? Base response: {'result': 'message'}
#models.AbilityCategories
@app.post(BASE_URLS['post'] + "/abilitycategory/") #to be used with ?name=[]&color=[hex], mainly
def add_new_ability_category(name: str, color: str, id: int = None, session: Session = Depends(get_db_session_dependency)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(AbilityCategory).where(AbilityCategory.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            return {"result": f"{name.title()} was not inserted, the id of category already exists!"}
        
    if name and color:
        session.add(AbilityCategory(id=id, name=name.title(), color=color))
        session.commit()
    else:
        return {"result": f"{name.title()} was not inserted. Please add name and color to request"}
    
    return {"result": f"{name.title()} inserted sucesfully."}

#models.AbilityCompatibility
@app.post(BASE_URLS['post'] + "/abilitycompatibility/") #to be used with ?pokemon=[name]&ability=[name], mainly
def add_new_compatibility(pokemon: str, ability: str, id: int = None, session: Session = Depends(get_db_session_dependency)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(AbilityCompatibility).where(AbilityCompatibility.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            return {"result": f"The compatibility was not added, the id of compatibility already exists!"}
        
    if pokemon and ability:
        selectPokeId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        pokemon_id = session.exec(selectPokeId).first().id
        ability_id = session.exec(selectAbilityId).first().id

        session.add(AbilityCompatibility(id=id, FK_pokemon_id=pokemon_id, FK_ability_id=ability_id))
        session.commit()
        return {"result": f"{pokemon.title()} added sucesfully."}
    else:
        return {"result": f"{pokemon.title()} was not added. Please add pokemon and ability to request"}

#* Deletes
#models.AbilityCompatibility


#TODO: Puts - to be considered
#models.AbilityTypes
#models.AbilityCategories