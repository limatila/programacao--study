from fcts import endCode
i = -1

out = ""
def checkeven(limiter):
    global i
    global out
    while i < limiter:
        i+= 1
        if i%2 == 0:
            out+= str(i) + " is even\n"
        else:
            out+= str(i) + " is odd\n"
    i = -1
    print(out) 

checkeven(13) #even/odd till 0-13
with open('fileoutp.txt', 'w') as f:
    f.write(out)
endCode()