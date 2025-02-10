from fcts0 import tspac, endCode, line
from multiprocessing import Lock
#with something active, to this, after the final line: deactivate resource
line(4)
with open('debugfile.txt','r'):
    print('do something')
    #will close file here

#the list of resources is big, like Locks, Database connections, Processes, 
print(''); line(11)
lockA = Lock()
with lockA:         #avoid deadlocks
    print('do something with locks')

#you can make class oriented context managers:
class ManageFile:
    def __init__(self, filename, filemode):
        print('init')
        self.filename = filename
        self.filemode = filemode

    def __enter__(self): 
        print('entered')
        self.file = open(self.filename, self.filemode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:    
            self.file.close()
        print('exited')

tspac(); line(31)
with ManageFile('debugfile.txt', 'r') as file_o:
    line1 = file_o.readline()
    print(line1)
print('finished')

#for exceptions, an example: 
class ManageFile_withExceptions:
    def __init__(self, filename, filemode):
        print('init')
        self.filename = filename
        self.filemode = filemode

    def __enter__(self): 
        print('entered')
        self.file = open(self.filename, self.filemode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback): #se algo sem ser True ser informado, irá usar exc
        if self.file:   
            self.file.close()
        print('EXCs:', exc_type, '///', exc_value) #exception class, exception value raised
        if exc_type is not None:
            print('exception handled.')
        print('\nexited')
        return True         #returning True, will ignore the error dealed

tspac(); line(54)
with ManageFile_withExceptions('debugfile.txt', 'r') as file_e:
    lines = list(file_e.read().splitlines())    #dividing lines
    print(lines[-1], '<- is my line.')          #selecting my line
    file_e.somemethod()  #error 
print('finished') #if excepted without handling, won't continue here


#can also use a function to make it a context manager:
from contextlib import contextmanager

@contextmanager
def openManagedFile(filename, filemode):
    f = open(filename, filemode)
    try:
        yield f
    finally:
        f.close()

tspac(); line(78)
with openManagedFile('debugfile.txt', 'r') as file:
    print(file.readline())      
    print('file used')

endCode()