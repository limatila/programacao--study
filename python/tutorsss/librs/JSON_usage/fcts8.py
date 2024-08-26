def say_hi(value):
    print(f"hi {value}")

def endCode():
    print("\n \nEND OF CODE")

def tspac():
    print("")
    print("")

def poten(value, pot):
    soma = value
    for i in range(pot - 1):
        soma = value * soma
    return soma

def line(linha):
    try: 
        print(f"line {int(linha)}:")
    except:
        return (f"line {int(linha)}:")
    
def empty(var): #'', 0, [], {}
    varType = type(var)
    var = varType()
    return var

#myVar = empty(myVar) in your code
