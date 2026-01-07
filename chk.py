import requests
import random
import string
import time
import asyncio
import re
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
class KullaniciAdiKontrol:
    def __init__(self, token, chat_id):
        self.console = Console()
        self.token = 8110267443:AAHNAgx0Yleg6JKLXomoTuhB_zEte-g-8HI
        self.chat_id = 6534222591
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; x64)"
        })
        self.rate_limit = 0.05  
        self.batch_size = 50  
        self.kontrol_edilenler = set()
    def kullanici_adi_olustur(self, platform):
        while True:
            if platform == "instagram":
                uzunluk = 4  
            elif platform == "tiktok":
                uzunluk = 5  
            else:
                uzunluk = 4  
            karakterler = string.ascii_lowercase + string.digits
            kullanici_adi = ''.join(random.choices(karakterler, k=uzunluk))
            if re.fullmatch(r"[a-z\d]{4,5}", kullanici_adi):
                return '@' + kullanici_adi
    async def kullanilabilir_mi(self, kullanici_adi, platform):        
        if kullanici_adi in self.kontrol_edilenler:
            return False
        self.kontrol_edilenler.add(kullanici_adi)
        url = ""
        if platform == "instagram":
            url = f"https://www.instagram.com/{kullanici_adi[1:]}/"
        elif platform == "tiktok":
            url = f"https://www.tiktok.com/@{kullanici_adi[1:]}"
        for _ in range(2):  
            try:
                r = await asyncio.to_thread(self.session.get, url, timeout=3)  
                if r.status_code == 404:
                    return True
                if r.status_code == 200:                
                    if "Page Not Found" in r.text or "Couldn't find this account" in r.text:
                        return True
                    return False
                return False
            except Exception:
                await asyncio.sleep(0.3)  
        return False
    def telegrama_gonder(self, platform, kullanici_adi):        
        mesaj = (
            f"â **YENÄ° HÄ°T BULUNDU!**\n"
            f"**Platform:** {platform.upper()}\n"
            f"**KullanÄ±cÄ± AdÄ±:** `{kullanici_adi}`\n"
            f"**Durum:** KullanÄ±labilir!\n"
            f"**Telegram :**@SahalBen"
        )
        try:
            self.session.post(
                f"https://api.telegram.org/bot{self.token}/sendMessage",
                data={
                    "chat_id": self.chat_id,
                    "text": mesaj,
                    "parse_mode": "Markdown"
                }
            )
        except requests.RequestException:
            self.console.print(f"[red]Telegram'a gÃ¶nderilemedi: {kullanici_adi}[/red]")
    async def kullanici_kontrol_et(self, kullanici_adi, platform, progress, gÃ¶rev):
        progress.update(gÃ¶rev, description=f"{kullanici_adi} ({platform}) kontrol ediliyor")
        kullanilabilir = await self.kullanilabilir_mi(kullanici_adi, platform)
        renk = "green" if kullanilabilir else "red"
        self.console.print(
            Panel(
                f"[bold {renk}]{kullanici_adi}[/bold {renk}] - {platform}",
                border_style=renk
            )
        )
        if kullanilabilir:
            self.telegrama_gonder(platform, kullanici_adi)
        await asyncio.sleep(self.rate_limit)
    async def toplu_kontrol(self, platformlar):     
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            gÃ¶rev = progress.add_task("BaÅlatÄ±lÄ±yor...", total=None)
            while True:
                gÃ¶revler = []
                for _ in range(self.batch_size):
                    platform = random.choice(platformlar)
                    kullanici_adi = self.kullanici_adi_olustur(platform)
                    gÃ¶revler.append(self.kullanici_kontrol_et(kullanici_adi, platform, progress, gÃ¶rev))
                await asyncio.gather(*gÃ¶revler)
def main():
    token = input("Bot Token Gir: ")
    chat_id = input("Chat ID Gir: ")
    print("SeÃ§im yapÄ±nÄ±z:")
    print("1 - TikTok")
    print("2 - Instagram")
    print("3 - Her ikisi")  
    secim = input("SeÃ§iminizi yapÄ±n : ")
    if secim == "1":
        return token, chat_id, ["tiktok"]
    elif secim == "2":
        return token, chat_id, ["instagram"]
    elif secim == "3":
        return token, chat_id, ["instagram", "tiktok"]
    else:
        print("GeÃ§ersiz seÃ§enek! DÃ¼zgÃ¼n deneyin.")
        return main()
async def baslat():
    console = Console()
    console.print(
        Panel(
            Text("KullanÄ±cÄ± AdÄ± Kontrol", style="bold cyan", justify="center"),
            subtitle="SÄ°ZLERÄ° SEVÄ°YORUMâ¤ï¸",
            border_style="blue"
        )
    )
    animation = Text("SEX BAÅLIYORR ", style="bold green")
    animation.append(".")
    for _ in range(3):
        console.print(animation)
        await asyncio.sleep(0.5)
        animation.append(".")    
    token, chat_id, platformlar = main()
    kontrol = KullaniciAdiKontrol(token, chat_id)    
    console.print("[yellow]Taramaya baÅlÄ±yoruz...[/yellow]")
    try:
        await kontrol.toplu_kontrol(platformlar)
    except KeyboardInterrupt:
        console.print("[yellow]Program durduruldu![/yellow]")
if __name__ == "__main__":