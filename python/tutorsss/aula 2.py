import pandas as pd

myData = {
    'name': ['atila', 'lima']
}

tabela = pd.DataFrame(myData)
print(tabela)

print("")
print(myData['name'])
print(myData["name"][0])