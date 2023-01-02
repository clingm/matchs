from Crypto.Util.number import *

class super_ecc:
    def __init__(self):
        self.a = 73101304688827564515346974949973801514688319206271902046500036921488731301311
        self.c = 78293161515104296317366169782119919020288033620228629011270781387408756505563
        self.d = 37207943854782934242920295594440274620695938273948375125575487686242348905415
        self.p = 101194790049284589034264952247851014979689350430642214419992564316981817280629

    def add(self, P, Q):
        (x1, y1) = P
        (x2, y2) = Q
        x3 = (x1 * y2 + y1 * x2) * inverse(self.c * (1 + self.d * x1 * x2 * y1 * y2), self.p) % self.p
        y3 = (y1 * y2 - self.a * x1 * x2) * inverse(self.c * (1 - self.d * x1 * x2 * y1 * y2), self.p) % self.p
        return (x3, y3)

    def mul(self, x, P):
        Q = INF
        x = x % self.p
        while x > 0:
            if x % 2 == 1:
                Q = self.add(Q, P)
            P = self.add(P, P)
            x = x >> 1
        return Q