from requests import get
from json import loads

resultIvysaur = get("http://localhost:8000/v0/get/pokemon/2/").content

Ivysaur = loads(resultIvysaur)
print(Ivysaur)
print(f"{Ivysaur["id"]} is the natural id of {Ivysaur["name"]}")