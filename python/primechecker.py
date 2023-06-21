def prime(limiter):#not finished 
    i = 1
    result = list()
    while i <= int(limiter):
        if i == 0 or 1:
            result.append([i, "not prime"])
        elif i == 2 or 3: 
            result.append([i, "is prime"])
        elif i/i != 1 and i%1 == 0: 
            result.append([i, "not prime"])
        else:
            result.append([i, "is prime"])
        i+= 1
    for x in result:  
        print(x)
     
            
prime(10)