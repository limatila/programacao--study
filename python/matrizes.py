from functools import reduce
from fcts import tspac, line, endCode

matriz1 = [             #3x3, ij
        [1, 2, 3],
        [5, 25, 100],
        [-1, 0, 24]
    ]

matriz2 = [
    [6, 7, 8],         #2x3, ij
    [10, 20, 30]
]

matriz3 = [
    [1, 1, 1],       #irregular, assimétrica
    [2, 2, 2],
    [3]
]

matriz4 = [         #2x3
    (1, 2, 3),
    (-1, 0, -2)
]

matriz5 = [         #3x2
    (1,2),
    (3,4),
    (5,1)
]

matriz6 = [
    [9, 29, 49],      #toda torta
    [50],
    [9, 18, 24, 100]
]
print(matriz3[2][0]) #acessar um valor
tspac(); line(39)
for linha in matriz4:
    for num in linha:
        print(num)
tspac()

#traço de matriz: a diagonal principal é somada
def traco(matriz):
    i = 0; soma = 0
    try:
        while i < len(matriz):
            soma += matriz[i][i]
            i += 1
    except IndexError:
        pass
    print(str(soma)+' sera o traco da matriz '+ str(matriz))
line(55)
traco(matriz5)

tspac(); line(59)
#multiplicação: o numero de colunas da primeira matriz deve ser igual ao numero de linhas da segunda. 2x3, 3x2..
def multipMatriz(m1, m2):
    i2 = 0
    multis_result = []
    final = []
    for linha in m1:
        i = 0
        if len(linha) == len(m2):
            for num in linha:
                resultm = num * m2[i][i2]
                multis_result.append(resultm)
                i+= 1
            soma = map(lambda x, y: x+y, multis_result)
            i+=0
        if len(linha) == len(m2):
            for num in linha:
                resultm = num * m2[i][i2]
                multis_result.append(resultm)
                i+= 1
            soma = map(lambda x, y: x+y, multis_result)          #need to make it work and clean
            final.append(tuple(soma))
        print('line done')
    return final

print(multipMatriz(matriz4, matriz5))