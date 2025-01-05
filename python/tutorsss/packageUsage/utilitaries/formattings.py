def formatString(string: str) -> str:
	return string.strip() + f", \nplus the last char: {string[-1]}"
	
def formatNameAttr(object) -> str:
	listNameAttrs: list[str] = ["name", "title"]
	nameFound: str = ""
	
	for aName in listNameAttrs:
		if hasattr(object, aName.lower()):
			nameFound = aName.lower()
			break;
	
	if nameFound == "":
		return "the Attr was not found."
	
	return getattr(object, nameFound) + " is your name! Nice!"

if __name__ == "__main__":
	test = formatString("hey, how are you?")
	print(test)
	
	class Person:
		name = "Atila"
	
	aPerson = Person()
	test2 = formatNameAttr(aPerson)
	print("\n\n" + test2)