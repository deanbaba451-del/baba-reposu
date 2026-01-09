from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

Sahal = 35884393
Mavi = "198bfa9cf22b84751bd630b76dbff753"
#my.telegram.org adresinden almak mümkündür
Seviyor = "8419439624:AAHUz30JcwMHPE_3DRG2WXkfwiathx13cZA"

app = Client(
    "joinRequestApproveBot",
    api_id=Sahal,
    api_hash=Mavi,
    bot_token=Seviyor
)
pending_requests = {}   
@app.on_chat_join_request()
async def join_req_handler(client: Client, req: ChatJoinRequest):
    user_id = req.from_user.id
    chat_id = req.chat.id
    pending_requests[user_id] = chat_id
    buttons = [
        [InlineKeyboardButton("✅ ONAYLA", callback_data=f"onayla_{user_id}")]
    ]
    try:
        await client.send_message(
            user_id,
            "Merhaba \n\n"
            "Gruba/Kanala katılmak için isteğini aldım.\n"
            "Lütfen ONAYLA butonuna bas → seni içeri alayım.",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        print(f"PM gönderilemedi → {e}")
@app.on_callback_query(filters.regex(r"onayla_(\d+)"))
async def approve_user(client, callback_query):
    user_id = int(callback_query.data.split("_")[1])
    if user_id != callback_query.from_user.id:
        return await callback_query.answer("Bu buton sana ait değil!", show_alert=True)
    chat_id = pending_requests.get(user_id)
    if not chat_id:
        return await callback_query.answer("İstek bulunamadı!", show_alert=True)
    try:
        await client.approve_chat_join_request(chat_id, user_id)
        await callback_query.answer("Onaylandı! 🎉 Artık gruptasın.")
        await callback_query.message.edit_text("✔ Onay verdin! Grup isteğin kabul edildi.")
        pending_requests.pop(user_id, None)

        print(f"{user_id} → {chat_id} için kabul edildi.")
    except Exception as e:
        await callback_query.answer("Hata oluştu!", show_alert=True)
        print(f"Onay hatası: {e}")
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user = message.from_user.first_name
    bot_username = (await client.get_me()).username
    add_link = f"https://t.me/{bot_username}?startgroup=true"
    buttons = [
        [InlineKeyboardButton("➕ Beni Grubuna / Kanalına Ekle", url=add_link)]
    ]
    text = (
        f" Merhaba {user}\n\n"
        "Ben gruplara ve kanallara gelen katılma isteklerini otomatik yöneten akıllı bir botum.\n"
        "Beni kullanabilmen için botu bir gruba veya kanala eklemen yeterlidir.\n\n"
        "Aşağıdaki butona tıklayarak beni ekleyebilirsin 👇"
    )
    await message.reply(text, reply_markup=InlineKeyboardMarkup(buttons))
app.run()