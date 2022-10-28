from sage.all import *
from sage.all_cmdline import *

'''
print("L:", x^1+y^3+z^3+w^7)
print("E:", y^1+z^3+w^3+x^7)
print("E:", z^1+w^3+x^3+y^7)
print("E:", w^1+x^3+y^3+z^7)
print("T:", x+y+z+w)
'''

P = 231609284865232306744388160907453774453
L = 213929627434382339098735177055751649916
E1 = 19199104003461693263250446715340616788
E2 = 81305572597778258494448971196865605263
E3 = 204055349607012377951682156574173649079
T = 2268211308285612387872477045295901103

PR = PolynomialRing(GF(P), ('x', 'y', 'z', 'w'))

x, y, z, w = PR._first_ngens(4)

eq = []
eq.append(x + y**3 + z**3 + w**7 - L)
eq.append(y + z**3 + w**3 + x**7 - E1)
eq.append(z + w**3 + x**3 + y**7 - E2)
eq.append(w + x**3 + y**3 + z**7 - E3)
eq.append(x+y+z+w - T)

I = PR.ideal(eq)
#assert I.dimension() == 0

print(I.variety())