from itertools import groupby, cycle, repeat, count


a = ['a', 'b', 'C', 'F', 5, 6]

def checkCap(val):
    try:
        return val.isupper()#pra cada valor vai retornar ESSE resultado
    except AttributeError: return 'not valid'

soma = groupby(a, key=checkCap)
for key, value in soma:
    print(key, list(value))

print(("\n"))
for i in count(5):
    print(i)
    if i == 5: break