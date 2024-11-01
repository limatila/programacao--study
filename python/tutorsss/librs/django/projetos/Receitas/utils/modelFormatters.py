
#Formatadores de string para models

def formatName(entryName: str) -> str:
    result: str = str(entryName)
    result[-1] = 'Z'
    return result