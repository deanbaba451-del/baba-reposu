import os
import telebot
from yt_dlp import YoutubeDL
import threading
import time
from queue import Queue

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"  # Bot token
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 5309382811  # Admin ID

download_queue = Queue()
queue_position = 1
completed_downloads = 0
user_requests = {}
banned_users = set()

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 1)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        percent = int(downloaded_bytes / total_bytes * 100) if total_bytes > 0 else 0
        if percent % 10 == 0:
            print(f"İndirme ilerlemesi: %{percent}")

def search_and_send_music(message, query, message_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch10',  # Güncellenmiş ytsearch kullanımı
        'max_downloads': 1,
        'progress_hooks': [progress_hook],
        'outtmpl': '%(title)s.%(ext)s',
        'concurrent_fragment_downloads': 1
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(f"ytsearch:{query}", download=False)
            if 'entries' in info_dict and info_dict['entries']:
                video_info = info_dict['entries'][0]
                video_url = video_info['webpage_url']
                video_title = video_info['title']
                safe_title = "".join(x for x in video_title if x.isalnum() or x in (" ", "_", "-")).rstrip()
                file_path = f"{safe_title}.mp3"
                
                download_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': file_path,
                    'noplaylist': True,
                    'concurrent_fragment_downloads': 1
                }
                
                with YoutubeDL(download_opts) as ydl_download:
                    ydl_download.download([video_url])
                
                with open(file_path, 'rb') as media:
                    bot.send_audio(message.chat.id, media, caption=f"Yapımcı: @woxy1446 Şarkı indirildi: {video_title}")
                os.remove(file_path)
                bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text="İndirme tamamlandı!")
            else:
                bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text="Aranan şarkı bulunamadı.")
        except Exception as e:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=f"Bir hata oluştu: {str(e)}")

def download_music_in_process():
    global queue_position, completed_downloads
    while True:
        message, query, message_id, user_position = download_queue.get()
        bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=f"Sıra size geldi! Şarkı indiriliyor...")
        try:
            search_and_send_music(message, query, message_id)
            completed_downloads += 1
        except Exception as e:
            bot.send_message(message.chat.id, f"Bir hata oluştu: {str(e)}")
        time.sleep(1)

@bot.message_handler(commands=['indir'])
def download_music(message):
    global queue_position
    
    user_id = message.from_user.id
    username = message.from_user.username
    if user_id in banned_users:
        bot.send_message(message.chat.id, "Bu botu kullanmanız yasaklandı.")
        return
    
    query = " ".join(message.text.split()[1:])
    if not query:
        bot.send_message(message.chat.id, "Lütfen bir şarkı adı girin. Örnek: /indir şarkı adı")
        return
    
    user_requests[user_id] = user_requests.get(user_id, 0) + 1
    if user_requests[user_id] > 3:
        bot.send_message(message.chat.id, "Çok fazla istek gönderdiniz. Lütfen biraz bekleyin.")
        return
    
    sent_message = bot.send_message(message.chat.id, f"İndirme sırasına alındınız. Sıra numaranız: {queue_position}")
    download_queue.put((message, query, sent_message.message_id, queue_position))
    queue_position += 1
download_thread = threading.Thread(target=download_music_in_process, daemon=True)
download_thread.start()

bot.polling(none_stop=True)