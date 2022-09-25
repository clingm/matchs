from Crypto.Util.number import getPrime, getRandomNBitInteger, inverse
from fractions import Fraction
from gmpy2 import lcm
import re

N = 512
safe_expr = re.compile(r'^([-+*/0-9.~%^&()=|<>]|and|or|not|MSG)+$')


def encode(m, n, g):
    r = getRandomNBitInteger(N)
    c = pow(g, m, n*n) * pow(r, n, n*n) % (n*n)
    return c


def decode(c, n, l, u):
    return int(Fraction(pow(c, l, n * n) - 1, n) * u % n)


def round(expr):
    p = getPrime(N)
    q = getPrime(N)

    n = p * q
    g = getRandomNBitInteger(N)
    print('n =', n)
    print('g =', g)

    a = getRandomNBitInteger(N)
    b = getRandomNBitInteger(N)

    print('a =', encode(a, n, g))
    print('b =', encode(b, n, g))

    msg = int(input("msg = "))

    l = int(lcm(p - 1, q - 1))
    u = inverse(Fraction(pow(g, l, n * n) - 1, n), n)

    return (a > b) is bool(eval(expr, None, {'MSG': decode(msg, n, l, u)}))


def main():
    expr = input('Hello, Give me your expr: ')
    expr = re.sub(r'\s', '', expr)

    if safe_expr.match(expr) is None:
        raise Exception('Hacker?')

    for i in range(100):
        print('Round:', i)
        try:
            assert round(expr)
        except:
            print('You lost.')
            break
    else:
        print('Congratulations!')
        print(open('/flag').read())


if __name__ == '__main__':
    main()