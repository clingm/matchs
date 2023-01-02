from Crypto.Util.number import *
from random import *


nbits = 2200
beta = 0.4090
p, q = getPrime(int((1. - beta) * nbits)), getPrime(int(beta * nbits))
dp = getrandbits(50) | 1
while True:
    d = (p - 1) * getrandbits(2800) + dp
    if GCD((p - 1) * (q - 1), d) == 1:
        break
e = inverse(d, (p - 1) * (q - 1))
N = p * q
flag = bytes_to_long(open('flag.txt', 'rb').read())

c = pow(flag, e, N)
print(N)
print(e)
print(c)

"""
46460689902575048279161539093139053273250982188789759171230908555090160106327807756487900897740490796014969642060056990508471087779067462081114448719679327369541067729981885255300592872671988346475325995092962738965896736368697583900712284371907712064418651214952734758901159623911897535752629528660173915950061002261166886570439532126725549551049553283657572371862952889353720425849620358298698866457175871272471601283362171894621323579951733131854384743239593412466073072503584984921309839753877025782543099455341475959367025872013881148312157566181277676442222870964055594445667126205022956832633966895316347447629237589431514145252979687902346011013570026217
13434798417717858802026218632686207646223656240227697459980291922185309256011429515560448846041054116798365376951158576013804627995117567639828607945684892331883636455939205318959165789619155365126516341843169010302438723082730550475978469762351865223932725867052322338651961040599801535197295746795446117201188049551816781609022917473182830824520936213586449114671331226615141179790307404380127774877066477999810164841181390305630968947277581725499758683351449811465832169178971151480364901867866015038054230812376656325631746825977860786943183283933736859324046135782895247486993035483349299820810262347942996232311978102312075736176752844163698997988956692449
28467178002707221164289324881980114394388495952610702835708089048786417144811911352052409078910656133947993308408503719003695295117416819193221069292199686731316826935595732683131084358071773123683334547655644422131844255145301597465782740484383872480344422108506521999023734887311848231938878644071391794681783746739256810803148574808119264335234153882563855891931676015967053672390419297049063566989773843180697022505093259968691066079705679011419363983756691565059184987670900243038196495478822756959846024573175127669523145115742132400975058579601219402887597108650628746511582873363307517512442800070071452415355053077719833249765357356701902679805027579294
"""
