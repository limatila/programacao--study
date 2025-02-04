from fcts8 import endCode, tspac, line
from itertools import permutations, combinations, product, accumulate, groupby, count, cycle, repeat
from itertools import combinations_with_replacement
import operator
a = [1, 7, 5]
b = [2]
soma = list(permutations(a))#object
for i in range(len(soma)):
    print(soma[i])
myStr = "são permutações"
myStr = myStr.encode(encoding = 'UTF-8', errors = 'strict')#encode utf, raise errors
myStr = myStr.decode()#decodes
print(myStr)

tspac()
soma = list(combinations(a, 2))#object, qualquer repetição de conjunto é eliminada
for i in range(len(soma)):
    print(soma[i])
print('são', len(soma), "combinações para 2 lugares")

tspac()
soma = list(combinations_with_replacement(a, 2))#object, repetições sao consideradas
for i in range(len(soma)):
    print(soma[i])
print('são', len(soma), "combinações para 2 lugares, \nrepetindo pessoas(como tipos)")

tspac(); line(30)
print("product:")
soma = list(product(b, a, [1]))#will group the variables to a tuple
print(soma)

tspac()
print("accumulate:")
print(a)
soma = list(accumulate(a))#object
print(soma)#opera na diagonal /, coloca o resultado no segundo slot

print(""); line(40)
soma = list(accumulate(a, func = operator.mul))#object, will multiply in / with .mul... will sub with .sub
print(f"accumulate multiplicando: \n{a} \n{soma}")
soma = list(accumulate(a, func = max)); print(f"accumulate decidindo máximo: \n{a} \n{soma}")#coloque um numero maior antes no list

tspac(); line(46)
def minor_2(val):
    return val <= 2

print("groupby 2 ou menos: ")
soma = groupby(a, key=minor_2)#first: var, second: my func/expecification #creates a key/value pair, like dicts(not a dict)
for key, value in soma:
    print(key, list(value))#need to list values object

