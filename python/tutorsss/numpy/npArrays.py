from fcts5 import tspac, line, endCode
import numpy as np #convention

#list: default python multivalored structure
#array: default for numpy, much faster because is written in C

#arrays can be multidimensional, from 1 to *


array1 = np.array([1, 3, 5, 10])
arrayRange_10 = np.arange(0, 10, 2) #mounts the array in a range, and can take steps (third Arg)

line(13)
#*Properties----
print(array1.size) #length of array
print(array1.ndim) #number of dimensions in array

print(array1.shape) #length of each dimension of array

print(array1.dtype) #prevalent type of data
print(array1.itemsize) #size in bytes of prevalent type of data


#*Operations----
tspac(); line(23)
list1 = array1.tolist() #a copy, for example.
print(list1) 

def smallLogic(npArr):
    print("\nsmall logic for array...")
    list1[0] = False
    if npArr[0] == 1:
        print("array is unchanged.")
        
smallLogic(array1)


print(""); line(38)
array2 = array1 * 2 #any kind of operation with unique values will be mapped in the array
list1 = list1 * 2 #default: python will operate in the list structure itself
print(array2, list1, sep=";\n")

print( "\n", array2 + 10) # +, -, *, /, %...
print(array2[0:2])

print(""); line(46)
calc1 = ( array2 / array1 ) #Broadcasting, it's selective calculation, can be done only with equal sized arrays
print(array2, calc1, sep=";\n") #This calc returns to the expoent used in 35


#*more operations
tspac(); line(51)
print(np.sqrt( np.array([4, 9, 144]) ))

print("")
dotProduct = np.dot( array1, np.array([3, 5, 10, 20]) ) #sum of the multiplication of every element by index
alsoDotProduct = array1 @ array2
print(dotProduct)
print(alsoDotProduct)

#comparing equality
print("it is", np.allclose(array1, array2 / 2), "that array1 and array2 are equal.")

#*Bidimensional
tspac(); line(63)
array3 = np.array( [[1, 2, 3], 
                    [2, 10, 25]] ) #i and j accordingly. accepts a list containing lists
                   
print(array3[1, 0])#second row, first column
print(array3.shape)

print("\nSlicing:")
print(array3[0:, 1:])#requires all the dimensions

print("\nInverting:\n", np.flip(array3[0:, 1:]))

#*Matrix operations:
transposedArray = array3.T #or .transpose()
invertedArray = np.linalg.inv(array3) # ^-1

tspac(); line(75)
#*Size Operations:
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

print(""); line(90)
print("Changing shape order of column/row as 9,2:\n", array6.reshape(9, 2))
print("Reducing to one single row:\n", array6.flatten())
array3 = array3.flatten()
print("Rearranging every element for a row:\n", array3[:, np.newaxis])

print(""); line(96)
#*Boolean Reshaping: reshapes according to a set rule
#comparators and logic operations will be performed in every item and returned as true/false
def evenArray(arr):
    return ( (arr % 2) == 0 ) #can be done in any sentence.

print(evenArray(array3))
#this then can be used to filter the array by the rule
print(array3[evenArray(array3)])
print(array3[array3 % 2 == 0]) #placed in sentence

print(""); line(107)
#*Where clause: uses a condition to remap the array
array3 = array3.reshape(2,3)
print(np.where(array3 >= 3, array3, None)) #Condition, Array to compare, Value to be assigned if condition is not met.

tspac(); line(112)
#*Functions and Axis: products and calculations built-in
print("Sum of the resulted array:\n", array3.sum()) #of all the elements
print("Sum of the array in the vertical way:\n", array3.sum(axis=0)) #of all the from top to bottom in the columns imaginary grid
print("Sum of the array in the horizontal way:\n", array3.sum(axis=1)) #of all the from left to right in the rows imaginary grid

print("Mean of the resulted array:\n", array3.mean()) #of all the elements
print("Mean of the array in the vertical way:\n", array3.mean(axis=0)) #for each column
print("Mean of the array in the horizontal way:\n", array3.mean(axis=1)) #for each row

print("Standard Deviation of the resulted array:\n", round( array3.std() , 2 )) #of all the elements, also able to use Axis.
#Can also be used as the proper numpy method: np.std(array, axis[optional])

print("Smaller and Greater element: ", array3.max(), array3.min())
#TODO: search for more methods and effects on these functions

tspac(); line(128)
#*Data types
alwaysInt = np.array([3.0001, 25.0], dtype = np.int16)
alwaysFloat = np.array([2, 1001], dtype = np.float32)

print("Data types of the arrays specified:")
print(alwaysInt.dtype)
print(alwaysFloat.dtype)

print(""); line(137)
#*Copying
array7 = np.array([True, False, True])
array8 = np.array(array7.copy()) #New reference created, won't be modified by the other.
print(array7, "Is a new array")

#*Generating arrays: new arrays from produced data
zerosArray = np.zeros((5, 5)) #only 0s in the selected grid 
onesArray = np.ones((5,5)) #only 1s
selectedNumberArray = np.full((2,4), 100) #creates with the shape, with the desired value
fillLikeOtherArray = np.full_like(selectedNumberArray, 5500) #creates with shape of another, selecting a value to fill
emptyArray = np.empty((10, 10), dtype = np.float16) #produced with shape, only declared, not initialized

diagonalFilledArray = np.eye(5) #fills the Matrix Diagonal with 1s in the selected shape (here 5x5)
#also the np.arange() generates an array from range()
linspaceArray = np.linspace(0, 100, 11)[1:11] #fills with equally spaced numbers, with start and stop values and the number of elements you want
line(152); print("Equally spaced from 10 to 100:\n", linspaceArray)

#? See more in other files!