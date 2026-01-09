import requests, re, binascii
from Crypto.Cipher import AES
MO = '\033[95m'
MA = '\033[94m'
O = '\033[96m'
Y = '\033[92m'
S = '\033[93m'
K = '\033[31m'
B = '\033[37m'
G = '\033[1;30;40m'
print('''⣿⣿⣿⣿⣿⣿⢽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠹⣿⠟⠛⢉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣻⣿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⢣⠿⣿⢿⣻⣿⣿⣿⡃⠀⠌⠠⠁⡀⠄⠂⡀⠂⠄⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⡄⠉⢻⣿⣿
⣿⣿⣿⢯⣿⣿⣿⠷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⡏⣿⣿⣯⢚⣿⣛⡿⣯⣿⣿⣿⣆⠈⡀⠂⢁⠠⢀⠁⡐⠀⢂⣽⣿⣿⣿⣿⣿⣿⡯⠃⡘⣤⢣⠀⢫⢻
⣷⣺⣟⣾⣿⣿⢇⣛⣻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣾⡽⣿⣛⢮⣭⣛⣿⣽⣿⣿⣿⣷⣦⠀⡁⠂⡀⠂⠄⠠⢡⣿⣿⣿⣿⣿⣿⣿⣿⣇⠰⣹⣾⣷⣃⠀⠸
⣧⡟⣯⠿⣿⣿⠰⢯⣽⣯⣏⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣾⣿⣷⣷⣿⣿⣿⣿⣿⣿⣿⣷⣄⠐⢀⠡⢀⢵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣊⢠⣿⣿⣿⣿⠇⣼
⣿⣿⣿⣿⣷⣾⣯⣻⣷⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣩⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣽⣿⣿⣯⣾⣿\n''')
print(O+'\t\tTelegram Emoji Basma Tool')
print(G+'\t\t    Dev: @YeniIgisiz')
amgot = input(MO+"post linki gir:"+B).strip()
if not amgot.startswith("https://t.me/"):
    print(K+"url yanlis"+B)
    exit()
ritalin = requests.Session()
ritalin.headers.update({
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36"
})
sayfa = ritalin.get("https://weathercheck.xo.je").text
anahtarhex, ivhex, sifrehex = re.findall(r'toNumbers\("([0-9a-f]{32})"\)', sayfa)[:3]
anahtar = binascii.unhexlify(anahtarhex)
iv = binascii.unhexlify(ivhex)
sifrelimetin = binascii.unhexlify(sifrehex)
aesci = AES.new(anahtar, AES.MODE_CBC, iv)
cozdugumetin = aesci.decrypt(sifrelimetin)
pad = cozdugumetin[-1]
temiz = cozdugumetin[:-pad] if pad <= 16 else cozdugumetin
testcerezi = binascii.hexlify(temiz).decode().lower()
ritalin.cookies.set("__test", testcerezi, domain="weathercheck.xo.je", path="/")
yenisayfa = ritalin.get("https://weathercheck.xo.je").text
captcha = re.search(r'<div class="captcha-box">(\d+)</div>', yenisayfa)
if not captcha:
    print(K+"blok")
    exit()
sayi = captcha.group(1)
url = "https://weathercheck.xo.je/reaction.php"
payload = {
    'user_secret': "JDSMM.in",
    'tg_link': amgot,
    'captcha': sayi
}
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'Cache-Control': "max-age=0",
    'sec-ch-ua': "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'Origin': "https://weathercheck.xo.je",
    'Upgrade-Insecure-Requests': "1",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-User': "?1",
    'Sec-Fetch-Dest': "document",
    'Referer': "https://weathercheck.xo.je/reaction.php",
    'Accept-Language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = ritalin.post(url, data=payload, headers=headers)
if "50 reaction Sent! Redirecting" in response.text or "msg success" in response.text.lower():
    print(Y+"\n50 reaksiyon gonderildi"+B)
elif 'This link already received views. Try again after 10 min.' in response.text:
    print(K+'10 dakika bekle daha once bu linke attin'+B)
else:
    print(K+"\nAyni posta yakin zamanda gonderdin"+B)