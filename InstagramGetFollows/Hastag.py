import sys

import instaloader
import requests
import time


hastag =  str(sys.argv[1])

def saveUserAndIdIntoDatabase(id,username):
    response = requests.get("http://2.230.243.113/instagram/saveUserIntoDatabaseUSER_TO_FOLLOW_HASTAG.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET=HASTAG"+hastag)
    print(response.content)


def find_end_cursor(content):
    content = str(content)
    return content[content.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):content.find("\"}")]

def geuUsernameFromId(id):
    print("Attendo 10 secondi prima di fare trovare l'username dall'identificativo")
    time.sleep(10)
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
    'pragma': 'no-cache',
    'cookie': 'mid=W1c7RAAEAAFDeNK-N46r0Fu-kuQk; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_cb=1; csrftoken=AxACHvi2CAl59FwDmIuKf7BCtGX1LzJN; shbid=18440; ds_user_id=1327040148; sessionid=IGSCa3dc5ebb359939240ed8ffaebe5f3cf584dd9cd63fb9c2f827bba01d17f4a174%3AP9RnSh8stKJ991oCoOClVn4hypdySrYx%3A%7B%22_auth_user_id%22%3A1327040148%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%221327040148%3Ac7k0keTYTDLQZJH0RLPgVsYVuRku6are%3A745f46e58b55bc832676244f57538d13c7c42b2f4342ef6de221ed3af51bfbf4%22%2C%22last_refreshed%22%3A1532504340.0497331619%7D; rur=PRN; fbsr_124024574287414=FfiugrGnU-jFeFKKX60n1hCEBSWhPfCefGkQBrJjcpk.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUMzR0ZOdnZTVUVVZmxRektoUk1FWktCcGRzTEpwZkE5ZGJ5WUx3dk1oM2pMSnZyVHpNXzI3d1pyUGlndjd0eFJfVm56TmRHT3lnOHJlQTIycXlLZGRaSmdVbldieWJWN1RuelczbVV0R2ZCaEFmeEVPZEhGclptTlJLdDZ4dUZtcHhPSFpxdVdKeWlhbUVKTTBuV3ZDWE9FVTRoNE1QUVR2SzdRMnlrQXlXVEdlbUZiX3JRa1JaMnhwa2VUWS1GQ3FYTVlJODh5TWJ1VFlScmlPOGZkWHlaUVYyb25Hamxra3AyaWl5OGItcVp5V2pid1UxTVRjbVR5bkJRNEE5QkJiSDFhSGhZVVAwRGc4YnBwUzlIemhteE1TQVRPbEtVRDZFdk9ESHpGTUtWem9MWVRnZWlGUDd6UWZzQTU2WVV2Q0Z3NEhFYUJyUGEyWFNpeGpDUWl3MSIsImlzc3VlZF9hdCI6MTUzMjUyNTQ4OCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1532504308\\054 \\"193.55.113.196\\": 2200}:1fiJu7:H7vs5PtQ2WfukZmN8U_MDeCIda0"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '29fd3a9dfe7f4771d34384d12e2fb6af',
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

time.sleep(10)
print("Primo Cursore")
print(end_cursor)

for i in range(0,1000):
    headers = {
    'pragma': 'no-cache',
    'cookie': 'mid=W1c7RAAEAAFDeNK-N46r0Fu-kuQk; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_cb=1; csrftoken=AxACHvi2CAl59FwDmIuKf7BCtGX1LzJN; shbid=18440; ds_user_id=1327040148; sessionid=IGSCa3dc5ebb359939240ed8ffaebe5f3cf584dd9cd63fb9c2f827bba01d17f4a174%3AP9RnSh8stKJ991oCoOClVn4hypdySrYx%3A%7B%22_auth_user_id%22%3A1327040148%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%221327040148%3Ac7k0keTYTDLQZJH0RLPgVsYVuRku6are%3A745f46e58b55bc832676244f57538d13c7c42b2f4342ef6de221ed3af51bfbf4%22%2C%22last_refreshed%22%3A1532504340.0497331619%7D; rur=PRN; fbsr_124024574287414=FfiugrGnU-jFeFKKX60n1hCEBSWhPfCefGkQBrJjcpk.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUMzR0ZOdnZTVUVVZmxRektoUk1FWktCcGRzTEpwZkE5ZGJ5WUx3dk1oM2pMSnZyVHpNXzI3d1pyUGlndjd0eFJfVm56TmRHT3lnOHJlQTIycXlLZGRaSmdVbldieWJWN1RuelczbVV0R2ZCaEFmeEVPZEhGclptTlJLdDZ4dUZtcHhPSFpxdVdKeWlhbUVKTTBuV3ZDWE9FVTRoNE1QUVR2SzdRMnlrQXlXVEdlbUZiX3JRa1JaMnhwa2VUWS1GQ3FYTVlJODh5TWJ1VFlScmlPOGZkWHlaUVYyb25Hamxra3AyaWl5OGItcVp5V2pid1UxTVRjbVR5bkJRNEE5QkJiSDFhSGhZVVAwRGc4YnBwUzlIemhteE1TQVRPbEtVRDZFdk9ESHpGTUtWem9MWVRnZWlGUDd6UWZzQTU2WVV2Q0Z3NEhFYUJyUGEyWFNpeGpDUWl3MSIsImlzc3VlZF9hdCI6MTUzMjUyNTQ4OCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; shbts=1532525583.2673147; urlgen="{\\"time\\": 1532504308\\054 \\"193.55.113.196\\": 2200}:1fiJuZ:q0GV9kfFMSwNSAZaCVR3GNG4t0Y"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '90f107095b4d637f6b8e57668a4e72c6',
    'referer': 'https://www.instagram.com/explore/tags/'+hastag+'/?hl=it',
    }

    params = (
    ('query_hash', 'ded47faa9a1aaded10161a2ff32abb6b'),
    ('variables', '{"tag_name":"'+hastag+'","first":10,"after":"'+end_cursor+'"}'),
    )

    response2 = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

    print(response2.content)
    end_cursor = find_end_cursor(response2.content)
    findUsernameAndId(str(response2.content))

