#adiciona funcionalidade de uma def para outra(extende)
from fcts0 import tspac, line
import functools
from itertools import count
#template sem args
def set_decorate(func): 
    def wrapper():
        print("START")
        func()
        print("END")
    return wrapper

#template com args:
def set_decorator(func):  #define the decorator fct
    #keep the function name in advance
    @functools.wraps(func)
    def say_hi(*args):
        print('Hi!')
        result = func(*args)
        print(result)
        print("End")
        return result
    return say_hi

@set_decorator #set the decorator
def add20(x): 
    return x+20 
add20(20) 
# @ stands for: 'add20 = set_decorator(add20)'

tspac(); line(29)
print(add20.__name__) #check func name


tspac(); line(33)
def repeater(num): #for loop
    def wrapper(func):
        @functools.wraps(func)
        def loop(*args):
            for _ in range(num):
                result = func(*args)
            return result
        return loop
    return wrapper

@repeater(num=4)
def print_this(o):
    print(f'{o} was printed!')
print(print_this.__name__)
print_this("OKAY")

#nested: vai executar o na ordem das linhas de codigo

import time
#time counter for single args:
tspac(); line(57)
def timing_dec(func):
    @functools.wraps(func)
    def timing(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        result = t2 - t1
        try:
            return (((result)*100_000))
        except AttributeError:
            print("not a .type arg")
            return ((result)*100_000)
    return timing

@timing_dec
def set_data(dat):
    dat             #returned normally as float

x = "abcde" * 10_000_00
print(set_data(x), type(x))

#HOW TO MAKE IT A FCT NOT JUST A PRINT? dude make it practical please...
# @set_data           
# def formatTimingProcess(x): 
#     print(set_data(x), type(x))

# a_data = ("abcde" * 10_000_00)
# formatTimingProcess(a_data)

#obs: printing the result is faster than storing with 'return'