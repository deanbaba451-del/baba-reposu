# temizle.py

# Orijinal ve yeni dosya isimleri
input_file = "sovus.py"
output_file = "sovus_clean.py"

# Dosyayı oku ve temizle
with open(input_file, "rb") as f:
    content_bytes = f.read()

# UTF-8 dışındaki karakterleri ignore ederek decode et
clean_content = content_bytes.decode("utf-8", errors="ignore")

# Temizlenmiş içeriği yeni dosyaya yaz
with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_content)

print(f"Dosya temizlendi ve '{output_file}' olarak kaydedildi.")