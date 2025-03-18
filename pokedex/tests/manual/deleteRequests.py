
from random import randint
from requests import delete, post, get
from datetime import datetime
from json import loads

from pokedex.main.api_pokedex import API_VERSION
from pokedex.tests.utils import write_output_local

if __name__ == "__main__":
    now = datetime.now()
    write_output_local(f"- DELETE Output from date: [{now}]", and_print=True, reset_output_file=False)

    #Testing with compatibility /w random pokemon
    randomPokeName = loads( get(
            f"http://localhost:8000/{API_VERSION}/get/pokemon/id/{randint(1, 1025)}/"
        ).content
    )["name"]
    abilityInsert = "Quick Attack"
    resultNewTestCompatibility = post(
        f"http://localhost:8000/{API_VERSION}/post/abilitycompatibility?pokemon={randomPokeName}&ability={abilityInsert}"
    ).content
    write_output_local("POST the test compatibility: " + str(resultNewTestCompatibility), and_print=True)

    #from time import sleep; sleep(10); #see it created in db, manually

    #Deleting Compatibility by names
    resultDeleteCompatibility = delete(f"http://localhost:8000/{API_VERSION}/delete/abilitycompatibility?pokemon={randomPokeName}&ability={abilityInsert}").content

    deletionResponse = loads(resultDeleteCompatibility)
    write_output_local(deletionResponse, and_print=True)

    #Check delete with GET
    resultCheckDeleted = get(f"http://localhost:8000/{API_VERSION}/get/abilitycompatibility?pokemon={randomPokeName}&ability={abilityInsert}").content

    CheckDeletion = loads(resultCheckDeleted)
    write_output_local("GET the compatilibility that was deleted: " + str(CheckDeletion), and_print=True)