#* Recursividade - chamada repetida gerando um ciclo de execução
# Deve ser finito (se não entra em loop infinito, bug)
# Gera uma pilha de execução

#* Recursividade Direta: Função chama a si mesma

#1. inicial: 5 -> 1 + 2 + 3 + 4 + 5 (15)
debugSoma = []
def somaDeInteiros(numero: int) -> int:
    # Operações (opcional)
    debugSoma.append(numero)
    #* Caso base
    if(numero == 1): return 1
    #* Chamada recursiva
    return numero + somaDeInteiros(numero - 1)
print(somaDeInteiros(5))
print(debugSoma) # vendo a pilha de execução ser processada

#2. 5³ (5 * 5 * 5 = 125)
debugPotencia = []
def potenciaRecursiva(base: int, expoente: int) -> int:
    debugPotencia.append(base)
    if(expoente == 1): return base
    return base * potenciaRecursiva(base, expoente - 1)
print( potenciaRecursiva(base=5, expoente=3) )
print(debugPotencia)


#3. Sort de maior para o menor ( [randint(1, 5)] * 5 ) -> (1, 2, 3, 4, 5)
debugHanoi = []
def hanoiTreeRecursivo(numeros: list[int]) -> list[int]:
    ...


#4. MDC de 10 e 25 (5)
debugMdc = []
def menorDivisorRecursivo(numeros: list[int]) -> int:
    ...