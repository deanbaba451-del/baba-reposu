import requests
import uuid
import time
import getpass

class InstagramSession:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        device_id = str(uuid.uuid4())
        login_data = {
            'username': self.username,
            'enc_password': f'#PWD_INSTAGRAM:0:{int(time.time())}:{self.password}',
            'device_id': device_id,
            'login_attempt_count': '0'
        }

        headers = {
            'User-Agent': 'Instagram 100.0.0.17.129 Android (28/9; 300dpi; 900x1600; Asus; ASUS_I003DD; ASUS_I003DD; intel; en_US; 161478664)',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-App-ID': '567067343352427',
            'X-FB-HTTP-Engine': 'Liger',
            'X-Pigeon-Session-Id': str(uuid.uuid4()),
            'X-Pigeon-Rawclienttime': str(time.time()),
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-Kbps': '-1.000',
            'X-IG-Bandwidth-Totalbytes-B': '0',
            'X-IG-Bandwidth-Totaltime-Ms': '0',
            'Connection': 'keep-alive',
        }

        response = self.session.post(url, headers=headers, data=login_data)

        try:
            result = response.json()
        except:
            return False, "Instagram geÃ§ersiz yanÄ±t verdi."

        if result.get("logged_in_user"):
            sessionid = self.session.cookies.get("sessionid")
            with open("sessionid.txt", "a") as f:
                f.write(f"{sessionid}\n")
            return True, sessionid
        elif result.get("message"):
            return False, result["message"]
        elif "error_type" in result:
            return False, result.get("error_type")
        else:
            return False, "Bilinmeyen hata oluÅtu."

def main():
    print("=" * 50)
    print("Instagram Session ID AlÄ±cÄ±")
    print("Developer: @BestEizon")
    print("=" * 50)
    
    username = input("Instagram kullanÄ±cÄ± adÄ±nÄ±z: ")
    password = getpass.getpass("Åifreniz: ")
    
    print("\nGiriÅ yapÄ±lÄ±yor...")
    
    try:
        login = InstagramSession(username, password)
        success, result = login.login()

        if success:
            print("\n" + "=" * 50)
            print("â BAÅARILI!")
            print("Session ID:")
            print(result)
            print("=" * 50)
            print("\nSession ID 'sessionid.txt' dosyasÄ±na kaydedildi.")
        else:
            print(f"\nâ Hata: {result}")
            
    except Exception as e:
        print(f"\nâ Bir hata oluÅtu: {str(e)}")
        
if __name__ == "__main__":
    main()