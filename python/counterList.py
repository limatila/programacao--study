from itertools import count
import pyautogui as pag
import time

time.sleep(3)
myCount = []
for i in count(0): 
    #can do anything here
    myCount.append(i) #code to count the iterations
    if myCount[-1] == 10: break
    time.sleep(0.3)
print(myCount)

