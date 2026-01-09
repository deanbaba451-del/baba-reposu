# temizl_turkce.py

input_file = "sovus.py"
output_file = "sovus_clean.py"

# Türkçe karakterler ve standart ASCII
allowed_chars = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "çğıöşüÇĞİÖŞÜ"
    " \t\n\r.,:;!?()[]{}+-=*/%\"'<>@#$^&_`|~\\"
)

try:
    # Orijinal dosyayı oku
    with open(input_file, "rb") as f:
        content_bytes = f.read()
    
    # UTF-8 olarak decode et (ignore ile problemli byte’ları at)
    content = content_bytes.decode("utf-8", errors="ignore")

    # Yalnızca allowed_chars içindekileri tut
    clean_content = "".join(c for c in content if c in allowed_chars)

    # Dosyanın başına encoding bildirimi ekle
    encoding_header = "# -*- coding: utf-8 -*-\n"
    clean_content = encoding_header + clean_content

    # Yeni dosyaya yaz
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(clean_content)

    print(f"Dosya temizlendi ve '{output_file}' olarak kaydedildi. Türkçe karakterler korundu!")

except FileNotFoundError:
    print(f"Hata: '{input_file}' dosyası bulunamadı.")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")