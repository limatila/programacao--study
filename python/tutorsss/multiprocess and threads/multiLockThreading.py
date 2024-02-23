from threading import Thread, Lock
import time

#a lock is holded by a thread to make it task
#a lock needs to be released to be used by another thread
#if i don't release it, it can be resulted in bugs or deadlocks. #.acquire(), .release()

#Defining locks
lockA = Lock()
lockB = Lock() 
lockC = Lock()
locks = [lockA, lockB, lockC] #using different locks means different memorys

#Defining task for threads
value = 3
def decreaseValue(lock, strin): #decrease in local and store back to the global value
    global value
    with lock: #will acquire and release the lock, to avoid deadlock.
        lockC.acquire()
        local_v = value
        local_v -= 1
        time.sleep(0.3)
        value = local_v
        print(strin) #aditional
        lockC.release()             #always holding a lock will share the memory between threads


#Set the threads used
if __name__ == '__main__': #It means if this file is executed directly, without being imported. __main__ suggest it is the original file that's being runned.
    print(f"this is the start value, folks: {value}")

    thread1 = Thread(target=decreaseValue, args= (locks[0], "thread done.")) #t1
    thread2 = Thread(target=decreaseValue, args= (locks[1], "thread done.")) #t2. do not use lock[2]
    threads = [thread1, thread2,] #can try more

    for t in threads:
        t.start() #starting
        t.join()  #waiting to close


    print(f'this is the end value, folks: {value}') #will change because the threads have solved it
#every ok marks one thread finished
#check out for memory leaks here