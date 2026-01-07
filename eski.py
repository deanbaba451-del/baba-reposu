import os
import sys
import subprocess
import requests
import uuid
import random
import re
import string
import hashlib
import base64
import time
import json
from io import BytesIO
import webbrowser
webbrowser.open("https://t.me/eizonxtool")



#-----------------------------------------------#

P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
a1 = '\x1b[1;35m'  # 
a2 = '\x1b[1;34m'  # 
a3 = '\x1b[1;32m'  # 
a4 = '\x1b[1;33m'  # 
a5 = '\x1b[1;36m'  # 
RED = '\x1b[1;31m'  # 
ORANGE = '\x1b[38;5;208m'  
W = '\x1b[0m'  
O = "\033[38;5;208m"
K = '\033[1;35;40m'
C = '\033[1;36;40m'
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
W = "\033[97m"
rest = "\033[0m"
#-----------------------------------------------#





class Eizon:
    def __init__(self):
        self.my_uuid = uuid.uuid4()
        self.my_uuid_str = str(self.my_uuid)
        self.modified_uuid_str = self.my_uuid_str[:8] + "should_trigger_override_login_success_action" + self.my_uuid_str[8:]
        self.rd = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        
    def login(self, user, password):
        data = {
            "params": json.dumps({
                "client_input_params": {
                    "contact_point": user,
                    "password": f"#PWD_INSTAGRAM:0:0:{password}",
                    "fb_ig_device_id": [],
                    "event_flow": "login_manual",
                    "openid_tokens": {},
                    "machine_id": "ZG93WAABAAEkJZWHLdW_Dm4nIE9C",
                    "family_device_id": "",
                    "accounts_list": [],
                    "try_num": 1,
                    "login_attempt_count": 1,
                    "device_id": f"android-{self.rd}",
                    "auth_secure_device_id": "",
                    "device_emails": [],
                    "secure_family_device_id": "",
                    "event_step": "home_page"
                },
                "server_params": {
                    "is_platform_login": 0,
                    "qe_device_id": "",
                    "family_device_id": "",
                    "credential_type": "password",
                    "waterfall_id": self.modified_uuid_str,
                    "username_text_input_id": "9cze54:46",
                    "password_text_input_id": "9cze54:47",
                    "offline_experiment_group": "caa_launch_ig4a_combined_60_percent",
                    "INTERNAL__latency_qpl_instance_id": 56600226400306,
                    "INTERNAL_INFRA_THEME": "default",
                    "device_id": f"android-{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
                    "server_login_source": "login",
                    "login_source": "Login",
                    "should_trigger_override_login_success_action": 0,
                    "ar_event_source": "login_home_page",
                    "INTERNAL__latency_qpl_marker_id": 36707139
                }
            })
        }
        
        data["params"] = data["params"].replace("\"family_device_id\":\"\"", f"\"family_device_id\":\"{self.my_uuid_str}\"")
        data["params"] = data["params"].replace("\"qe_device_id\":\"\"", f"\"qe_device_id\":\"{self.my_uuid_str}\"")

        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "ar_SA",
            "X-Ig-Device-Locale": "ar_SA",
            "X-Ig-Mapped-Locale": "ar_AR",
            "X-Pigeon-Session-Id": f"UFS-{uuid.uuid4()}-0",
            "X-Pigeon-Rawclienttime": str(time.time()),
            "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "true",
            "X-Ig-Device-Id": str(uuid.uuid4()),
            "X-Ig-Family-Device-Id": str(uuid.uuid4()),
            "X-Ig-Android-Id": f"android-{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "X-Ig-Timezone-Offset": "10800",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": f"Instagram 303.0.0.0.59 Android (28/9; 320dpi; 900x1600; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)",
            "Accept-Language": "ar-SA, en-US",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"
        }

        try:
            response = requests.post(
                'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',
                headers=headers,
                data=data
            )
            
            body = response.text
            if "Bearer" in body:
                session_match = re.search(r'Bearer IGT:2:(.*?)[,\}]', body)
                if session_match:
                    session = session_match.group(1).strip()
                    if len(session) > 8:
                        session = session[:-8]
                    try:
                        full = base64.b64decode(session).decode('utf-8')
                        sessionid_match = re.search(r'"sessionid":"(.*?)"', full)
                        if sessionid_match:
                            sessionid = sessionid_match.group(1).strip()
                            print(f"{a2}【 {a5}●{a2} 】{a3}Logged in with @{user}")
                            print(f"{a2}【 {a5}●{a2} 】{a3}Sessionid: {sessionid}")
                            return sessionid
                    except:
                        print(f"{a2}【 {a5}●{a2} 】{a3}Error decoding session")
                print(f"{a2}【 {a5}●{a2} 】{a3}Could not extract session")
            elif any(error in body for error in [
                "The password you entered is incorrect",
                "Please check your username and try again.",
                "inactive user",
                "should_dismiss_loading\", \"has_identification_error\""
            ]):
                print(f"{a2}【 {a5}●{a2} 】{a3}Bad Password or Username")
            elif "challenge_required" in body or "two_step_verification" in body:
                print(f"{a2}【 {a5}●{a2} 】{a3}Challenge required - please check your Instagram app/email")
                retry = input(f"{a2}【 {a5}●{a2} 】{a3}Press Enter to try again or 'q' to quit: ")
                if retry.lower() != 'q':
                    return self.login(user, password)
            else:
                print(f"{a2}【 {a5}●{a2} 】{a3}Something went wrong")
                print(f"{a2}【 {a5}●{a2} 】{a3}Response: {body}")
                
        except Exception as e:
            print(f"{a2}【 {a5}●{a2} 】{a3}Request failed: {e}")
            
        return None

    def run(self):
        print("=" * 50)
        USER = input(f"{a2}【 {a5}●{a2} 】{a3}Username : ")
        PASSW = input(f"{a2}【 {a5}●{a2} 】{a3}Password : ")
        result = self.login(USER, PASSW)
        if result:
            print(f"{a2}【 {a5}●{a2} 】{a3}Login successful!")
        else:
            print(f"{a2}【 {a5}●{a2} 】{a3}Login failed!")
        

