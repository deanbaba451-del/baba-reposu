import requests, uuid, random, time, json
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
ADMIN_ID = 6534222591

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

CHANNELS = ["@rwssiasohbet", "@alnaseerh"]

# ================== FSM ==================

class Support(StatesGroup):
    waiting = State()

# ================== INSTAGRAM RESET ==================

thomas = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
rid = lambda p="android-": p + uuid.uuid4().hex[:16]

def hdr():
    return {
        "user-agent":"Instagram 275.0.0.27.98 Android",
        "x-ig-app-id":"567067343352427",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
    }

def send_reset(q):
    d = {
        "adid": str(uuid.uuid4()),
        "guid": str(uuid.uuid4()),
        "device_id": rid(),
        "query": q,
        "waterfall_id": str(uuid.uuid4())
    }
    try:
        r = requests.post(
            thomas,
            headers=hdr(),
            data={"signed_body": "SIGNATURE."+json.dumps(d)}
        )
        return r.status_code == 200
    except:
        return False

# ================== START ==================

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("📢 Kanal 1", url="https://t.me/rwssiasohbet"),
        InlineKeyboardButton("📢 Kanal 2", url="https://t.me/alnaseerh")
    )
    kb.add(
        InlineKeyboardButton("✅ Onayla", callback_data="check"),
        InlineKeyboardButton("📩 Destek", callback_data="support")
    )
    await message.answer(
        "🔐 Reset işlemi için kanallara katıl:",
        reply_markup=kb
    )

# ================== KANAL KONTROL ==================

@dp.callback_query_handler(lambda c: c.data == "check")
async def check_sub(callback: types.CallbackQuery):
    for ch in CHANNELS:
        m = await bot.get_chat_member(ch, callback.from_user.id)
        if m.status not in ["member", "administrator", "creator"]:
            await callback.answer("❌ Kanallara katılmalısın", show_alert=True)
            return

    await bot.send_message(
        callback.from_user.id,
        "✅ Onaylandı\nTekrar /start yaz"
    )

# ================== DESTEK ==================

@dp.callback_query_handler(lambda c: c.data == "support")
async def support_start(callback: types.CallbackQuery):
    await callback.message.answer(
        "📩 Admine iletmek istediğiniz mesajı yazın:"
    )
    await Support.waiting.set()

@dp.message_handler(state=Support.waiting)
async def support_send(message: types.Message, state: FSMContext):
    text = f"""
📩 DESTEK MESAJI

👤 Kullanıcı: @{message.from_user.username}
🆔 ID: {message.from_user.id}

💬 Mesaj:
{message.text}
"""
    await bot.send_message(ADMIN_ID, text)
    await message.answer("✅ Mesajınız admine iletildi")
    await state.finish()

# ================== RESET ==================

@dp.message_handler(lambda m: not m.text.startswith("/"))
async def reset(message: types.Message):
    await message.answer("⏳ Reset isteği gönderiliyor...")
    ok = send_reset(message.text)

    # ADMIN LOG
    log = f"""
🔔 RESET LOG

👤 Kullanıcı: @{message.from_user.username}
🆔 ID: {message.from_user.id}
📩 Girdi: {message.text}
📊 Durum: {"BAŞARILI" if ok else "HATALI"}
"""
    await bot.send_message(ADMIN_ID, log)

    if ok:
        await message.answer("✅ Reset isteği gönderildi\n🔁 Tekrar: /start")
    else:
        await message.answer("❌ Hata oluştu\n🔁 Tekrar: /start")

executor.start_polling(dp)