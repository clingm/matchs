#!/usr/bin/env python
# coding=utf-8
from hashlib import sha256
from pwn import *
from pwnlib.util.iters import mbruteforce
import string
from Crypto.Util.Padding import pad
GOD = [b'Whitfield__Diffie']

# context.log_level = 'debug'

alphabet = string.ascii_letters + string.digits
sh = remote('120.78.131.38', 10010)
question = sh.recvline().decode("utf-8")
prefix = question[14:30]
target = question[32:-1]
proof = mbruteforce(lambda x: sha256((x + prefix).encode()).hexdigest() == target,
                    alphabet,
                    8,
                    method='upto')
sh.sendline(proof.encode())


sh.recvuntil(b'palace ')
Authentication = sh.recv(32)
print(Authentication)
payload = pad(GOD[0], 16) + xor(bytes.fromhex(Authentication.decode()), GOD[0][:-1]) + b'e'
print(payload)
print(len(payload))
sh.sendafter(b'-->', payload)

sh.interactive()
