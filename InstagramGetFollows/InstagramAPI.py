import base64
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
	print("FOLLOW" + username + response.content)

#TODO: Da ultimare
def unfollow(id,username, cookies, csrf):

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': '0fa00dc2cc1f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/'+username+'/',
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/friendships/'+id+'/unfollow/', headers=headers)
    print("UNFOLLOW" + username + response.content)


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

#Agggiorno l'array sul database
def updateUserFollowed(userFollowed,username):
    url = "http://getfollowersoninstagram.altervista.org/updateUserFollowed.php?username="+username+"&users_followed="+userFollowed
    requests.get(url)

#Salvo id dell'utente nel database
def saveIdIntoDatabase(username,id):
    url = "http://getfollowersoninstagram.altervista.org/saveIdIntoDatabase.php?username="+username+"&id="+id
    requests.get(url)

#salvo i cookie di un relativo utente sul server
def seveCookieIntoServer(username,cookie):
    cookie =  base64.b64encode(str(cookie))
    url = "http://getfollowersoninstagram.altervista.org/saveCookie.php?username=" + str(username) +"&cookie="+str(cookie)
    print requests.get(url).content




#prendo come input un numero random da 1 al numero massimo di persone che ho nel database di persone che posso
#seguire e facci ola richiesta pert farmene tornare 1 a caso
def getRandomUserToFollow(index):
    url = "http://getfollowersoninstagram.altervista.org/getUserToFollowFromIndex.php?index=" + str(index)
    return json.loads(requests.get(url).content)

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




