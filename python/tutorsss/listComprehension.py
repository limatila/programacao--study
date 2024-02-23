from fcts0 import tspac, line, endCode
myNums = [1, 3, -93, 357, 5, 59, 1230]
myChars = ['ati', 'bit', 'mom']

#*see more about in defsArgs.py
#About *Args - flexible args acceptance
line(6)
a, b, c = myChars
print(a, b, c) #vars separadas
del a, b, c

tspac(); line(11)
*primeiros, ultimo_num = myNums
print(primeiros)
print(ultimo_num)

print('')
primeiro, *ultimos_num = sorted(myNums)
print(primeiro, ' - ', ultimos_num)


tspac(); line(21)
def foo(a, b, *, c): #vai tornar 'c' um keyword parameter
    print(a, b, c)
foo(1, 2, c=1)

tspac(); line(26)
def fe(myVar):
    *firs, final = myVar
    return firs

names = ['well', 'gabu', 'yume']
print(fe(names)) #can be assigned to var
# print(firs) will error, firs is in local scope

#About **Kwargs - flexible KeyWord args acceptance
def faul(*direct, **described):
   print(*direct)
   for keys, values in described.items(): #*default printing of dicts items
      print(keys, ":", values)

#Actual List Comprehension - A single lined way to grab items for a list(study with dicts too?..)
tspac(); line(38)
todosNums = [num for num in myNums] #numero tirado de cada numero na lista Nums
pares = [num for num in todosNums  if num%2 == 0] #agora aceita apenas números com resto 0
quadrados = [num**2 for num in todosNums if num >= 0] #eleva os números e aceita números inteiros
print(*todosNums, *pares, *quadrados, sep=",\n")

endCode()