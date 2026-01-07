#+------------------------------------------------------+
# - Dev  : ⛧ 𝐓𝐡𝐨𝐦𝐚𝐬 ⛧         
# - Telegram : t.me/Thomas_Python                
# - Kanal :  t.me/ThomasGruplar      
#+------------------------------------------------------+       



import os
import telebot
from yt_dlp import YoutubeDL
BOT_TOKEN = "Bot_Token_gir"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")







class Downloads:
    def __init__(self, link):
        self.link = link
    def thomas(self):
        options = {
            "format": "mp4/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "noplaylist": True,
        }
        with YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(self.link, download=True)
            filename = ydl.prepare_filename(info_dict)

        filesize = os.path.getsize(filename) if os.path.exists(filename) else None

        return {
            "status": True,
            "s": filename.replace("\\", "/"),
            "title": info_dict.get("title", "video"),
            "filesize": f"{filesize / (1024*1024):.2f} MB" if filesize else "Unknown"
        }


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎥 <b>Merhaba! Hoşgeldin ☺️ -İndirmek için video bağlantısı gönder:</b>")



@bot.message_handler(func=lambda m: m.text and (m.text.startswith("http://") or m.text.startswith("https://")))
def download_video(message):
    link = message.text.strip()
    bot.reply_to(message, "⏳ <i>Video indiriliyor, lütfen bekle...</i>")

    try:
        dl = Downloads(link)
        result = dl.thomas()
        if result["status"]:
            caption = (
    f"🎥 <b>Video Linki:</b> {link}\n"
    f"📌 <b>Başlık:</b> {result['title']}\n"
    f"📦 <b>Boyut:</b> {result['filesize']}\n"
    f"👨‍💻 <b>Developer:</b> @thomas_python\n\n"
)

            with open(result["s"], "rb") as video:
                bot.send_video(message.chat.id, video, caption=caption)
            os.remove(result["s"])
        else:
            bot.reply_to(message, "❌ <b>Video indirilemedi.</b>")
    except Exception as e:
        bot.reply_to(message, f"⚠️ <b>Hata:</b> ")





print("Bot çalışıyor...✅")
while True:
    try:
        print("Bot çalışıyor...")
        bot.polling(non_stop=True, timeout=60)
    except Exception as e:
        print(f"{e}")
        time.sleep(3)