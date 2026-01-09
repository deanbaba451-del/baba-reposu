from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen import File
import os
import subprocess

WAIT_MP3, WAIT_TITLE, WAIT_ARTIST = range(3)

TOKEN = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 MP3 veya ses dosyasını gönder")
    return WAIT_MP3

async def get_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    audio = update.message.audio or update.message.voice
    if not audio:
        await update.message.reply_text("⚠️ Lütfen bir ses dosyası gönderin.")
        return WAIT_MP3

    file = await audio.get_file()
    original_path = f"{audio.file_id}_original"
    await file.download_to_drive(original_path)

    # Dosyayı MP3'e çevir
    path = f"{audio.file_id}.mp3"
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", original_path, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        await update.message.reply_text("⚠️ Dosya MP3'e çevrilemedi. Lütfen geçerli bir ses dosyası gönderin.")
        os.remove(original_path)
        return WAIT_MP3

    os.remove(original_path)
    context.user_data["mp3_path"] = path
    await update.message.reply_text("✏️ Yeni şarkı adını yaz")
    return WAIT_TITLE

async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text
    await update.message.reply_text("👤 Yeni sanatçı adını yaz")
    return WAIT_ARTIST

async def get_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    artist = update.message.text
    path = context.user_data["mp3_path"]

    # Dosya MP3 ve açılabilir mi kontrol et
    audio_file = File(path)
    if audio_file is None:
        await update.message.reply_text("⚠️ Dosya MP3 değil veya bozuk.")
        os.remove(path)
        return ConversationHandler.END

    # ID3 tag yoksa oluştur
    try:
        audio = EasyID3(path)
    except ID3NoHeaderError:
        ID3().save(path)
        audio = EasyID3(path)

    audio["title"] = context.user_data["title"]
    audio["artist"] = artist
    audio.save()

    await update.message.reply_audio(
        audio=open(path, "rb"),
        caption="✅ Şarkı bilgileri değiştirildi"
    )

    os.remove(path)
    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        WAIT_MP3: [MessageHandler(filters.AUDIO | filters.VOICE, get_mp3)],
        WAIT_TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_title)],
        WAIT_ARTIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_artist)],
    },
    fallbacks=[]
)

app.add_handler(conv)
app.run_polling()