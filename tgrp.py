import requests
import random
import re
import time
print("YOUTUBE 25 ABONE TOOL")
import json
import os
import requests, time
import webbrowser
webbrowser.open('https://t.me/+Q34zmJI_FZozOGNi')

RENKLER = {
    'KIRMIZI': '\033[1;31;40m',
    'SARI': '\033[1;33;40m', 
    'YESIL': '\033[1;32;40m',
    'BEYAZ': '\033[1;97;40m',
    'MAVI': '\033[1;36;40m',
    'MOR': '\033[1;35;40m',
    'SON': '\033[0m'
}

def baslik_goster():
    print(f"""

{RENKLER['MOR']}✧ Geliştirici: @Zeynalovs5 
{RENKLER['SARI']}✧ Kanal: Raizen Store 
{RENKLER['KIRMIZI']}⚠ Uyarı: Yasal olmayan kullanımlardan sorumlu değiliz! 
{RENKLER['SON']}""")

def eposta_olustur():
    uzanti = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@protonmail.com"]
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) + random.choice(uzanti)

def telefon_olustur():
    ulke_kodlari = ["+90", "+1", "+44", "+49"]
    return random.choice(ulke_kodlari) + ''.join(random.choices("0123456789", k=10))

def ulke_sec():
    diller = ["Türkçe", "İngilizce", "Almanca", "Fransızca", "İspanyolca"]
    return random.choice(diller)

def rapor_gonder():
    baslik_goster()
    
    mesaj_linki = input(f"{RENKLER['BEYAZ']}• {RENKLER['MAVI']}Mesaj Linki: {RENKLER['SON']}")
    kanal_linki = input(f"{RENKLER['BEYAZ']}• {RENKLER['MAVI']}Kanal Linki: {RENKLER['SON']}")

    oturum = requests.Session()
    oturum.cookies.update({'stel_ssid': f'raporcu_{random.randint(100000,999999)}'})

    while True:
        try:
            user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,125)}.0.0.0 Safari/537.36"
            
            basliklar = {
                'User-Agent': user_agent,
                'Referer': 'https://telegram.org/support',
                'Origin': 'https://telegram.org',
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            veriler = {
                'message': f"""Telegram platformunda ciddi bir sorunla karşılaştım:
                
Şüpheli Mesaj: {mesaj_linki}
İhlal Yapan Kanal: {kanal_linki}

Bu içerikler topluluk kurallarını açıkça ihlal etmektedir. Lütfen acilen müdahale edin!""",
                'email': eposta_olustur(),
                'phone': telefon_olustur(),
                'setln': ulke_sec()
            }

            yanit = oturum.post(
                url='https://telegram.org/support',
                headers=basliklar,
                data=veriler,
                timeout=15
            )

            if yanit.status_code == 200:
                basari_mesaji = re.search(r'<div class="alert alert-success">(.*?)</div>', yanit.text, re.DOTALL)
                if basari_mesaji:
                    print(f"{RENKLER['YESIL']}[✓] Rapor başarıyla gönderildi!{RENKLER['SON']}")
                else:
                    print(f"{RENKLER['KIRMIZI']}[✗] Rapor gönderilemedi!{RENKLER['SON']}")
            else:
                print(f"{RENKLER['SARI']}[!] Hata Kodu: {yanit.status_code}{RENKLER['SON']}")

            time.sleep(random.uniform(3, 7))

        except Exception as hata:
            print(f"{RENKLER['KIRMIZI']}[!] Kritik Hata: {str(hata)}{RENKLER['SON']}")
            time.sleep(10)

if __name__ == "__main__":
    rapor_gonder()
# @furkanws