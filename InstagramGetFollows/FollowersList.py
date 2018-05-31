import requests
import time
from threading import Thread


def find_end_cursor(content_originale,content):
    # Cerco end_cursor da mettere in input alla richiesta dopo
    content = content_originale[content_originale.find("end_cursor") + len("end_cursor") + 3: content.find("\"}")]
    end_cursor = content[:content.find("\"}")]
    return end_cursor

#Funzione da non chiamare dal main, permette di andare a prendere la pagina instagram collegata al nome passato come parametro
#e prende l'id della persona
def getPage(nome):

    headers = {
        'authority': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; rur=FRC; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; sessionid=IGSC8ed527fc1cda43ac5555695cbba25d643a1f566c1a145452aeb5b67b12fb5305%3A17hUaA9Ul0DdZyAsj2Os4HkJ1yVzZfCg%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527681913.5427627563%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1527681913\\054 \\"193.55.113.196\\": 2200}:1fO1o7:2az6OzqMKD6FoWtZ4xZOuq8St1Q"',
    }

    response = str(requests.get('https://www.instagram.com/'+nome, headers=headers).content)
    posizioneprofilePage_= response.find("profilePage_")
    inizio_id = response[posizioneprofilePage_ + len("profilePage_"):]
    id =unicode(str(inizio_id[:inizio_id.find("\"")]), 'utf-8')

    if id.isnumeric():
        print("Salvo sul server un utente con id: " +id + " e nome: " + nome)
        requests.get('http://2.230.243.113/foulo.php?id='+id+'&username='+ nome)

def findUsername(content_originale):
    content = content_originale
    for i in range(1, 50):
        index_username_start = content.find("\"username\"")
        s = content[index_username_start + len("\"username\"") + 2: index_username_start + len("\"username\"") + 80]
        username_1 = content[index_username_start + len("\"username\"") + 2: index_username_start + len(
            "\"username\"") + s.find("\"") + 2]
        content = content[content.find(username_1) + len(username_1):]
        t = Thread(target=getPage, args=(username_1,))  # li mando al server mio cosi posso poi vederli piu avanti
        t.start()
        time.sleep(0.5)
    return find_end_cursor(content_originale, content)


headers = {
    'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; rur=FRC; mcd=3; ig_cb=1; sessionid=IGSCbae91f5f3e783e3796ce92f7338e32ce23c4b6631c4a07c92290aefbe80afafa%3AbAcvU6HZnyXc178U0B4HGyJbAsQNrRey%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527768486.8264241219%7D; urlgen="{\\"time\\": 1527760068\\054 \\"193.55.113.196\\": 2200}:1fOMNj:e3v8GUbhevw_iGxPjSXypwXTllA"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/donze093/followers/?hl=it',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '0a2f877b31cab1edc4929d1c6a324adb',
}

params = (
    ('query_hash', '37479f2b8209594dde7facb0d904896a'),
    ('variables', '{"id":"2315985234","first":50}'),
)


    #Cerco tutti gli account
content_originale = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)



for i in range(1,100000):
    headers = {
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; rur=FRC; mcd=3; ig_cb=1; sessionid=IGSCbae91f5f3e783e3796ce92f7338e32ce23c4b6631c4a07c92290aefbe80afafa%3AbAcvU6HZnyXc178U0B4HGyJbAsQNrRey%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527768486.8264241219%7D; urlgen="{\\"time\\": 1527760068\\054 \\"193.55.113.196\\": 2200}:1fOMPA:JO7DXNqFXSz-X7Wp54lfgZaeSrU"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/donze093/followers/?hl=it',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'd70ee90ed3d353ce831e68562de9589f',
    }

    params = (
        ('query_hash', '37479f2b8209594dde7facb0d904896a'),
        ('variables',
         '{"id":"2315985234","first":12,"after":"' + findUsername(content_originale) + '"}'),
    )



    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    content_originale =  response.content
    time.sleep(100)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables=%7B%22id%22%3A%22232257039%22%2C%22first%22%3A12%2C%22after%22%3A%22AQDFNTQiGHGEEdaGk8AK6KgFyeSCDEqo8jzRBICgbK6ZylLpy6wJMXv7HH0Yg4Nm39WjZKd7RMyB1BpsmsjlfvgAq9ovZcQk2VGgf6MQaG3TWw%22%7D', headers=headers)
