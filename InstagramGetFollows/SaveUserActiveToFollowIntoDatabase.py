import requests
import time


def saveUserAndIdIntoDatabase(id, username):
    response = requests.get(
        "http://altridatabase.altervista.org/saveUserIntoDatabaseUSER_TO_FOLLOW.php?ID=" + str(id) + "&USERNAME=" + str(
            username) + "&TARGET=ITALIANO")
    print(response.content)


def find_end_cursor(content):
    content = str(content)
    return content[content.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):content.find("\"}")]


# Cerco lo username dal content che torna
def findUsername(content):
    # cerco quante volte e' contenuto username nella stringa e per tute le volte itero
    countUsername = content.count("username")

    print("CONTENT INIZIALE" + content)

    for i in range(0, countUsername):
        time.sleep(2)
        username = content[content.find("\"username\":\"") + len("\"username\":\""):content.find("\",\"full_name\"")]
        content = content[content.find("profile_pic_url") + len("profile_pic_url"):]

        id = getIDFromUsername(username)
        # Controllo che sia un numero l'id che torna

        if id.isdigit():
            saveUserAndIdIntoDatabase(id, username)
            print("username: " + username + " ID " + id)
        else:
            print(
                "Attendo 100 secondo perche l'id che torna non e' intero quindi significa che ha fatto troppe richieste")
            time.sleep(100)


'''
Lo script inizia da qui, per prima cosa mi faccio restituire i primi ad aver messo like
'''

headers = {
    'pragma': 'no-cache',
    'cookie': 'ig_cb=1; mcd=3; mid=W3LViAAEAAGiyUhfp2D5g_qGX8_S; shbid=15622; csrftoken=mKGeSrhbUwaGFq5UWzshdmdkUtJ4ipEX; ds_user_id=8519385814; sessionid=IGSC17b89a307883f3bd3a379943f33305add83860858654360a902e607a0d5dea39%3AVxDndko1hinzDbj0orErrVWL32cHNM0E%3A%7B%22_auth_user_id%22%3A8519385814%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%228519385814%3AcjwNDhtSHoEgZciaNmcqTwqT1S0l5LgY%3A72ddfbb16ea6228ff72e65d37a75e86ae0abd7f34b2173451a4b317e4d838c2b%22%2C%22last_refreshed%22%3A1536014304.4642820358%7D; csrftoken=mKGeSrhbUwaGFq5UWzshdmdkUtJ4ipEX; rur=FTW; urlgen="{\\"151.21.67.143\\": 1267}:1fxFob:Suii9hVji53DkdBIzVp1StNFba0"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '13e3ee266cc10031149f1eb5b7403564',
    'referer': 'https://www.instagram.com/p/BoEGExVAGt4/?taken-by=ignoranza_vecchietti_cantiere',
}

params = (
    ('query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'),
    ('variables', '{"shortcode":"BoEGExVAGt4","include_reel":false,"first":24}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=e0f59e4a1c8d78d0161873bc2ee7ec44&variables=%7B%22shortcode%22%3A%22Bm9EuPiF1WZ%22%2C%22include_reel%22%3Afalse%2C%22first%22%3A24%7D', headers=headers)


def getIDFromUsername(username):
    headers = {
        'cookie': 'mid=W37M3gAEAAEx9lqR4H0aOZLOqVc4; ig_cb=1; mcd=3; shbid=18815; rur=FRC; fbm_124024574287414=base_domain=.instagram.com; csrftoken=rxlEbcolK4pDSNRhiCEHFZcp4AohLV1Q; ds_user_id=819693525; sessionid=IGSC98c33d9bcdef58f8ae6cdea57472a8aa7e0a25020266d7d8830e5e53afc447d0%3ARq35wsShGimeNW4q2sNIsRj8gX0epNRj%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3AKFR2xT3exniP2Ws8gfIxmXGFuYNnA1Uf%3A395531c9b82e23f482d0d509d8d2598b7771284162d774268ef91a9cfe1c4d59%22%2C%22last_refreshed%22%3A1535371645.7728667259%7D; csrftoken=rxlEbcolK4pDSNRhiCEHFZcp4AohLV1Q; fbsr_124024574287414=ee3JNtMaz94eG9Q-9wWm72vJq6JaZG-fM1lbUs4N-4E.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFrcEJ2RDFySEVPWWtrYlRPS2pRWTdIbS1zajJ2dWxjaGl4U2xWVlJxd0JISlh6Y0hxRXFxaVN1VXNOUW14aENZNzZ3a1VIYldOV1ZhS0F1UGtlelI0c1J4Q0xMWTY5d3oyQTBjcDByaVRwaFVySWo4Um10WTl1UGtPWjVFZmtCYzNUVjVzZXhpaFZ1UTBLLTFKVFUwbDd0azlSdUMxWnQwQ1dlOG16THo5Z0ZfU2JLckJUOVRlcnMtTWpKRTEzTGllVGFhbnZTLUpIWjNiOUtaZllEcjJrNlJEYjJQUFkxV0V0ZGIxSmpVZnl6MVRkSzlJSGNETmlMNzVCNUc5X0pQSi1mZmdmSVZCcXZHN21mVGZUNk45S3NVT3FQVktHbGxkcVloVXphYU45eUJHQl9VN1d5WWJ0UzRqRXAzVVNtUGlzWmd5a0xWazlZTjM3SFJtdzVmdCIsImlzc3VlZF9hdCI6MTUzNTM3MTY0OCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; shbts=1535371663.8507757; urlgen="{\\"91.253.62.111\\": 24608\\054 \\"2.230.243.113\\": 12874\\054 \\"37.160.9.107\\": 51207\\054 \\"91.253.246.85\\": 24608}:1fuGJH:qwVk11wj0WEcLGi8uFiOfmzbmes"',
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
print(response)
cursore = find_end_cursor(response)
findUsername(str(response))

# Da qui in poi inizio a fare un while infinito da cui prendo i followers:
while True:


    headers = {
        'pragma': 'no-cache',
        'cookie': 'ig_cb=1; mcd=3; mid=W3LViAAEAAGiyUhfp2D5g_qGX8_S; shbid=15622; csrftoken=mKGeSrhbUwaGFq5UWzshdmdkUtJ4ipEX; ds_user_id=8519385814; sessionid=IGSC17b89a307883f3bd3a379943f33305add83860858654360a902e607a0d5dea39%3AVxDndko1hinzDbj0orErrVWL32cHNM0E%3A%7B%22_auth_user_id%22%3A8519385814%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%228519385814%3AcjwNDhtSHoEgZciaNmcqTwqT1S0l5LgY%3A72ddfbb16ea6228ff72e65d37a75e86ae0abd7f34b2173451a4b317e4d838c2b%22%2C%22last_refreshed%22%3A1536014304.4642820358%7D; csrftoken=mKGeSrhbUwaGFq5UWzshdmdkUtJ4ipEX; rur=FTW; urlgen="{\\"151.21.67.143\\": 1267}:1fxFoh:f8iVVbmOaqtLRxPAU8OP_Dkq0vk"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.75 Chrome/68.0.3440.75 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': '13e3ee266cc10031149f1eb5b7403564',
        'referer': 'https://www.instagram.com/p/BoEGExVAGt4/?taken-by=ignoranza_vecchietti_cantiere',
    }



    params = (
        ('query_hash', 'e0f59e4a1c8d78d0161873bc2ee7ec44'),
        ('variables', '{"shortcode":"BoEGExVAGt4","include_reel":false,"first":100,"after":"' + cursore + '"}'),
    )

    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    print("ALTRI")
    cursore = find_end_cursor(response.content)
    findUsername(str(response.content))
