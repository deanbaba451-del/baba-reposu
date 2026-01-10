port requests
import telebot
import json
from telebot import types

Sihal = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"  
bot = telebot.TeleBot(Sihal)
user_state = {}  

def instagram_reset_json(email):
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    payload = f"email_or_username={email}"
    headers = {
        'User-Agent': "Mozilla/5.0",
        'Content-Type': "application/x-www-form-urlencoded",
        'x-csrftoken': "r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc",
        'x-requested-with': "XMLHttpRequest",
        'x-ig-app-id': "936619743392459",
        'referer': "https://www.instagram.com/accounts/password/reset/",
        'Cookie': "mid=ZqPYMgABAAE1FS3FyA2mTh6D4nSn; csrftoken=r15fQwEdpDwDqwW2EkmYjOWCeyBiwQTc"
    }

    try:
        r = requests.post(url, data=payload, headers=headers, timeout=10)
        if r.status_code == 200:
            return json.dumps({
                "status": "success",
                "platform": "instagram",
                "email_or_username": email,
                "message": "Åifre sÄ±fÄ±rlama baÄlantÄ±sÄ± gÃ¶nderildi."
            }, indent=4, ensure_ascii=False)
        else:
            return json.dumps({
                "status": "error",
                "platform": "instagram",
                "email_or_username": email,
                "http_code": r.status_code,
                "error": "Instagram hata dÃ¶ndÃ¼rdÃ¼."
            }, indent=4, ensure_ascii=False)

    except Exception as e:
        return json.dumps({
            "status": "error",
            "platform": "instagram",
            "email_or_username": email,
            "error": str(e)
        }, indent=4, ensure_ascii=False)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    ig = types.InlineKeyboardButton("Instagram Åifre SÄ±fÄ±rla", callback_data="ig")
    keyboard.add(ig)
    bot.send_message(
        message.chat.id,
        "Instagram Åifre sÄ±fÄ±rlama kodu active.\n\nð BaÅlamak iÃ§in aÅaÄÄ±dan seÃ§im yap.",
        reply_markup=keyboard
    )
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "ig":
        user_state[call.from_user.id] = "instagram"
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="ð§ LÃ¼tfen e-posta veya kullanÄ±cÄ± adÄ±nÄ± yaz:"
        )# Sihal 31
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    uid = message.from_user.id
    if uid not in user_state:
        bot.send_message(message.chat.id, "â¹ï¸ BaÅlamak iÃ§in /start yaz.")
        return
    email = message.text.strip()
    bot.send_message(message.chat.id, "â³ Ä°Ålem yapÄ±lÄ±yor...")
    result_json = instagram_reset_json(email)
    bot.send_message(
        message.chat.id,
        f"```json\n{result_json}\n```",
        parse_mode="Markdown"
    )
    del user_state[uid]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Instagram Åifre SÄ±fÄ±rla", callback_data="ig"))
    bot.send_message(message.chat.id, "ð Yeni iÅlem iÃ§in:", reply_markup=keyboard)
print("Bot Pasif")
bot.infinity_polling()
