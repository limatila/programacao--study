import copy
from fcts0 import tspac, endCode, line, say_hi

say_hi('Atila, this is your')
valueA = 2
valueB = ['a', 'z', 0.5]
valueC = [
    list(valueB[::2]), #primeiro e ultimo
    [False, False]
]

# valueD = ValueA não copiará, só apontará pra mesma referencia
#shallow: cópia em 1 camada apenas, 'only references of nested child objects', dois métodos.
valueD = int(valueA)
valueD +=2; print(valueA, 'is copied valueA')

valueE = copy.copy(valueD); 
valueE -= 6; print(valueD, 'is copied valueD')
#still wont work with deeper objects:
tspac(); line(21)
valueC_co = copy.copy(valueC)
valueC_co[1][1] = valueE
print(valueC, 'is the original;', valueC_co, 'is the copy') #note que o ultimo valor será o mesmo pras duas, o valor original de 'valueC' sendo mudado tambem

#deep: cópia totalmente independente, todas as camadas serão avaliadas. Vale pra qualquer objeto como /class Person, Cat, etc.
line(27); del valueC_co
valueC_1 = copy.deepcopy(valueC)
valueC[1][1] = valueE
print(valueC, 'is the original;', valueC_1, 'is the copy')

endCode()
