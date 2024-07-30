#*Type anottation: the python way to inform types of data to certain variables
# WILL NOT be able to RESTRICT a type of data!!!

#Types available: str, int, float, object...

#* Variables
anInteger: int = 1
aFloatPoint: float = 1.17123901239
aListOfStrings: list[str] = ["Atila", "Marx", "Well"]
#You can test it: using these anottations will help seeing more errors in your code

#Create your own typos:
class Car:
    def __init__(self, velocity: float):
        self.velocity = velocity

aCar: Car = Car(90.917) #as the basic definition works, showing the typo.

#* Functions / methods
def loopAndPrint( listInserted: list ):
    for element in listInserted:
        print(element)

#if specified, will also consider strict typos of structures
#can be used such as typo 'list[int]' or 'dict[int, object]', and similarly.

def upperElementFromDict( dictionary: dict[int, str], entryInserted: int ) -> str:
    return dictionary[entryInserted].upper()

if __name__ == "__main__":
    loopAndPrint(aListOfStrings)
    print("\n" + upperElementFromDict( { 1: "Atila", 2: "lima" } , 2 ))

    a : str = 100
    print(a)
    print(type(a)) #still wont be cast to a String