import requests
from InstagramAPI import follow
from InstagramAPI import ottengoDatiDalServerMio
import sys
import time


def login(username,password):

    headers = {
        'cookie': 'ig_cb=1',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'Y5RToHUnJaNvziqQ24edFlMB0CFd3fH6',
        'pragma': 'no-cache',
        'x-instagram-ajax': '8958fe1e75ab',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/',
    }

    data = [
        ('username', username),
        ('password', password),
        ('queryParams', '{}'),
    ]

    response = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
    return response

if __name__ == "__main__":
    print "starting requests"
    username = sys.argv[1]
    password = sys.argv[2]
    r = login(username,password)
    print r.content
    print "*****************************"
    cookies_dict = r.cookies.get_dict()

    cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)
    print(cookies_str[:-2])
    utenti = ottengoDatiDalServerMio()
    for i in range(12000,13000):
        utente = utenti[i]
        print(username + " sta seguendo -> username : " + utente["USERNAME"] + " ID " + utente["ID"])
        follow(utente["ID"], utente["USERNAME"], cookies_str, cookies_dict['csrftoken'])
        time.sleep(30)
