import gmpy2
import numpy as np
from sympy import GF, ZZ, Poly, invert
from sympy.abc import x


def is_2_power(n):
    return n != 0 and (n & (n - 1) == 0)


class NTRUCipher:
    N = None
    p = None
    q = None
    f_poly = None
    g_poly = None
    h_poly = None
    f_p_poly = None
    f_q_poly = None
    R_poly = None

    def __init__(self, N, p, q) -> None:
        self.N = N
        self.p = p
        self.q = q
        self.R_poly = Poly(x ** N - 1, x).set_domain(ZZ)

    def random_poly(self, length, d, neg_ones_diff=0):
        return Poly(np.random.permutation(np.concatenate((np.zeros(length - 2 * d - neg_ones_diff), np.ones(d), -1 * np.ones(d + neg_ones_diff)))), x).set_domain(ZZ)

    def invert_poly(self, f_poly, R_poly, p):
        if gmpy2.is_prime(p):
            inv_poly = invert(f_poly, R_poly, domain=GF(p))
        elif is_2_power(p):
            inv_poly = invert(f_poly, R_poly, domain=GF(2))
            e = int(gmpy2.log2(p))
            for i in range(1, e):
                inv_poly = ((2 * inv_poly - f_poly * inv_poly ** 2) %
                            R_poly).trunc(p)
        else:
            raise Exception("Cannot invert polynomial in Z_{}".format(p))
        return inv_poly

    def generate(self):
        self.g_poly = self.random_poly(self.N, int(gmpy2.sqrt(self.q)))
        while (self.h_poly is None):
            self.f_poly = self.random_poly(
                self.N, self.N // 3, neg_ones_diff=-1)
            self.f_p_poly = self.invert_poly(self.f_poly, self.R_poly, self.p)
            self.f_q_poly = self.invert_poly(self.f_poly, self.R_poly, self.q)
            p_f_q_poly = (self.p * self.f_q_poly).trunc(self.q)
            h_before_mod = (p_f_q_poly * self.g_poly).trunc(self.q)
            self.h_poly = (h_before_mod % self.R_poly).trunc(self.q)

    def encrypt(self, plain_poly):
        rand_poly = self.random_poly(self.N, int(gmpy2.sqrt(self.q)))
        return (((rand_poly * self.h_poly).trunc(self.q) + plain_poly) % self.R_poly).trunc(self.q)

    def decrypt(self, cipher_poly):
        a_poly = ((self.f_poly * cipher_poly) % self.R_poly).trunc(self.q)
        b_poly = a_poly.trunc(self.p)
        return ((self.f_p_poly * b_poly) % self.R_poly).trunc(self.p)
