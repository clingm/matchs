from tqdm import tqdm
import hashlib

rng = 51492133
low = rng&(2 ** 16 - 1)
n = 10000000000
s = 4


def guess(seed):
    x = seed
    high = (int(hashlib.sha256(str(x).encode()).hexdigest(),16) >> 16) & (2 ** 16 - 1)
    low = x & (2 ** 16 - 1)
    result = high << 16 | low
    return result

for i in tqdm(range(0xffff+1)):
    x = i << 16 | low
    if (int(hashlib.sha256(str(x).encode()).hexdigest(),16) >> 16) & (2 ** 16 - 1) == rng >> 16:
        print("Found!", x)
        break
