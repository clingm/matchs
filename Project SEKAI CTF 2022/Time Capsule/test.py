import os

mes = "flag{this is test flag}"

def decrypt_stage_one(cipher, key):
    res = ["" for _ in range(8)]
    for i in range(len(cipher)):
        res[key[i % 8]] += cipher[i]
    
    return ''.join([res[i] for i in range(8)])

def encrypt_stage_one(message, key):
    u = [s for s in sorted(zip(key, range(len(key))))]
    res = ''

    for i in u:
        for j in range(i[1], len(message), len(key)):
            res += message[j]

    return res

rand_nums = []
while len(rand_nums) != 8:
    tmp = int.from_bytes(os.urandom(1), "big")
    if tmp not in rand_nums:
        rand_nums.append(tmp)
key = [s[1] for s in sorted(zip(rand_nums, range(len(rand_nums))))]
print(key)
c = encrypt_stage_one(mes, rand_nums)
m= decrypt_stage_one(c, key)
print(c)
print(m)
