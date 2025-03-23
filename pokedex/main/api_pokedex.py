from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select, Session
from sqlalchemy.sql import func #for db functions
from sqlalchemy.exc import IntegrityError

from pokedex.models import * #And many more if wanted for the API.
from pokedex.dependencies.connections import get_db_session_dependency
from pokedex.dependencies.security import verify_token as sec_verify_token
from pokedex.dependencies.config import MAX_POKEMON_NATIONAL_ID
from .custom_checkers import isValidColor

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


#TODO: rework a pattern in responses
#* Getters
#models.Pokemons
@app.get(BASE_URLS['get'] + '/pokemon/id/{id_inserted}')
def get_pokemon_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):    
    #* FastAPI already handles invalid insertion of ints

    if id_inserted < 1 or id_inserted > MAX_POKEMON_NATIONAL_ID:
        HTTPException(f"Pokemon could not be resolved, please select between valid IDs: 1 - {MAX_POKEMON_NATIONAL_ID}.")

    selectPokemon = select(Pokemon).where(Pokemon.id == id_inserted)
    queryResult = session.exec(selectPokemon).one_or_none()

    if queryResult:
        return queryResult
    else: 
        raise HTTPException(status_code=404, detail="Pokemon not found in DataBase.")

@app.get(BASE_URLS['get'] + '/pokemon/name/{name_inserted}')
def get_pokemon_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    selectPokemon = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(name_inserted))
    queryResult = session.exec(selectPokemon).one_or_none()

    if queryResult:
        return queryResult
    else: 
        raise HTTPException(status_code=404, detail="Pokemon not found in DataBase.")


#models.Abilities
@app.get(BASE_URLS['get'] + "/ability/id/{id_inserted}") 
def get_ability_by_id(id_inserted: int, session: Session = Depends(get_db_session_dependency)):
    selectAbility = (
        select(Ability.id, Ability.name, Ability.effect, Ability.generation,
               AbilityType.name, AbilityCategory.name)
               .join(AbilityType)
               .join(AbilityCategory)
               .where(Ability.id == id_inserted)
    )
    queryResult = session.exec(selectAbility).one_or_none()
    
    if queryResult:
        return {
            "id": queryResult.id,
            "name": queryResult.name,
            "effect": queryResult.effect,
            "generation": queryResult.generation,
            "type": queryResult[-2],
            "category": queryResult[-1]
        }
    else:
        raise HTTPException(status_code=404, detail="Ability not found in DataBase.")

@app.get(BASE_URLS['get'] + '/ability/name/{name_inserted}')
def get_ability_by_name(name_inserted: str, session: Session = Depends(get_db_session_dependency)):    
    selectAbility = (
        select(Ability.id, Ability.name, Ability.effect, Ability.generation,
               AbilityType.name, AbilityCategory.name)
               .join(AbilityType)
               .join(AbilityCategory)
               .where(func.lower(Ability.name) == func.lower(name_inserted))
               )         
    queryResult = session.exec(selectAbility).one_or_none()

    if queryResult: 
        return { 
                "id": queryResult.id,
                "name": queryResult.name,
                "effect": queryResult.effect,
                "generation": queryResult.generation,
                "type": queryResult[-2],
                "category": queryResult[-1]
            }
    else: 
        raise HTTPException(status_code=404, detail="Ability not found in DataBase.")


