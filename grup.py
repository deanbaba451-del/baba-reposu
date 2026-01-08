import telebot
from telebot import types
import logging
import time
import json
import os

logging.basicConfig(level=logging.INFO)
Sihal = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"  # BURAYA TOKENİNİ YAZ
bot = telebot.TeleBot(Sihal, parse_mode="HTML")

APPROVED_FILE = "approved_users.json"

def load_approved():
    if os.path.exists(APPROVED_FILE):
        with open(APPROVED_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
def save_approved(data):
    with open(APPROVED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
approved_users = load_approved()
def get_user_mention(user):
    return f"@{user.username}" if user.username else f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
def is_creator(message):
    try:
        return bot.get_chat_member(message.chat.id, message.from_user.id).status == "creator"
    except:
        return False
def main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("Bilgi", callback_data="info"),
        types.InlineKeyboardButton("Yardım", callback_data="help")
    )
    markup.add(types.InlineKeyboardButton("Komutlar", callback_data="commands"))
    markup.add(types.InlineKeyboardButton("Gruba Ekle", url=f"https://t.me/{bot.get_me().username}?startgroup=0"))
    return markup
def back_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Geri", callback_data="back"))
    return markup
@bot.message_handler(commands=['start'])
def start_command(message):
    if message.chat.type != "private":
        return
    bot.send_message(
        message.chat.id,
        "<b>Merhaba! Ben Gelişmiş Grup Koruma Botuyum</b>\n\n"
        "Sticker ve mesaj düzenlemeleri yasaktır.\n"
        "Sadece grup kurucusu kullanıcılara izin verebilir.",
        reply_markup=main_menu_markup()
    )
@bot.callback_query_handler(func=lambda call: True)
def button_callback(call):
    if call.message.chat.type != "private":
        return

    try:
        if call.data == "back":
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="<b>Merhaba! Ben Gelişmiş Grup Koruma Botuyum</b>\n\n"
                     "Sticker ve mesaj düzenlemeleri yasaktır.\n"
                     "Sadece grup kurucusu kullanıcılara izin verebilir.",
                reply_markup=main_menu_markup()
            )
            return
        texts = {
            "info": "<b>Bilgi</b>\n\n"
                    "• Sticker atmak ve mesaj düzenlemek yasaktır\n"
                    "• Bu eylemler otomatik silinir\n"
                    "• Her silme işleminde adminlere bildirim gider\n"
                    "• Sadece grup kurucusu /approve ile izin verebilir",

            "help": "<b>Yardım</b>\n\n"
                    "Botu gruba ekle → <b>Mesajları Sil</b> yetkisi ver\n"
                    "→ Otomatik koruma başlar!\n\n"
                    "İzin vermek için bir mesaja yanıt verip /approve yaz",

            "commands": "<b>Komutlar (Sadece Kurucu)</b>\n\n"
                        "/approve → Yanıt verilen kişiye izin ver\n"
                        "/unapprove → İzni kaldır\n"
                        "/approved → Onaylı kullanıcıları listeler"
        }
        text = texts.get(call.data, "Bilinmeyen komut.")
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=text,
            reply_markup=back_markup()
        )
    except Exception as e:
        logging.error(f"Callback hatası: {e}")
@bot.message_handler(commands=['approve', 'unapprove', 'approved'])
def admin_commands(message):
    if message.chat.type == "private": return
    if not is_creator(message):
        bot.reply_to(message, "Bu komutları sadece grup kurucusu kullanabilir.")
        return
    chat_id = str(message.chat.id)
    if message.text.startswith("/approve"):
        if not message.reply_to_message:
            return bot.reply_to(message, "Bir mesaja yanıt vererek kullanın.")
        target = message.reply_to_message.from_user
        if chat_id not in approved_users:
            approved_users[chat_id] = []
        if target.id not in approved_users[chat_id]:
            approved_users[chat_id].append(target.id)
            save_approved(approved_users)
            bot.reply_to(message, f"{get_user_mention(target)} artık serbest!")
        else:
            bot.reply_to(message, f"{get_user_mention(target)} zaten onaylı.")
    elif message.text.startswith("/unapprove"):
        if not message.reply_to_message:
            return bot.reply_to(message, "Bir mesaja yanıt vererek kullanın.")
        target = message.reply_to_message.from_user
        if chat_id in approved_users and target.id in approved_users[chat_id]:
            approved_users[chat_id].remove(target.id)
            if not approved_users[chat_id]: 
                approved_users.pop(chat_id, None)
            save_approved(approved_users)
            bot.reply_to(message, f"{get_user_mention(target)} izni kaldırıldı.")
        else:
            bot.reply_to(message, f"{get_user_mention(target)} zaten onaylı değil.")

    elif message.text.startswith("/approved"):
        if chat_id not in approved_users or not approved_users[chat_id]:
            return bot.reply_to(message, "Onaylı kullanıcı yok.")
        text = "<b>Onaylı Kullanıcılar:</b>\n\n"
        for uid in approved_users[chat_id]:
            try:
                user = bot.get_chat_member(message.chat.id, uid).user
                text += f"• {get_user_mention(user)}\n"
            except:
                text += f"• <code>{uid}</code> (hesap silinmiş)\n"
        bot.reply_to(message, text)
@bot.message_handler(content_types=['sticker'])
def sticker_delete(message):
    if message.chat.type == "private": return
    chat_id = str(message.chat.id)
    if chat_id in approved_users and message.from_user.id in approved_users[chat_id]:
        return
    delete_and_notify(message, "sticker attığı")
#@BenAtaniz Mavi için yazdığım kod
@bot.edited_message_handler(func=lambda m: True)
def edit_delete(message):
    if message.chat.type == "private": return
    chat_id = str(message.chat.id)
    if chat_id in approved_users and message.from_user.id in approved_users[chat_id]:
        return
    delete_and_notify(message, "mesaj düzenlediği")

def delete_and_notify(message, reason):
    try:
        if not bot.get_chat_member(message.chat.id, bot.get_me().id).can_delete_messages:
            return
        bot.delete_message(message.chat.id, message.message_id)
        notify = (
            f"<b>Mesaj Silindi!</b>\n\n"
            f"<b>Kullanıcı:</b> {get_user_mention(message.from_user)}\n"
            f"<b>ID:</b> <code>{message.from_user.id}</code>\n"
            f"<b>Neden:</b> {reason} için\n"
            f"<b>Grup:</b> {message.chat.title}\n"
            f"<b>Zaman:</b> {time.strftime('%d.%m.%Y %H:%M')}"
        )
        for admin in bot.get_chat_administrators(message.chat.id):
            try:
                bot.send_message(admin.user.id, notify, disable_web_page_preview=True)
            except:
                pass
    except Exception as e:
        logging.error(f"Silme hatası: {e}")
if __name__ == "__main__":
    print("BOT PASİF")
    while True:
        try:
            bot.infinity_polling(none_stop=True)
        except Exception as e:
            print("Bağlantı koptu onu beklediğin gibi bağlantının gelmesinide bekle", e)
            time.sleep(5)