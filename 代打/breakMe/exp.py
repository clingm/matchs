from sage.all import *
from sage.all_cmdline import *

out = [(10104838556837572425858698219763292763650577822827673166610165534445905790599515983298170585537299796651687586519310335005278459900442296258190069157011689, 7564828531806668305145314143078783846371361009728098013923139274278986668460078185780789906860320972246757193033127803017086784149355945294908935420078516, 4485282300120902750491340174759104149475684698869265622396467866957919693682690175170986883471126578030682174788280328493147605703476577928850956031397969), (9565548877530896106016727232483590558935243658719980153279803247495028412133813638614011877483865630231054031084370990573419237535803428480492680139453999, 6038408119341558448569646184012774768725225345959109849115178440273061081156678389998969575922258723126076562743356339971035685064411166619777569139016508, 8750745342976938305411200510628417969404035221738007736422965823102502205577159397824830272988223657169242542971101468532748569435454625452166610190128781), (7032132827543709857775159929155596851822367214393091928329402747976746664890617830698759196796244901655353689522245761374585849734855765538189679713755499, 537414417641982152632158507627084083552317654751808484984901390258392606135955264531766980767789787016920198980507584546004466948509548457976277102756022, 6922262573315623933995838201220725774224132378664014973566219095767042719198956812716498145319448424126056354168025846702083830628832406132772890238012895), (10867950060245850877527719152309028431430000864654153258281294463898174216443333061889067616907305797497470525064325706490087786413068565388484751510567929, 2817477928396391253997165521234258370798748353920680581012362899514855249356663733557730846938679462940826446464369055820695102402810943359431061366297287, 6437402158704542412615350656111816825238327397134975867813883010385929819022183388539677074062781989152267579279340992202100004308737301019250714974969949)]

n, r, enc = out[0]
Zn = Zmod(n)
enc = Zn(enc)

PR = PolynomialRing(Zn, 'x')
x = PR.gen()

r_ = inverse_mod(r, n)

f = x**4 + 3*x**2 + r*x - enc
print(f.roots(multiplicities=False))