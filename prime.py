import random
import math
import xgcd as xgcd

def GetPrime(min, max):
    primes = [i for i in range(min, max) if isPrime(i)]
    return random.choice(primes)

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def isCoPrime(a, b):
    if(xgcd.egcd(a, b)[0] == 1):
        return True
    else:
        return False

