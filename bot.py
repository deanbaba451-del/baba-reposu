from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)
from mutagen.easyid3 import EasyID3
import os

TOKEN = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"
LOG_CHANNEL = "@cokonemlibirkanal"

WAIT_FILE, WAIT_TITLE, WAIT_ARTIST = range(3)

# ───── START ─────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 MP3 gönder\n"
        "✏️ Şarkı adı ve sanatçı ayarlanır\n"
        "🖼 Kapak fotoğraf kullanılmayacak"
    )
    return WAIT_FILE

# ───── FILE ─────
async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.audio:
        audio = update.message.audio
        file = await audio.get_file()
        audio_path = f"{audio.file_id}.mp3"
        await file.download_to_drive(audio_path)
        context.user_data["audio"] = audio_path
    else:
        await update.message.reply_text("❌ MP3 gönder")
        return WAIT_FILE

    await update.message.reply_text("✏️ Şarkı adını yaz")
    return WAIT_TITLE

# ───── TITLE ─────
async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text
    await update.message.reply_text("👤 Sanatçı adını yaz")
    return WAIT_ARTIST

# ───── ARTIST ─────
async def get_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["artist"] = update.message.text
    await finalize(update, context)
    return ConversationHandler.END

# ───── FINAL ─────
async def finalize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = context.user_data["audio"]

    audio = EasyID3(path)
    audio["title"] = context.user_data["title"]
    audio["artist"] = context.user_data["artist"]
    audio.save()

    await update.message.reply_audio(
        audio=open(path, "rb"),
        caption="✅ MP3 hazır"
    )

    # 📜 LOG
    await context.bot.send_message(
        LOG_CHANNEL,
        f"🎵 Yeni işlem\n"
        f"👤 {update.effective_user.username}\n"
        f"🎶 {context.user_data['title']} - {context.user_data['artist']}"
    )

    os.remove(path)

# ───── APP ─────
app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        WAIT_FILE: [MessageHandler(filters.AUDIO, get_file)],
        WAIT_TITLE: [MessageHandler(filters.TEXT, get_title)],
        WAIT_ARTIST: [MessageHandler(filters.TEXT, get_artist)],
    },
    fallbacks=[]
)

app.add_handler(conv)
app.run_polling()