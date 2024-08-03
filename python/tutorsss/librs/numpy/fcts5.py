def say_hi(value):
    print(f"hi {value}!")

def endCode():
    print("\n\nEND OF CODE")

def tspac():
    print(("\n"))

def poten(value, pot):  #give potencys, depending on args(PORQUE EU NAO LEMBRO COMO FUNCIONA?????)
    finalValue = int(value)
    for i in range(pot - 1):
        finalValue = value * finalValue
    return finalValue

def line(linha): #printa linhas(int apenas)
    try: 
        print(f"line {int(linha)}:")
    except:
        return (f"line {int(linha)}:")
