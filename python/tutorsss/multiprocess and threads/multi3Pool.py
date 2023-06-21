from multiprocessing import Pool  #creates multiprocesses that takes small chunks of a process to do it simoutaneously
from fcts4 import say_hi

if __name__ == '__main__':
    pool = Pool()     #map, apply, join, close,... (check docs)
    numbers = range(10)
    mylist = []       #range to list obj
    for i in numbers:
        mylist.append(i)

    result = pool.map(say_hi, mylist)
    #result2 = pool.apply(say_hi, numbers[2])

    pool.close()
    pool.join()
    
    print(result)   
    print(result2)