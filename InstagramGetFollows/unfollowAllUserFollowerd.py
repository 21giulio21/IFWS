import sys

import requests
import base64
import requests
import time

from InstagramAPI import login



username = str(sys.argv[1])
password = str(sys.argv[2])



def getIDFromUsername(username):

    headers = {
        'authority': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; rur=FRC; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; sessionid=IGSC8ed527fc1cda43ac5555695cbba25d643a1f566c1a145452aeb5b67b12fb5305%3A17hUaA9Ul0DdZyAsj2Os4HkJ1yVzZfCg%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527681913.5427627563%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1527681913\\054 \\"193.55.113.196\\": 2200}:1fO1o7:2az6OzqMKD6FoWtZ4xZOuq8St1Q"',
    }

    response = str(requests.get('https://www.instagram.com/' + username, headers=headers).content)
    posizioneprofilePage_= response.find("profilePage_")
    inizio_id = response[posizioneprofilePage_ + len("profilePage_"):]
    id = str(inizio_id[:inizio_id.find("\"")])
    return id



def unfollw2(cookies, csrf):


    #Ottengo i primi 24 che seguo e ne prendo 1

    headers = {
        'pragma': 'no-cache',
        'cookie': cookies ,
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': csrf,
        'referer': 'https://www.instagram.com/'+username+'/following/',
    }

    params = (
        ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
        ('variables', '{"id":'+id+',"include_reel":true,"first":24}'),
    )

    content_request =  str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)
    usernameToUnfollow = content_request[content_request.find("username") + len("username\":\""):content_request.find("\",\"full_name\"")]
    idToUnfollow = getIDFromUsername(usernameToUnfollow)

    #Ottengo username - identificativo e faccio unfollow

    headers = {
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': csrf,
        'pragma': 'no-cache',
        'x-instagram-ajax': '6c1f67754dc0',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/'+username+'/following/',
        'content-length': '0',
    }

    link = 'https://www.instagram.com/web/friendships/'+str(idToUnfollow)+'/unfollow/'
    print(link)

    response = requests.post(link, headers=headers)
    print("UNFOLLOW " + str(usernameToUnfollow) + " " + str(response.content))

#Dall'utente prend



#per prima cosa effettuo il login con quelle credenziali
content_request = login(username, password)
cookies_dict = content_request.cookies.get_dict()
# Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

#prendo l'id della persona da cui voglio mandare le richieste di unfollow
id = getIDFromUsername(username)

for i in range(1,3000):
    print("Ho mandato la richiesta di follow a: " + str(i) + " utenti" )
    unfollw2(cookies_str,cookies_dict['csrftoken'])

    time.sleep(40)
