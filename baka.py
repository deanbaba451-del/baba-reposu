from telegram import Update, InputFile
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)
import eyed3

ASK_MP3, ASK_TITLE, ASK_ARTIST, ASK_COVER = range(4)
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! MP3 dosyanı gönder.")
    return ASK_MP3

async def ask_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.audio.get_file()
    await file.download_to_drive(f"{update.message.chat_id}.mp3")
    user_data[update.message.chat_id] = {"file": f"{update.message.chat_id}.mp3"}
    await update.message.reply_text("Şarkı ismi ne olsun?")
    return ASK_TITLE

async def ask_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data[update.message.chat_id]["title"] = update.message.text
    await update.message.reply_text("Sanatçı ismi ne olsun?")
    return ASK_ARTIST

async def ask_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data[update.message.chat_id]["artist"] = update.message.text
    await update.message.reply_text("Kapak fotoğrafını gönder.")
    return ASK_COVER

async def process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = await update.message.photo[-1].get_file()
    await photo.download_to_drive(f"{update.message.chat_id}_cover.jpg")

    data = user_data[update.message.chat_id]

    audiofile = eyed3.load(data["file"])
    if audiofile.tag is None:
        audiofile.initTag()

    audiofile.tag.title = data["title"]
    audiofile.tag.artist = data["artist"]
    with open(f"{update.message.chat_id}_cover.jpg", "rb") as img:
        audiofile.tag.images.set(3, img.read(), "image/jpeg")

    audiofile.tag.save()

    await update.message.reply_audio(audio=open(data["file"], "rb"))
    await update.message.reply_text("İşlem tamam! /new ile yeniden başlayabilirsin.")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("İşlem iptal edildi.")
    return ConversationHandler.END

app = ApplicationBuilder().token("8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik").build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        ASK_MP3: [MessageHandler(filters.AUDIO, ask_title)],
        ASK_TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_artist)],
        ASK_ARTIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_cover)],
        ASK_COVER: [MessageHandler(filters.PHOTO, process)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

app.add_handler(conv_handler)
app.run_polling()