class RemovingFormerUsers:
    def __init__(self):
        self.clear_console()
        
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_random_csrf(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

    def display_header(self):
        self.clear_console()
        print("-" * 60)
        print()

    def download_image(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                image_bytes = BytesIO(response.content)
                return {"profile_pic": ("profile.jpg", image_bytes, "image/jpeg")}
        except:
            pass
        return None

    def change_profile_picture(self, sessionid, url_img):
        url = 'https://www.instagram.com/accounts/web_change_profile_picture/'
        csrf_token = self.generate_random_csrf()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/edit/",
            "X-CSRFToken": csrf_token,
            "Cookie": f"sessionid={sessionid}; csrftoken={csrf_token}"
        }

        try:
            files = self.download_image(url_img)
            if not files:
                return False
                
            response = requests.post(url, headers=headers, files=files, timeout=30)
            return response.status_code == 200 and response.json().get("status") == "ok"
        except:
            return False

    def verify_session(self, sessionid):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": f"sessionid={sessionid}"
            }
            response = requests.get(
                "https://www.instagram.com/api/v1/accounts/current_user/",
                headers=headers,
                timeout=10
            )
            return response.status_code == 200 and "user" in response.text
        except:
            return False

    def niggers(self, sessionid):
        pfp_urls = [
            'https://i.pinimg.com/550x/35/3f/c5/353fc517a4f4fac8d9ecfc734818e048.jpg',
            'https://i.pinimg.com/236x/c1/43/43/c1434392c4c11ac42b782e9397eb2b58.jpg',
            'https://i.pinimg.com/originals/0f/42/27/0f42279ce48796e63c920ba9aa0295a2.jpg',
            'https://i.pinimg.com/236x/bf/8d/0d/bf8d0d9df86c121ad4e9ed65b4bb92cb.jpg'
        ]
        
        basarili = 0
        yarrak = 0
        max_attempts = 20
        
        
        
        try:
            for attempt in range(max_attempts):
                for i, url in enumerate(pfp_urls):
                    if not self.verify_session(sessionid):
                        print(f"{a2}【 {a5}●{a2} 】{a3}Session expired or invalid!")
                        return
                        
                    print(f"{a2}【 {a5}●{a2} 】{a3}Attempt {attempt + 1}.{i + 1}:", end=" ")
                    
                    if self.change_profile_picture(sessionid, url):
                        basarili += 1
                        print("SUCCESS ✅")
                    else:
                        yarrak += 1
                        print("FAILED ❌")
                    
                    print(f"Progress: Changes: {basarili}, Errors: {yarrak}")
                    
                    if attempt < max_attempts - 1 or i < len(pfp_urls) - 1:
                        print("Waiting 20 seconds before next change...")
                        time.sleep(20)
                        
        except KeyboardInterrupt:
            ''
        
        l

    def run(self):
        self.display_header()
        sessionid = input(f"{a2}【 {a5}●{a2} 】{a3}Session id: ").strip()
        
        if not sessionid:
            print(f"{a2}【 {a5}●{a2} 】{a3}No sessionid provided!")
            return
            
        
        if not self.verify_session(sessionid):
            print(f"{a2}【 {a5}●{a2} 】{a3}Invalid sessionid!")
            return
            
        
        
        confirm = ("y").strip().lower()
        if confirm == 'y':
            self.niggers(sessionid)
        else:
            ''
        
        

def emir():
    while True:
        
        print(f"{a2}【 {a5}●{a2} 】{a3}dev; @besteizon / @eizonxtool")
        print("-" * 50)
        print(f"{a2}【 {a5}●{a2} 】{a3}1. İnstagram Session İd alma.")
        print(f"{a2}【 {a5}●{a2} 】{a3}2. İnstagram Eski Kullanici Adlarini Silme. ")
        print("-" * 50)
        
        c = input(f"{a2}【 {a5}●{a2} 】{a3}(1-2): ").strip()
        
        if c == '1':
            tool = Eizon()
            tool.run()
        elif c == '2':
            tool = RemovingFormerUsers()
            tool.run()
            break
        else:
            ''
            input()

if __name__ == "__main__":
    emir()
    
    
    # tg @besteizon
    
    
    