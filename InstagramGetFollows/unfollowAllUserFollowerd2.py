import sys

import requests
import base64
import requests
import time

from InstagramAPI import login



username = "giulio_tavella"#str(sys.argv[1])
password = "21CICCIO21ciccio"#str(sys.argv[2])
numero_utenti_da_defollow = 140

def accorcioResponse(response):
    return response[response.find("\"username\":\"") + len("\"username\":\""):]


headers = {
    'pragma': 'no-cache',
    'cookie': 'ds_user_id=819693525; csrftoken=uIRAdAycNyPwxwZfb3oejtNfS26052AM; shbid=18815; sessionid=IGSCb82b71795320950eac0f74c2c46e93e041fd22a31bd122087af53dbfe5b05c35%3ABpVrs3l2hTqVvqZmElEKC4IRe0H1imDh%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ABqqRucQSEvqwNuZtYw0e6eyzVg83VgVG%3A3b3a9e8b7f5555b9479f5e474d30bdbb7c59a1141b2d89f50c08740962d514b0%22%2C%22last_refreshed%22%3A1539522157.3820323944%7D; rur=FRC; ig_cb=1; mid=W8M-bAAEAAF0AtY2upYe5T9gWcWD; mcd=3; shbts=1539522158.405899; urlgen="{\\"2001:b07:ac9:e9a2:5d1e:8fbf:2b21:648e\\": 12874}:1gBg2d:-cBFc2aDyfVF5ZuuwIAZO-VUxFc"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': 'b29d031141e0f95b87f6bf55d0a71069',
    'referer': 'https://www.instagram.com/giulio_tavella/following/',
}

params = (
    ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
    ('variables', '{"id":"819693525","include_reel":true,"fetch_mutual":false,"first":50}'),
)

response = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)
end_cursor = response[response.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):response.find("\"},\"edges\":[{\"node\"")] #QVFEQ0E3MW0xM3U4Z0VnMzU3YllwdC0wNGpxSlAxZ1FweGs5NjFlQi1MWDgtZXRvUmM0MHdoa1ZubldmdzV1emx2eWNObEZWQXRvcDMyRjViVXk2b0lzaA==
print(response)
print(end_cursor)

#da qui in poi cerco gli username
numero_username = response.count("\"username\":\"")

#accorcio la risposta in modo da ottenere subito gli username
response = response[response.find("\"username\":\"") + len("\"username\":\""):]
array_utenti_da_defollow = []
for i in range(0,numero_username):
    username = response[:response.find("\",\"full_name\"")]


    if len(username) < 20:
        print("UU " + username)
        array_utenti_da_defollow.append(username)
    response = accorcioResponse(response)

#Qui ne chiedo altri 50
while len(array_utenti_da_defollow) < numero_utenti_da_defollow:
    headers = {
        'pragma': 'no-cache',
        'cookie': 'ds_user_id=819693525; csrftoken=uIRAdAycNyPwxwZfb3oejtNfS26052AM; shbid=18815; sessionid=IGSCb82b71795320950eac0f74c2c46e93e041fd22a31bd122087af53dbfe5b05c35%3ABpVrs3l2hTqVvqZmElEKC4IRe0H1imDh%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ABqqRucQSEvqwNuZtYw0e6eyzVg83VgVG%3A3b3a9e8b7f5555b9479f5e474d30bdbb7c59a1141b2d89f50c08740962d514b0%22%2C%22last_refreshed%22%3A1539522157.3820323944%7D; rur=FRC; ig_cb=1; mid=W8M-bAAEAAF0AtY2upYe5T9gWcWD; mcd=3; shbts=1539522158.405899; urlgen="{\\"2001:b07:ac9:e9a2:5d1e:8fbf:2b21:648e\\": 12874}:1gBg2k:t6HfbesIo2Nf_0NPKEJg_AN49H4"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': '4e2ef70d566fde5cfbd5596cf2e9e71c',
        'referer': 'https://www.instagram.com/giulio_tavella/following/',
    }

    params = (
        ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
        ('variables', '{"id":"819693525","include_reel":true,"fetch_mutual":false,"first":12,"after":"'+end_cursor+'"}'),
    )

    response = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)
    end_cursor = response[response.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):response.find(
        "\"},\"edges\":[{\"node\"")]  # QVFEQ0E3MW0xM3U4Z0VnMzU3YllwdC0wNGpxSlAxZ1FweGs5NjFlQi1MWDgtZXRvUmM0MHdoa1ZubldmdzV1emx2eWNObEZWQXRvcDMyRjViVXk2b0lzaA==
    numero_username = response.count("\"username\":\"")
    response = response[response.find("\"username\":\"") + len("\"username\":\""):]
    for i in range(0, numero_username):
        username = response[:response.find("\",\"full_name\"")]

        if len(username) < 20:
            print("UU " + username)
            array_utenti_da_defollow.append(username)
        response = accorcioResponse(response)

print(array_utenti_da_defollow)