import random #not indicated for security
from fcts import endCode, line, tspac

lowerC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperC = lowerC.upper()
nums = "1234567890"
symb = "!#@*_"

all = lowerC + symb + upperC + nums
m = 9
line(12)
def generatePass(use, rep): #creates secure random password
    soma = ""
    password = random.sample(use, int(rep))
    for iter in range(len(password)):
        soma += password[iter]
    return soma
print(generatePass(all, m))

#randint, randrange, normalvariate, choice, choices, shuffle, 

import secrets
tspac(); line(22)
a = secrets.randbits(7)#args is bits from binary 0101
b = secrets.choice(all)
print(a, b)

tspac(); line(27)
import numpy as np
a = np.random.rand(3)#creates 3 (or - 3x3 - with colon)
b = np.random.randint(0,10,3)#start, end(excluded), size(can be tuple to make grid)
#random.shuflle, random.seed





endCode()