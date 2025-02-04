from fcts8 import tspac, line, endCode

from itertools import batched, zip_longest, starmap

exampleList: list[int] = [1, 2, 3, 4, 5]

#* Batching --
line(8)
batchedList: batched = batched(exampleList, n=2) #Create batches (small chunks) with 'n' size.
#visualizing, returns tuples (can be interpreted to List)
print(next(batchedList))
print(next(batchedList))

tspac(); line(13)
batchedList_Strictly: batched = batched(exampleList, n=4 ,strict=True) #Will error when used, if it cannot complete the last batch in the 'n' specified
try:    
    print(list(batchedList_Strictly))
except ValueError as err:
    print(err.args[0], 
          "\n...skipping error") #You can see the error in console.
    
#* Zip-Longest --
tspac(); line(24)
# Creates a Zip (combines iterables in consecutive multivalored tuples)
# in original Zipping, it would only be able to produce Zip when the index of every iteratable has a value
# in the itertools solution, by default it will replace indexes without value to 'None'
# so if we still need to iterate, it won't stop in the last fully working iteration (all values existent)
exampleList2: list[int] = ["one", "two", "three", "four", "five"]
zippedOriginal: zip = zip(exampleList, exampleList2, ["um"]) # will only combine in i = 0
zippedLongest: zip_longest = zip_longest(exampleList, exampleList2, ["um"]) # will only all values

print(f"first try has {len(list(zippedOriginal))} values")
print(f"second try has {len(list(zippedLongest))} values")

zippedLongest2: zip_longest = zip_longest(exampleList, exampleList2, ["um"]) #! Caution: after any use (like in the list conversion in line 33), the zip empties
print(f"combining every element of the index 3 of the lists: {list(zippedLongest2)[3]}") 
# Notice as the 3° value will be 'None', as the 3rd list only contains value on index 0.
#You can also specify the arg 'fillvalue', to change it from default None to any other you may need.

#* Starmap --
# As of example, imagine a function takes multiple args
def getSum_multivalues(*args):
    return sum(args)

#And you want to use it to run it for multiple lists/tuples
tspac(); line(42)
exampleList3 = [tuple(exampleList), (10, 20, 30, -10)] # args
sums = list( starmap(getSum_multivalues, exampleList3) ) #Starmap is a Map that can run the function in more than just one value (>= 1 list)
print(f"the first sum of all elements is: {sums[0]}, and the second is: {sums[1]}")
#You could be applying it to different chunks of data, that could need to be 'reduced', or remaped in a set of rules

endCode()