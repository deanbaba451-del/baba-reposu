import telebot
import random
import sqlite3
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = "8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI"
bot = telebot.TeleBot(TOKEN)
MAX_TRIES = 7
POINTS_PER_WORD = 10
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

CATEGORIES = {
    "programlama": [
        ("python", "Popüler bir programlama dili"),
        ("java", "Bir başka yaygın programlama dili"),
        ("algoritma", "Problemleri çözmek için adımlar"),
        ("debug", "Hata ayıklama işlemi"),
        ("fonksiyon", "Tekrar kullanılabilir kod bloğu"),
        ("değişken", "Veri tutmak için kullanılan isim"),
        ("sahal", "Kod geliştiricisi"),
    ],
    "teknoloji": [
        ("telegram", "Mesajlaşma uygulaması"),
        ("yapayzeka", "Bilgisayarın insan gibi düşünmesi"),
        ("bot", "Otomatik program"),
        ("discord", "Oyuncular için sohbet platformu"),
        ("internet", "Dünya çapında ağ ağı"),
        ("gadget", "Teknolojik küçük cihaz")
    ],
    "ask": [
        ("sevgi", "Kalpten gelen en güzel duygu"),
        ("aşk", "İki kalbin birbirine olan derin bağlılığı"),
        ("romantizm", "Duygusal ve etkileyici davranış biçimi"),
        ("kalp", "Duyguların merkezi, sevginin simgesi"),
        ("özlem", "Uzakta olanı çok istemek, hasret çekmek"),
        ("bakış", "İçten bir duyguyu anlatan göz teması"),
        ("seni seviyorum", "En güçlü sevgi ifadesi"),
        ("flört", "İki kişinin birbirine karşı ilgi göstermesi"),
        ("dua", "Sevgi için kalpten edilen dilek"),
        ("umut", "Aşkta beklentilerin yeşermesi"),
        ("gözler", "Seven erkeğin unutmadığı, unutamayacağı en derin yeridir onun🥹 ")
    ]
}

DB_PATH = "hangman.db"
def get_conn():
    return sqlite3.connect(DB_PATH)
def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            user_id INTEGER PRIMARY KEY,
            points INTEGER NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            chat_id INTEGER PRIMARY KEY,
            category TEXT NOT NULL,
            word TEXT NOT NULL,
            correct_guesses TEXT NOT NULL,
            wrong_guesses TEXT NOT NULL,
            tries_left INTEGER NOT NULL,
            hint_used INTEGER NOT NULL,
            finished INTEGER NOT NULL,
            won INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()#Db
def save_score(user_id, points):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT points FROM scores WHERE user_id=?", (user_id,))
    row = c.fetchone()
    if row:
        new_points = row[0] + points
        c.execute("UPDATE scores SET points=? WHERE user_id=?", (new_points, user_id))
    else:
        c.execute("INSERT INTO scores(user_id, points) VALUES (?, ?)", (user_id, points))
    conn.commit()
    conn.close()
