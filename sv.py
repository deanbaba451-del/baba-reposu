# -*- coding: utf-8 -*-

from telethon import TelegramClient, events
import asyncio
import time
import openai

# ---------- AYARLAR ----------

api_id = 26902485
api_hash = "b97a7adcec1307292baea6117d60a64f"

openai.api_key = "OPENAI_API_KEYINI_BURAYA_YAZ"

client = TelegramClient("userbot_session", api_id, api_hash)

spam_aktif = False
ai_aktif = False
son_cevap = {}

# ---------- CHATGPT FONKSIYONU ----------

def temizle(metin):
    tr_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return metin.translate(tr_map).lower()

async def chatgpt_cevap(mesaj):
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "turkce konus. kucuk harf kullan. "
                        "ozel karakter kullanma. "
                        "gunluk sohbet gibi cevap ver. "
                        "kisa ve dogal ol."
                    )
                },
                {"role": "user", "content": mesaj}
            ],
            max_tokens=60,
            temperature=0.8
        )
        return temizle(resp.choices[0].message.content)
    except Exception as e:
        return "bilemedim ya"

# ---------- KOMUTLAR ----------

@client.on(events.NewMessage(pattern=r"\.basla"))
async def basla(event):
    global spam_aktif
    spam_aktif = True
    await event.reply("basladi")

@client.on(events.NewMessage(pattern=r"\.dur"))
async def dur(event):
    global spam_aktif
    spam_aktif = False
    await event.reply("durdu")

@client.on(events.NewMessage(pattern=r"\.ai"))
async def ai_ac(event):
    global ai_aktif
    ai_aktif = True
    await event.reply("ai acildi")

@client.on(events.NewMessage(pattern=r"\.unai"))
async def ai_kapat(event):
    global ai_aktif
    ai_aktif = False
    await event.reply("ai kapandi")

@client.on(events.NewMessage(pattern=r"\.liste"))
async def liste(event):
    await event.reply(
        ".basla  cevaplari baslatir\n"
        ".dur    durdurur\n"
        ".ai     chatgpt ac\n"
        ".unai   chatgpt kapa\n"
        ".liste  komutlar"
    )

# ---------- OTOMATIK CEVAP ----------

@client.on(events.NewMessage)
async def otomatik(event):
    if event.out:
        return

    if not spam_aktif or not ai_aktif:
        return

    user_id = event.sender_id
    simdi = time.time()

    if user_id in son_cevap:
        if simdi - son_cevap[user_id] < 5:
            return

    son_cevap[user_id] = simdi
    await asyncio.sleep(2)

    cevap = await chatgpt_cevap(event.text)
    await event.reply(cevap)

# ---------- CALISTIR ----------

async def main():
    await client.start()
    print("chatgpt userbot aktif")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())