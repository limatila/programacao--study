from fcts5 import tspac, line, endCode
import numpy as np #convention

#list: default python multivalored structure
#array: default for numpy, much faster because is written in C

#arrays can be multidimensional, from 1 to *


array1 = np.array([1, 3, 5, 10])
arrayRange_10 = np.arange(0, 10, 2) #mounts the array in a range, and can take steps (third Arg)

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
    print("\nsmall logic for array...")
    list1[0] = False
    if npArr[0] == 1:
        print("array is unchanged.")
        
smallLogic(array1)


print(""); line(35)
array2 = array1 * 2 #any kind of operation with unique values will be mapped in the array
list1 = list1 * 2 #default: python will operate in the list structure itself
print(array2, list1, sep=";\n")

print( "\n", array2 + 10) # +, -, *, /, %...
print(array2[0:2])

print(""); line(42)
calc1 = ( array2 / array1 ) #Broadcasting, it's selective calculation, can be done only with equal sized arrays
print(array2, calc1, sep=";\n") #This calc returns to the expoent used in 35


#more operations
tspac(); line(47)
print(np.sqrt( np.array([4, 9, 144]) ))

print("")
dotProduct = np.dot( array1, np.array([3, 5, 10, 20]) ) #sum of the multiplication of every element by index
alsoDotProduct = array1 @ array2
print(dotProduct)
print(alsoDotProduct)


#Bidimensional
tspac(); line(61)
array3 = np.array( [[1, 2, 3], 
                    [2, 10, 25]] ) #i and j accordingly. accepts a list containing lists
                   
print(array3[1, 0])#second row, first column
print(array3.shape)

print("\nSlicing:")
print(array3[0:, 1:])#requires all the dimensions

print("\nInverting:\n", np.flip(array3[0:, 1:]))

tspac(); line(73)
#Size Operations:
array4 = np.array( [[10, 103, 59, 88, 23],
                   [5, 30, {"a": 59}, 22, 500]] )

#vertical (2° array, row)
array5 = np.vstack((array4, [1, 14, 9, 16, 25]))
#horizontal (append to array)
array6 = np.hstack((array5, [[55], [34], [64]] )) #Adding values to each array.
#ALL THE ARRAYS NEED TO HAVE A UNIFORM SHAPE (think like a rectangle, it needs to be uniform and scrict about every column and row be filled equally)

print("Adding vertically: \n", array5)
print("Adding horizontally: \n", array6)
print(array6.shape)

print(""); line(89)
print("Changing shape order of column/row as 9,2:\n", array6.reshape(9, 2))
print("Reducing to one single row:\n", array6.flatten())
array3 = array3.flatten()
print("Rearranging every element for a row:\n", array3[:, np.newaxis])

print(""); line(91)
#Boolean Reshaping: reshapes according to a set rule
#comparators and logic operations will be performed in every item and returned as true/false
def evenArray(arr):
    return ( (arr % 2) == 0 ) #can be done in any sentence.

print(evenArray(array3))
#this then can be used to filter the array by the rule
print(array3[evenArray(array3)])
print(array3[array3 % 2 == 0]) #placed in sentence

print(""); line(102)
#Where clause: uses a condition to remap the array
array3 = array3.reshape(2,3)
print(np.where(array3 >= 3, array3, None)) #Condition, Array to compare, Value to be assigned if condition is not met.

tspac(); line(111)
#Broadcasting
initialArray = np.hstack((np.where(arrayRange_10 < 0, arrayRange_10, 10), [10] * 10)).reshape(3,5)
reshapedArray = arrayRange_10
#shapes need to be compatible.

resultedSumArray = initialArray + reshapedArray #every single value + every single in compatible shape. If theres more elements, it'll add to them again if compatible
print("Broadcasting sum to all of the elements:\n", resultedSumArray)