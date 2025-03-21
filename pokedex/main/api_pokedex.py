from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select, Session
from sqlalchemy.sql import func #for db functions
from sqlalchemy.exc import IntegrityError, NoResultFound

from pokedex.models import * #And many more if wanted for the apis.
from pokedex.dependencies.connections import get_db_session_dependency
from pokedex.dependencies.security import verify_token as sec_verify_token

API_VERSION = "v1"
app = FastAPI()

#Pattern: vNumber/method/model/etc...
BASE_URLS: dict[str, str] = {
    "get": f"/{API_VERSION}/get",
    "post": f"/{API_VERSION}/post",
    "put": f"/{API_VERSION}/put",
    "delete": f"/{API_VERSION}/delete",
    #"customs": { }
}


#* Getters
#models.Pokemons
@app.get(BASE_URLS['get'] + '/pokemon/id/{id_inserted}')
def get_pokemon_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    #* FastAPI already handles invalid insertion of ints

    if id_inserted < 1 or id_inserted > 1025:
        return {"result": "Pokemon could not be resolved, please select between valid IDs: 1 - 1025."}

    statement = select(Pokemon).where(Pokemon.id == id_inserted)
    queryResult = session.exec(statement).one_or_none()

    if queryResult:
        return queryResult
    else: 
        raise HTTPException(status_code=404, detail="Pokemon not found in DataBase.")

@app.get(BASE_URLS['get'] + '/pokemon/name/{name_inserted}')
def get_pokemon_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one_or_none()

    if queryResult:
        return queryResult
    else: 
        raise HTTPException(status_code=404, detail="Pokemon not found in DataBase.")


#models.Abilities
@app.get(BASE_URLS['get'] + '/ability/id/{id_inserted}')
def get_ability_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(Ability.id == id_inserted)
    queryResult = session.exec(statement).one_or_none()

    #? i could refactor the following, into a decorator that apply the the search for the names
    if queryResult: 
        if queryResult.FK_type_id:
            statement = select(AbilityType).where(AbilityType.id == queryResult.FK_type_id)
            TypeResult = session.exec(statement).one_or_none()
        if queryResult.FK_category_id:
            statement = select(AbilityCategory).where(AbilityCategory.id == queryResult.FK_category_id)
            CategoryResult = session.exec(statement).one_or_none()

        return { 
                "id": queryResult.id,
                "name": queryResult.name,
                "effect": queryResult.effect,
                "generation": queryResult.generation,
                "AbilityType": TypeResult.name,
                "AbilityCategory": CategoryResult.name
            }
    else: 
        raise HTTPException(status_code=404, detail="Ability not found in DataBase.")

@app.get(BASE_URLS['get'] + '/ability/name/{name_inserted}')
def get_ability_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    statement = select(Ability).where(func.lower(Ability.name) == func.lower(name_inserted))
    queryResult = session.exec(statement).one_or_none()

    #? i could refactor the following, into a decorator that apply the the search for the names
    if queryResult: 
        if queryResult.FK_type_id:
            statement = select(AbilityType).where(AbilityType.id == queryResult.FK_type_id)
            TypeResult = session.exec(statement).one_or_none()
        if queryResult.FK_category_id:
            statement = select(AbilityCategory).where(AbilityCategory.id == queryResult.FK_category_id)
            CategoryResult = session.exec(statement).one_or_none()

        return { 
                "id": queryResult.id,
                "name": queryResult.name,
                "effect": queryResult.effect,
                "generation": queryResult.generation,
                "AbilityType": TypeResult.name,
                "AbilityCategory": CategoryResult.name
            }
    else: 
        raise HTTPException(status_code=404, detail="Ability not found in DataBase.")


