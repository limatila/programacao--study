from pokedex.models import *

from fastapi import FastAPI, Depends
from sqlmodel import select

app = FastAPI()

BASE_URLS: dict[str, str] = {
    "get": "v0/get",
    "post": "v0/post",
    "delete": "v0/delete",
}

#TODO: get_engine based generator for api defs

@app.get(f'/{BASE_URLS['get']}/pokemon/{id_inserted}')
def get_pokemon_by_id(id_inserted: int, session: Session = Depends(get_engine)):    
    statement = select(Pokemon).where(Pokemon.id == id)
    queryResult = session.exec(statement).one_or_none()

    return queryResult

