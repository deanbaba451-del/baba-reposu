from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
import eyed3
import os

# Durumlar
ASK_MP3, ASK_TITLE, ASK_ARTIST, ASK_COVER = range(4)
user_data = {}

# /start veya /new
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! MP3 dosyanı gönder.")
    return ASK_MP3

# MP3 alındı
async def ask_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.audio.get_file()
    mp3_path = f"{update.message.chat_id}.mp3"
    await file.download_to_drive(mp3_path)
    user_data[update.message.chat_id] = {"file": mp3_path}
    await update.message.reply_text("Şarkı ismi ne olsun?")
    return ASK_TITLE

# Şarkı ismi alındı
async def ask_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data[update.message.chat_id]["title"] = update.message.text
    await update.message.reply_text("Sanatçı ismi ne olsun?")
    return ASK_ARTIST

# Sanatçı ismi alındı
async def ask_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data[update.message.chat_id]["artist"] = update.message.text
    await update.message.reply_text("Kapak fotoğrafını gönder veya /skip yap.")
    return ASK_COVER

# Kapak foto veya skip alındı
async def process_cover(update: Update, context: ContextTypes.DEFAULT_TYPE, skip=False):
    chat_id = update.message.chat_id
    data = user_data[chat_id]
    mp3_path = data["file"]

    audiofile = eyed3.load(mp3_path)
    if audiofile is None:
        await update.message.reply_text("Dosya yüklenemedi. Lütfen tekrar gönder.")
        return ConversationHandler.END
    if audiofile.tag is None:
        audiofile.initTag()

    audiofile.tag.title = data["title"]
    audiofile.tag.artist = data["artist"]

    # Eğer foto gönderilmiş ve skip yapılmamışsa kapak ekle
    if not skip and update.message.photo:
        photo = await update.message.photo[-1].get_file()
        cover_path = f"{chat_id}_cover.jpg"
        await photo.download_to_drive(cover_path)
        with open(cover_path, "rb") as img:
            audiofile.tag.images.set(3, img.read(), "image/jpeg")
        os.remove(cover_path)

    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    await update.message.reply_audio(audio=open(mp3_path, "rb"))
    await update.message.reply_text("İşlem tamam! /new ile yeniden başlayabilirsin.")
    return ConversationHandler.END

# /skip komutu
async def skip_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kapak fotoğrafı atlandı.")
    return await process_cover(update, context, skip=True)

# /cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("İşlem iptal edildi.")
    return ConversationHandler.END

# Bot kurulumu
app = ApplicationBuilder().token("8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik").build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler(['start','new'], start)],
    states={
        ASK_MP3: [MessageHandler(filters.AUDIO, ask_title)],
        ASK_TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_artist)],
        ASK_ARTIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_cover)],
        ASK_COVER: [
            MessageHandler(filters.PHOTO, process_cover),
            CommandHandler('skip', skip_cover)
        ],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

app.add_handler(conv_handler)
app.run_polling()