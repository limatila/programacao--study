from fcts0 import tspac, line

#needs yield keyword
def mygen():        #save memory for large data(não salva vars)
    yield 'name'
    yield 2
    yield 4

g = mygen()

v = next(g) #return and pause
print(v)

v = next(g) #return and pause
print(v)

#will stop at the final iteration, wont continue

#sum(), sorted(), 

tspac(); line(22)
def counting():
    print('Starting...')
    num = 0
    while not num >5:
        yield num
        num+=1

for i in counting(): print(i)

nums = []
tspac(); line(33)
def listCount(numb):
    num = 1
    while num <= numb:
        nums.append(num)
        num+=1
    return nums

print(listCount(3))

def listCount_generator(n):
    start = 1
    while start <= n:
        yield start
        start +=1

print(sum(listCount_generator(3))) #a diferença é que eu não atribui nada a um list, e sim só usei o gerador.
soma = [x for x in listCount_generator(3)]#list comprehension
print(soma)#aqui eu salvei(usando mais memória)

#posso salvar o gerador em list()
tspac(); line(54)
def newGen():
    yield range(100000) 

newGenRange = [x for x in newGen()]
newGenList = list()
for i in newGenRange[0]:
    newGenList.append(i)

import sys
print(sys.getsizeof(newGen()))
print(sys.getsizeof(newGenList)) #for a significative ammount, generators is much better
print(newGenRange)
print(newGenList[0], newGenList[-1])

#to get a specific value, i can use an list and erase it..
selected = newGenList[3609] #0 = 0, 1 = 1, index 3609 = 3609
print(selected)
del newGenList
try:
    print('')
    print(newGenList)
except NameError as e:
    print(e)

print('a') #code continues

