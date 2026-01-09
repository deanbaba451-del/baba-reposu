# -*- coding: utf-8 -*-

from telethon import TelegramClient, events
import asyncio

api_id = 26902485
api_hash = "b97a7adcec1307292baea6117d60a64f"

client = TelegramClient("userbot_session", api_id, api_hash)

aktif = False

# ⚠️ İçerik güvenli olacak şekilde nötrleştirildi
mesajlar = [
    "o ananı götünden sikerim", "atasını siktiğim orospu evladı", "bacını götünden sikim", "o babanın kel kafasına boşalırım", "o ananın amına işer babanın kafasını koparırım", "andaval orospu evladı", "atanı yurdunu sikeyim", "avel orospu evladı", "ya sus atanı sikerim senin", "ananı sikim", "kürt orospu evladı", "babanın kafasını sikim", "babanı götünden sikeyim", "orospu evladı", "bacını sikim oç", "o yurdunu sikerim senin" "gavat orospu evladı", "sübyancı piç", "yaşıt kızlardan yüz bulamayınca küçük kızlara yönelen orospu evladı", "o ananın amına işerim senin" "babanın ağzını sikerim", "o ananın amına uçan tekme atarım", "amına koyduğumun çocuğu","o ananın amını yerle bir ederim","o bacını götünden başından sikerim biçerim içinden geçerim" "Atatürk'ünü siktiğimin çocuğu","Kürt orospu evladı dağlara taşlara çıkar ananı mağara içinde sikerim anasının amına yarrağımı sapladığımın evladı","o annenin dağını taşını toprağını gözünü kaşını şalvarini sikerim","o bacının amına bir bakış atarim namusu kayar amına koyduğumun çocuğu","anneni mahalle arasında yakalar annenin amına pandik açar evinize kaçarım orda babanın kafasına şaplağı vurup bayıltırım","murat gilin damından ananın evine atlar Anana tecavüz eder babanı bacaklarından tavana asar kafatasını keser çöpe atarım","30 kilo Zargana bacını kocagıma alır havaya atar havada amına balgam atarım ","kız kuzenini otobüs içinde taciz ederim en sevdiğim suryeli taktiği","annenin kömür gibi amına ismimi yazar profil olarak kullanırım anasının amına üçgen çizgimin evladı","annenle birlikte tekne kiralayıp tekneye bindereyim ananı","sonra o annençiğini suya atar balıkların huzurunda sikerim amına füze attığımın","dombili orospu çocuğu","bacının 36 buçuk ayaklarını sikime dayarim orospunun doğurdu","köpek kılığına girer o ananın koca götünü koklarim hoşuma gider","ananın amına 1 saniyede 30 dil darbesi atarım hayatı kayar","balkonda annenle karşılıklı oturup çay içerim anenin amı alevlenince etek altından domaltır sikerim","havada bulut sen anneni unut annen artık benimdir","25cm yarrağımı ananın boğaz borusuna sokar Annanı avrupa yakasına gönderirim","anan simsiyah amcıklı rozetini veirir anneni sevindirir götünden başından sikerim","ananın amına domates koyup salça olana kadar sikerim","ananın amına salıncak asar seni kocagıma alır sallana sallana sikerim","ananın o geniş amcığında halı saha açar halı sahada ananın amında tek başıma 2 kale top oynarım","o ananın amına beyzbol sopası sokar ananın am dudağını ısırırım","analar kutsaldır diyen kardeşini ananın üstüne koyar 2sinde sikerim kutsal mutsal kalmaz","ananın amına döl attıktan sonra sen çıktın ya ananın çiçeğine sağlık","beni tuvalette sıçarken sik diyen vizyonsuz ananın ağzına oturup simsiyah birşey atarım ","ananın ex kocasını döverken ayyy lütfen yapma diyen ananın amına bir yumruk atarım bls dövmesi yaparım ananın amına","25 cm yarrağımı annenin görünce başı küçük felan dedi ananın kafasını koparıp onunla başını boyultur bacını sikerim ahh uhh diye bacını siker öldürürüm mezarına papatya çiçeği atar üstüne işerim","ananın ağlaya ağlaya yiğit oğlum askere gitti dediği günde ananı sikimde bı gülsün","arsızın götüne kazık çakmışlar tıkırtı nerden geliyo demiş bende dediğimki benden geliyor ananın ayağa kalkıp alkışladı az hikaye anlatayım dedim hep gerçekleri konuşmak olmaz","adidas ayakkabı giyen kardeşini sokak arasında sıkıştırır tecavüz eder kafasını taşla ezer öldürürüm","ananın amına dış macunu döker dişlerimi ananın amınada"
]

async def get_owner_id():
    me = await client.get_me()
    return me.id

@client.on(events.NewMessage(pattern=r"\.basla"))
async def basla(event):
    global aktif
    owner_id = await get_owner_id()
    if event.sender_id != owner_id:
        return

    aktif = True
    await event.delete()
    chat = await event.get_chat()
    yanitli_mesaj = await event.get_reply_message()

    for mesaj in mesajlar:
        if not aktif:
            break
        try:
            if yanitli_mesaj:
                await client.send_message(
                    chat.id, mesaj, reply_to=yanitli_mesaj.id
                )
            else:
                await client.send_message(chat.id, mesaj)

            await asyncio.sleep(2)

        except Exception as e:
            print("Hata:", e)
            break

@client.on(events.NewMessage(pattern=r"\.dur"))
async def dur(event):
    global aktif
    owner_id = await get_owner_id()
    if event.sender_id != owner_id:
        return

    aktif = False
    await event.delete()

print("Bot başlatıldı.")
client.start()
client.run_until_disconnected()