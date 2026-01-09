# -*- coding: utf-8 -*-

from telethon import TelegramClient, events
import asyncio
import random
from datetime import datetime, timedelta

api_id = 26902485
api_hash = "b97a7adcec1307292baea6117d60a64f"

client = TelegramClient("userbot_session", api_id, api_hash)

aktif = False
reply_message_id = None
reply_chat_id = None

admins = set()  # admin ID listesi
bot_messages = []  # botun attığı mesaj ID’leri

# Örnek mesaj listesi
mesajlar = [
 "o ananı götünden sikerim", "atasını siktiğim orospu evladı", "bacını götünden sikim", "o babanın kel kafasına boşalırım", "o ananın amına işer babanın kafasını koparırım", "andaval orospu evladı", "atanı yurdunu sikeyim", "avel orospu evladı", "ya sus atanı sikerim senin", "ananı sikim", "kürt orospu evladı", "babanın kafasını sikim", "babanı götünden sikeyim", "orospu evladı", "bacını sikim oç", "o yurdunu sikerim senin" "gavat orospu evladı", "sübyancı piç", "yaşıt kızlardan yüz bulamayınca küçük kızlara yönelen orospu evladı", "o ananın amına işerim senin" "babanın ağzını sikerim", "o ananın amına uçan tekme atarım", "amına koyduğumun çocuğu","o ananın amını yerle bir ederim","o bacını götünden başından sikerim biçerim içinden geçerim" "Atatürk'ünü siktiğimin çocuğu","Kürt orospu evladı dağlara taşlara çıkar ananı mağara içinde sikerim anasının amına yarrağımı sapladığımın evladı","o annenin dağını taşını toprağını gözünü kaşını şalvarini sikerim","o bacının amına bir bakış atarim namusu kayar amına koyduğumun çocuğu","anneni mahalle arasında yakalar annenin amına pandik açar evinize kaçarım orda babanın kafasına şaplağı vurup bayıltırım","murat gilin damından ananın evine atlar Anana tecavüz eder babanı bacaklarından tavana asar kafatasını keser çöpe atarım","30 kilo Zargana bacını kocagıma alır havaya atar havada amına balgam atarım ","kız kuzenini otobüs içinde taciz ederim en sevdiğim suryeli taktiği","annenin kömür gibi amına ismimi yazar profil olarak kullanırım anasının amına üçgen çizgimin evladı","annenle birlikte tekne kiralayıp tekneye bindereyim ananı","sonra o annençiğini suya atar balıkların huzurunda sikerim amına füze attığımın","dombili orospu çocuğu","bacının 36 buçuk ayaklarını sikime dayarim orospunun doğurdu","köpek kılığına girer o ananın koca götünü koklarim hoşuma gider","ananın amına 1 saniyede 30 dil darbesi atarım hayatı kayar","balkonda annenle karşılıklı oturup çay içerim anenin amı alevlenince etek altından domaltır sikerim","havada bulut sen anneni unut annen artık benimdir","25cm yarrağımı ananın boğaz borusuna sokar Annanı avrupa yakasına gönderirim","anan simsiyah amcıklı rozetini veirir anneni sevindirir götünden başından sikerim","ananın amına domates koyup salça olana kadar sikerim","ananın amına salıncak asar seni kocagıma alır sallana sallana sikerim","ananın o geniş amcığında halı saha açar halı sahada ananın amında tek başıma 2 kale top oynarım","o ananın amına beyzbol sopası sokar ananın am dudağını ısırırım","analar kutsaldır diyen kardeşini ananın üstüne koyar 2sinde sikerim kutsal mutsal kalmaz","ananın amına döl attıktan sonra sen çıktın ya ananın çiçeğine sağlık","beni tuvalette sıçarken sik diyen vizyonsuz ananın ağzına oturup simsiyah birşey atarım ","ananın ex kocasını döverken ayyy lütfen yapma diyen ananın amına bir yumruk atarım bls dövmesi yaparım ananın amına","25 cm yarrağımı annenin görünce başı küçük felan dedi ananın kafasını koparıp onunla başını boyultur bacını sikerim ahh uhh diye bacını siker öldürürüm mezarına papatya çiçeği atar üstüne işerim","ananın ağlaya ağlaya yiğit oğlum askere gitti dediği günde ananı sikimde bı gülsün","arsızın götüne kazık çakmışlar tıkırtı nerden geliyo demiş bende dediğimki benden geliyor ananın ayağa kalkıp alkışladı az hikaye anlatayım dedim hep gerçekleri konuşmak olmaz","adidas ayakkabı giyen kardeşini sokak arasında sıkıştırır tecavüz eder kafasını taşla ezer öldürürüm","ananın amına dış macunu döker dişlerimi ananın amınada"
]

