import telebot
import os
import yt_dlp
import requests
from urllib.parse import quote

SAHAL = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
bot = telebot.TeleBot(SAHAL, parse_mode="Markdown")
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "Ben senin şarkı indirme botun isim belirle\n\n"
        "Kullanım örneği:\n"
        "`/indir Tarkan Dudu`\n"
        "`/indir https://youtu.be/link`\n\n"
        "Format: `.m4a ve ya ffmpeg yüklü değilse .webm ile atar`"
    )

@bot.message_handler(commands=['indir'])
def indir(msg):
    try:
        args = msg.text.split(' ', 1)
        if len(args) < 2:
            bot.reply_to(msg, "Lütfen şarkı adını veya YouTube bağlantısını yaz.\n\nÖrnek: `/indir Hadise Feryat`")
            return
        sorgu = args[1].strip()
        durum = bot.send_message(msg.chat.id, "🔍 Şarkı aranıyor, lütfen bekle...")
        if "youtube.com" in sorgu or "youtu.be" in sorgu:
            url = sorgu
        else:
            url = youtube_ara(sorgu)
        if not url:
            bot.edit_message_text("Şarkı bulunamadı, başka bir isim dene.", msg.chat.id, durum.message_id)
            return
        bot.edit_message_text("🎧 Şarkı indiriliyor...", msg.chat.id, durum.message_id)
        try:
            ydl_opts = {
                'format': 'bestaudio[ext=m4a]',
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                dosya_adi = ydl.prepare_filename(info)
        except Exception:
            
            ydl_opts = {
                'format': 'bestaudio',
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                dosya_adi = ydl.prepare_filename(info)

        baslik = info.get("title", "Bilinmeyen Şarkı")
        sanatci = info.get("uploader", "Bilinmeyen")
        sure = info.get("duration", 0)
        thumbnail = info.get("thumbnail")
        caption = (
            f"🎵 *{baslik}*\n"
            f"👤 *Sanatçı:* {sanatci}\n"
            f"⏱ *Süre:* {int(sure//60)}:{int(sure%60):02d}\n"
            f"💽 Format: `.m4a`\n"
            f"🔗 [YouTube'da Aç]({url})"
        )
        bot.edit_message_text(f"✅ {baslik} indirildi, gönderiliyor...", msg.chat.id, durum.message_id)
#karımı seviyorum
        thumb_path = None
        if thumbnail:
            try:
                thumb_data = requests.get(thumbnail).content
                thumb_path = f"{baslik}.jpg"
                with open(thumb_path, "wb") as f:
                    f.write(thumb_data)
            except:
                thumb_path = None

        with open(dosya_adi, "rb") as sarki:
            bot.send_audio(
                msg.chat.id,
                sarki,
                caption=caption,
                title=baslik,
                performer=sanatci,
                thumb=open(thumb_path, "rb") if thumb_path else None
            )
        os.remove(dosya_adi)
        if thumb_path and os.path.exists(thumb_path):
            os.remove(thumb_path)
        bot.send_message(msg.chat.id, "✅ Şarkı başarıyla gönderildi!")
    except Exception as e:
        bot.send_message(msg.chat.id, f" Bir hata oluştu:\n`{e}`") #Sahal

def youtube_ara(sorgu):
    try:
        q = quote(sorgu)
        html = requests.get(f"https://www.youtube.com/results?search_query={q}", timeout=10).text
        idx = html.find("/watch?v=")
        if idx != -1:
            video_id = html[idx:idx+20]
            return "https://www.youtube.com" + video_id
    except:
        pass
    return None

bot.infinity_polling()
