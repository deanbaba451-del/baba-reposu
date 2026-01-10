import telebot
import requests
import ssl
import socket
from urllib.parse import urlparse

TOKEN = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"
bot = telebot.TeleBot(TOKEN)

def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
        info = f"📜 SSL Sertifika Bilgileri:\n"
        info += f"• Yayınlayan: {cert.get('issuer')}\n"
        info += f"• Geçerlilik Başlangıç: {cert['notBefore']}\n"
        info += f"• Geçerlilik Bitiş: {cert['notAfter']}\n"
        return info
    except:
        return "❌ SSL bilgisi alınamadı (HTTPS olmayabilir)."
def fetch_headers(url):
    try:
        r = requests.get(url, timeout=6, allow_redirects=True)
        headers_text = "🔍 Site Headers Bilgisi\n"
        headers_text += f"URL: `{r.url}`\n"
        headers_text += f"📡 Status Code: {r.status_code}\n\n"
        headers_text += "Headers:\n"
        for key, value in r.headers.items():
            headers_text += f"• *{key}:* `{value}`\n"
        if r.cookies:
            headers_text += "\n Cookies:;\n"
            for cookie in r.cookies:
                headers_text += f"• {cookie.name} = {cookie.value}\n"
        parsed = urlparse(url)
        domain = parsed.hostname
        if parsed.scheme == "https":
            headers_text += "\n" + get_ssl_info(domain)
        return headers_text
    except Exception as e:
        return f"❌ Bir hata oluştu:\n`{e}`"
@bot.message_handler(commands=['start'])
def start_cmd(message):
    text = (
        "Hoş geldin\n\n"
        "Bu bot sana gönderdiğin herhangi bir sitenin tüm headersi çekrr "
        "bilgilerini getirir.\n\n"
        " Kullanım:\n"
        "`/headers https://pornohub.com`\n\n"
        "Hazırsan bir site atabilirsin"
    )
    bot.reply_to(message, text, parse_mode="Markdown")
@bot.message_handler(commands=['headers'])
def get_headers(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.reply_to(message, "❗ Kullanım:\n/headers https://site.com")
            return
        url = parts[1].strip()
        if not url.startswith("http"):
            url = "https://" + url
        bot.reply_to(message, "⏳ Bilgiler getiriliyor...")
        result = fetch_headers(url)
        bot.send_message(message.chat.id, result, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f" Hata: `{e}`")

print("Bot Pasif")
bot.infinity_polling()
