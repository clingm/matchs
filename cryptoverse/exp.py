from sage.all import *
from sage.all_cmdline import *

# Question 1
p = 13229
a = 575
b = 1970
P = (2273, 11906)

E = EllipticCurve(GF(p), [a, b])
P = E(P)
Qx, Qy, _ = P * 6448
print(f"({Qx}, {Qy})")

# Question 2
p = 59260206515491228276234044455682098935659054221164716729246346835555911501970770577934457035913892405248729355404657393616549643031314742151350159473445030078732776159265677388535265451399
Mx, My = (30971288249532591101397035939335353866777407168095611981961131636226757780716277739016156217420329232448871480650732799345566352718047178891628828085110305406904879509870948747876359704375, 57171968487246715556398530094840476366170759532150812306878752481499744628037490337522525062397717282954597306332855677228202345363884217084822828348756779280112664809503606730140815819638)
Nx, Ny = (150923074787259102026641532856668019240840620143072243230895608899334115994086522123741438269501329156554504967217520153854986489437362857237989778139488550571364161735317384644999727156, 49212740084294391129391348507403599670759095834595837322153941457143122833124875180156403132105705945046220920987918745699021971701588021143681234963195574564585004030542768020321913886894)

# a = (((My**2 - Ny**2) - (Mx**3 - Nx**3)) // (Mx - Nx))
# b = (My**2 - Mx**3 - a*Mx)
# print(f'({a % p}, {b % p})')

a, b = var('a b')
eq1 = My**2 == Mx**3 + a * Mx + b
eq2 = Ny**2 == Nx**3 + a * Nx + b
r = solve([eq1, eq2], a, b,solution_dict=True)
print(f'({int(r[0][a]) % p}, {int(r[0][b]) % p})')

# Question 3
p = 1265716264036450577614097302529
a = 869091923016915507276101796550
b = 1264119743277152509949380483705
P = (139255669696397040604990890681, 19092416236196150566729789953)
Q = (1080294921522519732557580992469, 1231439852027864159829505344577)
E = EllipticCurve(GF(p), [a, b])

P = E(P)
Q = E(Q)

u = P.discrete_log(Q)
print(u)