#models.AbilityCompatibilities
@app.get(BASE_URLS['get'] + '/abilitycompatibility/') #to be used with ?pokemon=[name]&ability=[name]
def get_compatibility_by_names(pokemon: str, ability: str, session: Session = Depends(get_db_session_dependency)):   
    #searching data + detailed erroring
    try:
        selectPokemonId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        pokemon_id = session.exec(selectPokemonId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, pokemon \'{pokemon.title()}\' could not be found in DB.")

    try:
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        ability_id = session.exec(selectAbilityId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, ability \'{ability.title()}\' could not be found in DB.")

    #searching compatibility
    compatibilityStatement = (
        select(AbilityCompatibility.id, Pokemon.name, Ability.name)
            .join(Pokemon)
            .join(Ability)
            .where(AbilityCompatibility.FK_pokemon_id == pokemon_id)
            .where(AbilityCompatibility.FK_ability_id == ability_id)
        )
    queryResult = session.exec(compatibilityStatement).one_or_none()

    if queryResult:
        return {
            "result": "Compatibility was found.",
            "isCompatible": True,
            "pokemon": queryResult[-2],
            "ability": queryResult[-1]
        }
    else: 
        raise HTTPException(status_code=404, detail={
                                "error": "Compatibility not found in DataBase.",
                                "isCompatible": f"{str(False)}",
                                "pokemon": f"{str(queryResult[-2])}",
                                "ability": f"{str(queryResult[-1])}"
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
        selectAbility = select(Ability).where(Ability.id == id)
        abilityIdExists = session.exec(selectAbility).one_or_none()
        if abilityIdExists:
            raise HTTPException(status_code=409, detail="The compatibility was not added, the id of compatibility already exists.")
        
    #searching data
    if category: 
        selectAbilityCategoryId = select(AbilityCategory).where(func.lower(AbilityCategory.name) == func.lower(category))
        category_id = session.exec(selectAbilityCategoryId).one_or_none().id
    if type: 
        selectAbilityTypeId = select(AbilityType).where(func.lower(AbilityType.name) == func.lower(type))
        type_id = session.exec(selectAbilityTypeId).one_or_none().id


    try:
        session.add(Ability(id=id, name=name.title(), effect=effect.capitalize(), generation=int(generation),
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
        selectType = select(AbilityType).where(AbilityType.id == id)
        abilityTypeIdExists = session.exec(selectType).one_or_none()
        if abilityTypeIdExists:
            raise HTTPException(status_code=409, detail=f"The Ability {name.title()} was not added, the id of type already exists.")
        
    if isValidColor(color) == False:
        raise HTTPException(status_code=400, detail="The ability type color was not well inserted. Plase insert a valid Hex color, like \'#1f3a6d\'")
        
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
        selectCompatibility = select(AbilityCompatibility).where(AbilityCompatibility.id == id)
        compatibilityIdExists = session.exec(selectCompatibility).one_or_none()
        if compatibilityIdExists:
            raise HTTPException(status_code=409, detail="Compatibility was not added, the id of compatibility already exists.")
        
    #searching data + detailed errors
    try:
        selectPokemonId = select(Pokemon).where(func.lower(Pokemon.name) == func.lower(pokemon))
        pokemon_id = session.exec(selectPokemonId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, pokemon \'{pokemon.title()}\' could not be found in DB.")

    try:
        selectAbilityId = select(Ability).where(func.lower(Ability.name) == func.lower(ability))
        ability_id = session.exec(selectAbilityId).one_or_none().id
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Compatibility could not be solved, ability \'{ability.title()}\' could not be found in DB.")

    #check if combination of compatibility already exists
    selectCompatibility = (
                select(AbilityCompatibility) \
                .where(AbilityCompatibility.FK_pokemon_id == pokemon_id) \
                .where(AbilityCompatibility.FK_ability_id == ability_id)
            )
    compatibilityExists = session.exec(selectCompatibility).one_or_none()
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
#models.AbilityCompatibilities
@app.delete(BASE_URLS['delete'] + "/abilitycompatibility/") #to be used with ?id=[number], or ?pokemon=[name]&ability=[name]
def delete_compatibility(id: int = None, pokemon: str = None, ability: str = None, 
                         session: Session = Depends(get_db_session_dependency), token: str = Depends(sec_verify_token)):

    if id:
        id = int(id)
        selectCompatibility = select(AbilityCompatibility).where(AbilityCompatibility.id == id)
        compatibilityToDelete = session.exec(selectCompatibility).one_or_none()

    elif pokemon and ability:
        selectCompatibility = (
            select(AbilityCompatibility)
            .join(Pokemon)
            .join(Ability)
            .where(func.lower(Pokemon.name) == func.lower(pokemon))
            .where(func.lower(Ability.name) == func.lower(ability))
        )
        compatibilityToDelete = session.exec(selectCompatibility).one_or_none()
    else: 
        return HTTPException(status_code=400, detail="Compatibility was not deleted. Please check parameters sent in request (needs [id] of compatibility / [pokemon] name + [ability] name)")

    if compatibilityToDelete:
        session.delete(compatibilityToDelete)
        session.commit()
        return {
                "result": "Compatibility was sucessfully deleted.",
                "compatibilityId": compatibilityToDelete.id
            }
    else:
        raise HTTPException(status_code=404, detail="Compatibility does not exist (not found). Please check with GET the compatibilities that exist.")



#Puts - to be considered
#models.AbilityTypes
#models.AbilityCategories

