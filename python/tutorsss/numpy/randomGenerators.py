from fcts5 import tspac, line, endCode
import numpy as np

tspac(); line(5)
#*Random Numbers generators
randomRawArray = np.random.random((4,4)) #in selected shape, from 0 to 1 random generator
print("Raw Random array:\n", randomRawArray)

randomRadn = np.random.randn(2,2) #generator do normal/Gaussian numbers
print("Gaussian Random array:\n", randomRadn)

randomIntArray = np.random.randint(1, 50, size=(3,24) ) #range of integers, and specified size
print("Integer random generated array:\n", randomIntArray)

randomChoice = np.random.choice(["Átila", "Gabu", "Marx"], size=1) #pick a value from a list
#can also be used to pick from ranges of numbers.
print("random pick:\n", randomChoice[0])

#TODO: search more