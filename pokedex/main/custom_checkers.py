# Useful BOOLEAN return typed checkers for client input values

from re import findall

def isValidColor(hex_input: str) -> bool:
    """
    Checks if a hex_input is a valid Hex Color string, apllying several checks.\n
    Will return False if any of the checks are failed.
    """
    
    #checking hashtag in start
    if hex_input.startswith("#") == False:
        return False
    else:
        #For future checkage
        hex_input = hex_input.replace("#", '')
    
    #checking count of values
    charCount: int = 0
    for _ in hex_input:
        charCount += 1
    if charCount != 6:
        return False
    
    #checking only valid hex values
    try:
        hexaPattern = r'\b[A-Fa-f0-9]{6}\b'
        hex_extracted: str = findall(hexaPattern, hex_input)
        if len(hex_extracted[0]) != 6:
            return False
    except IndexError: #if 
        return False
    
    #if none of the cases matched
    return True
    
if __name__ == "__main__":
    #prints False:
    print(isValidColor("112123"))
    print(isValidColor("#11213"))
    print(isValidColor("#1f12!3"))

    
    print(isValidColor("#1a2b3d")) #prints True