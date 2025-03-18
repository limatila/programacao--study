from requests import post, get
from datetime import datetime
from json import loads

from pokedex.main.api_pokedex import API_VERSION
from pokedex.tests.utils import write_output_local

if __name__ == "__main__":
    #* Executing these POSTs should require knowledge of what exists in DB, for related data to be added.
    now = datetime.now()
    write_output_local(f"- POST (modified) Output from date: [{now}]", and_print=True, reset_output_file=False)

    #New Ability Category
    HashtagCharacter = "%23"
    categoryName = "waTEr"
    colorValue = f"{HashtagCharacter}51A8FF"
    resultFire = post(f"http://localhost:8000/{API_VERSION}/post/abilitycategory?name={categoryName}&color={colorValue}").content

    FireCategory = loads(resultFire)
    write_output_local(FireCategory, and_print=True)

    #New Ability Compatibility w/ pokemon
    pokemonName = "iVySaur"
    abilityName = "tackle"
    resultCompatibility = post(f"http://localhost:8000/{API_VERSION}/post/abilitycompatibility?id=3&pokemon={pokemonName}&ability={abilityName}").content

    NewCompatibility = loads(resultCompatibility)
    write_output_local(NewCompatibility, and_print=True)

    # Checking new Compatibility in GET method
    resultCompatibility = get(f"http://localhost:8000/{API_VERSION}/get/abilitycompatibility?id=3&pokemon={pokemonName}&ability={abilityName}").content

    Compatibility = loads(resultCompatibility)
    write_output_local("GET the last POST - " + str(Compatibility), and_print=True)