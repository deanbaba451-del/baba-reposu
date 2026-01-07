# temizle.py
import unicodedata

INPUT = "main.py"
OUTPUT = "main_clean.py"

with open(INPUT, "rb") as f:
    raw = f.read()

# UTF‑8 BOM varsa temizle
if raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

text = raw.decode("utf-8", errors="ignore")

clean_chars = []
for ch in text:
    cat = unicodedata.category(ch)

    # Görünmez / format karakterlerini SİL
    if cat in ("Cf",):  # zero-width, BOM, vs
        continue

    # NBSP → normal boşluk
    if ch == "\u00a0":
        clean_chars.append(" ")
    else:
        clean_chars.append(ch)

clean_text = "".join(clean_chars)

# Satır sonlarını normalize et
clean_text = clean_text.replace("\r\n", "\n").replace("\r", "\n")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(clean_text)

print("OK → görünmez karakterler temizlendi:", OUTPUT)