#models.AbilityCompatibilities
@app.get(BASE_URLS['get'] + '/abilitycompatibility/') #to be used with ?pokemon=[name]&ability=[name]
def get_compatibility_by_names(pokemon: str, ability: str, session: Session = Depends(get_db_session_dependency)):   
    #searching data
    try:
        selectPokeId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        pokemon_id = session.exec(selectPokeId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, pokemon \'{pokemon.title()}\' could not be found in DB.")

    try:
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        ability_id = session.exec(selectAbilityId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, ability \'{ability.title()}\' could not be found in DB.")

    #searching compatibility
    compatibilityStatement = (
            select(AbilityCompatibility) \
            .where(AbilityCompatibility.FK_pokemon_id == pokemon_id) \
            .where(AbilityCompatibility.FK_ability_id == ability_id)
        )
    queryResult = session.exec(compatibilityStatement).one_or_none()

    if queryResult:
        return {
            "result": f"Compatibility was found, for {pokemon.title()} and ability {ability.title()}.",
            "isCompatible": True,
            "pokemon_id": pokemon_id,
            "ability_id": ability_id
        }
    else: 
        raise HTTPException(status_code=404, detail={
                                "error": "Compatibility not found in DataBase.",
                                "isCompatible": f"{str(False)}",
                                "pokemon_id": f"{str(pokemon_id)}",
                                "ability_id": f"{str(ability_id)}"
                            })



#* Posts
#? Base response: {'result': 'message'}
#models.Abilities
@app.post(BASE_URLS['post'] + "/ability/") #to be used with ?name=[name]&effect=[name]&generation=[number], along with &category=[name]&type=[name]
def post_new_ability(name: str, effect: str, generation: int, id: int = None, category: str = None, type: str = None,
                      session: Session = Depends(get_db_session_dependency), token: str = Depends(sec_verify_token)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(Ability).where(Ability.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            raise HTTPException(status_code=409, detail="The compatibility was not added, the id of compatibility already exists.")
        
    #searching data
    if type: 
        selectAbilityTypeId = select(AbilityType).where(func.lower(AbilityType.name) == func.lower(type))
        type_id = session.exec(selectAbilityTypeId).one_or_none().id
    if category: 
        selectAbilityCategoryId = select(AbilityCategory).where(func.lower(AbilityCategory.name) == func.lower(category))
        category_id = session.exec(selectAbilityCategoryId).one_or_none().id

    try:
        session.add(Ability(id=id, name=name.title(), effect=effect, generation=int(generation),
                            FK_category_id=category_id, FK_type_id=type_id))
        session.commit()
        return {"result": f"{name.title()} ability added sucesfully."} 
    except IntegrityError: 
        raise HTTPException(status_code=409, detail=f"Ability '{name.title()}' was not added. The ability name already exists.")


#models.AbilityTypes
@app.post(BASE_URLS['post'] + "/abilitytype/") #to be used with ?name=[]&color=[hex], mainly
def post_new_ability_type(name: str, color: str, id: int = None, 
                          session: Session = Depends(get_db_session_dependency), token: str = Depends(sec_verify_token)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(AbilityType).where(AbilityType.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            raise HTTPException(status_code=409, detail=f"The Ability {name.title()} was not added, the id of type already exists.")
        
    try:
        session.add(AbilityType(id=id, name=name.title(), color=color))
        session.commit()
        return {"result": f"{name.title()} type inserted sucesfully."}
    except IntegrityError:
        raise HTTPException(status_code=409, detail=f"Type '{name.title()}' was not added. The type name already exists.")
    

#models.AbilityCompatibilities
@app.post(BASE_URLS['post'] + "/abilitycompatibility/") #to be used with ?pokemon=[name]&ability=[name], mainly
def post_new_compatibility(pokemon: str, ability: str, id: int = None, 
                           session: Session = Depends(get_db_session_dependency), token: str = Depends(sec_verify_token)):
    #Check if id already exists
    if id:
        id = int(id)
        idExistsStatement = select(AbilityCompatibility).where(AbilityCompatibility.id == id)
        idExists = session.exec(idExistsStatement).one_or_none()
        if idExists:
            raise HTTPException(status_code=409, detail="Compatibility was not added, the id of compatibility already exists.")
        
    #searching data
    try:
        selectPokeId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        pokemon_id = session.exec(selectPokeId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, pokemon \'{pokemon.title()}\' could not be found in DB.")

    try:
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        ability_id = session.exec(selectAbilityId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, ability \'{ability.title()}\' could not be found in DB.")

    #check if combination of compatibility already exists
    compatibilityExistsStatement = (
                select(AbilityCompatibility) \
                .where(AbilityCompatibility.FK_pokemon_id == pokemon_id) \
                .where(AbilityCompatibility.FK_ability_id == ability_id)
            )
    compatibilityExists = session.exec(compatibilityExistsStatement).one_or_none()
    if compatibilityExists:
        raise HTTPException(
            status_code=409,
            detail={
                "error": "Compatibility was not added, it already exists.",
                "compatibilityId": str(compatibilityExists.id)
        })

    compatibilityToAdd = AbilityCompatibility(id=id, FK_pokemon_id=pokemon_id, FK_ability_id=ability_id)
    session.add(compatibilityToAdd)
    session.commit()
    return {
            "result": "Compatibility added sucesfully.",
            "compatibilityId": str(compatibilityToAdd.id)
        }
        


#* Deletes
#models.AbilityCompatibilities #TODO: reanalize return and if-else logic
@app.delete(BASE_URLS['delete'] + "/abilitycompatibility/") #to be used with ?pokemon=[name]&ability=[name], mainly
def delete_compatibility(id: int = None, pokemon: str = None, ability: str = None, 
                         session: Session = Depends(get_db_session_dependency), token: str = Depends(sec_verify_token)):
    try:
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
        else: 
            return {"result": "Compatibility was not deleted. Please check parameters sent in request (needs id of compatibility / pokemon name + ability name)"}
    except NoResultFound as err:
        raise HTTPException(status_code=404, detail=f"Compatibility does not exists (not found). Please check with GET the compatibilities that exist.")
    
    if compatibilityToDelete:
        session.delete(compatibilityToDelete)
        session.commit()
        return {
            "result": "Compatibility was sucessfully deleted.",
            "compatibilityId": compatibilityToDelete.id
        }
    else: 
        raise Exception("Compatibility 404 was not caught in except NoResultFound block.")


#TODO: replace wheres with suitable joins


#Puts - to be considered
#models.AbilityTypes
#models.AbilityCategories

