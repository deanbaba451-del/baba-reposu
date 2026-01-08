import telebot
import requests

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
bot = telebot.TeleBot(TOKEN)
API_LIST = [
    "https://namaz-vakti.vercel.app/api/timesFromPlace?country=Turkey&city=",
    "https://api.aladhan.com/v1/timingsByCity?country=Turkey&city=",
    "https://ezanvakti.herokuapp.com/vakitler?ilce="
]
VAKIT_ADLARI = {
    "sabah": ["Fajr", "Fajr", "Imsak"],
    "ogle": ["Dhuhr", "Dhuhr", "Ogle"],
    "ikindi": ["Asr", "Asr", "Ikindi"],
    "aksam": ["Maghrib", "Maghrib", "Aksam"],
    "yatsi": ["Isha", "Isha", "Yatsi"],
    "sahur": ["Fajr", "Fajr", "Imsak"],
    "iftar": ["Maghrib", "Maghrib", "Aksam"]
}
def sahal_get_vakit(sehir, vakit):  
    for i, api in enumerate(API_LIST):
        try:
            response = requests.get(f"{api}{sehir}")
            if response.status_code == 200:
                data = response.json()
                if i == 0:
                    return f"🕌 {sehir.capitalize()} için {vakit.capitalize()} vakti: {data['times'][VAKIT_ADLARI[vakit][i]]}"
                elif i == 1:
                    return f"🕌 {sehir.capitalize()} için {vakit.capitalize()} vakti: {data['data']['timings'][VAKIT_ADLARI[vakit][i]]}"
                elif i == 2 and len(data) > 0:
                    return f"🕌 {sehir.capitalize()} için {vakit.capitalize()} vakti: {data[0][VAKIT_ADLARI[vakit][i]]}"
        except:
            continue
    return "❌ Namaz vakitleri alınamadı, lütfen daha sonra tekrar deneyin."
@bot.message_handler(commands=["start"])
def sahal_send_welcome(message):  
    bot.reply_to(
        message,
        "Namaz Vakitleri Botu\n"
        " Türkiye'deki namaz vakitlerini öğrenmek için aşağıdaki komutları kullanabilirsiniz:\n\n"
        "Komutlar:\n"
        " /sabah <şehir> - Sabah namazı vakti\n"
        "/ogle <şehir> - Öğle namazı vakti\n"
        " /ikindi <şehir> - İkindi namazı vakti\n"
        " /aksam <şehir> - Akşam namazı vakti\n"
        " /yatsi <şehir> - Yatsı namazı vakti\n"
        " /sahur <şehir> - Sahur (imsak) vakti\n"
        " /iftar <şehir> - İftar vakti\n\n"
        " Örnek Kullanım:\n"
        " /sabah Antalya\n"
        "/iftar İstanbul\n"
        "/sahur Adana\n"
        "Kaynak: 3 farklı API kullanıyor (Namaz Vakti, Aladhan, Diyanet)"
    )
@bot.message_handler(commands=["sabah", "ogle", "ikindi", "aksam", "yatsi", "sahur", "iftar"])
def sahal_send_vakit(message):  
    komut = message.text.split()
    if len(komut) < 2:
        bot.reply_to(message, "⚠️ Lütfen şehir adını da girin. Örn: `/sabah İstanbul`")
        return
    sehir = " ".join(komut[1:]).capitalize()
    vakit_adi = komut[0][1:]
    cevap = sahal_get_vakit(sehir, vakit_adi)  
    bot.reply_to(message, cevap)
print("✅ Namaz Vakitleri Botu Çalışıyor...")
bot.polling()