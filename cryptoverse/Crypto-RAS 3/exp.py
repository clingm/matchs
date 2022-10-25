from sage.all import *
from Crypto.Util.number import *
from gmpy2 import iroot
n1 = 10480986263357390015776470181687227178789606027421931997838384791742875910740767389246374147263556772853587957944523942275151679101459733138053053868296673001380927326933789522979485694557912270649491855915057695526288927912392755094947658151794487408589779116492196917747227095902085192796677356230719805408407894098051080100555244027086695517636080914515567794113748950479340319290224106355540133172960042012975782865677547318761116292218860387111643145220906974483669879938581991263332497728771664063360699109134813005243727844276144233529640805049364427549884319412107240148780531109743201547633043255767320797549
e = 17
c1 = 1944514616413732313411062389518969823732098553485072226021622420228817362202202432655723662236737135533446777534145997293648634996567373802314589406681574767065586031848878322965116556917183983633654493265702847737988057588589625497140913201252910399747574090017869382512609748537443156899876149577431868096825588886933039011708685475383898002210008019226431401156814110153165252322204388377053939495696167160602899619081251712202611920091032273976751669265936960167858665186696144927485379006839191003041265397192288246572518646057687955062539635338138972966657941697159448179837178395393868967794129115307638660723

n2 = 17081905369470608320832480909215027382194520027682751402481901395654142291841274970996502220788374100498895975046651634331752662097440244113329447105731279791080049344777670022149670791955239461050220375774330210479761560244379026394952222667758338366059670868224053688609737323012913263618470354335440342439504872132761698032484261594530051342946571979574854463924908563542713262852549456836307906310406722434828257487329524512269669547713385142224652781025065422821914508978650666817792771857820413598590236749360373247704500401328915185355447792798708348597871271521271366434853051511213548478944378553646738763627
c2 = 10660876633585763553967383503078084106051183613108311021028023836416074739000765329366323618796132530196772158364298157065471936452217875003849761228518137259410800010969393976263052706470700413060840315724153281566273929446215507820685288644279713041920857566246492527871165920211525270098499296922986767803875569813333849265543431425042434465971355205458545481949737427072195861873595972318531220798071366813945180768921045257075495700332903002996110215823319674374321174889668802066568665805173865526835205053473741726957418168472174642454409911850149393535173251608630814032586357598350015640217392884487120027858

n3 = 23608972201608453857186409830664114428445571104241087062847677147249385652282109821578298723346296382519369386317834581218783295384808491592390362307437576866815502355179179010125432254181733446066771357726422068596485601604203659561812180026900611476387400388689982812141763512027570615500250380933522381568764648696416331069551492411131210598543741491110096863540564053179028434189715536643648622027255219828940938909462684595383117190561124317182480201215187672761118460868568800610912335735328979180588383558824396691167900251113231731028072404209932701804629894137831155285074153427302127628525021836895649312173
c3 = 8554251401725536958126780836303496256028407374595092702230575912645611908291278982583524147821787532594295638110614401122200633219779285147403126560206629384987062298917668350340919421431031893074184452275167333773712750501181575464097183876671355565363774390113635293970657157009096373576750277203158398399684398783160471804095538503806105350954656968471969953594028453016230275934747722012348223919893380012369108807222353442555304685463881928793141617338944486678737098532635793442313060174039305221921913686460980710271645903914265821835975818027570567394214923669742084039988195988476659666364931337228467388948

c = CRT_list([c1, c2, c3], [n1, n2, n3])

print(long_to_bytes(iroot(c, e)[0]))