from Crypto.Util.number import getPrime, bytes_to_long, long2str
from random import randint, choices
from string import ascii_uppercase, digits

q = getPrime(160)
while True:
    key = "rctf_" + "".join(choices(ascii_uppercase + digits, k=15))
    x = bytes_to_long("".join(sorted(key)).encode())
    if x < q:
        break
l = 2
T = []
U = []
for i in range(90):
    t = randint(1, q)
    u = x * t - randint(1, q >> l)
    T.append(t)
    U.append(u)

u = 28806433277886440373682012291070551778270877465555764166805321657370037926640631630814849746940
t = 100521670049861880888869494619548416828134082045

print(long2str(u // t))
key = long2str(u // t)[:-1] + b't'
print(bytes_to_long(key))