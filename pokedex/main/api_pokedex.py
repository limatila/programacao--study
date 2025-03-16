from fastapi import FastAPI, Depends
from sqlmodel import select, Session

from models import Pokemon, Ability, AbilityCategory, AbilityType, AbilityCompatibility #And many more if wanted for the apis.
from dependencies.connections import engine_generator

app = FastAPI()

#Pattern: vNumber/method/model/etc...
BASE_URLS: dict[str, str] = {
    "get": "/v0/get",
    "post": "/v0/post",
    "delete": "/v0/delete",
}

@app.get(BASE_URLS['get'] + '/pokemon/{id_inserted}')
def get_pokemon_by_id(id_inserted: int, session: Session = Depends(engine_generator)):    
    statement = select(Pokemon).where(Pokemon.id == id_inserted)
    queryResult = session.exec(statement).one_or_none()

    return queryResult
