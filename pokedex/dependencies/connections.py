from sqlmodel import create_engine, Session 
from .config import DB_ENGINE_CHOICE, sqlite_heading, pgsql_heading

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
            return create_engine(f"sqlite:///{sqlite_heading['filename']}")
        case _:
            raise Exception("Not a valid choice of engine, please select between \"sqlite\" and \"pgsql\".")

def get_db_session_dependency():
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
    
if __name__ == "__main__":
    an_engine = get_engine(DB_ENGINE_CHOICE)
