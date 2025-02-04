from fcts0 import tspac, endCode, line
from timeit import default_timer as timerit
import time
#if using assignment "=", vars will be the same
#create a copy: .copy() or conversion: list(), tuple(), set(), frozenset(), dict(), str(), int/float()

myList = [0, "name", 18, False]
myList2 = [0, 1, 0, 24]
#list: list()
myListAdd = myList + myList2
print(type(myListAdd))#list

#tuple: tuple()
myTuple = ("okBit",)#only usable, imutable
print(type(myTuple))#tuple
#ARRAYS USE MORE MEMORY AND TIME
tspac(); line(18)
myList3 = myList.pop()
myList.append("none")
print(f'{myList}\n{myList3}')

tspac()
line(26)
myList4 = list(myList)#copy the list
myList4.append(myTuple)#tuple inside list
myList += myTuple#new list value
print(myList4)
print(myList)

tspac()
line(32)
myList5 = list(myList)#0-4
print(myList5[1:3])#value setted to vallue setted-1
print(myList5[::2])
print(myList5[-2])#inversed direction
print(myList5[::-1])#easy inverted list

myList6 = [0, 29, 10, 1]
print(sorted(myList6))#same values, sorted
myList6.sort()
print(myList6[::-1])#decrescent sort

tspac()
#sets: set() literalmente teoria de grupos
line(45)
print("meu Set é:")
mySet = {1, 5, 3, 2, 2, 2}#mutable, no duplicates
print(mySet)
#mySetSorted = set(sorted(mySet)) not needed!!!
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 0}

#interseçoes
print("")
line(55)
print(f"{mySet.intersection(odds)} são os ímpares")
print(f"{mySet.intersection(evens)} são os pares")
print("")
if 10 in mySet: #nao completo! checar ultimo algarismo para dezenas e centenas!
    print(f"{mySet.union(evens)} é sua união com pares")
else:
    mySet.add(10)
    print(f"{mySet.union(evens)} é sua união com pares")

line(65)
print(f"{mySet.union(odds)} é sua união com ímpares")
print("estatisticamente mais impares que pares no original rsrs")
tspac()#valores não foram alterados, menos o 10 que foi adicionado no if statement.
mySet.pop()#saiu o primeiro el.
print(f"my set is: {mySet}")
print(f"{mySet.difference(odds)} é a diferença (Set - ímpares)")#diff dos conjuntos
print(f"{mySet.difference_update(odds)} é a diferença (Set - ímpares)")#retira os el
print(f"{mySet.symmetric_difference(odds)} é diferença simétrica ")#todos os elementos não comuns.
print(f"{mySet.symmetric_difference_update(odds)}  ")
print(f"{mySet.intersection_update(evens)} são os pares")#estudar _update

print(f"{mySet.issuperset(evens)} todos no Set estão nos pares")
mySet.remove(2)
print(f"{mySet.issubset(odds)} Set é subconjunto dos ímpares ")
mySet2 = frozenset([1, 2, 57])#imutavel.
print(mySet2, "is a frozenset, imutable")

tspac()
#strings: iteravel, mutável, str ""
line(86)
value = ("hello").title()#capitalize first letter(dont use in var)
print(value[0])
a = str(1)
try: 
    print(a + 1)#CANT ADD MATH here
except: print("cant do math")

a = """hello \
world"""
#lines are considered(triple "), \ tells code to continue in the next line
print(a)
line(98)
b = "Aa"
for i in range(len(b)):
    if b[i].isupper() == True:
        print("upper")
    else: print("lower") #.islower()

c = "okay"
print(c[::-1])#iterable.

print("")
line(109)
d = "oloco manows "  + c#adding str
print(d)
d = d + c#cant subtr
print(d)

print("")
line(116)
d = d.split("o")#separate (list) by excluding arg
print(d)
e = ",".join(d)#from list to string with arg("") in between
print(e)
e = "        " + e#blank space
print(e)
e = e.strip()#remove it :O
print(e)

print("")
line(127)
z = "many examples start with names"
if z.endswith("names") is True:
    print("z endswith.")
if z.startswith("many") is True:
    print("z startswith.")
else:
    print(z)

#timeit import default_timer, 

tspac(); line(138)
twArra= [d[5], d[3], 1, 58]
print(twArra)
onArra= ["ok", "NO"]
twArra.append(onArra)#if inserted an list, will go entirely. if +=, will only add vars (clean)
print(twArra)

tspac(); line(145)
def timing(dat):
    time.sleep(3)
    t1 = time.perf_counter()
    dat
    t2 = time.perf_counter()
    try:
        print(((t2 - t1)*100_000), type(dat))
    except AttributeError:
        print("not a .type arg")
        print(((t2 - t1)*100_000))
    return (t2-t1)*100_000#will print if print(def)

timing("abcde" * 10_000_00)
timing(["a", "b", "c", "d", "e"] * 10_000_000)
timing(["abcde"] * 10_000_000)
timing(set(["a", "b", "c", "d", "e"] * 10_000_000))
dat5 = ("abcde", ) * 10_000_000
timing(dat5)
#3, 1, 4, 4, 5, 3, 3, 1, 5, 4 ; multiple str list and set best of 10

#enquanto . se refere a um method da class type, def() se refere a funções aplicadas a estas
#time.sleep() por exemplo é uma method apenas do module time
endCode()
