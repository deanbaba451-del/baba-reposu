import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests, json, os, time

Seviyordum = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
Kanal = "https://t.me/kafirIerorgut"
Kendin = "https://t.me/cekmem"
bot = telebot.TeleBot(Seviyordum)
def sihol(girdi):
    girdi = girdi.replace(",", " ")
    return [d.strip() for d in girdi.split() if d.strip()]
def sihal(current, total, size=10):
    dolu = int(size * current / total)
    bos = size - dolu
    return "█" * dolu + "░" * bos
def miyaba(domain):
    url = f"https://free.zirveexec.com/api_public.php?site={domain}"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    try:
        data = r.json()
        is_json = True
        count = len(data) if isinstance(data, list) else 1
    except json.JSONDecodeError:
        data = r.text
        is_json = False
        count = data.count("\n") + 1 if data.strip() else 0

    dosya = f"{domain}.txt"
    with open(dosya, "w", encoding="utf-8") as f:
        f.write(f"Site: {domain}\n")
        f.write(f"Kayıt Sayısı: {count}\n")
        f.write(f"Format: {'JSON' if is_json else 'TEXT'}\n")
        f.write("-" * 40 + "\n")
        f.write(json.dumps(data, indent=2, ensure_ascii=False) if is_json else data)
    return dosya, count
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_chat_action(m.chat.id, "typing")
    time.sleep(1)

    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("📢 Kanal", url=Kanal),
        InlineKeyboardButton("👨‍💻 Dev", url=Kendin)
    )
    bot.send_message(
        m.chat.id,
        f"👋 Hoş geldin *{m.from_user.first_name}*\n\n"
        "🔍 Domain log botu\n\n"
        "📌 Kullanım:\n"
        "`/bul exxen.com`\n"
        "`/bul neftlix.com,blutv.com`",
        parse_mode="Markdown",
        reply_markup=kb
    )
@bot.message_handler(commands=["bul"])
def bul(m):
    args = m.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(m, "❌ Kullanım:\n/bul neftlix.com")
        return
    domainler = sihol(args[1])
    toplam = len(domainler)
    durum = bot.send_message(
        m.chat.id,
        f"⏳ İşleniyor...\n{sihal(0, toplam)} 0/{toplam}",
    )
    for i, domain in enumerate(domainler, start=1):
        bot.edit_message_text(
            f"🔄 `{domain}`\n{sihal(i, toplam)} {i}/{toplam}",
            m.chat.id,
            durum.message_id,
            parse_mode="Markdown"
        )
        try:
            dosya, count = miyaba(domain)
            bot.send_chat_action(m.chat.id, "upload_document")
            bot.send_document(
                m.chat.id,
                open(dosya, "rb"),
                caption=f"✅ `{domain}`\n📊 Kayıt: `{count}` \n Dev: @SihalBen",
                parse_mode="Markdown"
            )
            os.remove(dosya)
        except Exception as e:
            bot.send_message(
                m.chat.id,
                f"❌ `{domain}`\nHatanı: `{e}`",
                parse_mode="Markdown"
            )
    bot.edit_message_text(
        "✅ Tüm domainler hazır knk",
        m.chat.id,
        durum.message_id
    )
print("🤖 Bot aktif...")
bot.infinity_polling()
