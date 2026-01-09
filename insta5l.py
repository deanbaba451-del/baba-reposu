import requests,random,threading,os;from cfonts import render
T=render('{user}',colors=['white','blue'],align='center')
print(f"\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n          {T}\n~Programmer:@T5OMASR|Channel:@THOMASHACK~\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n");print("—"*60)
cid=input("•Id:");print("—"*60);tok=input("•Token:");os.system("clear")
hit,good,bad,fb=0,0,0,0;L=threading.Lock()
def p(user,tok,cid):
    global hit,good,bad,fb
    try:
        r=requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',
            headers={'Host':'www.instagram.com','content-length':'85','sec-ch-ua':'" Not A;Brand";v="99","Chromium";v="101"','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','sec-ch-ua-mobile':'?0','x-instagram-ajax':'81f3a3c9dfe2','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/101.0.4951.40 Safari/537.36','x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-encoding':'gzip,deflate,br','accept-language':'en-IQ,en;q=0.9','cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv;mid=YtsQ1gABAAEszHB5wT9VqccwQIUL;ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425;ig_nrcb=1'},
            data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
        with L:
            os.system("clear");s=r.text
            if'feedback_required'in s or'"errors": {"username"'in s or'"code":"username_is_taken"'in s:
                bad+=1;print(f"\rHit:{hit}~Bad:{bad}~User:{user}")
            else:
                hit+=1;print(f"\rHit:{hit}~Bad:{bad}~User:{user}")
                msg=f"𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨\n🇹🇷 Kullanıcı Adı:{user}\nTelegram:@thomashack|@t5omasr\n𒋨────━𓆩𝐓𝐇𝐎𝐌𝐀𝐒𓆪‏━────𒋨"
                requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={cid}&text={msg}')
    except:pass
def k(choice,tok,cid):
    vwl="aeiou";cns="bcdfghjklmnpqrstvwxyz";allc="1234567890qwertyuiopasdfghjklzxcvbnm._"
    while 1:
        if choice==1:
            user=''.join(random.choice(vwl if i%2<1 else cns) for i in range(5))
        elif choice==2:
            user=''.join(random.choice("abcdefghijklmnopqrstuvwxyz.") for _ in range(5))
        else:
            user=''.join(random.choice(allc) for _ in range(5))
        p(user,tok,cid)
if __name__=="__main__":
    print(T);print("—"*60)
    print("1-VIPUSERAPI|2-RandomAPI|3-RandomAPIv2")
    n=int(input("•Choice:"))
    for _ in range(15):threading.Thread(target=k,args=(n,tok,cid)).start()