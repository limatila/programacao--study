from multiprocessing import Process, freeze_support
import os
from fcts4 import say_hi
import time
from functools import wraps

import sys 
#reference counting(example for GIL). conta quantas vezes a variável foi usada
a = []
b = a
print(sys.getrefcount(b))#'a' foi refericiado em 4, 5, e no arg em 6. (3 vezes)
#b = a. 'b' é 'a' até mesmo como nome de var

#GIL will only allow 1 thread per time by using a global lock, only adding more time to execute the other. 
#still can be avoided with multiprocessing

#Py_BEGIN_ALLOW_THREADS
#Py_END_ALLOW_THREADS should close and reopen the GIL

meus_processos = []
minhas_cpus = os.cpu_count()

"""trying to decorate the time.sleep()
def waiting(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        time.sleep(0.3)         #debug
    return wrapper

say_hi = waiting(say_hi)
"""

#creating process:
if __name__ == '__main__':  #need to use cuz of a tiny time delay in cpus
    freeze_support()
    for i in range(minhas_cpus):                                  #para cada cpu: os.cpucount()
        p = Process(target=say_hi, args= "A")                     #crie um processo com target em algo. args=1 caractere ou int
        meus_processos.append(p)                                  #adicione eles a lista de processos

#starting process:
for processo in meus_processos:
    processo.start()
#join processes:
for processo in meus_processos:  
    processo.join()                #a main thread deve esperar os processos acabarem para acabar
#join() está entrando no processo em si, só adicionando a si mesmo na lista
print("END MAIN")#need more study.