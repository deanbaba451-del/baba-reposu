import requests

def eizon(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                           '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                           'en_GB; 161478664)'),
            'Accept-Language': 'en-GB,en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
        }

        data = {
            'signed_body': (
                '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                f'{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                f'"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                f'"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                f'"device_id":"android-b93ddb37e983481c",'
                f'"query":"{user}"}}'
            ),
            'ig_sig_key_version': '4'
        }

        url = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print("baÅarÄ±lÄ±:")
            print(response.json())
        else:
            print(f"Hata: HTTP {response.status_code}")
            print(response.text)

    except Exception as e:
        print("hata:", e)

if __name__ == "__main__":
    user = input("KullanÄ±cÄ± adÄ± girin: ")
    eizon(user)




#by @besteizon channel @eizonxtool