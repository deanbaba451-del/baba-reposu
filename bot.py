from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
from moviepy.editor import VideoFileClip
import os

WAIT_FILE, WAIT_TITLE, WAIT_ARTIST, WAIT_COVER = range(4)

TOKEN = "BOT_TOKEN_BURAYA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 MP3 veya Video gönder\n\n"
        "Video gönderirsen MP3'e çevrilir."
    )
    return WAIT_FILE

async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        video = update.message.video
        file = await video.get_file()
        video_path = f"{video.file_id}.mp4"
        audio_path = f"{video.file_id}.mp3"
        await file.download_to_drive(video_path)

        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path)
        clip.close()

        os.remove(video_path)
        context.user_data["audio_path"] = audio_path

    elif update.message.audio:
        audio = update.message.audio
        file = await audio.get_file()
        audio_path = f"{audio.file_id}.mp3"
        await file.download_to_drive(audio_path)
        context.user_data["audio_path"] = audio_path

    else:
        await update.message.reply_text("❌ MP3 veya Video gönder")
        return WAIT_FILE

    await update.message.reply_text("✏️ Şarkı adını yaz")
    return WAIT_TITLE

async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text
    await update.message.reply_text("👤 Sanatçı adını yaz")
    return WAIT_ARTIST

async def get_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["artist"] = update.message.text
    await update.message.reply_text(
        "🖼 Kapak foto gönder\n"
        "Ya da /skip yaz"
    )
    return WAIT_COVER

async def skip_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_audio(update, context)
    return ConversationHandler.END

async def get_cover(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    cover_path = f"{photo.file_id}.jpg"
    await file.download_to_drive(cover_path)
    context.user_data["cover"] = cover_path

    await process_audio(update, context)
    return ConversationHandler.END

async def process_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = context.user_data["audio_path"]

    audio = EasyID3(path)
    audio["title"] = context.user_data["title"]
    audio["artist"] = context.user_data["artist"]
    audio.save()

    if "cover" in context.user_data:
        id3 = ID3(path)
        with open(context.user_data["cover"], "rb") as img:
            id3.add(
                APIC(
                    encoding=3,
                    mime="image/jpeg",
                    type=3,
                    desc="Cover",
                    data=img.read()
                )
            )
        id3.save()
        os.remove(context.user_data["cover"])

    await update.message.reply_audio(
        audio=open(path, "rb"),
        caption="✅ MP3 hazır\nMetadata + Kapak eklendi"
    )

    os.remove(path)

app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        WAIT_FILE: [
            MessageHandler(filters.AUDIO | filters.VIDEO, get_file)
        ],
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