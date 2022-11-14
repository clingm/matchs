from Crypto.Util.number import *
import random, os
from secret import flag

x = bytes_to_long(flag + os.urandom(128 - len(flag)))

for i in range(4):
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    a = random.randint(0,n-1)
    b = random.randint(0,n-1)
    Ep = EllipticCurve(GF(p),[a,b])
    Eq = EllipticCurve(GF(q),[a,b])
    while True:
        try:
            Gp = Ep.lift_x(x)
            Gq = Eq.lift_x(x)
            y = crt([int(Gp[1]),int(Gq[1])],[p,q])
            break
        except:
            x += 1
    print(n,a,b,y)
    
