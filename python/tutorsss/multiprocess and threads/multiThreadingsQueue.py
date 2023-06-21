from threading import Thread, Lock, current_thread
from queue import Queue     #first in is first out.
import time

def write():
    print('')

def list_threads(queue, lock):
    while True: 
        #with lock: #if i put a lock here it will only generate 1 thread(but will be cleaner in output) e a memoria vai ficar segura
            value = queue.get() #while loop is infinite, this blocks the execution to the queue length.
            time.sleep(0.2)
            print(f'in {current_thread().name} got {value}')#completely random
            print(f'{queue.empty()} que a fila esta vazia.')
            print('')
            time.sleep(0.5)
            queue.task_done()                                #para acabar cada thread/processo(em queue), e vai para o proximo

if __name__ == '__main__':   
    lockA = Lock()
    lockB = Lock()
    fila = Queue()
    total_threads = [] #apenas anotando, nao vai ser usado
    num_maxthreads = 5
        
    for n in range(num_maxthreads):
        t = Thread(target=list_threads, args=(fila, lockA))
        t.daemon = True             #mata o loop quando sai da main.
        total_threads.append(t)
        t.start()

    for i in range(1, 6): #1 - 5
        fila.put(i)         #setar posições
                 #block para que a main thread se junte inteira

    fila.join()
    print("END MAIN")


#value = fila.get()  #queue obj will return the first that got assigned// cant leave it in plain here.
print(fila.empty())  #T/F, now that it finished it will be empty.

#queues are often very used environment to build threads safely, with some level of management

print(__name__)