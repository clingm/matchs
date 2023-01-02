# BabySSS

Shamir's Secret Sharing but without modulus. So can recover the poly from only one shared massage.

But x is 16 bit , and $a_n$ is 64 bit, so need use CRT to recover the correct $a_n$

here is my exp:

```python
from sage.all import *
from sage.all_cmdline import *
from Crypto.Cipher import AES
from hashlib import sha256

DEGREE = 128

with open('./output.txt', 'r') as f:
    shared = eval(f.readline().strip())
ct = b'G$\xf5\x9e\xa9\xb1e\xb5\x86w\xdfz\xbeP\xecJ\xb8wT<<\x84\xc5v\xb4\x02Z\xa4\xed\x8fB\x00[\xc0\x02\xf9\xc0x\x16\xf9\xa4\x02\xb8\xbb'
nonce = b'\x8f\xa5z\xb4mZ\x97\xe9'

x_list = [i[0] for i in shared]
y_list = [i[1] for i in shared]

poly = []

def polyeval(poly, x):
    return sum([a * x**i for i, a in enumerate(poly)])

def recover_poly(i):
    an = []
    mn = []
    for n in range(8):
        an.append(((y_list[n] % x_list[n]**(i+1)) - (polyeval(poly, x_list[n])) % x_list[n]**(i+1)) // x_list[n]**i)
        mn.append(x_list[n])
    return CRT_list(an, mn)

for i in range(DEGREE+1):
    poly.append(recover_poly(i))

for i in range(8):
    assert polyeval(poly, x_list[i]) == y_list[i]

secret = polyeval(poly, 0x48763)
key = sha256(str(secret).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
print(cipher.decrypt(ct))

```