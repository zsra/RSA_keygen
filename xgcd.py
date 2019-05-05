def GCD(x, y):  
   while(y): 
       x, y = y, x % y 
  
   return x 

def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, m)
    if g == 1:
        return x % m