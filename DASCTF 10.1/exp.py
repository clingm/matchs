from sage.all import *
from sage.all_cmdline import *
from Crypto.Util.number import *

n = 139101934863352477680537166901007739770523630774378366180026691277439423208746121861557365671785442123546910684871568616149710608884061872209110735933668052403115934545874163445003076722267135352166992293153339410739582737805220845283317197718412383748027930162218209042796960903975172461034518440898030328381
c1 = 109169967535160806208768678599352299690002016545713034263725223821346179898091545423328527158451555206010707769519910908955601500128237278224907793229965500971841089487086030175517572037647789338101039809954971057128909690225662108377598229356953056854940942307141694086065081673996274447311021563848212711188
c2 = 61646610042739459994461626406279915771252887311586474329650515776122404285063818909462942590860287479423847150864364566111480801953026903676149427898768771683846628566869540534265462180234702087341585697790664004963025137940580741008684159270494176394027856451236116352904950636561259856582366367187091006097

e1 = 3
e2 = 5

R = PolynomialRing(Zmod(n), 'm'); (m, ) = R._first_ngens(1)
m1 = 2021 * m ** 9 + 2022 * m ** 8 + 2023 
m2 = 1001 * m ** 4 + 1002 * m ** 3 + 1003 * m ** 2 + 1004 * m + 1005

p1 = m1**e1 - c1
p2 = m2**e2 - c2

def Gcd(x, y):
    if y == 0:
        return x.monic()
    return Gcd(y, x%y)

v = Gcd(p1, p2)
print(v)
print(long_to_bytes(n - int(v.coefficients()[0])))
