from fcts5 import tspac, line, endCode
import numpy as np

matrix1 = np.array([[1, 2],
                    [1, 4]])

#*Linear Algebra module: useful functions
#Transpose
transposedMatrix = np.linalg.matrix_transpose(matrix1) #se a more faster option in npArrays:

#Inverse
invertedMatrix = np.linalg.inv(matrix1)

#Eigen Values: e_vec * e_val = matrixA * e_vec 
eigenValues, eigenVectors = np.linalg.eig(matrix1) #must be symmetric/squared matrix.
# 'np.linalg.eigvals' for non simetric

#TODO: learn more commands to work with

#*Solving linear systems
A = np.array([ [1, 1],
               [1.5, 4.0] ])
b = np.array([1920, 3102])

#linear equation principle: Ax = b <=> x = A^-1 * b
# '<=>' as equivalent 

#Manually
result1 = np.linalg.inv(A).dot(b)
print("Solution 1:\n", result1)

#.solve, simple and faster
result1 = np.linalg.solve(A, b)
print("Solution 2:\n", result1)