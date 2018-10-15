import sys

import instaloader
import requests
import time

from InstagramAPI import login

username = str(sys.argv[1])
password = str(sys.argv[2])
target = str(sys.argv[3])
hastag =  str(sys.argv[4]) #"pugilato"


def saveUserAndIdIntoDatabase(id,username):
    response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET="+target)
    print(response.content)


def find_end_cursor(content):
    content = str(content)
    return content[content.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):content.find("\"}")]

def geuUsernameFromId(id):
    print("Attendo 10 secondi prima di fare trovare l'username dall'identificativo")
    #time.sleep(0.4)
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_id(L.context, int(id))
        print("username: " + profile.username + " id " + str(id) + " hastag="+hastag + " target="+target)
        saveUserAndIdIntoDatabase(id, profile.username)

    except instaloader.exceptions.LoginRequiredException:
        print("impossibile trovare username, passo al prossimo")


def findUsernameAndId(content):
    array= content.split(",\"owner\":{\"id\":\"")
    for i in array:
        id = i[:i.find("\"},")]
        if len(id) < 30:
            #Controllo se ho gia inserito un ID cosi
            controlloSeNelDBHoGiaUnUtenteConQuelID(id)



def controlloSeNelDBHoGiaUnUtenteConQuelID(id):
    #Faccio una richiueata al url: http://altridatabase.altervista.org/controlloSeNelDBHoGiaUnUtenteConQuelID.php?ID=1632792873    torna TRUE SE POSSO INSERIRE L?UTENTE
    url = "http://altridatabase.altervista.org/controlloSeNelDBHoGiaUnUtenteConQuelID.php?ID=" + id + "&TARGET="+target
    response = requests.get(url)
    if str(response.content).__contains__("TR"):
        geuUsernameFromId(id)
    else:
        print("ID Gia inserito " + id + " con il target" + target)

#per prima cosa effettuo il login con quelle credenziali
content_request = login(username, password)



cookies_dict = content_request.cookies.get_dict()
# Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

headers = {
    'pragma': 'no-cache',
    'cookie': cookies_str ,
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': cookies_dict['csrftoken'],
    'referer': 'https://www.instagram.com/explore/tags/'+hastag+'/?hl=it',
}

params = (
    ('query_hash', 'ded47faa9a1aaded10161a2ff32abb6b'),
    ('variables', '{"tag_name":"'+hastag+'","first":100,"after":""}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)


#Con questa funziona immediatamente trovo username e mando sul server pero trappe richieste insieme
findUsernameAndId(str(response.content))

end_cursor = find_end_cursor(response.content)

#time.sleep(10)
print("Primo Cursore")

for i in range(0,1000):
    headers = {
    'pragma': 'no-cache',
    'cookie': cookies_str ,
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': cookies_dict['csrftoken'],
    'referer': 'https://www.instagram.com/explore/tags/'+hastag+'/?hl=it',
    }

    params = (
    ('query_hash', 'ded47faa9a1aaded10161a2ff32abb6b'),
    ('variables', '{"tag_name":"'+hastag+'","first":10,"after":"'+end_cursor+'"}'),
    )

    response2 = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

    end_cursor = find_end_cursor(response2.content)
    findUsernameAndId(str(response2.content))

