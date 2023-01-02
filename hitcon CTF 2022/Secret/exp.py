from sage.all import *

with open('output.txt') as f:
    es = eval(f.readline().strip())
    cs = eval(f.readline().strip())

""" L = matrix(es).T.augment(matrix([1]*len(es)).T)
L = L.augment(matrix.identity(len(es)))
L[:, 0] *= 2**1024
L[:, 1] *= 2**1024
L = L.LLL()

assert sum([a*e for a, e in zip(L[0][2:], es)]) == 0
assert sum([b*e for b, e in zip(L[1][2:], es)]) == 0
assert sum(L[0]) == 0
assert sum(L[1]) == 0

def get_kn(an):
    prod_p = 1
    prod_n = 1
    for i, a in enumerate(an):
        if a < 0:
            prod_n *= cs[i]**(-a)
        else:
            prod_p *= cs[i]**(a)
    return prod_p - prod_n


n1 = get_kn(L[0][2:])
n2 = get_kn(L[1][2:])

n = gcd(n1, n2)

for i in range(2, 300):
    while n % i == 0:
        n //= i 

print(n) """

n = 17724789252315807248927730667204930958297858773674832260928199237060866435185638955096592748220649030149566091217826522043129307162493793671996812004000118081710563332939308211259089195461643467445875873771237895923913260591027067630542357457387530104697423520079182068902045528622287770023563712446893601808377717276767453135950949329740598173138072819431625017048326434046147044619183254356138909174424066275565264916713884294982101291708384255124605118760943142140108951391604922691454403740373626767491041574402086547023530218679378259419245611411249759537391050751834703499864363713578006540759995141466969230839

delta_e1 = es[1] - es[0]
for i in range(64):
    delta_e2 = es[i] - es[1]
    if delta_e2 > 0 and gcd(delta_e2, delta_e1) == 1:
        break
c1 = (cs[1] * inverse_mod(cs[0], n)) % n
c2 = (cs[i] * inverse_mod(cs[1], n)) % n

def attack(c1, c2, e1, e2):
    g, a, b = xgcd(e1, e2)
    if g != 1:
        return
    return power_mod(c1, a, n) * power_mod(c2, b, n) % n

m = attack(c1, c2, delta_e1, delta_e2)
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(m))