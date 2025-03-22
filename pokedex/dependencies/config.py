
#* for Connections - data for db string connection
#Recommended to not change keys, only values.
sqlite_heading: dict[str, str] = {
        "filename": "data.db"
}
pgsql_heading: dict[str, str] = {
    "user": "root",
    "password": "3223",
    "adress": "127.0.0.1:8089", 
    "db": "pokedex_data"
}

#* global consts
DB_ENGINE_CHOICE: str = "pgsql" # Global db choice configuration, used in dependencies.connections functions.

MAX_POKEMON_NATIONAL_ID: int = 1025 # as of 13-03-2025, the max number.
