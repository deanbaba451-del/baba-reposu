import requests
import json
import os

ensar = "https://apiv2.tsgonline.net/tsgapis/Botaltyapi/"

def SoryTuul(oe, params):
    try:
        response = requests.get(f"{ensar}{oe}", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def ae(data, indent=4):
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except Exception:
        return str(data)

def sory():
    print("            | Zeynalovs |")
    print("1 - TC Pro (TC Sorgu)")
    print("2 - Ad Soyad (Ad Soyad Sorgu)")
    print("3 - Ad Soyad İl (Ad Soyad Sorgu)")
    print("4 - Adres (Adres Sorgu)")
    print("5 - Apartman (Apartman Sorgu)")
    print("6 - TC > GSM (TC > GSM Sorgu)")
    print("7 - GSM > TC (GSM > TC Sorgu)")
    print("8 - Tg sorgu")
    print("9 - Sülale (Sülale Sorgu)")
    print("10 - Aile (Aile Sorgu)\n")

    choice = input("Seçiminizi girin (1-10): ").strip()

    if choice == "1":
        tc = input("TC no girin: ").strip()
        params = {"auth": "tsgxyunus", "tc": tc}
        oe = "adpro.php"
    elif choice == "2":
        ad = input("Ad girin: ").strip()
        soyad = input("Soyad girin: ").strip()
        params = {"auth": "tsgxyunus", "ad": ad, "soyad": soyad}
        oe = "adpro.php"
    elif choice == "3":
        ad = input("Ad girin: ").strip()
        soyad = input("Soyad girin: ").strip()
        il = input("İl girin: ").strip()
        params = {"auth": "tsgxyunus", "ad": ad, "soyad": soyad, "il": il}
        oe = "adpro.php"
    elif choice == "4":
        tc = input("TC no girin: ").strip()
        params = {"tc": tc}
        oe = "adres.php"
    elif choice == "5":
        tc = input("TC no girin: ").strip()
        params = {"tc": tc}
        oe = "apartman.php"
    elif choice == "6":
        tc = input("TC no girin: ").strip()
        params = {"tc": tc}
        oe = "tcgsm.php"
    elif choice == "7":
        gsm = input("GSM no girin: ").strip()
        params = {"gsm": gsm}
        oe = "gsmtc.php"
    elif choice == "8":
        username = input("Username girin: ").strip()
        params = {"username": username}
        oe = "tg.php"
    elif choice == "9":
        tc = input("TC no girin: ").strip()
        params = {"tc": tc}
        oe = "sulale.php"
    elif choice == "10":
        tc = input("TC no girin: ").strip()
        params = {"tc": tc}
        oe = "aile.php"
    else:
        print("Geçersiz seçim.")
        return

    soryy = SoryTuul(oe, params)
    oc = ae(soryy)

    kaydet = input("Sonuç dosyaya (rolex.txt) kaydedilsin mi? (y/n): ").strip().lower()
    baslik = "Zeynalovs"

    if kaydet == "y":
        dosya_yolu = os.path.join(os.getcwd(), "rolex.txt")
        with open(dosya_yolu, "w", encoding="utf-8") as f:
            f.write(baslik + "\n\n")
            f.write(oc)
        print(f"Sonuç kaydedildi: {dosya_yolu}")
    else:
        print(f"\n{baslik}\n")
        print(oc)

if __name__ == "__main__":
    sory()