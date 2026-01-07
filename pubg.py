import webbrowser
import requests
import random
print("PUBG HESAP        RAİZEN STORE SUNAR")
import json
import os
import requests, time
import webbrowser
webbrowser.open('https://t.me/+Q34zmJI_FZozOGNi')


tok = input("8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI:")
ID = input("6534222591: ")
accounts_count = int(input(" Hesap sayısı: "))


for _ in range(accounts_count):
    characters = "1234567890QWERTYUIOPASDFGHJKLXCVBNM"
    
    
    us = ''.join(random.choice(characters) for _ in range(7))
    username = "GE" + us
    password = "BF" + us
    us4 = ''.join(random.choice(characters) for _ in range(8))
    
    
    tlg_message = f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ᯓ ʟᴏɢɪɴ ➥ Facebook\n\n 
\n ✓ ➥ 𝙴 posta ➪ {username}@gmail.com
\n ✓ ➥ Şifre ➪ +{us4}
\n ✓ ➥ Ülke ➪ Türkiye
\n ✓ ➥ Kod ➪ +90
\n ✓ ➥ Zaman ➪ 2022-10-22
\n\nᯓ BY : 𓏺 Zeynalovs </> - @Zeynalovs5'''
    

    response = requests.post(tlg_message)
    
 
    if response.status_code == 200:
        print(f"[✓]Hesab gönderme başarılı: {username}")
    else:
        print(f"[✗] Gönderme hatası: {username}")