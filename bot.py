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
import os

WAIT_MP3, WAIT_TITLE, WAIT_ARTIST = range(3)

TOKEN = "BOT_TOKEN_BURAYA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 MP3 dosyasını gönder")
    return WAIT_MP3

async def get_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    audio = update.message.audio
    file = await audio.get_file()
    path = f"{audio.file_id}.mp3"
    await file.download_to_drive(path)

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

    audio = EasyID3(path)
    audio["title"] = context.user_data["title"]
    audio["artist"] = artist
    audio.save()

    await update.message.reply_audio(
        audio=open(path, "rb"),
        caption="✅ değiştirildi"
    )

    os.remove(path)
    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        WAIT_MP3: [MessageHandler(filters.AUDIO, get_mp3)],
        WAIT_TITLE: [MessageHandler(filters.TEXT, get_title)],
        WAIT_ARTIST: [MessageHandler(filters.TEXT, get_artist)],
    },
    fallbacks=[]
)

app.add_handler(conv)
app.run_polling()