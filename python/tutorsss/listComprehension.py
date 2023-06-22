from fcts0 import tspac, line, endCode
myNums = [1, 3, 5]
myChars = ['ati', 'bit', 'mom']

line(6)
a, b, c = myChars
print(a, b, c) #vars separadas
del a, b, c

tspac(); line(11)
*primeiros, ultimo_num = myNums
print(primeiros)
print(ultimo_num)

print('')
primeiro, *ultimos_num = myNums
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

endCode()