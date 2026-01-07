import pyfiglet
print(pyfiglet.figlet_format("Pubg Tool"))
import random
import requests
import webbrowser
import os
import json
import requests, time

webbrowser.open("https://t.me/Mrzpyx")

tok = input("8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI: ")
id = input("6534222591: ")
accounts_count = int(input("Hesap Sayısı: "))

for _ in range(accounts_count):
    characters = "123456789QWERTYUİOPASDFGHJKLZXCVBNM"
    us = ''.join(random.choice(characters) for _ in range(7))
    username = "GE" + us
    password = "BF" + us
    us4 = ''.join(random.choice(characters) for _ in range(8))
      
    tlg_message = f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=ᯓ ʟᴏɢɪɴ ➥ Facebook\n\n 
\n 🎖 😶‍🌫 𝙴 posta ➪ {username}@gmail.com
\n 🎖 😶‍🌫 Şifre ➪ +{us4}
\n 🎖🀽򝠍🌫 Ülke ➪ Türkiye
\n\nᯓ BY 🀠: @mrzpyx 𓏺< </> - @KorkumYokki'''   

    response = requests.post(tlg_message)
    
    if response.status_code == 200:
        print(f"[✓] Hesap gönderme başarılı: {username}")
    else:
        print(f"[✗] Gönderme hatası: {username}"