from fcts0 import endCode, line, tspac
#args x parameters: parametros são o que a função pede para funcionar, argumentos são o que é dado para a função funcionar. um é pré, o outro pós definição da Def. Um paramêtro pode ter sua arg definida na criação(são chamados default args).
line(4)
def attr(x, attr=2): #parameters defined
    x = attr
    return x

print(attr(10)) #only needed one arg

#keyword x positional args: em vez de apenas organizar os argumentos na ordem necessária, atribuir 'parametro=arg'(parametro=dado). arg posicional não usa atribuições com '='. Posso misturar tudo
#argumentos variáveis: *args, **kwargs, for positional and keyword. Aceitam qualquer número de args na função, quando chamada
print(''); line(13)
def printarQualquerCoisaTudoJunto(*args):
    soma = ''
    for arg in args:
        soma += arg
    print(soma)
print(2, 3, 'a', '5', attr(20))

tspac(); line(21) 
def print_theargs(*args, **kwargs): 
    #args é um list, kwargs é um dict:
    argsArra = []
    kwargsDict = {}
    print('args:')
    for arg in args:
        argsArra.append(arg) #mais organizado
    print(argsArra)

    print('kwargs:')
    for key in kwargs:
        soma = {f'{key}': kwargs[key]} #key/value: par/arg
        kwargsDict.update(soma)
    print(kwargsDict) 


print_theargs(1, 3, 52, 3, 4.4, six=6, myBoy="BOY")

print('')
args_I_wantToCall = (2, 4, 'tree')
print_theargs(*args_I_wantToCall)        #unpacking args. 
# with ** we can unpack dicts with keys and their args '{'key': arg}'

tspac(); line(45)
def fe(a, b, c):
    print(a, b, c)

myArgs = {'a': 1, 'a': 5, 'b': 3, 'c': 4, 'a': "fe"} #o ultimo declarado é levado em conta
fe(**myArgs)


#local vs global args: i can make the local(only defined in my Def) to be Global(out of the Def):
#def myDef(): 
#    global 'var'; .....
#if i need to read something outside of the Def, it will need to be Global. 

#parameter passing - by value or parameter: 
tspac(); line(59) #the args passed in the call are not changed if they are an imutable class(list), because they are local(only changed in Def).
def reasign(x):
    #global x will give error(see it for urself)
    x += 2

x = 5 #out of the function
print(x, 'will still be the same cuz local')
#see more of it...


