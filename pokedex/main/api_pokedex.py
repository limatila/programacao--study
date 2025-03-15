from fastapi import FastAPI, Depends
from sqlmodel import select, Session

from models import *
from models.models import get_engine

DB_ENGINE_CHOICE: str = "sqlite" #change later

def engine_generator():
    """
    Yields a created session for use in FastAPI decorated Functions\n
    Expects that DB_ENGINE_CHOICE global variable is either:
        #SQLite:
        - 'sqlite'
        - 'sqlite3'

        #PostgreSQL
        - 'pgsql'
    """
    if DB_ENGINE_CHOICE == "sqlite" or DB_ENGINE_CHOICE == "sqlite3":
        with Session(get_engine("sqlite3")) as session:
            yield session
    elif DB_ENGINE_CHOICE == "pgsql":
        with Session(get_engine("pgsql")) as session:
            yield session
    else:
        raise Exception("Not a valid choice of engine for the generator, please select between \"sqlite\" and \"pgsql\".")

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
