import requests
import time
import cfonts
from colorama import Fore, Style, init
from functools import partial
from copy import deepcopy

init(autoreset=True)

def renkli_yazı(yazı, renk=Fore.WHITE):
    print(renk + yazı + Style.RESET_ALL)

def countdown(sure, renk=Fore.CYAN):
    for remaining in range(sure, 0, -1):
        print(renk + f"\rKalan süre: {remaining} saniye", end="")
        time.sleep(1)
    print(renk + "\rSüre doldu!            " + Style.RESET_ALL)

def ramazan_banner():
    cfonts.say("SMM", colors=["black", "yellow"], align="center")

def api_istek_yap(url, cookies, headers, veri):
    try:
        cevap = requests.post(url, cookies=cookies, headers=headers, data=veri)
        cevap.raise_for_status()
        return cevap.json()
    except requests.exceptions.RequestException as hata:
        renkli_yazı(f"İstek hatası: {hata}", Fore.RED)
        return None

def sosyal_islem(tür, platform, cookies, headers, veri):
    link = input(f"{platform} {tür} için link/kullanıcı adı giriniz: ")
    veri["freetool[process_item]"] = link
    return genel_islem_akışı(cookies, headers, veri)

def genel_islem_akışı(cookies, headers, veri):
    json_cevap = api_istek_yap("https://instaavm.com/action/", cookies, headers, veri)
    
    if not json_cevap:
        return False
    
    if json_cevap.get("alert", {}).get("statu") == "danger":
        renkli_yazı(f"Başarısız: {json_cevap.get('alert', {}).get('text', 'Bilinmeyen hata')}", Fore.RED)
        return False
    
    if not (token := json_cevap.get("freetool_process_token")):
        renkli_yazı("Token alınamadı!", Fore.RED)
        return False
    
    veri["freetool[token]"] = token
    bekleme = int(json_cevap.get("freetool_delay_minute", 2)) * 60
    
    renkli_yazı(f"İşlem başlatıldı, {bekleme} saniye bekleniyor...", Fore.CYAN)
    countdown(bekleme, Fore.CYAN)
    
    for deneme in range(10):
        json_cevap = api_istek_yap("https://instaavm.com/action/", cookies, headers, veri)
        
        if json_cevap and "freetool_process_success" in json_cevap:
            renkli_yazı("Başarılı: İşlem tamamlandı!", Fore.GREEN)
            return True
            
        renkli_yazı("İşlem henüz tamamlanmadı, 10 saniye bekleniyor...", Fore.CYAN)
        countdown(10, Fore.CYAN)
    
    renkli_yazı("Maksimum deneme sayısına ulaşıldı!", Fore.YELLOW)
    return False

def ana_menu():
    ramazan_banner()
    ortak_cookies = {
        '_gcl_au': '1.1.471031389.1738431492',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_first_add': 'fd%3D2025-02-01%2020%3A38%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Finstaavm.com%2Fyoutube-ucretsiz-abone%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F',
        'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29',
        '_ga': 'GA1.1.1847029614.1738431494',
        '_hjSessionUser_3892406': 'eyJpZCI6ImE5YThkNmIwLWIzZTItNTJhMC1hYTBjLWJhNjQ0ZmViYTVkMiIsImNyZWF0ZWQiOjE3Mzg0MzE0OTMyNDAsImV4aXN0aW5nIjp0cnVlfQ==',
        'crisp-client%2Fsession%2F396f3338-5774-48ef-bba7-fc121928303a': 'session_5378fc0c-ec7e-4b36-9f7d-0e2e3c0caa8b',
        'PHPSESSID': '91e0c9a7fa83ac2289d8f180ae9d05db',
        'sessionExpirationDate': '1740839703309',
        'sbjs_current_add': 'fd%3D2025-03-01%2017%3A28%3A57%7C%7C%7Cep%3Dhttps%3A%2F%2Finstaavm.com%2Finstagram-ucretsiz-izlenme%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F',
        'sbjs_udata': 'vst%3D17%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Finstaavm.com%2Finstagram-ucretsiz-izlenme%2F',
        '_ga_0J6DVJ02HM': 'GS1.1.1740835882.6.1.1740839348.47.0.1948133288',
    }

    ortak_headers = {
        'authority': 'instaavm.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://instaavm.com',
        'referer': 'https://instaavm.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    islemler = {
        1: ("Instagram Takipçi", partial(sosyal_islem, "Takipçi", "Instagram", 
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/instagram-ucretsiz-takipci/"},
            {"ns_action": "freetool_start", "freetool[id]": "2", "freetool[quantity]": "40"})),
        
        2: ("Instagram Beğeni", partial(sosyal_islem, "Beğeni", "Instagram",
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/instagram-ucretsiz-begeni/"},
            {"ns_action": "freetool_start", "freetool[id]": "1", "freetool[quantity]": "50"})),
        
        3: ("Instagram İzlenme", partial(sosyal_islem, "İzlenme", "Instagram",
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/instagram-ucretsiz-izlenme/"},
            {"ns_action": "freetool_start", "freetool[id]": "3", "freetool[quantity]": "250"})),
        
        4: ("TikTok Takipçi", partial(sosyal_islem, "Takipçi", "TikTok",
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/tiktok-ucretsiz-takipci/"},
            {"ns_action": "freetool_start", "freetool[id]": "4", "freetool[quantity]": "50"})),
        
        5: ("TikTok Beğeni", partial(sosyal_islem, "Beğeni", "TikTok",
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/tiktok-ucretsiz-begeni/"},
            {"ns_action": "freetool_start", "freetool[id]": "5", "freetool[quantity]": "75"})),
        
        6: ("TikTok İzlenme", partial(sosyal_islem, "İzlenme", "TikTok",
            deepcopy(ortak_cookies),
            {**deepcopy(ortak_headers), "referer": "https://instaavm.com/tiktok-ucretsiz-izlenme/"},
            {"ns_action": "freetool_start", "freetool[id]": "6", "freetool[quantity]": "250"})),
        
        7: ("Çıkış", None)
    }

    while True:
        renkli_yazı("\n" + "═"*60, Fore.BLUE)
        renkli_yazı("~ BATU - SOSYAL MEDYA ARACI ~", Fore.MAGENTA)
        renkli_yazı("═"*60, Fore.RED)
        for key, (text, _) in islemler.items():
            renkli_yazı(f"{key}. {text}", Fore.CYAN)
        renkli_yazı("═"*60, Fore.GREEN)
        try:
            secim = int(input(Fore.YELLOW + "Seçiminiz: " + Style.RESET_ALL))
            if secim == 7:
                renkli_yazı("Çıkış yapılıyor...", Fore.LIGHTBLUE_EX)
                break
                
            if secim not in islemler:
                renkli_yazı("Geçersiz seçim!", Fore.RED)
                continue
                
            _, fonksiyon = islemler[secim]
            if fonksiyon and fonksiyon():
                renkli_yazı("\nİşlem tamamlandı! Yeni işlem için bekleniyor...", Fore.LIGHTGREEN_EX)
                
        except ValueError:
            renkli_yazı("Lütfen geçerli bir sayı girin!", Fore.RED)

if __name__ == "__main__":
    ana_menu()
#@ea7capone