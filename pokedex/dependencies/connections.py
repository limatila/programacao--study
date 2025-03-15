from models.models import get_engine

# global consts
DB_ENGINE_CHOICE: str = "pgsql" # Global db choice configuration for get_engine.

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
    """
    Returns a engine for SQLModel Sessions.
        Will Accept:
        #SQLite:
        - 'sqlite'
        - 'sqlite3'

        #PostgreSQL
        - 'pgsql'

        #Others:
        - will return an Anon-Exception.
    """
    match(engineChoice):
        case "pgsql":
            return create_engine(f"postgresql://{pgsql_heading['user']}:{pgsql_heading['password']}" +
                                 f"@{pgsql_heading['adress']}/{pgsql_heading['db']}",
                                 echo=True, pool_pre_ping=True)
        case "sqlite" | "sqlite3":
            return create_engine(f"sqlite:///{sqlite_filename}")
        case _:
            raise Exception("Not a valid choice of engine, please select between \"sqlite\" and \"pgsql\".")

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