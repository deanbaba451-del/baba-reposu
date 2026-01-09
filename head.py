import requests
import ssl
import socket
from urllib.parse import urlparse
def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
        info = "\n SSL Sertifika Bilgileri:\n"
        info += f"• Yayınlayan: {cert.get('issuer')}\n"
        info += f"• Geçerlilik Başlangıç: {cert['notBefore']}\n"
        info += f"• Geçerlilik Bitiş: {cert['notAfter']}\n"
        return info
    except:
        return "\ SSL bilgisi alınamadı."
def fetch_headers(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        r = requests.get(url, timeout=6, allow_redirects=True)
        result = " Site Bilgisi\n"
        result += f" URL: {r.url}\n"
        result += f" Status Code: {r.status_code}\n\n"
        result += " Headerlar:\n"
        for key, value in r.headers.items():
            result += f"• {key}: {value}\n"
        if r.cookies:
            result += "\n🍪 Cookies:\n"
            for cookie in r.cookies:
                result += f"• {cookie.name} = {cookie.value}\n"
        parsed = urlparse(url)
        if parsed.scheme == "https":
            result += get_ssl_info(parsed.hostname)
        return result
    except Exception as e:
        return f"❌ Hata: {e}"
if __name__ == "__main__":
    site = input("Site gir: ")
    print(fetch_headers(site))
