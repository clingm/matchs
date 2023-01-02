from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from random import randint, choices
from string import ascii_uppercase, digits
from sage.all import *

p = getPrime(160)
d = 90
while True:
    key = "rctf_" + "".join(choices(ascii_uppercase + digits, k=15))
    x = bytes_to_long("".join(sorted(key)).encode())
    if x < p:
        break
l = 2
T = []
U = []
for i in range(d):
    t = randint(1, p)
    u = x * t - randint(1, p >> l)
    T.append(t)
    U.append(u)

answers = [-u for u in U]
inputs = T
print(x)

def build_basis(t_i, a_i):
    """Returns a basis using the HNP game parameters and inputs to our oracle
    """
    basis_vectors = []
    for i in range(d):
        p_vector = [0] * (d+2)
        p_vector[i] = p * p
        basis_vectors.append(p_vector)
    T = list(map(lambda x: x*p, t_i))
    A = list(map(lambda x: x*p, a_i))
    basis_vectors.append(T + [ZZ(p>>l)] + [0])
    basis_vectors.append(A + [0] + [ZZ(p >> l)*p])
    return Matrix(ZZ, basis_vectors)
# def build_basis(t_i, a_i):
#     """Returns a basis using the HNP game parameters and inputs to our oracle
#     """
#     basis_vectors = []
#     for i in range(d):
#         p_vector = [0] * (d+2)
#         p_vector[i] = p
#         basis_vectors.append(p_vector)
#     basis_vectors.append(list(t_i) + [QQ(p >> l)/QQ(p)] + [0])
#     basis_vectors.append(list(a_i) + [0] + [QQ(p >> l)])
#     return Matrix(QQ, basis_vectors)

lattice = build_basis(inputs, answers)
# print("Solving SVP using lattice with basis:\n%s\n" % str(lattice))
L = lattice.BKZ()
print(L[0])
ks = L[1]

if (-answers[0] + ZZ(ks[0])) % p == (inputs[0] * x) % p:
    # print(f"Recovered nonce! {ks}")
    recovered_x = ( (-answers[0] + ZZ(ks[0])) * inverse_mod(inputs[0], p) ) % p
    assert recovered_x == x
    print("Recovered private key! private key is %d" % recovered_x)
else:
    print("faild to recover!")

# inputs = [[u] for u in U]
# gen = attack(inputs, answers, p, p>>2)
# s = list(gen)
# for xi in s[0][0]:
#     if xi == x:
#         print(xi)
#         break


def build_basis(oracle_inputs):
    """Returns a basis using the HNP game parameters and inputs to our oracle
    """
    basis_vectors = []
    for i in range(d):
        p_vector = [0] * (d+1)
        p_vector[i] = p*p
        basis_vectors.append(p_vector)
    T = list(map(lambda x: x*p, oracle_inputs))
    basis_vectors.append(T + [ZZ(1)])
    return Matrix(ZZ, basis_vectors)

def approximate_closest_vector(basis, v):
    """Returns an approximate CVP solution using Babai's nearest plane algorithm.
    """
    BL = basis.LLL()
    G, _ = BL.gram_schmidt()
    _, n = BL.dimensions()
    small = vector(ZZ, v)
    for i in reversed(range(n)):
        c = QQ(small * G[i]) / QQ(G[i] * G[i])
        c = c.round()
        small -= BL[i] * c
    return (v - small).coefficients()


lattice = build_basis(T)
u = vector(ZZ, list(U) + [0])
v = approximate_closest_vector(lattice, u)

recovered_alpha = (v[-1] * p) % p
print(recovered_alpha)