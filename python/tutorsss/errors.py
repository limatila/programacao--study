from fcts0 import endCode, tspac, line
#NameError: uma var ou um def nao reconhecido ou nao existe
#SyntaxError: digitação errada, espaços e parenteses,
#IndentationError: indentação errada, usar tab certo
#ValueError: valor não achado ou nao existe; uso errado entre tipos de vars(str, int, boolean)
#IndexError: index não foi achado, devido tamanho da lista não corresponder
#KeyError: index de key num dict() não foi achado ou não existe
#TypeError: soma entre vars de tipos diferentes(str, int, boolean)
#AttributeError: uso de um metodo ou atribuição nao existente para o dado
#ImportError
#circular import: o import está sendo usado infinitamente, mudar o nome do arquivo
#ModuleNotFoundError: modulo mal digitado ou não existe
#FileNotFound: arquivo chamado não reconhecido, não existe
#ZeroDivisionError: divisão por 0 não é permitida
'''
a = 2
if a == 2:
    raise Exception("SHOULDNT BE 2 OKKK")#mostra qualquer coisa como erro, para o codigo
'''

x = 6
assert(x>5), 'x nao e maior que 5' #AssertionError se o return é False

a = 8
try:
    b = a/0
except ZeroDivisionError: #or "Exception as e"
    b = 'NO'
print(b)

tspac()
try:
    c = a/0
except ZeroDivisionError as e: #printa a descrição do e
    print(e)
finally:
    print("non existant")#executa e continua o código; finallys' will be executed anyway...

print(""); line(40)
try:
    d = a/0
except Exception as e: #não especifico
    print(e)

tspac()
try:
    d = a/1
    a = 2
    d = a/2
except ZeroDivisionError as e:
    print(e)
except TypeError as e: #catches the first ocorrence possible
    print(e) 
else: #in case no error is catched
    print("no errors")
finally: #code end dealing with errors here, continues the code
    del d
    del a
    print("ok and cleaned")

    #print(a) #will raise NameError

tspac()
###create an err class: -------------------------------------
class myPipiSmol(Exception): 
    pass  #passa a exception
#raise myPipiSmol("han") #remove tag

#call it in some code
def checkErr(x):
    if x < 17: raise myPipiSmol("TOO SMOL BROOOO")
    else: print("ok ele e grande")
#checkErr(14) #remove tag
#to only print the err:
try:
    checkErr(14)
except myPipiSmol as e:
    print(e) #raise, dont stop program
finally:
    print("error dealed.")


#class with init:
class littleStr(Exception):
    def __init__(self, message, value): #with args
        self.message = message
        self.value = value

def strInterp(x):
    if len(x) < 10:
        raise littleStr('str is too small', x)#attribution
tspac()
try:
    myStr = "atilalim"
    strInterp(myStr)
except littleStr as e:
    print(e.value, "is the value") #can acess any args,
    print(e, "entire error class") #or print all
finally:   
    print("error dealed.")

endCode()