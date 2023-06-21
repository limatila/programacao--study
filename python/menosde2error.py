from fcts import endCode
file = [0, 3, 5, 2, 6, 12]*50 
#levantar erro mostrando quantos nums abaixo de 2 há na lista

coun = 0 
for i in file: #adicional -----
    if i == 0: coun+= 1
print("there are", coun, "0s in file") #2 instances.50= 100
del coun

#programa------------------------------------------------------------------------------
def whosMinor2(arra): 
    obj = set(filter(lambda x: x<2, file))
    return obj #retorna "set()"

minor2 = whosMinor2(file)

if len(minor2) > 0:
    raise Exception(f"there are {len(minor2)} numbers lesser then 2 in the file: {minor2}")


endCode()#need to test doing try-except now
'''
class entitledError(Exception):
    def __init__(self, message, coun):
        self.message = message
        self.coun = int(coun)


def xInList(arr, num):
    soma = 0
    for memo in arr:
        if arr[memo] ==num: 
            soma+=1
    return soma

def menosDe2(x):
    if x <2: raise entitledError('é um numero menor de 2', xInList(file, ))
'''