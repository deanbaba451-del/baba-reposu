import requests
import random
import threading
from bs4 import BeautifulSoup

Z = '\033[1;31m'  # أحمر
C = '\033[2;35m'  # وردي
F = '\033[2;32m'  # أخضر
B = '\033[1;36m'  # سماوي
R = '\033[1;30m'  # رصاصي
W = '\033[1;39m'  # أبيض
X = '\033[1;33m'

print(B + '▬' * 71)
print(f'''
{X}BY : @alonemarkaa
''')

tok = input(Z+'[÷] Token : ')
id = input(B + '[÷] ID : ')

# Kullanıcıdan ilk ve son harfi alma
first_char = input(Z + '[÷] İlk Harf a,b,c,d,e,t,r,w,q,y,z,u: ').lower()
last_char = input(B + '[÷] Son Harf a,b,c,d,e,t,r,w,q,y,z,u: ').lower()

def check_username():
    while True:
        # 5 harfli kullanıcı adı oluşturuyoruz
        username = first_char + ''.join(random.choice('abcdeturwqyz') for _ in range(3)) + last_char
        
        # Kullanıcı adının Telegram'da var olup olmadığını kontrol et
        url = requests.get(f'https://t.me/{username}').text
        if 'tgme_username_link' in url:
            url = f'https://fragment.com/?query={username}&sort=price_asc'
            re = requests.get(url).content
            soup = BeautifulSoup(re, 'html.parser')
            cards = soup.find_all("div", {"class": "table-cell-status-thin thin-only tm-status-unavail"})
            try:
                teamB = cards[0].text.strip()
                if teamB == 'Unavailable':  # Kullanıcı adı boşta ise
                    print(F + f'Hit : {username}')
                    message_text = f'''
<b>Hit User TELEGRAM </b>
******************
@<code>{username}</code>
##############

BY @alonemarkaa - @sanallider
'''
                    response = requests.post(
                        f'https://api.telegram.org/bot{tok}/sendMessage',
                        data={
                            'chat_id': id,
                            'text': message_text,
                            'parse_mode': 'HTML'
                        }
                    )
            except:
                print(Z + f'Bad user Telegram : {username}')
        else:
            print(Z + f'Bad user Telegram : {username}')

# Thread oluşturma
Threads = []
for t in range(50):  # 50 farklı thread başlatıyoruz
    x = threading.Thread(target=check_username)
    x.start()
    Threads.append(x)

# Thread'lerin tamamlanmasını bekle
for Th in Threads:
    Th.join()