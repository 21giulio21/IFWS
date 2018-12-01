import requests
import time

from InstagramAPI import login

username = "giulo_tavella"#str(sys.argv[1])
password = "21CICCIO21ciccio"#str(sys.argv[2])



target = "ITALIANO"


def saveUserAndIdIntoDatabase(id,username):
    response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET="+target)
    print(response.content)



def find_end_cursor(content):
    content = str(content)
    return content[content.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):content.find("\"}")]


# Cerco lo username dal content che torna
def findUsername(content):
    # cerco quante volte e' contenuto username nella stringa e per tute le volte itero
    countUsername = content.count("username")

    #print("CONTENT INIZIALE" + content)

    for i in range(0, countUsername):
        time.sleep(2)
        username = content[content.find("\"username\":\"") + len("\"username\":\""):content.find("\",\"full_name\"")]
        content = content[content.find("profile_pic_url") + len("profile_pic_url"):]

        id = getIDFromUsername(username)
        # Controllo che sia un numero l'id che torna

        if id.isdigit():
            saveUserAndIdIntoDatabase(id, username)
            print("username: " + username + " ID " + id + " target=" + target)
        else:
            print(
                "Attendo 100 secondo perche l'id che torna non e' intero quindi significa che ha fatto troppe richieste")
            time.sleep(100)


'''
Lo script inizia da qui, per prima cosa mi faccio restituire i primi ad aver messo like
'''


#per prima cosa effettuo il login con quelle credenziali
content_request = login(username, password)
cookies_dict = content_request.cookies.get_dict()
# Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)


headers = {
    'cookie':cookies_str,
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/p/Boy3Xreisbi/?taken-by=temptationisland_official',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': cookies_dict['csrftoken'],
}

params = (
    ('query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'),
    ('variables', '{"shortcode":"Boy3Xreisbi","include_reel":true,"first":24}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=e0f59e4a1c8d78d0161873bc2ee7ec44&variables=%7B%22shortcode%22%3A%22Bm9EuPiF1WZ%22%2C%22include_reel%22%3Afalse%2C%22first%22%3A24%7D', headers=headers)


def getIDFromUsername(username):
    headers = {
        'cookie': cookies_str,
        'authority': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = str(requests.get('https://www.instagram.com/' + username, headers=headers).content)
    posizioneprofilePage_ = response.find("profilePage_")
    inizio_id = response[posizioneprofilePage_ + len("profilePage_"):]
    id = str(inizio_id[:inizio_id.find("\"")])
    return id


# Dalla risposta torna un cursore e parso la risposta per ottenere il cursore
response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content
#print(response)
cursore = find_end_cursor(response)
findUsername(str(response))

# Da qui in poi inizio a fare un while infinito da cui prendo i followers:
while True:
    headers = {
        'cookie': cookies_str,
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/Boy3Xreisbi/?taken-by=temptationisland_official',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': cookies_dict['csrftoken'],
    }

    params = (
        ('query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'),
        ('variables',
         '{"shortcode":"Boy3Xreisbi","include_reel":true,"first":100,"after":"' + cursore + '"}'),
    )






    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    print("ALTRI")
    cursore = find_end_cursor(response.content)
    findUsername(str(response.content))
