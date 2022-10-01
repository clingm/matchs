import time
import os
import random

def encrypt_stage_one(message, key):
    u = [s for s in sorted(zip(key, range(len(key))))]
    res = ''

    for i in u:
        for j in range(i[1], len(message), len(key)):
            res += message[j]

    return res


def decrypt_stage_two(message, now):
    random.seed(now)
    key = [random.randrange(256) for _ in range(len(message)-18)]
    
    return [m ^ k for (m,k) in zip(message + now, key + [0x42]*len(now))]

def decrypt_stage_one(cipher, key):
    res = [[] for _ in range(8)]

    for i in range(len(cipher)):
        for j in range(8):
            res[key[j]].append(cipher[i])
    
    return ''.join([res[i] for i in range(8)])



with open("./flag.enc", 'rb') as f:
    enc = f.read()

now =  bytes([i ^ 0x42 for i in enc])[-18:]
print(now)
stage2 = bytes(decrypt_stage_two(enc, now))[:-18].decode()
print(stage2)
