import requests
import time







#@Ritalin404
#@godlesstekno






S = '\033[33m'
B = '\033[37m'
Y = '\033[92m'
K = '\033[91m'

print(K+'''⣿⣟⡿⣟⣿⣻⢿⣻⣟⡿⣟⣿⡻⢿⣻⣿⡻⣟⡿⣟⣿⣻⢿⣻⣟⡿⣟⣿⣻⢿
⣿⣞⡿⣯⣷⢿⣻⣽⠾⠛⠉⠀⠀⠀⣀⣠⣤⡴⠚⠛⠳⣿⣻⣽⡾⣟⣯⣷⢿⣻
⣿⡼⣿⣻⣼⡿⣟⠛⠀⠀⠀⠀⣠⣼⣿⣻⠇⠀⠀⠀⠀⠀⠻⣧⣿⢿⣻⣼⡿⣿
⣿⡽⣿⡽⣞⡟⠁⠀⠀⠀⢠⣾⣟⡷⣯⣿⠀⠀⠀⠀⠀⠀⠀⠙⢾⡿⣽⣳⡿⣽
⣿⡽⣷⢿⡛⠀⠀⠀⠀⢠⣿⣟⡾⣿⡽⣯⡿⣷⣦⡀⠀⠀⠀⠀⠘⣿⢯⡿⣽⢿
⣿⣽⣻⢿⡅⠀⠀⠀⠀⣿⢷⣯⢿⡷⣟⣯⣿⣳⣯⢿⡀⠀⠀⠀⠀⢸⣿⣻⢯⣿
⣿⣞⣯⣿⠀⠀⠀⠀⠀⣿⣻⢾⡿⣽⣻⢷⣯⡷⣟⡿⣇⠀⠀⠀⠀⢸⣷⣻⢿⣽
⣿⡽⣿⣽⠆⠀⠀⠀⠀⢻⣟⡾⣷⣻⣟⣾⡽⣷⢿⣳⠏⠀⠀⠀⠀⢸⣯⢿⣞⣿
⣿⡽⣷⣻⣇⠀⠀⠀⠀⠀⠻⣿⡽⣷⣻⣽⣻⣽⡟⠏⠀⠀⠀⠀⢀⣿⡽⣯⡿⣾
⣿⣽⣻⢷⣻⣇⠀⠀⠀⠀⠀⠈⠙⠋⠿⠷⠛⠃⠁⠀⠀⠀⠀⢀⣿⣽⣻⣽⢿⣽
⣿⣞⣿⣻⣽⣻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣻⢾⣽⢯⣿⢾
⣿⣾⢳⣿⢳⣿⣯⣿⢳⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⡟⣿⣾⣽⣿⣽⢻⣾⣿
⣿⢾⣻⣽⢿⡾⣽⡾⣟⣯⡿⣟⣶⡶⣤⣶⢶⣶⣿⣻⢷⣟⡿⣞⣷⣯⣟⣯⣷⢿
⣿⣻⣽⢯⣿⡽⣿⣽⣻⢷⣟⣿⣳⢿⣻⡽⣟⣾⣳⣿⣻⢾⣟⣯⣷⣟⡾⣟⣾⢿''')
print(B+"\nVodafone 150 Gb Alma Tool\n")


