#Extra: from typing import Generator

primes: set[int] = {1, 2, }

def checkDivisibleByPrime(entry) -> bool:
    #primes = numbers not divisible by the primes set.
    #so check if entry % is not 0 for finding primes 
    # ?or decimals?


    #all divisible must be discarted, all primes must be added to primes set.


def primeListing(limiter) -> list:  #* a function that returns prime numbers until a max explicited 'limiter'
    int(limiter)
    #1. start a loop in 2 to infinity
    #2. check if number is prime
    #2.1 {1, 2, ...} are primes
    #2.2 if True, all divisibles of primes must be excluded in further iterations
    #3. continue till the 'limiter'


if __name__ == "__main__":
    print(primeListing(10))
