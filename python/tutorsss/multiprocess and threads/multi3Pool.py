from multiprocessing import Pool  #creates multiprocesses that takes small chunks of a process to do it simoutaneously
from fcts4 import say_hi, endCode

if __name__ == '__main__':
    pool = Pool()     #map, apply, join, close,... (check docs)

    result = pool.map(say_hi, 'atila')
    #result2 = pool.apply(say_hi, numbers[2])

    pool.close()
    pool.join()
    
    #print(result2)

endCode()