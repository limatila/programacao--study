from fcts5 import tspac, line, endCode
import numpy as np 
from numpy import array as newArr

arrayRange_10 = np.arange(0, 10, 2)

line(7)
#* Broadcasting in Numpy: a sensible way to doing element-wise operations
numbersAdded = newArr([1, 10, 51]) + 1020
print("Broadcasted addition:\n", numbersAdded)
numbersAdded = newArr([11000, 320, 5000]) - 1020
print("Broadcasted subtraction:\n", numbersAdded)

#It is available for every math operation & is highlighted in light blue in Synthwave '84 VScode Theme.

print(""); line(16)
#* Using arrays to broadcast:
addingHorizontally = newArr([[1, 2, 3], 
                             [10, 20, 30]]) + newArr([2, 3, 10])
addingVertically = newArr([[1, 2], 
                           [3, 4]]) + newArr([[10], 
                                              [20]]) #will add based on the axis
print("Added horizontally:\n", addingHorizontally)
print("Added vertically:\n", addingVertically)

tspac(); line(28)
#shapes need to be compatible.
initialArray = np.hstack((np.where(arrayRange_10 < 0, arrayRange_10, 10), [10] * 10)).reshape(3,5)
reshapedArray = arrayRange_10
resultedSumArray = initialArray + reshapedArray #every single value + every single in compatible shape. If theres more elements, it'll add to them again if compatible
print("Broadcasting sum to all of the elements:\n", resultedSumArray)

#TODO: Search more about compatibility