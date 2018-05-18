import json
import random
import time

import requests


#Dato ub username ottengo l'id della prima immagine per il primo like
def da_username_ottengo_id_prima_immagine(username):
    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'shbid=18815; rur=FRC; mid=Wv04-wAEAAHKaoK4SD8Hm37McmMb; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; fbsr_124024574287414=4SjrOMXaEn9avgH7pDc6wfhS8XpvF3nWJbOGtLiHU8I.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUQ4S2J4T3VjYTdxSGFzcEZ6ZzhqTWdvdnhUU05nWTczaTVUdVJYdU1rby1oUnFnRWpKV21mNXEtVnlxUkRxc0ZHM3ZwQ0JTTW1BWkJUOW05eVoyTndUT3piY2dvMTd6Q0VZSG9FdVgxTHc1RzlneUZrWmQtZTUzck1ZSnowdkFXdVgzTm9aTFdvWjhDenhzMzhLR1BpQ3ViRk82NV9Yc2JCMWJaTFV0bmZuRGZ0anVmZUUweTNxejdvMEg2VHJkZU5rbmljOFA4eW1hS2U1VFZHa2hKWWlvY21ZRU5fa0U5UjFBc0NQY0hUdmdyNWJENXZ5VXNBNWJDejQxVldDNm9ILUUzckRPbUo1dXAyUElhVjQ5WlFEUTBNaW9xaTlYd0pJamx5RXRGc1Jrd0RwR2tqclRzMXl2bmJlQTR3Y3pkLU1ZX0JLOGtETkNWSWY5aEZGTDlzXyIsImlzc3VlZF9hdCI6MTUyNjU0NTQxNCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1526544635\\054 \\"193.55.113.196\\": 2200}:1fJECO:1s0EgO4Z4xw4Fpl3x6S20oX0Ft0"',
    }

    response = str(requests.get('https://www.instagram.com/'+username+'/', headers=headers).content)
    id_1 = response[response.find("__typename") + 31: response.find("edge_media_to_caption")-3]
    print(id_1)
    return id_1

def da_id_e_username_metto_like(id,username):

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'cookie': 'shbid=18815; rur=FRC; mid=Wv04-wAEAAHKaoK4SD8Hm37McmMb; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; fbsr_124024574287414=w0bmyY6LTRCmLqUM-6uzYoabrtie3pJSySQLj5lp6tg.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFtMlRLajdwX1pVLVhNN2VkTDlSY1pHRzBFX1kzcVVTZlhIRzRKRFVURFVoWFNXQjFHT0Z4UFBTclRtWE9hQlJoMUNFazRCMWxUbVpuZVozX3ZVV3ZCcjNoZXBZVGxwXzBDQlZYeHBheExEa2lVLUx4bGt1UW9jWkQwNWdlY2hPS0cyeGJ4d1Uxd0NvX3N4X0dpdU5PR1VoTEIxWjQyTFh3aXY1bjRqQUNFRW9ucDV4VXd4SExVd19xWUxOQXBjRzNDOC1YQWtSQ3RnWkNQbU5CUjRLZ2Vfd1Jyck1heWpGbEwyTFRQT09aNmlSZHk5N2FLeFdSQUlVX2xhWDZiVDlTNVpHLWdzaEpoZHEtVmt4RGlsMFpJYmtLRk1RRXZBb21ZbUJjVzlCS1V0Skp3OEdLczJINTZ5ZWZneDhRVlg0R0hRWVRJWU8zaXhNV0RDcklTRkUyRyIsImlzc3VlZF9hdCI6MTUyNjU0NTQ4MCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1526544635\\054 \\"193.55.113.196\\": 2200}:1fJEE6:uFMHmHhgTxA7LmyaYLwsgk7ZruY"',
        'x-csrftoken': 'F1cSYjQFyJ13hBayadSHigpivVa7PvTX',
        'x-instagram-ajax': '1b36312e9ac7',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BiPYa5IDaXY/?taken-by='+username+'',
        'authority': 'www.instagram.com',
        'content-length': '0',
    }
    response = requests.post('https://www.instagram.com/web/likes/'+id+'/like/', headers=headers)
    print("ID DELLA FOTO DI " + username + " = " + id)
    print(response.content)

def ottengoDatiDalServerMio():
    return json.loads(requests.get("http://2.230.243.113/getFoulo.php").content)


if __name__ == "__main__":
    data = ottengoDatiDalServerMio()
    numero_dati = len(data)
    indice = 0
    for i in range(1234, numero_dati):
        print(i)
        indice = indice + 1
        # Dopo 20 secondi mi fermo per 20 secondi
        if indice % 4 == 0:
            time.sleep(20)

        id = data[i]["ID"]
        username = data[i]["USERNAME"]
        print("Metto like a " + username)
        da_id_e_username_metto_like(da_username_ottengo_id_prima_immagine(username),username)
        time.sleep(15 + random.randint(3, 6))





