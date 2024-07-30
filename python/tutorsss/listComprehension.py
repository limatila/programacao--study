from fcts0 import tspac, line, endCode
myNums = [1, 3, -93, 357, 5, 59, 1230]
myChars = ['ati', 'bit', 'mom']

#*see more about in defsArgs.py
#*About *Args - flexible args acceptance
line(8)
a, b, c = myChars
print(a, b, c) #vars separadas
del a, b, c

tspac(); line(13)
*primeiros, ultimo_num = myNums
print(primeiros)
print(ultimo_num)

print('')
primeiro, *ultimos_num = sorted(myNums)
print(primeiro, ' - ', ultimos_num)


tspac(); line(23)
def foo(a, b, *, c): #vai tornar 'c' um keyword parameter
    print(a, b, c)
foo(1, 2, c=1)

tspac(); line(28)
def fe(myVar):
    *first, final = myVar
    return first

names = ['well', 'gabu', 'yume']
print(fe(names)) #can be assigned to var
# print(firs) will error, firs is in local scope

#*About **Kwargs - flexible KeyWord args acceptance
def faul(*direct, **described):
   print(*direct)
   for keys, values in described.items(): #*default printing of dicts items
      print(keys, ":", values)

#*Actual List Comprehension - A single lined way to grab items for a list(study with dicts too?..)
#? It is a faster option!!!
tspac(); line(44)
todosNums = [num for num in myNums] #numero tirado de cada numero na lista Nums
pares = [num for num in todosNums  if num%2 == 0] #agora aceita apenas números com resto 0
quadrados = [num**2 for num in todosNums if num >= 0] #eleva os números e aceita números inteiros
print(*todosNums, *pares, *quadrados, sep=",\n")

tspac(); line(50)
apenas_ati = [
    nome
    for nome in myChars
    if nome == "ati"
    if nome[0] == 'a' #várias condições sendo usadas para aceitar um elemento(nome)
]
print("Só o Ati: ", *apenas_ati)

tspac(); line(60)
import numpy as np
umArray = np.array([[1, 2, 3],
                    [10, 20, 30]], dtype=np.int8)
arrayFiltrado = [
    int(num) #? converting objects to int
    for fila in umArray
    for num in fila #o elemento principal, referenciado no começo
    if num % 2 != 0
] #nesse caso, foi como um np.array.flatten()
print("Elementos ímpares: ", arrayFiltrado)

print(""); line(72)
#Classificando numeros:
impar_par = [ "Par" if num % 2 == 0 else "Impar" for num in range(5) ]
print("classificação entre ímpares e pares: ", *impar_par, sep="\n")


tspac(); line(71)
#* Em Dicts:
umDict = {
    "a": 1,
    "b": 2
}

lista_de_valores = [
    value
    for key, value in umDict.items() #use the built-in methods!
]
print(lista_de_valores)

#? There's also much more complex comprehensions

endCode()