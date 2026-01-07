import random
import string

def generate_play_code():
    """16 haneli rastgele Play kodu oluşturur."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

def is_code_valid():
    """Kodu geçersiz yapma oranını kontrol eder (örneğin %10 çalışabilir)."""
    return random.random() < 0.1  # LOREXTOOL

def generate_captcha():
    """Emoji ile süslenmiş bir CAPTCHA döndürür."""
    emojis = ['✨', '🔥', '💥', '🎉', '🌟']
    message = "Katıl:@lorextool"
    captcha = f"{' '.join(random.choices(emojis, k=3))} {message} {' '.join(random.choices(emojis, k=3))}"
    return captcha

def main():
    while True:
        try:
            count = int(input("Kaç adet Play kodu oluşturmak istiyorsunuz? "))
        except ValueError:
            continue

        for _ in range(count):
            code = generate_play_code()
            valid = is_code_valid()
            captcha = generate_captcha()

            print(f"Kod: {code}")
            print(f"Durum: {'Geçerli ✅' if valid else 'Geçersiz ❌'}")
            print(f"CAPTCHA: {captcha}")
            print("--------------------------")

        cont = input("Daha fazla üretmek için bir tuşa basın (çıkmak için 'q' girin): ")
        if cont.lower() == 'q':
            break

if __name__ == "__main__":
    main()