# Yardım menüsü
komutlar = {
    "/liste": "Tüm komutları listeler",
    "/basla": "Yanıtlanan mesaja spam başlatır",
    "/dur": "Spam durdurur",
    "/id": "Kendi ID’nizi gösterir",
    "/addadmin <id>": "Belirtilen ID’yi admin yapar",
    "/removeadmin <id>": "Belirtilen ID’yi adminlikten kaldırır",
    "/admins": "Mevcut adminleri listeler",
    "/delall": "Botun attığı mesajları siler",
    "/clear <adet>": "Son X mesajı siler (izin varsa)",
    "/userinfo <id>": "Belirtilen ID’nin kullanıcı bilgilerini gösterir",
    "/whois": "Yanıtlanan mesajın sahibinin bilgilerini gösterir",
    "/spam <mesaj> <adet>": "Mesajı belirlenen sayıda gönderir",
    "/repeat <mesaj>": "Mesajı sürekli tekrarlar (durdur /dur ile)",
    "/schedule <saat> <mesaj>": "Belirli saatte mesaj gönderir (HH:MM formatında)",
    "/forward <reply> <chat_id>": "Yanıtlanan mesajı başka chat’e iletir",
    "/chatinfo": "Bulunduğu chat bilgilerini gösterir",
    "/me": "Botun ID ve adını gösterir",
    "/ping": "Botun canlılığını test eder",
    "/dice": "Zar atar (1-6)",
    "/roll <XdY>": "RPG tarzı zar atışı, örn: 3d6",
    "/quote": "Hazır motivasyon mesajı gönderir",
    "/random": "Listeden rastgele mesaj seçip gönderir"
}

# ---------------- YARDIMCI FONKSİYON ---------------- #

async def is_admin(user_id):
    owner = await client.get_me()
    return user_id == owner.id or user_id in admins

# ---------------- KOMUTLAR ---------------- #

@client.on(events.NewMessage(pattern=r"/liste"))
async def liste(event):
    if not await is_admin(event.sender_id):
        return

    text = "📜 Komut Listesi:\n"
    for cmd, desc in komutlar.items():
        text += f"{cmd} → {desc}\n"
    await event.reply(text)

@client.on(events.NewMessage(pattern=r"/id"))
async def get_id(event):
    await event.reply(f"🆔 ID: `{event.sender_id}`")

@client.on(events.NewMessage(pattern=r"/addadmin"))
async def add_admin(event):
    if not await is_admin(event.sender_id):
        return

    try:
        admin_id = int(event.text.split()[1])
        admins.add(admin_id)
        await event.reply(f"✅ Admin eklendi: `{admin_id}`")
    except:
        await event.reply("❗ Kullanım: /addadmin <id>")

@client.on(events.NewMessage(pattern=r"/removeadmin"))
async def remove_admin(event):
    if not await is_admin(event.sender_id):
        return

    try:
        admin_id = int(event.text.split()[1])
        admins.discard(admin_id)
        await event.reply(f"✅ Admin kaldırıldı: `{admin_id}`")
    except:
        await event.reply("❗ Kullanım: /removeadmin <id>")

@client.on(events.NewMessage(pattern=r"/admins"))
async def list_admins(event):
    text = "👑 Adminler:\n"
    for a in admins:
        text += f"{a}\n"
    owner = await client.get_me()
    text += f"💠 Owner: {owner.id}"
    await event.reply(text)

@client.on(events.NewMessage(pattern=r"/delall"))
async def del_all(event):
    if not await is_admin(event.sender_id):
        return

    for mid in bot_messages:
        try:
            await client.delete_messages(event.chat_id, mid)
        except:
            pass
    bot_messages.clear()
    await event.reply("🗑️ Botun attığı mesajlar silindi.")

