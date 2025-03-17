from requests import get
from datetime import datetime
from json import loads

from pokedex.main.api_pokedex import API_VERSION
from pokedex.tests.utils import write_output_local

if __name__ == "__main__":
    #* It's wise that you run this after DB has some data inserted.
    now = datetime.now()
    write_output_local(f"- Output from date: [{now}]", and_print=True, reset_output_file=False)

    #Pokemons w/ id
    resultIvysaur = get(f"http://localhost:8000/{API_VERSION}/get/pokemon/id/2/").content

    Ivysaur = loads(resultIvysaur)
    write_output_local(Ivysaur)
    print(f"{Ivysaur["id"]} is the natural id of {Ivysaur["name"]}")

    #Pokemons w/ name
    resultMewtwo = get(f"http://localhost:8000/{API_VERSION}/get/pokemon/name/mewtwo/").content

    Mewtwo = loads(resultMewtwo)
    write_output_local(Mewtwo)
    print(f"{Mewtwo["name"]} has the natural id of {Mewtwo["id"]}")

    #Abilitys
    resultTackle = get(f"http://localhost:8000/{API_VERSION}/get/ability/name/tackle/").content

    Tackle = loads(resultTackle)
    AbilityType = Tackle.get("AbilityType")
    AbilityCategory = Tackle.get("AbilityCategory")
    write_output_local(Tackle)
    print(f"Ability {Tackle["name"]} was seen since {Tackle["generation"]}")
    print(f"Ability {Tackle["name"]} is of type {AbilityType}") #! temporary
    print(f"Ability {Tackle["name"]} is of category {AbilityCategory}")

    #AbilityCompatibilities
    pokemonToVerify = "bulbasaur"
    abilityToVerify = "tackle"
    resultCompatibility = get(f"http://localhost:8000/{API_VERSION}/get/abilitycompatibility?pokemon={pokemonToVerify}&ability={abilityToVerify}").content
    
    compatibility = loads(resultCompatibility)
    write_output_local(compatibility, and_print=True)
    assert compatibility["isCompatible"] == True
