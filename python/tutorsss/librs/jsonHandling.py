import json #will read
import C/ #need a file rn

jsonFile = {}
convertedFile = json.dumps(jsonFile, indent=2, separators=('; ', '= '), sort_keys=True)#convert to file

#json.load will load from a file(without assignment in the json)