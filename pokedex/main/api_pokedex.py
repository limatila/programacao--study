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
        pokemon_id = session.exec(selectPokeId).one().id
        ability_id = session.exec(selectAbilityId).one().id
    #! else:
    #!     return HTTPException
    
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
#models.Abilities
@app.post(BASE_URLS['post'] + "/ability/") #to be used with ?name=[name]&effect=[name]&generation=[number], along with &category=[name]&type=[name]
def add_new_ability(name: str, effect: str, generation: int, id: int = None, category: str = None, type: str = None, session: Session = Depends(get_db_session_dependency)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(Ability).where(Ability.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            return {"result": f"The compatibility was not added, the id of compatibility already exists!"}
        
    if name and effect and generation:
        if type: 
            selectAbilityTypeId = select(AbilityType).where(func.lower(AbilityType.name) == func.lower(type))
            type_id = session.exec(selectAbilityTypeId).one_or_none().id
        if category: 
            selectAbilityCategoryId = select(AbilityCategory).where(func.lower(AbilityCategory.name) == func.lower(category))
            category_id = session.exec(selectAbilityCategoryId).one_or_none().id

        session.add(Ability(id=id, name=name.title(), effect=effect, generation=int(generation),
                            FK_category=category_id, FK_type=type_id))
        session.commit()
        return {"result": f"{name.title()} added sucesfully."}
    else:
        return {"result": f"{name.title()} was not added. Please check parameters sent in request"}

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
        return {"result": f"{name.title()} inserted sucesfully."}
    else:
        return {"result": f"{name.title()} was not inserted. Please add name and color to request"}
    

#models.AbilityCompatibilities
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
        pokemon_id = session.exec(selectPokeId).one().id
        ability_id = session.exec(selectAbilityId).one().id

        session.add(AbilityCompatibility(id=id, FK_pokemon_id=pokemon_id, FK_ability_id=ability_id))
        session.commit()
        return {"result": f"{pokemon.title()} added sucesfully."}
    else:
        return {"result": f"{pokemon.title()} was not added. Please add pokemon and ability to request"}



#* Deletes
#models.AbilityCompatibilities
@app.delete(BASE_URLS['delete'] + "/abilitycompatibility/") #to be used with ?pokemon=[name]&ability=[name], mainly
def delete_compatibility(id: int = None, pokemon: str = None, ability: str = None, session: Session = Depends(get_db_session_dependency)):
    if id:
        id = int(id)
        selectCompatibility = select(AbilityCompatibility).where(AbilityCompatibility.id == id)
        compatibilityToDelete = session.exec(selectCompatibility).one()

    elif pokemon and ability:
        selectPokeId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        pokemon_id = session.exec(selectPokeId).one().id
        ability_id = session.exec(selectAbilityId).one().id

        selectCompatibility = (
            select(AbilityCompatibility)
            .where(AbilityCompatibility.FK_pokemon_id == pokemon_id)
            .where(AbilityCompatibility.FK_ability_id == ability_id)
        )
        compatibilityToDelete = session.exec(selectCompatibility).one()
    else: return {"result": "Compatibility was not deleted. Please check parameters sent in request."}
    
    if compatibilityToDelete:
        session.delete(compatibilityToDelete)
        session.commit()
        return {
            "result": f"Compatibility was sucessfully deleted.",
            "compatibilityId": compatibilityToDelete.id
        }
    else: 
        return {"result": "Compatibility not found. Please check with GET the compatibilities that exist."}

#TODO: replace wheres with suitable joins


#Puts - to be considered
#models.AbilityTypes
#models.AbilityCategories

