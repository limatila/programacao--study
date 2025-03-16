
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
DB_ENGINE_CHOICE: str = "pgsql" # Global db choice configuration for get_engine.
