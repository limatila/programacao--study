from collections import deque
import time
#'with open()' always
#.read(amount of indexes), .readline, .readlines, 
#modes of open(): r, w, a, r+; adding b

#quickly writing to other file
with open('fileinput.txt', 'r') as rfile:
    with open('output2.txt', 'w') as wf:
        for line in rfile:
            wf.write(line)  
        wf.write('\nnew line here ;)')


#pick some data, modify with list, write later in other file
time.sleep(1)
with open('output2.txt', 'r', encoding= 'utf-8') as f1:
    x = deque(f1.read().splitlines()) #split into list
    x.appendleft('this is a random file')
    print(x)

a = "\n".join(x)    

with open('output3.txt', 'w') as f2:
    f2.write(a)

