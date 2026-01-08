import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import yt_dlp
import os
import random
import string
import time

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
user_links = {}
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = InlineKeyboardMarkup()
    dev = InlineKeyboardButton("Yapımcı", url="https://t.me/BenAtaniz")
    markup.add(dev)

    bot.send_message(
        message.chat.id,
        "Hoş geldin dostum\nSadece Instagram Reels bağlantısını gönder, senin için video ve ya sesini atayım",
        reply_markup=markup
    )
@bot.message_handler(func=lambda message: "instagram.com/reel" in message.text)
def handle_reel(message):
    url = message.text.strip()
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    user_links[short_id] = url
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🎥 Video", callback_data=f"video|{short_id}"),
        InlineKeyboardButton("🔊 Ses", callback_data=f"audio|{short_id}")
    )
    bot.send_message(
        message.chat.id,
        "Reels bağlantısı alındı\nHangi formatda atılsın seç:",
        reply_markup=markup
    )
@bot.callback_query_handler(func=lambda call: True)
def handle_choice(call):
    try:
        action, short_id = call.data.split("|", 1)
        url = user_links.get(short_id)
        if not url:
            bot.send_message(call.message.chat.id, "Link süresi dolmuş, lütfen tekrar gönder.")
            return
        status_msg = bot.send_message(call.message.chat.id, "Hazırlanıyor...")
        time.sleep(1)
        bot.edit_message_text("Bağlantı kontrol ediliyor...", call.message.chat.id, status_msg.id)
        time.sleep(1)
        bot.edit_message_text(" İndiriliyor, lütfen bekle...", call.message.chat.id, status_msg.id)
        ydl_opts = {
            "outtmpl": "%(title).90s.%(ext)s",
            "quiet": True,
            "noplaylist": True,
            "skip_download": False
        }
        if action == "video":
            ydl_opts["format"] = "best[ext=mp4]/best"
        else:
            ydl_opts["format"] = "bestaudio[ext=m4a]/bestaudio/best"
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        bot.edit_message_text("Yükleniyor...", call.message.chat.id, status_msg.id)
        with open(file_path, "rb") as f:
            if action == "video":
                bot.send_video(call.message.chat.id, f, caption="Hazır. w Size Kaliteli Halde Sunar")
            else:
                bot.send_audio(call.message.chat.id, f, caption="Hazır. w Size Kaliteli Halde Sunar")
        bot.edit_message_text("✅ Tamamlandı!", call.message.chat.id, status_msg.id)
        os.remove(file_path)
        del user_links[short_id]

        markup = InlineKeyboardMarkup()
        dev = InlineKeyboardButton("Yapimci", url="https://t.me/BenAtaniz")
        markup.add(dev)
        bot.send_message(call.message.chat.id, "Teşekkürler, tekrar görüşürüz canimmm seni seviyorummm", reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Hata oluştu:\n<code>{e}</code> lütfen Sahala hatayı bildirin")

print("SAHAL NİLİ SEVİYOR")
bot.polling()
