# banall_bot.py
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import time

print("1 - Kod başladı, kütüphaneler import ediliyor...")

try:
    api_id = 26902485       # BURAYA KENDİ api_id
    api_hash = "b97a7adcec1307292baea6117d60a64f"  # BURAYA KENDİ api_hash
    bot_token = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"  # BURAYA BOTFATHER TOKEN

    print("2 - Client oluşturuluyor...")
    app = Client("banall_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

    ALLOWED = [SENİN_USER_ID]  # örnek: 123456789  -- kendi telegram id'ni koy

    @app.on_message(filters.private & filters.command("banall") & filters.user(ALLOWED))
    async def banall(client: Client, message: Message):
        print(f"Komut geldi: {message.text}")
        args = message.text.split()
        
        if len(args) != 3:
            await message.reply("Kullanım: /banall @grupadi 50")
            print("Yanlış kullanım")
            return

        hedef = args[1].replace("@", "")
        try:
            adet = int(args[2])
        except:
            await message.reply("Son sayı olmalı amk")
            return

        msg = await message.reply(f"@{hedef} grubunda son {adet} kişiyi banlıyorum...")

        try:
            chat = await client.get_chat(f"@{hedef}")
            print(f"Grup bulundu: {chat.title}")
        except Exception as e:
            await msg.edit(f"Grup bulunamadı: {str(e)}")
            print(f"Hata grup: {e}")
            return

        me = await client.get_me()
        yetki = await client.get_chat_member(chat.id, me.id)
        if not yetki.privileges or not yetki.privileges.can_restrict_members:
            await msg.edit("Ban yetkim yok, siktir git yetki ver")
            print("Yetki yok")
            return

        sayac = 0
        hata = 0
        async for msg_history in client.get_chat_history(chat.id, limit=adet + 30):
            if not msg_history.from_user:
                continue
            uid = msg_history.from_user.id
            if uid == me.id:
                continue

            try:
                uye = await client.get_chat_member(chat.id, uid)
                if uye.status in ["administrator", "creator"]:
                    continue
            except:
                pass

            try:
                await client.ban_chat_member(chat.id, uid)
                sayac += 1
                print(f"Banlandı: {uid}")
                await asyncio.sleep(1.1)  # flood yememek için
            except Exception as e:
                hata += 1
                print(f"Ban hatası {uid}: {e}")

            if sayac >= adet:
                break

        await msg.edit(
            f"**Bitti lan!**\n"
            f"Başarılı: {sayac}\n"
            f"Hatalı: {hata}\n"
            f"Grup: @{hedef}"
        )

    print("3 - Bot çalışıyor, komut bekleniyor...")
    app.run()

except Exception as e:
    print("KRİTİK HATA:", str(e))
    time.sleep(3)
    raise e