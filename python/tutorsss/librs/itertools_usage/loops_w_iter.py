from fcts8 import tspac, line, endCode
from itertools import count, cycle, repeat
tspac(); line(51)
print("loops:")
for i in count(3, step=1.5):  # starts at arg
    print("to", i)
    if i == 6:
        print("finished counting")
        break;

exampleArray = ["one", "two", "three", "four", "five"]
print("")
for i in cycle(exampleArray):
    print(i)
    if i == "five":
        print("finished cycling")  # else it will go to infinity
        break;

print("")
for i in repeat(exampleArray, times=3):  # repeat given value, second arg stops it
    print(len(i))
print('finished repeating')

endCode()
