import prime as prime
import xgcd as xgcd
import random

import decrypt as decrypt
import encrypt as encrypt

min_prime = 10
max_prime = 100

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

msg_raw = input("Message:\t")
print("Encrpyted Text:")
msg_encrypt = encrypt.msg(int(msg_raw), e, N)
print(str(msg_encrypt))
print("Decrpyted Text:")
msg_decrypt = decrypt.msg(msg_encrypt, d,N)
print(str(msg_decrypt))
