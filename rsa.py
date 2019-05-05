import prime as prime
import xgcd as xgcd
import random


min_prime = 100000
max_prime = 1000000

p = prime.GetPrime(min_prime, max_prime)
q = prime.GetPrime(min_prime, max_prime)
N = p * q
Totien = (p - 1) * (q - 1)

while True:
    e = random.randrange(1, Totien)
    if prime.isCoPrime(e, Totien):
        break

d  = xgcd.modinv(e, Totien)

print("RSA key genrator")
print("p:\t" + str(p))
print("q:\t" + str(q))
print("N:\t" + str(N))
print("Totien:\t" + str(Totien))
print("\nPrivate key:\t(" + str(d) + ", " + str(N) + ")")
print("Public key:\t(" + str(e) + ", " + str(N) + ")")
