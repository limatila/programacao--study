from fcts5 import tspac, line, endCode
import numpy as np #convention

#list: default python multivalored structure
#array: default for numpy, much faster because is written in C

#arrays can be multidimensional, from 1 to *


array1 = np.array([1, 3, 5, 10])

#properties----
print(array1.size) #length of array
print(array1.ndim) #number of dimensions in array
print(array1.shape) #length of each dimension of array

print(array1.dtype) #prevalent type of data
print(array1.itemsize) #size in bytes of prevalent type of data


#operations----
tspac(); line(23)
list1 = array1.tolist() #a copy, for example.
print(list1) 

def smallLogic(npArr):
    print("\nsmall logic for array:")
    if npArr[0] == 1:
        print("array is unchanged.")
        
smallLogic(array1)


print(""); line(35)
array2 = array1 * 2 #any kind of operation with unique values will be mapped in the array
list1 = list1 * 2 #default: python will operate in the list structure itself
print(array2, list1, sep=";\n")

print( "\n", array2 + 10, sep="") # +, -, *, /, %...

print(""); line(42)
calc1 = ( array2 / array1 ) #Broadcasting, it's selective calculation, can be done only with equal sized arrays
print(array2, calc1, sep=";\n") #This calc returns to the expoent used in 35


#more operations
tspac(); line(47)
print(np.sqrt( np.array([4, 9, 144]) ))