@client.on(events.NewMessage(pattern=r"/clear"))
async def clear_messages(event):
    if not await is_admin(event.sender_id):
        return
    try:
        adet = int(event.text.split()[1])
        msgs = await client.get_messages(event.chat_id, limit=adet)
        ids = [m.id for m in msgs]
        await client.delete_messages(event.chat_id, ids)
        await event.reply(f"🗑️ Son {adet} mesaj silindi.")
    except:
        await event.reply("❗ Kullanım: /clear <adet>")

@client.on(events.NewMessage(pattern=r"/userinfo"))
async def userinfo(event):
    if not await is_admin(event.sender_id):
        return
    try:
        uid = int(event.text.split()[1])
        user = await client.get_entity(uid)
        await event.reply(f"📌 {user.first_name} @{getattr(user,'username','')} ID:{user.id}")
    except:
        await event.reply("❗ Kullanım: /userinfo <id>")

@client.on(events.NewMessage(pattern=r"/whois"))
async def whois(event):
    if not await is_admin(event.sender_id):
        return
    reply = await event.get_reply_message()
    if not reply:
        await event.reply("❗ Yanıtlanan mesaj yok")
        return
    user = await client.get_entity(reply.sender_id)
    await event.reply(f"📌 {user.first_name} @{getattr(user,'username','')} ID:{user.id}")

@client.on(events.NewMessage(pattern=r"/basla"))
async def basla(event):
    global aktif, reply_message_id, reply_chat_id
    if not await is_admin(event.sender_id):
        return
    reply = await event.get_reply_message()
    if not reply:
        await event.reply("❗ /basla komutunu bir mesaja yanıtlayarak kullan")
        return
    aktif = True
    reply_message_id = reply.id
    reply_chat_id = event.chat_id
    await event.delete()
    for mesaj in mesajlar:
        if not aktif:
            break
        m = await client.send_message(reply_chat_id, mesaj, reply_to=reply_message_id)
        bot_messages.append(m.id)
        await asyncio.sleep(2)

@client.on(events.NewMessage(pattern=r"/dur"))
async def dur(event):
    global aktif
    if not await is_admin(event.sender_id):
        return
    aktif = False
    await event.delete()

@client.on(events.NewMessage(pattern=r"/spam"))
async def spam(event):
    if not await is_admin(event.sender_id):
        return
    try:
        parts = event.text.split()
        text = " ".join(parts[1:-1])
        adet = int(parts[-1])
        for _ in range(adet):
            m = await event.reply(text)
            bot_messages.append(m.id)
            await asyncio.sleep(1)
    except:
        await event.reply("❗ Kullanım: /spam <mesaj> <adet>")

@client.on(events.NewMessage(pattern=r"/repeat"))
async def repeat(event):
    if not await is_admin(event.sender_id):
        return
    text = " ".join(event.text.split()[1:])
    while aktif:
        m = await event.reply(text)
        bot_messages.append(m.id)
        await asyncio.sleep(2)

@client.on(events.NewMessage(pattern=r"/ping"))
async def ping(event):
    await event.reply("🏓 Pong!")

@client.on(events.NewMessage(pattern=r"/me"))
async def me(event):
    user = await client.get_me()
    await event.reply(f"💠 Bot: {user.first_name} ID: {user.id}")

@client.on(events.NewMessage(pattern=r"/chatinfo"))
async def chatinfo(event):
    chat = await event.get_chat()
    await event.reply(f"💬 Chat: {getattr(chat,'title',chat.id)} ID: {chat.id}")

@client.on(events.NewMessage(pattern=r"/dice"))
async def dice(event):
    await event.reply(f"🎲 Zar: {random.randint(1,6)}")

@client.on(events.NewMessage(pattern=r"/roll"))
async def roll(event):
    try:
        xdy = event.text.split()[1].lower()
        x, y = map(int, xdy.split('d'))
        rolls = [random.randint(1, y) for _ in range(x)]
        await event.reply(f"🎲 Rolls: {rolls} = {sum(rolls)}")
    except:
        await event.reply("❗ Kullanım: /roll XdY, örn: 3d6")

@client.on(events.NewMessage(pattern=r"/quote"))
async def quote(event):
    quotes = ["Başarı azimle gelir", "Kod yazmak bir sanattır", "Hayat bir oyundur"]
    await event.reply(random.choice(quotes))

@client.on(events.NewMessage(pattern=r"/random"))
async def random_msg(event):
    await event.reply(random.choice(mesajlar))

# ---------------- ÇALIŞTIR ---------------- #
async def main():
    await client.start()
    print("Bot çalışıyor ve hazır.")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())