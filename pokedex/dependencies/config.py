
#* for Connections - data for db string connection
sqlite_filename: str = "data.db"  #change for desired db file name
pgsql_heading: dict[str, str] = { #entrys must not change, only the values!
    "user": "root",
    "password": "3223",
    "adress": "127.0.0.1:8089", 
    "db": "pokedex_data"
}

#* global consts
DB_ENGINE_CHOICE: str = "pgsql" # Global db choice configuration for get_engine.
