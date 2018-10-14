import sys

import instaloader
import requests
import time

target = "GENOVA_PALESTRA"
posizione =  "hifit-genova"
id_posizione = "480454162"


def saveUserAndIdIntoDatabase(id,username):

    response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET="+target)
    print(response.content)


def find_end_cursor(content):
    content = str(content)
    return content[content.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):content.find("\"},\"edges\":[{")] #1885017018580283412

def geuUsernameFromId(id):
    print("Attendo 5 secondi prima di fare trovare l'username dall'identificativo")
    #time.sleep(2)
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_id(L.context, int(id))
        print("username: " + profile.username + " id " + str(id) + " target: "+target + " posizione: "+ posizione)
        saveUserAndIdIntoDatabase(id, profile.username)

    except instaloader.exceptions.LoginRequiredException:
        print("impossibile trovare username, passo al prossimo")


def findUsernameAndId(content):
    array= content.split(",\"owner\":{\"id\":\"")
    for i in array:
        stringa = i[:i.find("\"},")]
        if len(stringa) < 30:
            geuUsernameFromId(stringa)


headers = {
    'cookie': 'ig_cb=1; shbid=18815; mid=W6psGQAEAAF5riW6zcT8sQriqsly; mcd=3; rur=FRC; csrftoken=9fqTt9iMcoT7Ny8M2Ral5dSnIasl1VVy; ds_user_id=8688326939; sessionid=IGSCf8f0ef554fac890ac2ba2f47be00e15f0cf421903a9dd2e0765ed16f7ec55f20%3ALZCMcH0ob1oTwNYUy0wmQ4w3V40pWoxd%3A%7B%22_auth_user_id%22%3A8688326939%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%228688326939%3A9l8MOiZZP05vgZBw94idyNFu3J2ugcUg%3A24d2ec11b7340b11b74a840c1d81023dba7255069f2baa93b29f208542da4435%22%2C%22last_refreshed%22%3A1539250908.1195034981%7D; urlgen="{\\"2.230.243.113\\": 12874}:1gAXtt:4kAvOKCaZ97eJX-3r0k10Iaox6A"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/explore/locations/'+id_posizione+'/'+posizione+'/',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '2c4301ef7ff7d551a03c56533d78da7b',
}


params = (
    ('query_hash', '1b84447a4d8b6d6d0426fefb34514485'),
    ('variables', '{"id":"'+id_posizione+'","first":12,"after":""}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

#print(response.content)



#Con questa funziona immediatamente trovo username e mando sul server pero trappe richieste insieme
findUsernameAndId(str(response.content))

end_cursor = find_end_cursor(response.content)

time.sleep(10)
print("Primo Cursore")
print(end_cursor)

for i in range(0,1000):
    headers = {
        'cookie': 'ig_cb=1; shbid=18815; mid=W6psGQAEAAF5riW6zcT8sQriqsly; mcd=3; rur=FRC; csrftoken=9fqTt9iMcoT7Ny8M2Ral5dSnIasl1VVy; ds_user_id=8688326939; sessionid=IGSCf8f0ef554fac890ac2ba2f47be00e15f0cf421903a9dd2e0765ed16f7ec55f20%3ALZCMcH0ob1oTwNYUy0wmQ4w3V40pWoxd%3A%7B%22_auth_user_id%22%3A8688326939%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%228688326939%3A9l8MOiZZP05vgZBw94idyNFu3J2ugcUg%3A24d2ec11b7340b11b74a840c1d81023dba7255069f2baa93b29f208542da4435%22%2C%22last_refreshed%22%3A1539250908.1195034981%7D; urlgen="{\\"2.230.243.113\\": 12874}:1gAXtt:4kAvOKCaZ97eJX-3r0k10Iaox6A"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/explore/locations/' + id_posizione + '/' + posizione + '/',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': '2c4301ef7ff7d551a03c56533d78da7b',
    }

    params = (
        ('query_hash', '1b84447a4d8b6d6d0426fefb34514485'),
        ('variables', '{"id":"'+id_posizione+'","first":120,"after":"'+end_cursor+'"}'),
    )


    response2 = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

    #print(response2.content)
    end_cursor = find_end_cursor(response2.content)
    findUsernameAndId(str(response2.content))
