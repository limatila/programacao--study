from fcts5 import tspac, line, endCode
import numpy as np 

arrayRange_10 = np.arange(0, 10, 2)

#Broadcasting in Numpy:
#TODO: elaborate and deconstruct
initialArray = np.hstack((np.where(arrayRange_10 < 0, arrayRange_10, 10), [10] * 10)).reshape(3,5)
reshapedArray = arrayRange_10
#shapes need to be compatible.

resultedSumArray = initialArray + reshapedArray #every single value + every single in compatible shape. If theres more elements, it'll add to them again if compatible
print("Broadcasting sum to all of the elements:\n", resultedSumArray)