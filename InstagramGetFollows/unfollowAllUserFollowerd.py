import sys

import requests
import base64
import requests
import time

from InstagramAPI import login



username = "alessandrogino_"#str(sys.argv[1])
password = "n>}Qb$11$(>,*i%J02ohd.lF^%{R*:ey1u^_#=5r"#str(sys.argv[2])



def getIDFromUsername(username):

    headers = {
        'authority': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; shbid=14394; rur=PRN; mid=WwWZlQAEAAG_zXJpoNK1kd3gNgBY; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=jCMA3LcYOYgH0CKycMKs7kPBvhU86lRi0J7kKEUjBow.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURhRUpMWlBPQ1hCbVlqU2hJSE4xbENDR2VkbkZzT3VvRnZXaGxxUGxoRlh5TWQ5RnE5S19US0dNd25DLVVodGpSSEVGS1diNERNbVlfMG5WUjdZSkVlYjZ2Q3F4Z1pxd0RKNnNTbEs0MXhuWUhncklBNXVGS3lkMkZaRFJCMUswaGNQbmRscjhpMk92OE1fTjQwYmZ1ZEhBSEdTQURqb2N3eWFZUnNIOGhhV1N1QUhTYTVVeE5RcXBwZUFBeGJBWWdJUk00aFRYVUZtVDU1dzFqV3haNVZVTGVra25vZXFpTlpHWGEwblRrdjVFMVVEZERaNnhVTVRCODVwMW5DbEFwenFIZGJtS3lDN190NVpTdWV2eVdWUFFDT0JJMkxxZ2hYTGVCRnBfTUpidVpEZ29Fb0g0LW9maTVyNXRJX0dMV01TOGhSN2ZxcTIzZXVjUHVFdXdyVSIsImlzc3VlZF9hdCI6MTUyNzA5Mzk3MiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1527093653\\054 \\"91.253.85.98\\": 24608}:1fLWw5:CeahbLDKdr-qr7LIG_H6YV30jcg"',
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
