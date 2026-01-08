from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from moviepy.editor import VideoFileClip
import os

TOKEN = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"
LOG_CHANNEL = "@cokonemlibirkanal"

WAIT_FILE, WAIT_TITLE, WAIT_ARTIST, WAIT_COVER = range(4)

# ───── START ─────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 MP3 veya Video gönder\n"
        "✏️ Şarkı adı ve sanatçı ayarlanır\n"
        "🖼 Kapak foto eklenir"
    )
    return WAIT_FILE

# ───── FILE ─────
async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        video = update.message.video
        file = await video.get_file()
        video_path = f"{video.file_id}.mp4"
        audio_path = f"{video.file_id}.mp3"
        await file.download_to_drive(video_path)

        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path, logger=None)
        clip.close()
        os.remove(video_path)

        context.user_data["audio"] = audio_path

    elif update.message.audio:
        audio = update.message.audio
        file = await audio.get_file()
        audio_path = f"{audio.file_id}.mp3"
        await file.download_to_drive(audio_path)
        context.user_data["audio"] = audio_path

    else:
        await update.message.reply_text("❌ MP3 veya Video gönder")
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
    await update.message.reply_text(
        "🖼 Kapak foto gönder\n"
        "Atlaman için /skip"
    )
    return WAIT_COVER

# ───── SKIP COVER ─────
async def skip_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await finalize(update, context)
    return ConversationHandler.END

# ───── GET COVER ─────
async def get_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    cover_path = f"{photo.file_id}.jpg"
    await file.download_to_drive(cover_path)
    context.user_data["cover"] = cover_path

    await finalize(update, context)
    return ConversationHandler.END

# ───── FINAL ─────
async def finalize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = context.user_data["audio"]

    audio = EasyID3(path)
    audio["title"] = context.user_data["title"]
    audio["artist"] = context.user_data["artist"]
    audio.save()

    # 🎨 KAPAK (DÜZELTİLDİ)
    if "cover" in context.user_data:
        id3 = ID3(path)
        with open(context.user_data["cover"], "rb") as img:
            id3.add(APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=img.read()
            ))
        id3.save()
        os.remove(context.user_data["cover"])

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
        WAIT_FILE: [MessageHandler(filters.AUDIO | filters.VIDEO, get_file)],
        WAIT_TITLE: [MessageHandler(filters.TEXT, get_title)],
        WAIT_ARTIST: [MessageHandler(filters.TEXT, get_artist)],
        WAIT_COVER: [
            CommandHandler("skip", skip_cover),
            MessageHandler(filters.PHOTO, get_cover)
        ],
    },
    fallbacks=[]
)

app.add_handler(conv)
app.run_polling()