from pwn import *
from pwnlib.util.iters import mbruteforce
import string
import hashlib

context.log_level = 'debug'

table = string.printable

hashes = [
    'd.0.....f5...5.6.7.1.30.6c.d9..0',
    '1b.8.1.c........09.30.....64aa9.',
    'c.d.1.53..66.4.43bd.......59...8',
    '.d.d.076........eae.3.6.85.a2...']

print(hashlib.md5('cvctf'.encode()).hexdigest())

guess = mbruteforce(lambda x: hashlib.md5(x.encode()).hexdigest()[-6:-1] == '64aa9' and hashlib.md5(x.encode()).hexdigest()[:2] == '1b', table, length=5)
print(guess)
