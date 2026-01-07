#+------------------------------------------------------+
#| Dev  : -thomas                               |
#| Telegram : t.me/t5omasr                 |
#| Kanal :  t.me/ThomasHack        |
#+------------------------------------------------------+

import telebot
import yt_dlp
import os
import time 

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
bot = telebot.TeleBot(TOKEN)



kanal_id = "@alnaseerh"
grup_id = "@rwssiasohbet"




@bot.message_handler(commands=['start'])
def start(message):
    try:
        kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
        grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
    except Exception as e:
        bot.reply_to(message, "Hata oluştu: Kanal veya Grup bulunamadı.")
        return

    if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
        mesaj = f"*Merhaba* 🥰 {message.from_user.first_name},\n\n*Beni kullanabilmek için  Aşağıdaki kanal ve gruba katılmalısın😊*"
        kanala_katil = telebot.types.InlineKeyboardButton("𝐊𝐚𝐧𝐚𝐥𝐚 𝐊𝐚𝐭ı𝐥", url="https://t.me/alnaseerh")
        gruba_katil = telebot.types.InlineKeyboardButton("𝐆𝐫𝐮𝐛𝐚 𝐊𝐚𝐭ı𝐥", url="https://t.me/rwssiasohbet")
        butonlar = telebot.types.InlineKeyboardMarkup(row_width=2)
        butonlar.add(kanala_katil, gruba_katil)
        photo_url = 'https://t.me/iskocyalog/5964'
        bot.send_photo(message.chat.id, photo=photo_url, caption=mesaj, reply_markup=butonlar,parse_mode="Markdown")
    else:
        photo_url = ''
        mesaj = ("*Merhaba*🎀\n\n"
                 "*Ben Bir Muzik Botuyum Beni kullanmaya başlayabilirsin.*\n"
       
                 "*En güncel haberler için @https://t.me/alnaseerh kanalında kal!*")
        butonlar = telebot.types.InlineKeyboardMarkup()
        gruba_ekle = telebot.types.InlineKeyboardButton("➕ 𝐁𝐞𝐧𝐢 𝐆𝐫𝐮𝐛𝐚 𝐄𝐤𝐥𝐞", url="https://t.me/kendimizebot?startgroup=CallToneBot")
        iletisim = telebot.types.InlineKeyboardButton("⛧ 𝐓𝐡𝐨𝐦𝐚𝐬 ⛧", url="https://t.me/t5omasr")
        muzik_indir = telebot.types.InlineKeyboardButton("𝐌𝐮𝐳𝐢𝐤 𝐈𝐧𝐝𝐢𝐫 🎧", callback_data="muzik_indir")
        butonlar.row(iletisim, gruba_ekle)
        butonlar.add(muzik_indir)
        bot.send_photo(message.chat.id, photo=photo_url, caption=mesaj, parse_mode="Markdown", reply_markup=butonlar)









@bot.callback_query_handler(func=lambda call: call.data == "muzik_indir")
def muzik_indirme_mesaji(call):
    bot.send_message(call.message.chat.id, "*🎵 Şarkı indirmek için örnek kullanım*\n\n`/indir Sezen Aksu - Tükeneceğiz`", parse_mode="Markdown")
last_run = {}
@bot.message_handler(commands=['indir'])
def indir(message):
    user_id = message.from_user.id
    now = time.time()
    if user_id in last_run and now - last_run[user_id] < 20:
        yarak = int(20 - (now - last_run[user_id]))
        bot.send_message(
            message.chat.id,
            f"*Lütfen tekrar denemeden önce {yarak} saniye bekleyin.*",
            parse_mode="Markdown"
        )
        return

   
    last_run[user_id] = now

    sarki_adi = " ".join(message.text.split()[1:])
    if not sarki_adi:
        bot.send_message(message.chat.id, "*Örnek kullanım:* `/indir Sezen Aksu - Tükeneceğiz`", parse_mode="Markdown")
        return

    bot.send_message(message.chat.id, "*🔍 Şarkı aranıyor, indiriliyor...*", parse_mode="Markdown")
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{sarki_adi}.webm',
            'noplaylist': True,
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{sarki_adi}", download=True)
            if 'entries' in info:
                info = info['entries'][0]
            dosya_adi = ydl.prepare_filename(info)
        total_seconds = info.get('duration', 0)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        sure_str = f"⌛ Zaman : {minutes} dakika {seconds} saniye"
        sanatci = info.get('uploader', 'Bilinmeyen Sanatçı')
        baslik = info.get('title', 'Bilinmeyen Şarkı')

        caption = (
            f"🎶 *{baslik}*\n"
            f"🥷🏻 *Sanatçı:* *{sanatci}*\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"*{sure_str}*\n\n"
            f"*Telegram:* @cekmem / @sabikasizim"
        )

        with open(dosya_adi, 'rb') as audio:
            bot.send_audio(
                message.chat.id,
                audio,
                caption=caption,
                parse_mode="Markdown"
            )
        os.remove(dosya_adi)

    except Exception as e:
        bot.send_message(message.chat.id, "h")
        
        
        
while True:
    try:
        print("Bot çalışıyor...")
        bot.polling(non_stop=True, timeout=60)
    except Exception as e:
        print(f"{e}")
        time.sleep(3)