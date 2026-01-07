from colorama import Fore, Style, init
import requests, json, os
init(autoreset=True)
class Batuflex:
    def __init__(self):
        self.headers = {
            'authority': 'www.fenomist.com',
            'accept': 'text/html, */*; q=0.01',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.fenomist.com',
            'referer': 'https://www.fenomist.com/telegram-ucretsiz-kanal-uyesi',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
    def ebenmi(self):
        belkieben = f"""{Fore.BLUE}
{self.centered("â â â â â â â â â â â â â â â â â â â£â£¤â£´â£¾â£¿â£¿â£¿â¡")}
{self.centered("â â â â â â â â â â â â â â¢â£ â£´â£¶â£¿â£¿â¡¿â ¿â â¢â£¿â£¿â ")}
{self.centered("â â â â â â â â â¢â£â£¤â£¶â£¾â£¿â£¿â ¿â â â â â â â£¸â£¿â£¿â ")}
{self.centered("â â â â â£â£¤â£´â£¾â£¿â£¿â¡¿â â â â â â£ â£¤â â â â â£¿â£¿â¡â ")}
{self.centered("â â£´â£¾â£¿â£¿â¡¿â ¿â â â â â â¢â£ â£¶â£¿â â â â â â¢¸â£¿â£¿â â ")}
{self.centered("â ¸â£¿â£¿â£¿â£§â£â£â â â£â£´â£¾â£¿â£¿â â â â â â â â£¼â£¿â¡¿â â ")}
{self.centered("â â â â »â ¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â â â â â â â â â¢ â£¿â£¿â â â ")}
{self.centered("â â â â â â â â£¿â£¿â£¿â£¿â¡â â£â£â¡â â â â â¢¸â£¿â£¿â â â ")}
{self.centered("â â â â â â â â ¸â£¿â£¿â£¿â£ â£¾â£¿â£¿â£¿â£¦â¡â â â£¿â£¿â¡â â â ")}
{self.centered("â â â â â â â â â¢¿â£¿â£¿â£¿â¡¿â â â »â£¿â£¿â£¦â£¸â£¿â£¿â â â â ")}
{self.centered("â â â â â â â â â â â â â â â â â â »â£¿â£¿â£¿â â â â â ")}
"""
        print(belkieben)
        print(Fore.CYAN + "=" * 60)
        print (Fore.RED + "by: @Zeynalovs5")
        print(Fore.CYAN + "=" * 60)
    def centered(self, nataÅa):
        uzatmabebekyataÅa = os.get_terminal_size().columns
        return nataÅa.center(uzatmabebekyataÅa)
    def sapladÄ±(self):
        self.ebenmi()
        batu = input(Fore.GREEN + 'â¢ KANAL LÄ°NKÄ° GÄ°R KANKA: ' + Fore.BLUE)
        print(Fore.YELLOW + "=" * 60)
        data = {
            'captcha': '',
            'page': '15712',
            'free_email': '',
            'user': batu,
            'product_id': '527',
        }
        try:
            response = requests.post('https://www.fenomist.com/free-profile', headers=self.headers, data=data)
            manita = response.json()
            if manita.get("status") == "success":
                print(Fore.GREEN + "[BAÅARILI] " + manita.get("returnMessage"))
            else:
                print(Fore.RED + "[BAÅARISIZ] " + manita.get("returnMessage"))
        except json.JSONDecodeError:
            print(Fore.YELLOW + "[HATA] GeÃ§ersiz yanÄ±t alÄ±ndÄ±:\n" + response.text)
Batuflex().sapladÄ±()