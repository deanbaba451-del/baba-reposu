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

# Durumlar
ASK_MP3, ASK_TITLE, ASK_ARTIST = range(3)
user_data = {}

# /start veya /new
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! MP3 dosyanı gönder.")
    return ASK_MP3

# MP3 alındı
async def ask_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.audio:
        await update.message.reply_text("Lütfen bir MP3 dosyası gönder.")
        return ASK_MP3
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

# Sanatçı alındı, MP3 işleniyor
async def process_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    # Kapak tamamen kaldırıldı, sadece metadata kaydediliyor
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    await update.message.reply_audio(audio=open(mp3_path, "rb"))
    await update.message.reply_text("İşlem tamam! /new ile yeniden başlayabilirsin.")
    return ConversationHandler.END

# /cancel komutu
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
        ASK_ARTIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_audio)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

app.add_handler(conv_handler)

# Bot komutları (BotFather için)
# /start - Botu başlatır
# /new   - Yeni MP3 işleme başlatır
# /cancel- İşlemi iptal eder

app.run_polling()