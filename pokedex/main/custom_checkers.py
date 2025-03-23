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
        
    #checking only valid hex values
    hexaPattern = r"^--[0-9a-fA-F]+(--)?\s"
    hex_extracted: str = findall(hexaPattern, hex_input)
    if len(hex_input) != len(hex_extracted):
        return False
    
    #checking count of hex values
    charCount: int = 0
    for _ in hex_input.replace("#", ''):
        charCount++
    if charCount != 6:
        return False
    
    #if none of the cases matched
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    