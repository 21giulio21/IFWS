import requests
import time
from threading import Thread

url_server_save_followers = "http://getfollowersoninstagram.altervista.org/saveUsetIntoDatabase.php"

def find_end_cursor(content_originale,content):
    # Cerco end_cursor da mettere in input alla richiesta dopo
    content = content_originale[content_originale.find("end_cursor") + len("end_cursor") + 3: content.find("\"}")]
    end_cursor = content[:content.find("\"}")]
    return end_cursor

#Funzione da non chiamare dal main, permette di andare a prendere la pagina instagram collegata al nome passato come parametro
#e prende l'id della persona
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
    id =unicode(str(inizio_id[:inizio_id.find("\"")]), 'utf-8')
    print("id " + id + " username " + username)
    response = requests.get(url_server_save_followers+"?username="+username+"&id="+id)
    print(response.content)


def findUsername(content_originale):
    content = content_originale
    for i in range(1, 50):
        index_username_start = content.find("\"username\"")
        s = content[index_username_start + len("\"username\"") + 2: index_username_start + len("\"username\"") + 80]
        username_1 = content[index_username_start + len("\"username\"") + 2: index_username_start + len(
            "\"username\"") + s.find("\"") + 2]
        content = content[content.find(username_1) + len(username_1):]
        t = Thread(target=getIDFromUsername, args=(username_1,))  # li mando al server mio cosi posso poi vederli piu avanti
        t.start()
        time.sleep(0.5)
    return find_end_cursor(content_originale, content)


headers = {
    'pragma': 'no-cache',
    'cookie': 'csrftoken=M9hDLKHUHgxBSnmnu4DbTzNbQmH4yOW4; rur=FRC; mid=WxknwgAEAAGl82aft9P3SbdxtGr_; ds_user_id=7914483784; sessionid=IGSC5d2324a5fd49edcfdc098f4e896a94e9405a83e66e0ab80fad97220febea196d%3AR6ZsN489PUmch6Xrq68uX4mPnRKuPJKZ%3A%7B%22_auth_user_id%22%3A7914483784%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227914483784%3Akul866H9wytMPLXCHLmjsntAJOURCLlO%3A11e23f566bd991a76a72c92e6546b1f505979d1843aad7b9b9bd203059314fb3%22%2C%22last_refreshed%22%3A1528375234.6884109974%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1528375235\\054 \\"193.55.113.196\\": 2200}:1fQuDu:2yGAvvVvMEhmR4r-i82MkFRiACE"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': 'fcaa4e4dddf2e10d66fe8bcd1f4a5273',
    'referer': 'https://www.instagram.com/ssavinow/followers/',
}

params = (
    ('query_hash', '37479f2b8209594dde7facb0d904896a'),
    ('variables', '{"id":"1077103383","first":50}'),
)


    #Cerco tutti gli account
content_originale = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)



for i in range(1,100000):
    headers = {
        'pragma': 'no-cache',
        'cookie': 'csrftoken=M9hDLKHUHgxBSnmnu4DbTzNbQmH4yOW4; rur=FRC; mid=WxknwgAEAAGl82aft9P3SbdxtGr_; ds_user_id=7914483784; sessionid=IGSC5d2324a5fd49edcfdc098f4e896a94e9405a83e66e0ab80fad97220febea196d%3AR6ZsN489PUmch6Xrq68uX4mPnRKuPJKZ%3A%7B%22_auth_user_id%22%3A7914483784%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227914483784%3Akul866H9wytMPLXCHLmjsntAJOURCLlO%3A11e23f566bd991a76a72c92e6546b1f505979d1843aad7b9b9bd203059314fb3%22%2C%22last_refreshed%22%3A1528375234.6884109974%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1528375235\\054 \\"193.55.113.196\\": 2200}:1fQuDy:wdO1DmCJEdFgEI3LjOZFRU4JJno"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'b267d4e2d75162fbf6d469bb21fe30bc',
        'referer': 'https://www.instagram.com/ssavinow/followers/',
    }

    params = (
        ('query_hash', '37479f2b8209594dde7facb0d904896a'),
        ('variables',
         '{"id":"1077103383","first":50,"after":"' + findUsername(content_originale) + '"}'),
    )

    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    content_originale =  response.content
    time.sleep(100)
