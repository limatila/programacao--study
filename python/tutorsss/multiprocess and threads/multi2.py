from multiprocessing import Process, Value, Array, Lock, freeze_support
import os
import time
from fcts4 import tspac
from queue import Queue

lockA = Lock()
fila = Queue()


def myTask(name, number, list):
    with lockA:
        time.sleep(0.005)
        print(f'printing:\n + {name}\n + {number.value}\n + {list[:]}') #slice to access all indexes


def acrescent(add_n, my_num):
    with lockA:
        time.sleep(0.005)     #only thing holding the pattern in output in 4th place, and still roughly.
        my_num.value += add_n
        print('done adding')


if __name__ == '__main__':
    total_processos = []
    num_processes = 4 
    value_share = Value('i', 60) #primeiro arg: uma string como nome de var: f, i, s, b, d
    list_share = Array('b', [True, False, True])

    print(f'values at beggining are {value_share.value}; {list_share}')
    tspac()
    for i in range(num_processes):
        p = Process(target=myTask, args=('vtnc', value_share, list_share,))
        p.daemon = True
        total_processos.append(p)
    p5 = Process(target=acrescent, args= (20, value_share,))

    p1, p2, p3, p4 = total_processos
    total_processos2 = [p1, p2, p3, p5, p4] #order of doing, should inplement a queue or a lock, probably

    for p in total_processos2: p.start()
    for p in total_processos2: p.join()
  
    print('END MAIN') 
    print(__name__)    
