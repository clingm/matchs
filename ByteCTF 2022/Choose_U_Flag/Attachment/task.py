import ast
import random
import signal
import string
import os

import numpy as np
from sympy import ZZ, Poly
from sympy.abc import x

from ntru import NTRUCipher


def exitHandler(signum, frame):
    print("timeout")
    exit()


signal.signal(signal.SIGALRM, exitHandler)
signal.alarm(30)

flag = os.environ.get("CTF_CHALLENGE_FLAG")

N = 107
p = 3
q = 64

cipher = NTRUCipher(N, p, q)
cipher.generate()
print(f"[+]h_poly: {cipher.h_poly.all_coeffs()}")

random_key = ''.join(random.sample(string.printable, 12))
key_arr = np.unpackbits(np.frombuffer(random_key.encode(), dtype=np.uint8))
key_enc = cipher.encrypt(Poly(key_arr, x).set_domain(ZZ))
key_coeffs = key_enc.all_coeffs()
print(f"[+]key coeffs: {key_coeffs}")

dec_data = input("decrypt data > ")
dec_arr = ast.literal_eval(dec_data)
if dec_arr == key_coeffs:
    exit(-1)
dec = cipher.decrypt(Poly(dec_arr, x).set_domain(ZZ))
dec_coeffs = dec.all_coeffs()
print(f"[+]decrypt coeffs: {dec_coeffs}")

while N > 0:
    try:
        u_key = input("u key > ")
        if u_key == random_key:
            print(flag)
            exit(-1)
        else:
            print("key err")
    except:
        print("input err")
    N = N - 1
