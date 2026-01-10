import telebot
import urllib.parse

Sahal = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"
bot = telebot.TeleBot(Sahal)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        " Merhaba 31\n\n"
        "Mesaj at qr kpde yapayım hemrn✅",
        parse_mode="Markdown"
    )
print("Bot pasif...")    
@bot.message_handler(content_types=['text'])
def qr_olustur(message):
    sihal = message.text
    data = urllib.parse.quote(sihal)
    sikerim = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={data}"
    bot.send_photo(
        message.chat.id,
        sikerim,
        caption="✅ QR Code hazır"
    )
bot.infinity_polling()