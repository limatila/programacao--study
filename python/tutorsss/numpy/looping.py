from fcts5 import tspac, line, endCode
import numpy as np

line(5)
#* Looping as normal 1D array
array1: np.ndarray = np.array( [1, 2, 3, 5, 8, 13] )

for number in array1:
    print(number)

print("finished loop.")

tspac(); line(14)
#* Looping on 2D
array1: np.ndarray = np.array( [ [1, 2, 3],
                                 [4, 5, 6] ] )

for row in array1:
    for number in row:
        print(number)


#TODO: for 3D?