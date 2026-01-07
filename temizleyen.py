import re
import string

def temizle(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    # HTML taglerini temizle
    data = re.sub(r"<!DOCTYPE.*?>", "", data, flags=re.IGNORECASE | re.DOTALL)
    data = re.sub(r"<html.*?>|</html>", "", data, flags=re.IGNORECASE)
    data = re.sub(r"<body.*?>|</body>", "", data, flags=re.IGNORECASE)
    data = re.sub(r"<.*?>", "", data, flags=re.DOTALL)

    # Görünmez / bozuk karakterleri temizle
    temiz = "".join(
        ch for ch in data
        if ch in string.printable or ch == "\n"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(temiz)

    print(f"[✓] Temiz dosya oluşturuldu: {output_file}")

if __name__ == "__main__":
    temizle("chk.py", "chk_temiz.py")