from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import re

# ── BOT BİLGİLERİ ──
api_id = 26902485
api_hash = "b97a7adcec1307292baea6117d60a64f"
bot_token = "8110267443:AAEJILVkcebQ-vYIqNkBbczEBDqB6YOspik"

app = Client("banall_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Sadece belirli kişiler kullanabilsin diye (güvenlik için)
ALLOWED_USERS = [123456789, 987654321]  # senin user id'lerini koy


@app.on_message(filters.private & filters.command("banall") & filters.user(ALLOWED_USERS))
async def ban_all_command(client: Client, message: Message):
    if len(message.command) != 3:
        await message.reply("Doğru kullanım:\n`/banall @kullanıcıadı 50`\nÖrnek: `/banall @BeyazKurtlar 30`")
        return

    target = message.command[1].strip()
    try:
        count = int(message.command[2])
        if count < 1 or count > 200:
            await message.reply("1-200 arası sayı girebilirsin.")
            return
    except:
        await message.reply("Son parametre sayı olmalı.")
        return

    if not target.startswith("@"):
        await message.reply("Grup kullanıcı adı @ ile başlamalı.")
        return

    target = target[1:]  # @ işaretini kaldır

    msg = await message.reply(f"**{target}** grubunda son **{count}** kişiyi banlamaya başlıyorum...")

    try:
        chat = await client.get_chat(f"@{target}")
    except Exception as e:
        await msg.edit(f"Gruba erişilemedi: `{e}`")
        return

    if chat.type not in ["group", "supergroup", "channel"]:
        await msg.edit("Sadece grup ve supergroup destekleniyor.")
        return

    # Botun o chatta ban yetkisi var mı kontrolü
    me = await client.get_me()
    try:
        member = await client.get_chat_member(chat.id, me.id)
        if not member.privileges or not member.privileges.can_restrict_members:
            await msg.edit("Bu grupta **ban yetkim yok**! Yetki verin sonra deneyin.")
            return
    except:
        await msg.edit("Yetki bilgisi alınamadı, büyük ihtimal yetkim yok.")
        return

    banned_count = 0
    failed_count = 0

    async for user in client.get_chat_history(chat.id, limit=count + 50):  # biraz fazla çekip bot/admin vs atlayalım
        if user.from_user is None:
            continue

        uid = user.from_user.id

        # Kendini banlamasın, botu banlamasın, adminleri banlamasın
        if uid == me.id:
            continue

        try:
            admin = await client.get_chat_member(chat.id, uid)
            if admin.status in ["administrator", "creator"]:
                continue  # admin ve owner'ı banlama
        except:
            pass

        try:
            await client.ban_chat_member(chat.id, uid)
            banned_count += 1
            await asyncio.sleep(0.7)  # flood wait'i azaltmak için
        except Exception as e:
            failed_count += 1
            print(f"Ban hatası {uid}: {e}")

        if banned_count >= count:
            break

    text = f"**İşlem bitti!**\n\n"
    text += f"Başarıyla banlanan: **{banned_count}**\n"
    text += f"Başaramadığım: **{failed_count}**\n"
    text += f"Hedef grup: @{target}\n"
    text += f"İstenen miktar: {count}"

    await msg.edit(text)


# Botu çalıştır
if __name__ == "__main__":
    print("BanAll bot başlatıldı...")
    app.run()