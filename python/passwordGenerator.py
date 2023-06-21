import random
from fcts import endCode, line, tspac

lowerC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperC = lowerC.upper()
nums = "1234567890"
symb = "!#@*_"

all = lowerC + symb + upperC + nums
m = 9
line(12)
def generatePass(use, rep):
    soma = ""
    password = random.sample(use, int(rep))
    for iter in range(len(password)):
        soma += password[iter]
    return soma
print(generatePass(all, m))

endCode()