cookies = {
    'f5avraaaaaaaaaaaaaaaa_session_': 'EAEFPABPBCPADNNMLGOBADDGGDCDJEMJGGLJALEEFEAAACEKBAPIKPCKJHDAMKPFFOADAHHCHIJICGAAKBOAEOHMHLEEMDNHCJHOJFDAJMJHDCBNCDHOKJPGACCGCPDA',
    '0458575580b69d9c2f5da7501c44bda1': 'c69553830742568da5c23316e515f6e4',
    'Vodafone': '!nFlzcM1dTrvOH48zhFmGl/Zx8GzsljUe2LOZ/1mPOCLSUd8G2ilALJEuFxLs5jjRTniK9bIdX9Lagm4=',
    'utag_main__sn': '1',
    'utag_main_ses_id': '1732294824649%3Bexp-session',
    'OptanonAlertBoxClosed': '2024-11-22T17:00:28.571Z',
    'utag_main__ss': '0%3Bexp-session',
    'utag_main_vapi_domain': 'vodafone.com.tr',
    's_fid': '48790EE4A2CB6289-27D1926D972B4AC2',
    's_cc': 'true',
    '_gcl_au': '1.1.956115259.1732294829',
    'at_check': 'true',
    '_ga': 'GA1.1.216672396.1732294829',
    's_vi': '[CS]v1|33A05C5717C657D6-40000B482483AA5A[CE]',
    '_fbp': 'fb.2.1732294829752.155018018299024079',
    'AMCVS_C1701C8B532E6C990A490D4D%40AdobeOrg': '1',
    '_tt_enable_cookie': '1',
    '_ttp': 'qz-Vug5w9NL1Wu-bT2UULkndD0q.tt.2',
    's_ecid': 'MCMID%7C26553906245585140084508814135803485316',
    'AMCV_C1701C8B532E6C990A490D4D%40AdobeOrg': '1176715910%7CMCIDTS%7C20050%7CMCMID%7C26553906245585140084508814135803485316%7CMCAAMLH-1732899630%7C6%7CMCAAMB-1732899630%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1732302030s%7CNONE%7CMCAID%7C33A05C5717C657D6-40000B482483AA5A%7CvVersion%7C5.4.0',
    'utag_main__pn': '2%3Bexp-session',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22TyBYe1ZLyt1wItG4JbSh%22%2C%22expiryDate%22%3A%222025-11-22T17%3A00%3A31.572Z%22%7D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Nov+22+2024+20%3A00%3A31+GMT%2B0300+(GMT%2B03%3A00)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8e23c08e-64f7-4044-819a-af2979c756e9&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=TR%3B&AwaitingReconsent=false',
    'utag_main__se': '9%3Bexp-session',
    'utag_main__st': '1732296649226%3Bexp-session',
    '_ga_KV33Y2N8ST': 'GS1.1.1732294829.1.1.1732294849.40.0.0',
    'mbox': 'session#00526f4c7290479aa6f159800223c857#1732296710|PC#00526f4c7290479aa6f159800223c857.37_0#1795539650',
    'VF02abd0f0': '02b25bcfcb78c90149830af48312a3a426dd4264bb62897845afcd0544c6ab6dbf75807cf48e5471c10bbc281bd632aab5cb4ae3cd4e027850f06ee1b322e8f3fb83c0f5fa25acef92e719756d0044a5cf3d256db1e0ae2029313bf6350dacda6e07a6e90e2eca638098a4ceaf5422ba5d951de9c2',
    'VFa24a1cc3029': '085b62fc7eab2000f590975c76ed76aa41fd71f45eb8d177c7bcf263b1cffbbf95008faf57155c9908c115b63e113000c531e2d680433164293547c172bd7952fd3ba529e8b328bc06cf90e80303eb381e0518a1f8821fb6913623d2f050a48a',
}

headers = {
    'authority': 'www.vodafone.com.tr',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.vodafone.com.tr',
    'referer': 'https://www.vodafone.com.tr/anket/arastirma-anketi-912',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

no = int(input(S+"Numara girin (5xxxx): "+B))

json_data = {
    'control_key': '',
    'branch_code': '',
    'survey_id': '912',
    'otp_code': '',
    'is_nvf_user': '',
    'sid': '',
    'data_type[4765]': no,
    'data_type[4789]': 'Hizmet',
    'data_type[4789][other]': '',
    'data_type[4790]': '',
    'data_type[4784]': '',
    'data_type[4784][other]': '',
    'data_type[4787]': '',
    'data_type[4787][other]': '',
    'session_id': 'x4oqu3fevt495',
}

for i in range(30):
    try:
        response = requests.post(
            'https://www.vodafone.com.tr/api/survey',
            cookies=cookies,
            headers=headers,
            json=json_data
        )
        if response.status_code == 200:
            print(f"{Y}Başarılı ({i + 1}): {response.json()}")
        else:
            print(f"{K}Hata ({i + 1}): {response.status_code} - {response.text}")
        time.sleep(2)
    except requests.RequestException as e:
        print(K+"Bağlantı hatası")