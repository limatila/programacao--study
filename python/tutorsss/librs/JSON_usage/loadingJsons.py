from fcts8 import tspac, line, endCode
from json import dumps, loads, dump, load
from json import JSONDecoder


example_data = { # Key-Value structure
    "number": 4,
    "word": "four",
    "rules": [
        True, False, True, True,
    ]
}


line(16)
#* Using the basic json functions
#Saving
data_dumped = dumps(example_data)
print(type(data_dumped))       # As JSON, it is represented as a String (single line).

#Loading
data_loaded = loads(data_dumped)
print(type(data_loaded))       # As Python interprets, it is represented as a Dict.


tspac(); line(26)
#* In files: remove the plural.
# Saving in file
with(open("./data.json", "w")) as file:
    dump(example_data, file)    # ? will be saved in root dir of execution...
    print("Saved!")

#Loading from file
with(open("./data.json", "r")) as file:
    data_loaded = load(file)
    print("Loaded!")    

print(data_loaded.get('rules')[2])  # Dictionary loaded from the Json.


tspac(); line(42)
#* Costumization of loading: usage of JSONDecoder / Encoder
# the json module uses a default object for CODEC of Jsons in their functions.
# we can create a object of our own to stablish rules when parsing a Json
class binaryRulesDecoder(JSONDecoder):
    def decode(self, Json_string):     #* 'def default' in JSONEncoder implementation
        Json_obj = super().decode(Json_string)
        if 'rules' in Json_obj:
            Json_obj['rules'] = ['Yah' 
                                 if x == 1 #If True
                                 else 'Nah' #Else
                                 for x in Json_obj['rules']
            ]
        return Json_obj
    

with(open("./data.json", "r")) as file:
    binaryInterpreted: list = load( file, cls = binaryRulesDecoder ).get('rules') # 'cls' takes the Decoder implemented Class
print(binaryInterpreted, "Decoded from file") # Dict loaded from interpreted Json

#or with created object
binaryInterpreted_two: list = binaryRulesDecoder().decode(data_dumped).get('rules')

print(binaryInterpreted_two, 'Decoded from var')

#TODO: There is more to know about how the decoding works, so you can create rulesets more easily and that will work well.

endCode()