import requests
from bs4 import BeautifulSoup

k = input("Site adi gir: ")

r = requests.post(
    "https://tools.prinsh.com/home/",
    params={"tools": "adfind"},
    cookies={"VISITOR": "mobile", "BROWSER": "Google%20Chrome"},
    headers={
        "authority": "tools.prinsh.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-language": "tr-TR,tr;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://tools.prinsh.com",
        "referer": "https://tools.prinsh.com/home/?tools=adfind",
        "user-agent": "Mozilla/5.0 (Linux; Android 10) Chrome Mobile"
    },
    data={"url": k, "submit": "Check Now!!!"}
)

s = BeautifulSoup(r.text, "html.parser")
p = s.find("p", string="Result:")

[print(("\033[91m[NOT FOUND]\033[0m " if "does not exist" in t else "\033[92m[FOUND]\033[0m ") + t)
 for t in ([b.get_text(strip=True) for b in p.find_all_next("b")] if p else [])]