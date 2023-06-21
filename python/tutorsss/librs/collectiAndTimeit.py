from fcts0 import tspac, endCode, line
#import pandas as pd #coment for better time
from collections import Counter, namedtuple, OrderedDict, deque, defaultdict
import time
from timeit import default_timer as timer

strin = "aaaabbbbccwopq"
counter = Counter(strin)#counts, creates dict
line(7)
print(f"var strin: {strin}")
print(counter.most_common(1)[0][0])
print(counter.keys())#every char
print(counter.values())#counting

"""
tspac()
line(16) #experiment with pandas
times = list(counter.values())
dataf = {
    'letters': None,
    'times': times
}
dataf['letters'] = list(counter.keys())

tabela = pd.DataFrame(dataf)
print(tabela)
"""

tspac()
line(29)
graphPoint = namedtuple('Point', 'x, y, name')#easy create Class and Args
point = graphPoint(20, 2, "atila")#call atributted var, not Class name
"""if point.x or point.y != int:
    raise ValueError"""
print(point)

tspac()
line(36)#ignorable after p3.7
ordDict = OrderedDict()
#create simple dict that remember values per line added

print(""); line(37); myl= deque()
myl.append(1)
myl.append(5)
myl.append(7)
myl.append(3)
myl.rotate(2)#rotate inside itself, by the arg
myl.appendleft(True)#add to the left of list
print(myl)
myl[0] = None; print(myl[0]); print("deque is now", myl)

tspac(); line(55)
myd = defaultdict(int)
myd['a'] = 1
myd['b']= 2
print(myd)
print(myd[0])
print(myd)

endCode()