from pwn import *

sh = remote('137.184.215.151', 22666)

sh.interactive()