from pwn import *
from hashlib import sha256
# Quick hack
import sys
sys.path.append('./source')
# Import symbolic execution
from MT19937 import MT19937, MT19937_symbolic

#context.log_level = "debug"


def sendandrecv(send_n):
    sh.recvuntil(b'Your guess > ')
    sh.sendline(cards[send_n].encode())
    t = sh.recv(1).decode()
    ret_n = 0
    if t == 'C':
        ret_n = send_n
    elif t == 'S':
        sh.recvuntil(b'My card is ')
        card = sh.recvuntil(b'.').decode()[:-1]
        ret_n = cards.index(card)
    return ret_n


cards = []
for t in ('Hearts', 'Spades', 'Diamonds', 'Clubs'):
    for p in ('J', 'Q', 'K', 'A'):
        cards.append(f'{p} {t}')

sh = process(['./wscat', '--endpoint', 'wss://telnet.2022.capturetheflag.fun/ws/' + 'd81cc24e77ba5ad460cc552a5fab4ac2'])
_ = sh.recvuntil(b"sha256(XXXX+")
suffix = sh.recv(28).decode()
_ = sh.recvuntil(b") == ")
target = sh.recv(64).decode()
proof = iters.mbruteforce(lambda x: sha256((x + suffix).encode()).hexdigest() == target, string.printable, length=4,
                          method='fixed')
sh.sendlineafter(b'Give me XXXX >', proof)
print("running......")
nbits = 4
eqns = []
n_test = []
for round in range(624*32//nbits):
    print(f"r : {round}")
    n = sendandrecv(1)
    n_test.append(n)
print("got needed bit massage!")
t = time.time()

rng_clone = MT19937(state_from_data = (n_test, nbits))

print("Time taken: {}s".format(time.time() - t))

# Test if cloning has been successful
for n in n_test:
    assert n == rng_clone() >> (32-nbits), "Clone failed!"
    
print("[*] Cloning successful!")

while 1:
    sendandrecv(rng_clone() >> (32-nbits))

sh.interactive()