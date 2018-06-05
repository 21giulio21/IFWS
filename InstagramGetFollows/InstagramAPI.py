'''
Questo main permette di dare in input un nome ad esempio fedez
e scarico tutti gli id e i nomi delle persone che lo seguono
cosi ho la certezza che sono tutte persone vere e non capitano mai
nomi del tipo: 001 ecc..
'''

import requests
import re
import time
import json
import random


#fedez: 46071423
#fedex: 232257039

url_get_all_user = "http://getfollowersoninstagram.altervista.org/getAllUser.php"

def follow(id,username, cookies, csrf):

	headers = {
    'cookie' : cookies,
    'origin': 'https://www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': csrf,
    'x-instagram-ajax': '8958fe1e75ab',
    'authority': 'www.instagram.com',
    'referer': 'https://www.instagram.com/' + username,

	}



	response = requests.post('https://www.instagram.com/web/friendships/' + str(id) + '/follow/', 	headers=headers)
	print(response.content)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.instagram.com/web/friendships/232257039/follow/?hl=en', headers=headers)






'''
DA SISTEMARE
'''
def unfollow():

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
        'cookie': 'csrftoken=lFhhLQoVs9oV50indCYzEq7IcgqDtWYe; shbid=18815; ds_user_id=819693525; rur=FRC; mid=WvmbbgAEAAGkE8-Iw_fd2dUvCtgG; sessionid=IGSC9796ca437fcfd6d36398ab15e9a206dec873970556b0fe021dc95ff271b319f1%3ATv29t528QoF7ZhOLnfv3eghfYFZwWSRt%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3At78X57JbUvMQlDmPz5isBb5F4xzbvugf%3A20cdd64da7cfe4973813334c7d0de224fab20e6de545dcecd280dc280e6daa35%22%2C%22last_refreshed%22%3A1526307694.726708889%7D; mcd=3; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=0_t2vXeIk8q8fy5LPXxymigkKjiDRJ3NzA3P_RwvM60.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURBZ1NxeElsU205a05RX2kwU04wUEZEaTJENEFnZkF2ZzBpeWd0SEQybC15NVF4Q2lIcVY5ZVJsN3IwbFdkRGUzclZyWDA2TmJNMlE1M2NpMGdfNTU2ZV9mMEhFZXhzdENaT2Jxd29BZ256OEVzU3lBV2Nsb2NyR0c4ODRmeWF6b21oVF9WUXhRTWstOE9VQlhKc2hUT2ZJOW4zeHd0OEgzUy1acnlmTHZsbHVlaUVRSmI0Y0xHUERrbTYya01xdlNmcC1vdnRjLU4xbmNseEVOMVZmb1AycXh1SE9wbWgtUWF2SkZGMXhCVXl2OFE3S0N5TzN3X3IwcnNJQkw3MFc5OGZERVk4b0pzb0lDaUZfRFFEblBDQ3ZQd3pVUXZ1ZlNpYXJGOG1NNzBDV3Y4TFhSVjI0c1l1RG9XUVhpQW4wN0x0Uy04eGFNQ2Z1WjBxcVhlQWhZZSIsImlzc3VlZF9hdCI6MTUyNjMwODMyNiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; shbts=1526308327.404692; urlgen="{\\"time\\": 1526307694\\054 \\"193.55.113.196\\": 2200}:1fIEWF:VLTfQwtdAehiKHQaTUTc3rPUepA"',
        'x-csrftoken': 'lFhhLQoVs9oV50indCYzEq7IcgqDtWYe',
        'x-instagram-ajax': '0fa00dc2cc1f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/fedez/',
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/friendships/232257039/unfollow/', headers=headers)


def login(username,password):

    headers = {
        'cookie': 'ig_cb=1',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'Y5RToHUnJaNvziqQ24edFlMB0CFd3fH6',
        'pragma': 'no-cache',
        'x-instagram-ajax': '8958fe1e75ab',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/',
    }

    data = [
        ('username', username),
        ('password', password),
        ('queryParams', '{}'),
    ]

    response = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
    return response



def getUsersToFollow():
    return json.loads(requests.get(url_get_all_user).content)

#Ritorna quanti siano gli utenti registrati
def countUserIntoDatabase():
    url = "http://getfollowersoninstagram.altervista.org/getCountUsers.php"
    return requests.get(url).content

def selectUserFromDatabase(index):
    url = "http://getfollowersoninstagram.altervista.org/getUserFromIndex.php?index=" +str(index)
    return json.loads(requests.get(url).content)

#Ritorna il numero di utenti che sono nella tabella oin cui sono contenuti tutti
def getCountUsersToFollow():
    url = "http://getfollowersoninstagram.altervista.org/getCountUsersToFollow.php"
    return requests.get(url).content

#Ottengo l id del utente attraverso lo username
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
    id = unicode(str(inizio_id[:inizio_id.find("\"")]), 'utf-8')
    return id

if __name__ == "__main__":
	follow('','')




