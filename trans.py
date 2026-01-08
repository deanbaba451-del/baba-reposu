import telebot
import requests
sihal = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"

bot = telebot.TeleBot(sihal)
print("Bot pasif")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot aktif\n Atılan mesajı ingilizce yapacağım.")
@bot.message_handler(func=lambda m: True)
def tum_mesajlari_cevir(message):
    if not message.text:  
        return
    text = message.text.strip()
    if text.startswith('/'):
        return
    if len(text) < 3:
        return
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            'client': 'gtx',
            'sl': 'auto',
            'tl': 'en',
            'dt': 't',
            'q': text
        }
        r = requests.get(url, params=params, timeout=8)
        ceviri = r.json()[0][0][0]
        if ceviri.strip().lower() == text.strip().lower():
            return
        bot.reply_to(message, ceviri)
    except:
        pass  
bot.infinity_polling(none_stop=True, interval=0, timeout=20)