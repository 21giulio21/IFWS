import json
import re
import sys

import requests
import base64
import requests
import time

from InstagramAPI import login, updateUserFollowed

username_instagram = str(sys.argv[1])
#password_instagram = str(sys.argv[2])
numero_utenti_da_defollow = int(sys.argv[2])

def accorcioResponse(response):
    return response[response.find("\"username\":\"") + len("\"username\":\""):]

def geuUserFromUsername(username):
    url="http://www.elenarosina.com/instatrack/getUserFromUsername.php?username="+str(username)
    return json.loads(requests.get(url).content)


#ottengo dal mio server le persone che seguo gia.
user = geuUserFromUsername(username_instagram)


id_instagram = str(user[0]['ID'])
users_followed_string = str(user[0]['USERS_FOLLOWED'])
users_followed_array = re.split(';', users_followed_string)

headers = {
    'cookie': 'ig_cb=1; mid=W3qsUgAEAAGu-ppm_wmUJoV5q9wR; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=c5pdl6sExADIjF69mmwgKEcWHz4YIVrj; shbid=18440; shbts=1542453514.0048485; ds_user_id=819693525; sessionid=IGSC8164133ce2a8afbe954e0035fd173fc1a031b84d61c368b72dcab014a2e4796d%3AfkgWWcEgSUHEVVnBoscuOJFzb0HgG1bq%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ArqenMsQy95BQSJ5YYEcz4aWvP4SmLRTx%3A208ed358d825b42841b44bbed8693c29af3a23662b4df9d23eac4f52d2e48718%22%2C%22last_refreshed%22%3A1542453514.0061211586%7D; rur=FTW; urlgen="{\\"37.227.104.199\\": 24608}:1gNycm:xegbf6pnWDoWYArFIvnTbC1Bp2w"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/'+username_instagram+'/following/?hl=it',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '61dc4071f869747d2f42bbcdf73a43eb',
}

params = (
    ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
    ('variables', '{"id":"'+id_instagram+'","include_reel":true,"fetch_mutual":false,"first":12,"after":"QVFEYVRKdHFHdkJIRDV3OWsxeFAxZzdDRzJRXzZtdkwyTnBRODNRZXFVMms1MDZiMWRRMGoyYk5KR2V1UEVGM0F6MTZ5U2I3R3p5MnpESEtZbk9HeldsZg=="}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c56ee0ae1f89cdbd1c89e2bc6b8f3d18&variables=%7B%22id%22%3A%22819693525%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Afalse%2C%22first%22%3A12%2C%22after%22%3A%22QVFEYVRKdHFHdkJIRDV3OWsxeFAxZzdDRzJRXzZtdkwyTnBRODNRZXFVMms1MDZiMWRRMGoyYk5KR2V1UEVGM0F6MTZ5U2I3R3p5MnpESEtZbk9HeldsZg%3D%3D%22%7D', headers=headers)


response = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)



end_cursor = response[response.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):response.find("\"},\"edges\":[{\"node\"")] #QVFEQ0E3MW0xM3U4Z0VnMzU3YllwdC0wNGpxSlAxZ1FweGs5NjFlQi1MWDgtZXRvUmM0MHdoa1ZubldmdzV1emx2eWNObEZWQXRvcDMyRjViVXk2b0lzaA==
print("AAA")
print(response)

print(end_cursor)



#da qui in poi cerco gli username
numero_username = response.count("\"username\":\"")


#accorcio la risposta in modo da ottenere subito gli username
response = response[response.find("\"username\":\"") + len("\"username\":\""):]

array_utenti_da_defollow = []

for i in range(0,numero_username):

    username = response[:response.find("\",\"full_name\"")]


    if len(username) < 20:
        print("UU " + username)
        array_utenti_da_defollow.append(username)
    response = accorcioResponse(response)


#Qui ne chiedo altri 50
while len(array_utenti_da_defollow) < numero_utenti_da_defollow:

    headers = {
        'cookie': 'ig_cb=1; mid=W3qsUgAEAAGu-ppm_wmUJoV5q9wR; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=c5pdl6sExADIjF69mmwgKEcWHz4YIVrj; shbid=18440; shbts=1542453514.0048485; ds_user_id=819693525; sessionid=IGSC8164133ce2a8afbe954e0035fd173fc1a031b84d61c368b72dcab014a2e4796d%3AfkgWWcEgSUHEVVnBoscuOJFzb0HgG1bq%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ArqenMsQy95BQSJ5YYEcz4aWvP4SmLRTx%3A208ed358d825b42841b44bbed8693c29af3a23662b4df9d23eac4f52d2e48718%22%2C%22last_refreshed%22%3A1542453514.0061211586%7D; rur=FTW; urlgen="{\\"37.227.104.199\\": 24608}:1gNycm:xegbf6pnWDoWYArFIvnTbC1Bp2w"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/'+username_instagram+'/following/?hl=it',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': '61dc4071f869747d2f42bbcdf73a43eb',
    }
    params = (
        ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
        ('variables', '{"id":"'+id_instagram+'","include_reel":true,"fetch_mutual":false,"first":12,"after":"'+end_cursor+'"}'),
    )

    response = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)


    end_cursor = response[response.find("\"end_cursor\":\"") + len("\"end_cursor\":\""):response.find(
        "\"},\"edges\":[{\"node\"")]  # QVFEQ0E3MW0xM3U4Z0VnMzU3YllwdC0wNGpxSlAxZ1FweGs5NjFlQi1MWDgtZXRvUmM0MHdoa1ZubldmdzV1emx2eWNObEZWQXRvcDMyRjViVXk2b0lzaA==
    numero_username = response.count("\"username\":\"")
    response = response[response.find("\"username\":\"") + len("\"username\":\""):]

    print("response")
    print(response)

    for i in range(0, numero_username):
        username = response[:response.find("\",\"full_name\"")]

        if len(username) < 20:
            print("UU " + username)
            array_utenti_da_defollow.append(username)
        response = accorcioResponse(response)

print("Numero di utenti da defollow: " + str(len(array_utenti_da_defollow)))

utenti_da_defollow_string = ""
for i in array_utenti_da_defollow:
    utenti_da_defollow_string = utenti_da_defollow_string + ";" + i

print(utenti_da_defollow_string)

if users_followed_string == "":
    users_followed_string = utenti_da_defollow_string[1:]
else:
    users_followed_string = users_followed_string + utenti_da_defollow_string


users_followed_string = users_followed_string + ";"


print("Utenti che devo inserire all'interno del DB:")
print(users_followed_string)

print("\n")
print(updateUserFollowed(users_followed_string, username_instagram))

