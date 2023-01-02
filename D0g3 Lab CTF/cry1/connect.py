#!/usr/bin/env python
# coding=utf-8
from hashlib import sha256
from pwn import remote
from pwnlib.util.iters import mbruteforce
import string

alphabet = string.ascii_letters + string.digits
sh = remote('120.78.131.38', 10001)
question = sh.recvline().decode("utf-8")
prefix = question[14:30]
target = question[32:-1]
proof = mbruteforce(lambda x: sha256((x + prefix).encode()).hexdigest() == target,
                    alphabet,
                    8,
                    method='upto')
sh.sendline(proof.encode())
sh.interactive()