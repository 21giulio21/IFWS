#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import json
import itertools
import random



comment_list=[["Questa","La tua","La"],
                  ["foto", "fotografia", "immagine"],
                  ["è veramente", "è proprio", "è davvero"],
                  ["pazzesca", "unica", "sensazionale", "bellissima", "magnifica", "indimenticabile",
                   "meravigliosa", "straordinaria", "eccezionale", "magica",
                   "emozionante"],
                  [" "," "," "," "," "," ","❤"," "],
                  [".", "..", "...", "!", "!!", "!!!"]]




url_get_all_user = "http://getfollowersoninstagram.altervista.org/getAllUser.php"


# genera un commento a caso usando le parole di comment_list
def generate_comment():
        c_list = list(itertools.product(*comment_list))

        repl = [("  ", " "), (" .", "."), (" !", "!")]
        res = " ".join(random.choice(c_list))
        for s, r in repl:
            res = res.replace(s, r)
        return res.capitalize()


def ottengoIdPrimaFotoDaUsername(username, cookies, csrf):

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookies,
    }

    response = str(requests.get('https://www.instagram.com/' + username + "/", headers=headers).content)
    posizione__typename = response.find("GraphImage")
    stringa = response[posizione__typename + len("GraphImage") + 8  : posizione__typename + 100]
    posizione_id_foto = stringa.find("\"")

    return stringa[:posizione_id_foto]

def richiestaLike(username, cookies, csrf):

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': 'd2dfd728ae44',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BjIEnJAgwYS/?taken-by=' + username,
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/likes/'+ottengoIdPrimaFotoDaUsername(username, cookies, csrf)+'/like/', headers=headers)



#Permette di mettere un commento al media_id che gli passo
def comment(cookies, csrf,username_to_comment):

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': 'ac942a8a720f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BkkwR3ihMUn/?taken-by=' + str(username_to_comment),
        'authority': 'www.instagram.com',
    }

    data = [
        ('comment_text', generate_comment()),
    ]

    return requests.post('https://www.instagram.com/web/comments/'+ottengoIdPrimaFotoDaUsername(username_to_comment, cookies, csrf)+'/add/', headers=headers, data=data).content


def follow(id, username, cookies, csrf):

	headers = {
    'cookie' : cookies,
    'origin': 'https://www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': csrf,
    'x-instagram-ajax': '8958fe1e75ab',
    'authority': 'www.instagram.com',
    'referer': 'https://www.instagram.com/' + username,

	}

	return requests.post('https://www.instagram.com/web/friendships/' + str(id) + '/follow/', 	headers=headers).content




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

    return requests.post('https://www.instagram.com/web/friendships/'+id+'/unfollow/', headers=headers).content



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

#Questa funzione viene chiamata nel momento in cui un utente appena inserito ha sbagliato la password di instagram
#in particolare pre prima mette PASSWORD_SBAGLIATA a 1 nel database poi merre PROCESSING a 0 cosi lato app se ne accorge
def updatePasswordErrataAndProcessing(username,passwordErrata):
    updateSctiptActive(username,0)
    url = "http://getfollowersoninstagram.altervista.org/updatePasswordErrata.php?username=" + username + "&password_errata=" + str(
        passwordErrata)
    requests.get(url)
    updateProcessing(username,0)

def updateProcessing(username,value):
    url = "http://getfollowersoninstagram.altervista.org/updateProcessing.php?username=" + username + "&processing=" + str(value)
    print(url)
    print(requests.get(url).content)

def updateSctiptActive(username,valore):
    url = "http://getfollowersoninstagram.altervista.org/updateScriptActive.php?username=" + username + "&script_active=" + str(valore)
    requests.get(url)

def getUsersToFollow():
    return json.loads(requests.get(url_get_all_user).content)

#Update follow_unfollow nel database
def updateFollowUnfollowDatabase(username,follow_unfollow):
    url="http://getfollowersoninstagram.altervista.org/updateFollowUnfollow.php?username="+username+"&follow_unfollow="+follow_unfollow
    requests.get(url)

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
    print(requests.get(url).content)

#Questa funzione permette di settare il tempo di blocco
def setBlockTime(username,tempo_blocco_se_esce_errore,delta_t):
    print("Imposto il tempo di blocco per l'utente: " + username + " perche ha fatto troppe richueste")
    # Aggiorno ad attesa 10 minuti per l'utente a cui e' arrivato il blocco e aumento DT di 10 secondi
    updateTempoBlocco(username, tempo_blocco_se_esce_errore)
    # aumentoDelta t di 10 secondi
    delta_t = int(delta_t) + 50
    updateDeltaT(username, str(delta_t))




#prendo come input un numero random da 1 al numero massimo di persone che ho nel database di persone che posso
#seguire e facci ola richiesta pert farmene tornare 1 a caso
def getRandomUserToFollow(username_whants_to_follow):
    url = "http://getfollowersoninstagram.altervista.org/getUserToFollowFromUser.php?USERNAME=" + str(username_whants_to_follow)
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


#aggiorno nel mio databse la tupla con username: username e setto il tempo: time
def update_secondi_ultima_richiesta(username,time):
    url = "http://getfollowersoninstagram.altervista.org/updateSecondiUltimaRichiesta.php?username="+str(username)+"&time="+str(time)
    return requests.get(url).content

#funzione che aggiorna DT per quell'utente
def updateDeltaT(username,delta_t):
    url= "http://getfollowersoninstagram.altervista.org/updateDT.php?username="+str(username)+"&dt="+str(delta_t)
    return requests.get(url).content

#Aggiorno il tempo di blocco che deve attendere un utente prima che rinizi a mandare richieste
def updateTempoBlocco(username,tempo):
    url = "http://getfollowersoninstagram.altervista.org/updateTempoBlocco.php?username="+str(username)+"&tempo_blocco="+str(tempo)
    return requests.get(url).content

#Aggiorna il numere di richieste fatte, in questo modo dopo che un utente ne fa 100 posso
#diminuire il Delta T
def updateNumberRequestsDone(username,number_requests_done):
    url = "http://getfollowersoninstagram.altervista.org/updateNumberRequestsDone.php?username=" + str(username) + "&number_requests_done=" + str(number_requests_done)
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

def ottengoURLImmagineProfilo(username):
    headers = {
        'authority': 'www.instagram.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = str(requests.get('https://www.instagram.com/' + username, headers=headers).content)
    temp = response[response.find("<meta property=\"og:image\" content=\"") + len("<meta property=\"og:image\" content=\""):]
    url_immagine = temp[:temp.find("\" />") ]
    return url_immagine


#mando al mio server in formato Base64 l'url dell'immagine profilo in questo modo poi posso vederla sul'app o sito
def updateURLImmagineProfilo(username,url_immagine):
    url_encode = base64.b64encode(str(url_immagine))
    url = "https://getfollowersoninstagram.altervista.org/insertURLImageProfilo.php?username=" + str(username) + "&immagine_profilo=" + str(url_encode)
    return requests.get(url).content








