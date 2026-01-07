import string

# Temizlenecek dosya ve oluşturulacak yeni dosya
input_file = "bba.py"
output_file = "bba_clean.py"

# Sadece yazdırılabilir karakterleri ve yeni satır karakterlerini kabul ediyoruz
allowed_chars = string.printable

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Geçerli karakterleri filtrele
cleaned_content = "".join(c for c in content if c in allowed_chars)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(cleaned_content)

print(f"Temiz dosya '{output_file}' olarak oluşturuldu.")