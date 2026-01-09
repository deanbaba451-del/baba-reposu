# -*- coding: utf-8 -*-

from telethon import TelegramClient, events
import asyncio
import random
import time

api_id = 26902485
api_hash = "b97a7adcec1307292baea6117d60a64f"

client = TelegramClient("userbot_session", api_id, api_hash)

spam_aktif = False
ai_aktif = False
son_cevap = {}

# -------- AI GUNLUK KONUSMA HAVUZU --------

AI_CEVAPLAR = [
    "selam",
    "selam naber",
    "naber",
    "ne haber",
    "nasilsin",
    "iyi misin",
    "iyiyim sen",
    "idare eder",
    "eh iste",
    "normal ya",
    "yuvarlaniyoruz",
    "ne yapiyorsun",
    "ne var ne yok",
    "keyifler nasil",
    "bugun nasil gecti",
    "hmm",
    "hmm olabilir",
    "mantikli",
    "ilginç",
    "degisikmis",
    "bilmiyorum ya",
    "emin degilim",
    "oyle mi",
    "ciddi misin",
    "yok artik",
    "bence de",
    "katiliyorum",
    "pek katilmiyorum",
    "haklisin",
    "hakli olabilirsin",
    "o da bir bakis acisi",
    "anlatsana",
    "neden peki",
    "nasil yani",
    "ee sonra",
    "bosver ya",
    "takma kafana",
    "olur oyle",
    "normal bence",
    "abartma",
    "rahat ol",
    "aynen",
    "dogru",
    "yanlis",
    "olabilir",
    "bilemedim",
    "bakalim",
    "gorecegiz",
    "hayirlisi",
    "kismet",
    "nasip",
    "zaman gosterir",
    "belli olmaz",
    "sonra konusalim",
    "haberlesiriz",
    "kendine dikkat et"
]

# -------- SPAM MESAJLARI (ZARARSIZ) --------

SPAM_MESAJLAR = [
       "o ananı götünden sikerim", "atasını siktiğim orospu evladı", "bacını götünden sikim", "o babanın kel kafasına boşalırım", "o ananın amına işer babanın kafasını koparırım", "andaval orospu evladı", "atanı yurdunu sikeyim", "avel orospu evladı", "ya sus atanı sikerim senin", "ananı sikim", "kürt orospu evladı", "babanın kafasını sikim", "babanı götünden sikeyim", "orospu evladı", "bacını sikim oç", "o yurdunu sikerim senin" "gavat orospu evladı", "sübyancı piç", "yaşıt kızlardan yüz bulamayınca küçük kızlara yönelen orospu evladı", "o ananın amına işerim senin" "babanın ağzını sikerim", "o ananın amına uçan tekme atarım", "amına koyduğumun çocuğu","o ananın amını yerle bir ederim","o bacını götünden başından sikerim biçerim içinden geçerim" "Atatürk'ünü siktiğimin çocuğu","Kürt orospu evladı dağlara taşlara çıkar ananı mağara içinde sikerim anasının amına yarrağımı sapladığımın evladı","o annenin dağını taşını toprağını gözünü kaşını şalvarini sikerim","o bacının amına bir bakış atarim namusu kayar amına koyduğumun çocuğu","anneni mahalle arasında yakalar annenin amına pandik açar evinize kaçarım orda babanın kafasına şaplağı vurup bayıltırım","murat gilin damından ananın evine atlar Anana tecavüz eder babanı bacaklarından tavana asar kafatasını keser çöpe atarım","30 kilo Zargana bacını kocagıma alır havaya atar havada amına balgam atarım ","kız kuzenini otobüs içinde taciz ederim en sevdiğim suryeli taktiği","annenin kömür gibi amına ismimi yazar profil olarak kullanırım anasının amına üçgen çizgimin evladı","annenle birlikte tekne kiralayıp tekneye bindereyim ananı","sonra o annençiğini suya atar balıkların huzurunda sikerim amına füze attığımın","dombili orospu çocuğu","bacının 36 buçuk ayaklarını sikime dayarim orospunun doğurdu","köpek kılığına girer o ananın koca götünü koklarim hoşuma gider","ananın amına 1 saniyede 30 dil darbesi atarım hayatı kayar","balkonda annenle karşılıklı oturup çay içerim anenin amı alevlenince etek altından domaltır sikerim","havada bulut sen anneni unut annen artık benimdir","25cm yarrağımı ananın boğaz borusuna sokar Annanı avrupa yakasına gönderirim","anan simsiyah amcıklı rozetini veirir anneni sevindirir götünden başından sikerim","ananın amına domates koyup salça olana kadar sikerim","ananın amına salıncak asar seni kocagıma alır sallana sallana sikerim","ananın o geniş amcığında halı saha açar halı sahada ananın amında tek başıma 2 kale top oynarım","o ananın amına beyzbol sopası sokar ananın am dudağını ısırırım","analar kutsaldır diyen kardeşini ananın üstüne koyar 2sinde sikerim kutsal mutsal kalmaz","ananın amına döl attıktan sonra sen çıktın ya ananın çiçeğine sağlık","beni tuvalette sıçarken sik diyen vizyonsuz ananın ağzına oturup simsiyah birşey atarım ","ananın ex kocasını döverken ayyy lütfen yapma diyen ananın amına bir yumruk atarım bls dövmesi yaparım ananın amına","25 cm yarrağımı annenin görünce başı küçük felan dedi ananın kafasını koparıp onunla başını boyultur bacını sikerim ahh uhh diye bacını siker öldürürüm mezarına papatya çiçeği atar üstüne işerim","ananın ağlaya ağlaya yiğit oğlum askere gitti dediği günde ananı sikimde bı gülsün","arsızın götüne kazık çakmışlar tıkırtı nerden geliyo demiş bende dediğimki benden geliyor ananın ayağa kalkıp alkışladı az hikaye anlatayım dedim hep gerçekleri konuşmak olmaz","adidas ayakkabı giyen kardeşini sokak arasında sıkıştırır tecavüz eder kafasını taşla ezer öldürürüm","ananın amına dış macunu döker dişlerimi ananın amınada"
]

# -------- KOMUTLAR --------

@client.on(events.NewMessage(pattern=r"\.basla"))
async def basla(event):
    global spam_aktif
    spam_aktif = True
    await event.reply("spam basladi")

@client.on(events.NewMessage(pattern=r"\.dur"))
async def dur(event):
    global spam_aktif
    spam_aktif = False
    await event.reply("spam durdu")

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
        ".basla  spam baslatir\n"
        ".dur    spam durdurur\n"
        ".ai     ai cevaplari acar\n"
        ".unai   ai cevaplari kapatir\n"
        ".liste  komutlari gosterir"
    )

# -------- OTOMATIK CEVAP --------

@client.on(events.NewMessage)
async def otomatik(event):
    if event.out:
        return

    if not spam_aktif:
        return

    user_id = event.sender_id
    simdi = time.time()

    # flood koruma
    if user_id in son_cevap:
        if simdi - son_cevap[user_id] < 3:
            return

    son_cevap[user_id] = simdi
    await asyncio.sleep(random.uniform(1.0, 2.5))

    if ai_aktif:
        cevap = random.choice(AI_CEVAPLAR)
    else:
        cevap = random.choice(SPAM_MESAJLAR)

    await event.reply(cevap)

# -------- CALISTIR --------

async def main():
    await client.start()
    print("bot calisiyor")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())