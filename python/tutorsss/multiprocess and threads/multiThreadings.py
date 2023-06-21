from threading import Thread
import time
total_threads = []
numfor_threads = 4

def calculo():
    for i in range(20):
        if i%3 == 0:
            print(i * i)
    print("")


for i in range(numfor_threads):
    t = Thread(target=calculo)
    total_threads.append(t)

for t in total_threads:
    t.start()
    time.sleep(0.3) #more control in bugs

for t in total_threads:
    t.join() 

    #terrible for debugging.
    #is this bugging gil????????????????? dude

#sharing data between them