def get_score(user_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT points FROM scores WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else 0
def get_top_scores(limit=10):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT user_id, points FROM scores ORDER BY points DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows


def save_game(chat_id, game):
    conn = get_conn()
    c = conn.cursor()
    correct_json = json.dumps(list(game.correct_guesses))
    wrong_json = json.dumps(list(game.wrong_guesses))
    hint_used_int = 1 if game.hint_used else 0
    finished_int = 1 if game.finished else 0
    won_int = 1 if game.won else 0
    c.execute('''
        INSERT OR REPLACE INTO games
        (chat_id, category, word, correct_guesses, wrong_guesses, tries_left, hint_used, finished, won)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (chat_id, game.category, game.word, correct_json, wrong_json, game.tries_left, hint_used_int, finished_int, won_int))
    conn.commit()
    conn.close()
def load_games():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM games")
    rows = c.fetchall()
    conn.close()
    loaded_games = {}
    for row in rows:
        chat_id, category, word, correct_json, wrong_json, tries_left, hint_used_int, finished_int, won_int = row
        game = HangmanGame(chat_id, category)
        game.word = word
        game.correct_guesses = set(json.loads(correct_json))
        game.wrong_guesses = set(json.loads(wrong_json))
        game.tries_left = tries_left
        game.hint_used = bool(hint_used_int)
        game.finished = bool(finished_int)
        game.won = bool(won_int)
        loaded_games[chat_id] = game
    return loaded_games


class HangmanGame:
    def __init__(self, chat_id, category):
        self.chat_id = chat_id
        self.category = category
        self.word, self.hint = random.choice(CATEGORIES[category])
        self.word = self.word.lower()
        self.correct_guesses = set()
        self.wrong_guesses = set()
        self.tries_left = MAX_TRIES
        self.finished = False
        self.hint_used = False
        self.won = False
    def display_word(self):
        return ' '.join([c if c in self.correct_guesses else '_' for c in self.word])
    def display_hangman(self):
        pic_index = MAX_TRIES - self.tries_left
        if pic_index >= len(HANGMAN_PICS):
            pic_index = len(HANGMAN_PICS) - 1
        return HANGMAN_PICS[pic_index]
    def guess(self, letter_or_word):
        if self.finished:
            return "Oyun zaten bitti."
        guess = letter_or_word.lower()
        if len(guess) == 1:
            if guess in self.correct_guesses or guess in self.wrong_guesses:
                return f"'{guess}' zaten tahmin edildi."
            if guess in self.word:
                self.correct_guesses.add(guess)
                if all(c in self.correct_guesses for c in self.word):
                    self.finished = True
                    self.won = True
                    return f"Tebrikler! Kelimeyi doğru buldunuz: {self.word}"
                else:
                    return (f"Doğru tahmin! Kelime: {self.display_word()}\n"
                            f"{self.display_hangman()}\nKalan hak: {self.tries_left}")
            else:#Sahal
                self.wrong_guesses.add(guess)
                self.tries_left -= 1
                if self.tries_left <= 0:
                    self.finished = True
                    self.won = False
                    return f"Kaybettiniz! Kelime: {self.word}\n{self.display_hangman()}"
                else:
                    return (f"Yanlış tahmin! Kelime: {self.display_word()}\n"
                            f"{self.display_hangman()}\nKalan hak: {self.tries_left}")
        else:            
            if guess == self.word:
                self.finished = True
                self.won = True
                return f"Tebrikler! Kelimeyi doğru buldunuz: {self.word}"
            else:
                self.tries_left -= 1
                if self.tries_left <= 0:
                    self.finished = True
                    self.won = False
                    return f"Yanlış kelime tahmini! Kaybettiniz. Kelime: {self.word}\n{self.display_hangman()}"
                else:
                    return (f"Yanlış kelime tahmini! Kalan hak: {self.tries_left}\n"
                            f"{self.display_hangman()}")
    def get_hint(self):
        if self.hint_used:
            return "İpucunu zaten kullandınız."
        else:
            self.hint_used = True
            return f"İpucu: {self.hint}"
GAMES = {}

#bitirmem lazım
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Merhaba! Adam asmaca oyununa hoşgeldiniz.\n"
                     "Oynamak için /game komutunu kullanabilirsiniz.\n"
                     "Kategori seçmek için butonlardan seçin.\n"
                     "İpucu için /ipucu\n"
                     "Oyunu bırakmak için /quit\n"
                     "Puan tablosu için /puanlar")


@bot.message_handler(commands=['game'])
def newgame_handler(message):
    chat_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(text=cat.capitalize(), callback_data=f"startgame_{cat}") for cat in CATEGORIES.keys()]
    keyboard.add(*buttons)
    bot.send_message(chat_id, "Lütfen oynamak istediğiniz kategoriyi seçin:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith("startgame_"))
def callback_startgame(call):
    category = call.data.split("_", 1)[1]
    chat_id = call.message.chat.id

    if category not in CATEGORIES:
        keyboard = InlineKeyboardMarkup(row_width=3)
        buttons = [InlineKeyboardButton(text=cat.capitalize(), callback_data=f"startgame_{cat}") for cat in CATEGORIES.keys()]
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=f"Geçersiz kategori '{category}'. Lütfen doğru kategoriyi seçin:",
                              reply_markup=keyboard)
        bot.answer_callback_query(call.id)
        return

    start_new_game(chat_id, category)
    bot.answer_callback_query(call.id, f"'{category.capitalize()}' kategorisinde oyun başladı!")
    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                          text=f"Oyun başladı! Kategori: {category}\nKelime: {GAMES[chat_id].display_word()}\nKalan hak: {MAX_TRIES}\nTahmin etmek için harf veya kelime yazabilirsiniz.\nİpucu için /ipucu")


def start_new_game(chat_id, category):
    GAMES[chat_id] = HangmanGame(chat_id, category)
    save_game(chat_id, GAMES[chat_id])


@bot.message_handler(commands=['ipucu'])
def send_hint(message):
    chat_id = message.chat.id
    if chat_id not in GAMES:
        bot.send_message(chat_id, "Önce /game ile oyun başlatmalısınız.")
        return
    game = GAMES[chat_id]
    bot.send_message(chat_id, game.get_hint())
    save_game(chat_id, game)


@bot.message_handler(commands=['quit'])
def quit_game(message):
    chat_id = message.chat.id
    if chat_id in GAMES:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(text="Evet, çıkış yap", callback_data="quit_confirm"))
        keyboard.add(InlineKeyboardButton(text="Hayır, devam et", callback_data="quit_cancel"))
        bot.send_message(chat_id, "Oyundan çıkmak istediğinizden emin misiniz?", reply_markup=keyboard)
    else:
        bot.send_message(chat_id, "Şu anda oynanan bir oyun yok.")


@bot.callback_query_handler(func=lambda call: call.data in ["quit_confirm", "quit_cancel"])
def callback_quit_confirm(call):
    chat_id = call.message.chat.id
    if call.data == "quit_confirm":
        if chat_id in GAMES:
            del GAMES[chat_id]
            conn = get_conn()
            c = conn.cursor()
            c.execute("DELETE FROM games WHERE chat_id=?", (chat_id,))
            conn.commit()
            conn.close()
        bot.edit_message_text("Oyun iptal edildi.", chat_id=chat_id, message_id=call.message.message_id)
    else:
        bot.edit_message_text("Oyuna devam ediyorsunuz.", chat_id=chat_id, message_id=call.message.message_id)


@bot.message_handler(commands=['puanlar'])
def show_scores(message):
    top_scores = get_top_scores()
    if not top_scores:
        bot.send_message(message.chat.id, "Henüz puan tablosu boş.")
        return
    keyboard = InlineKeyboardMarkup(row_width=1)
    text = "🏆 Puan Tablosu:\n"
    for i, (user_id, points) in enumerate(top_scores[:10], 1):
        username = None
        try:
            if message.chat.type in ['group', 'supergroup']:
                user = bot.get_chat_member(message.chat.id, user_id).user
                username = user.first_name
            else:
                username = f"Kullanıcı {user_id}"
        except Exception:
            username = f"Kullanıcı {user_id}"
        text += f"{i}. {username}: {points} puan\n"
        keyboard.add(InlineKeyboardButton(text=f"{username}", callback_data=f"user_{user_id}"))
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith("user_"))
def callback_user_info(call):
    user_id = int(call.data.split("_")[1])
    points = get_score(user_id)
    username = None
    try:
        if call.message.chat.type in ['group', 'supergroup']:
            user = bot.get_chat_member(call.message.chat.id, user_id).user
            username = user.first_name
        else:
            username = f"Kullanıcı {user_id}"
    except Exception:
        username = f"Kullanıcı {user_id}"
    bot.answer_callback_query(call.id, f"{username} toplam {points} puana sahip.")


@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text.strip()

    if chat_id not in GAMES:
        bot.send_message(chat_id, "Önce /game ile oyun başlatmalısınız.")
        return

    game = GAMES[chat_id]
    response = game.guess(text)
    bot.send_message(chat_id, response)
    save_game(chat_id, game)

    if game.finished:
        if game.won:
            save_score(user_id, POINTS_PER_WORD)
            puan = get_score(user_id)
            bot.send_message(chat_id, f"Tebrikler! {POINTS_PER_WORD} puan kazandınız. Toplam puanınız: {puan}")
        # BİTİNCE TEMİZLEMELİ 
        del GAMES[chat_id]
        conn = get_conn()
        c = conn.cursor()
        c.execute("DELETE FROM games WHERE chat_id=?", (chat_id,))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    init_db()
    GAMES = load_games()
    bot.infinity_polling()
