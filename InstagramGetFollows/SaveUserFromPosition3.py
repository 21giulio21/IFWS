import sys

import instaloader
import requests
import time



target = "GENOVA_LICEALI"
posizione =  "liceo-s-pertini"
id_posizione = "771601924"

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
        print("username: " + profile.username + " id " + str(id))
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
    'cookie': 'csrftoken=CE2VyW7yiDQ7w0mUIcZxwDgAeOtBKHJK; ig_cb=1; shbid=18815; mid=W6psGQAEAAF5riW6zcT8sQriqsly; ds_user_id=819693525; mcd=3; csrftoken=CE2VyW7yiDQ7w0mUIcZxwDgAeOtBKHJK; rur=FRC; sessionid=IGSC7c58080aa928e195fef60c92f0f70010918e8a40cef395630eb98dc0573821d5%3A6r1bFcIxw3AFhiGtR0nU80BjmSmtZaz1%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3AAp1XRAMIbbIDL5jP9K9Tdx1g4Dyi3T9K%3A9438ede6546fdde51d4ab5394491ff9a1e041abca41944a68c98b9a8a9d0978e%22%2C%22last_refreshed%22%3A1539005517.3767206669%7D; shbts=1539005794.4424503; urlgen="{\\"93.41.120.53\\": 12874\\054 \\"37.162.69.104\\": 51207}:1g9ViB:tTEAgroko6Y_XLVNu11Dq2gQW4Y"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/explore/locations/'+id_posizione+'/'+posizione+'/',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': 'e90b5452fbe122df9fd3f5cab4d4cc9c',
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
        'cookie': 'csrftoken=CE2VyW7yiDQ7w0mUIcZxwDgAeOtBKHJK; ig_cb=1; shbid=18815; mid=W6psGQAEAAF5riW6zcT8sQriqsly; ds_user_id=819693525; mcd=3; csrftoken=CE2VyW7yiDQ7w0mUIcZxwDgAeOtBKHJK; rur=FRC; sessionid=IGSC7c58080aa928e195fef60c92f0f70010918e8a40cef395630eb98dc0573821d5%3A6r1bFcIxw3AFhiGtR0nU80BjmSmtZaz1%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3AAp1XRAMIbbIDL5jP9K9Tdx1g4Dyi3T9K%3A9438ede6546fdde51d4ab5394491ff9a1e041abca41944a68c98b9a8a9d0978e%22%2C%22last_refreshed%22%3A1539005517.3767206669%7D; shbts=1539005794.4424503; urlgen="{\\"93.41.120.53\\": 12874\\054 \\"37.162.69.104\\": 51207}:1g9ViB:tTEAgroko6Y_XLVNu11Dq2gQW4Y"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/explore/locations/' + id_posizione + '/' + posizione + '/',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'e90b5452fbe122df9fd3f5cab4d4cc9c',
    }

    params = (
        ('query_hash', '1b84447a4d8b6d6d0426fefb34514485'),
        ('variables', '{"id":"'+id_posizione+'","first":120,"after":"'+end_cursor+'"}'),
    )


    response2 = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

    #print(response2.content)
    end_cursor = find_end_cursor(response2.content)
    findUsernameAndId(str(response2.content))
