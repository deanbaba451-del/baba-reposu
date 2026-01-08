from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)
from mutagen.easyid3 import EasyID3
import os

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
FORCE_GROUP = "@rwssiasohbet"

WAIT_MP3, WAIT_TITLE, WAIT_ARTIST = range(3)

# 👇 KATILIM KONTROL
async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(FORCE_GROUP, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_join(update, context):
        await update.message.reply_text(
            "❌ Botu kullanmak için grubumuza katılmalısın!\n\n"
            "👉 @rwssiasohbet"
        )
        return ConversationHandler.END

    await update.message.reply_text("🎵 MP3 dosyasını gönder")
    return WAIT_MP3

async def get_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    audio = update.message.audio
    file = await audio.get_file()
    path = f"{audio.file_id}.mp3"
    await file.download_to_drive(path)

    context.user_data["mp3"] = path
    await update.message.reply_text("✏️ Şarkı adını yaz")
    return WAIT_TITLE

async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text
    await update.message.reply_text("👤 Sanatçı adını yaz")
    return WAIT_ARTIST

async def get_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = context.user_data["mp3"]

    audio = EasyID3(path)
    audio["title"] = context.user_data["title"]
    audio["artist"] = update.message.text
    audio.save()

    await update.message.reply_audio(
        audio=open(path, "rb"),
        caption="✅ Hazır"
    )

    os.remove(path)
    return ConversationHandler.END

# 🎯 /tmm KOMUTU
async def tmm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_join(update, context):
        await update.message.reply_text(
            "❌ Önce grubumuza katıl!\n👉 @rwssiasohbet"
        )
        return

    if not context.args:
        await update.message.reply_text("🎵 Şarkı ismini yaz\nÖrnek: /tmm Sezen Aksu")
        return

    song_name = " ".join(context.args)

    # ÖRNEK DOSYA (kendin değiştir)
    file_path = "hazir.mp3"

    audio = EasyID3(file_path)
    audio["title"] = song_name
    audio["artist"] = "RWSSIA"
    audio.save()

    await update.message.reply_audio(
        audio=open(file_path, "rb"),
        caption=f"🎶 {song_name}"
    )

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
app.add_handler(CommandHandler("tmm", tmm))

app.run_polling()