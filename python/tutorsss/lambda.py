from fcts0 import endCode, tspac, line
a = 2

nam = lambda x: x==2 #var is def name, after lambda is args, return the content after:
print(nam(a))#2 == 2
#nam(def) = lambda(shortcut) x(any arg): _return_ 'content'

adicionar10 = lambda x: x + 10
var1 = adicionar10(34)
print(var1)

tspac(); line(16); odd_even = lambda x: x %2
def checkOE(memo):
    if odd_even(int(memo)) == 0:print("even")
    else: print("odd")
print(odd_even(6))
checkOE(6)

tspac(); line(23)
points2d = [[-453,455],[3,10]]
sortY = lambda x: x[1]#returns the second index of iterable 
points2d_Y_sorted = sorted(points2d, key= sortY)#make it sort var for every key(y coordinate)
print(points2d_Y_sorted)
sortPlus = lambda x: x[0] + x[1]#return the sum of iterable
points2d_sum_sorted = sorted(points2d, key = sortPlus)#make it sor var for every key(sum)
print(points2d_sum_sorted)

tspac(); line(31)
points2d_mixed = map(lambda x: (x[0] + x[1])*2, points2d)#map(func, list); mapeia de acordo com a func, está juntando e dobrando as vars
points2d_mixed = list(points2d_mixed)#need to stored to be read in 34
print(points2d_mixed)

tspac()
points3d = map(lambda x: [x/2, x/2+60, x/2], points2d_mixed)
print(list(points3d))#not converted(stored), not usable

print(''); line(39)
points2d_filtered = filter(lambda x: x%2 == 0, points2d_mixed)#filtra e atribui
print(list(points2d_filtered))

from functools import reduce
tspac(); line(44)
points2d_reduced = reduce(lambda x, y: x*y, points2d_mixed)#aplica a func para cada el., retorna um valor unico
print(points2d_reduced)

#every of this methods: def(func(lambda for shorter), var)

endCode()