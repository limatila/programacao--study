# Trying to stablish a constant in a defined Class
from copy import deepcopy

class Constant():
    def __init__(self, value: any):
        self.__dict__["__value"] = deepcopy(value)

    #* preventing changes
    @property
    def __VALUE__(self):
        return self.__dict__["__value"]  # Return the constant value

    def __setattr__(self, key, value): #__setattr__ constrols behavior when a key of class is changed.
        if key != "__backupdict__":
            raise AttributeError("Cannot modify Constants.")
            
    
    #finally, dispensing use of .value when printing
    def __str__(self):
        return str(self.__VALUE__)
    def __call__(self, *args, **kwargs):
        return(self.__VALUE__)


if __name__ == "__main__":
    a = { 
        "value1": 1,
        "value2": 2
    }
    constant_one = Constant(a)
    constant_two = Constant("abc")
    try:
        constant_two.__VALUE__ = constant_two.__VALUE__.replace("a", "!")
    except AttributeError as err:
        print("Error caught! ->" + str(err))

    try:
        constant_one.__VALUE__["value1"] = constant_two.__VALUE__ #! still passing with no issues...
    except AttributeError as err:
        print("Error caught! ->" + str(err))

    print(constant_one)