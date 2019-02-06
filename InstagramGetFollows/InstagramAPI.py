#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import base64
import datetime

from email.mime.text import MIMEText
from threading import *
import requests
import json
import itertools
import random
import time

from termcolor import colored


import re


url_bot = "http://www.giuliovittoria.it"
url_sms_mail = "http://www.utentidaseguire.eu"

FILE_NAME = "a.html"

comment_list=[  ["Complimenti","Bravo","Grande"],
                ["!",".","..","...","!","!!","!!!","!!!!"],
                ["Questa ","La tua","La"],
                ["foto", "fotografia", "immagine"],
                [" è veramente ", " è proprio ", " è davvero "," è "," secondo me è"],
                ["pazzesca", "unica", "sensazionale", "bellissima", "magnifica", "indimenticabile","meravigliosa", "straordinaria", "eccezionale", "magica","emozionante"],
                [" "," "," "," "," "," ","❤"," "],
                [".", "..", "...", "!", "!!", "!!!"," "]
                ]

'''

comment_list = [["\n"],
                ["Ciao ❄","Ciao!! ❄","Ciao!!! ❄","Buongiorno ❄","Buongiorno!! ❄","Buongiorno! ❄","Ehy! ❄","Ehy!!! ❄","Ehy!! ❄","Ehy ❄"],
                [" 🔥Aumenta i tuoi seguaci \n"],
                [" ▶️REALI \n"],
                [" ▶️ATTIVI \n "],
                [" ▶️100% IN TARGET"],
                [" 🚀 Collegati al sito per accedere alla PROMOZIONE LANCIO  \n"],
                [" ▶️ www.instatrack.eu"],
                [" Per info"," Per maggiori informazioni"],
                [" contattami in privato! 🎉"]
                ]

'''





# genera un commento a cauthenticated = str(content_request_JSON["authenticated"])aso usando le parole di comment_list
def generate_comment():
        c_list = list(itertools.product(*comment_list))

        repl = [("  ", " "), (" .", "."), (" !", "!")]
        res = " ".join(random.choice(c_list))
        for s, r in repl:
            res = res.replace(s, r)
        return res.capitalize()


def ottengoIdPrimaFotoDaUsername(username, cookies, csrf):
    # Genero random l'ip da cui viene fatto il login, deve esserequalcosa come: 64.1.3559.543
    primoNumero = random.randint(2, 100)
    secondoNumero = random.randint(2, 100)
    terzoNumero = random.randint(2, 100)
    quartoNumero = random.randint(2, 100)
    ip = str(str(primoNumero) + "." + str(secondoNumero) + "." + str(terzoNumero) + "." + str(quartoNumero) + ".")

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/'+ip+' Chrome/'+ip+' Safari/537.36',
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
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': 'd2dfd728ae44',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BjIEnJAgwYS/?taken-by=' + username,
        'authority': 'www.instagram.com',
        'content-length': '0',
    }
    return requests.post('https://www.instagram.com/web/likes/'+ottengoIdPrimaFotoDaUsername(username,cookies, csrf) +'/like/', headers=headers)



#Permette di mettere un commento al media_id che gli passo
def comment(cookies, csrf,username_to_comment):
    # Genero random l'ip da cui viene fatto il login, deve esserequalcosa come: 64.1.3559.543
    primoNumero = random.randint(2, 100)
    secondoNumero = random.randint(2, 100)
    terzoNumero = random.randint(2, 100)
    quartoNumero = random.randint(2, 100)
    ip = str(str(primoNumero) + "." + str(secondoNumero) + "." + str(terzoNumero) + "." + str(quartoNumero) + ".")

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

    return requests.post('https://www.instagram.com/web/comments/'+ottengoIdPrimaFotoDaUsername(username_to_comment,cookies, csrf)+'/add/', headers=headers, data=data).content


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

	return requests.post('https://www.instagram.com/web/friendships/' + str(id) + '/follow/', 	headers=headers)


def follow_thread(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict,username,number_requests_done,tempo_blocco_se_esce_errore,delta_t,target,email):
    # Seguo la persona che ho scaricato e gli metto un like alla prima foto
    contet_request = follow(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict['csrftoken'])

    # In questo punto aumento la variabile:  number_requests_done di 1 e mando al server il nuovo valore di number_requests_done
    updateNumberRequestsDone(username, str(int(number_requests_done) + 1))

    print( str(username) + " FOLLOW :  " + username_user_to_follow + " " + str(
        contet_request.content) + " TARGET DELL?UTENTE CHE SEGUO: " + target)

    parse_content_request(contet_request, 'FOLLOW-UNFOLLOW', username, tempo_blocco_se_esce_errore, delta_t,
                          email)


def unfollow_thread(username_user_to_unfollow,cookies_str,cookies_dict,username,tempo_blocco_se_esce_errore,delta_t,email,users_followed_string):

    # chiedo al mio database di utenti li della persona con quell username
    try:
        id_to_unfollow = int(getIdFromUsernameToUnfollow(username_user_to_unfollow))
        id_to_unfollow = str(id_to_unfollow)

    #nel caso in cui non ci sia lo chiedo ad Instagram
    except:
        id_to_unfollow = getIDFromUsername(username_user_to_unfollow)




    content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str, cookies_dict['csrftoken'])

    print("\n" + username + " UNFOLLOW " + username_user_to_unfollow + " id: " + str(id_to_unfollow) + " " + str(
        content_request.content) + "\n")

    parse_content_request(content_request, "FOLLOW-UNFOLLOW", username, tempo_blocco_se_esce_errore, delta_t, email)

    # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
    update_secondi_ultima_richiesta(username, int(time.time()))
    updateUserFollowed(users_followed_string, username)




def unfollow(id,username, cookies, csrf):



    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': '0fa00dc2cc1f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/'+username+'/',
        'authority': 'www.instagram.com',
        'content-length': '0',


    }

    return requests.post('https://www.instagram.com/web/friendships/'+id+'/unfollow/', headers=headers)



def login(username,password):
    headers = {
        'cookie': 'ig_cb=1; mid=W1nvMQAEAAFu2gGrVLf9bSIPaRj0; mcd=3; fbm_124024574287414=base_domain=.instagram.com; shbid=18815; rur=FRC; csrftoken=8PTQJQ7SinBSjbsmVnBExspM0dwYyNZ8; fbsr_124024574287414=8YD7u-K_rHKaSPA5xcY6uah59VJCd41My7qDi7TU_Hc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURTdTZuVG0zbVl2YXhPd2UwWXdnQ2JUVlZsM3VRTEltRzNmelk5cll6MlZEemhWQW1DejJONFpjUjN1NURKNjNSUndjSlBPU282dF9sNHlfN3U1eHE4TDNoMGFXUTNrUDc4YkFHM1JleFBSbjhoMzhXRFBpbjhBLWRYaTBtcER6MHJ1TE1LaUdsMUgzcmlDd2ZkV1UtTnMwX2Zld2VGelFBQXQyNnFMRGhMZTgtRnJfTVhIWXFGSFFrUnVJTmhZdGx2Tl9Gc254el9MOVlibWgwVTNJRllOYnM5VUFPaU9JdndPTWhwalR0Zm13NG5fRmduYlZ3VGV0TXpSbG9OdlZ1cGxZbGxDNGw4a3dqaDlTYW84dUdtUHJ4YUxQS2YzRjFGdUs5Y2ZzS1pkSFNOdE91LXdaaWVrWDl5M1Q0QkVITnpnZTNydzR2MllCTGNvRDFiNDBmRSIsImlzc3VlZF9hdCI6MTUzMjYyMDkxMCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1532620593\\054 \\"193.55.113.196\\": 2200}:1fiiiC:RUN1GvUYgXRNI-ZXGepzKJ_5Ybs"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '8PTQJQ7SinBSjbsmVnBExspM0dwYyNZ8',
        'pragma': 'no-cache',
        'x-instagram-ajax': 'f122ed33a26e',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
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
def updatePasswordErrataAndProcessing(username,passwordErrata,email):
    updateSctiptActive(username,0)
    url = url_bot + "/instatrack/updatePasswordErrata.php?username=" + username + "&password_errata=" + str(passwordErrata)
    requests.get(url)
    updateProcessing(username,0)


    #MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
    print("Mando la mail a " + email + " per comunicare che la password Instagram e' errata")
    msg = "Ciao "+str(username)+",\n\nLa password Instagram inserita risulta errata.\nCollegati al sito instatrack.eu e inseriscila correttamente!\nNon perdere l'occasione di guadagnare con Instagram\n\n\n\n\nA presto,\nInstatrack.eu"
    subject = "Instatrack.eu - Password Instagram Errata"
    email = "21giulio21@gmail.com"

    sendMailToUser(email, msg, subject)

#QUesta funzione prmette di capire se gia precedentemente seguivo una persona.
#Se gia seguivo una persona allora non rimando la richiesta
#QUesta funziona torna: true nel caso in cui precedentemente seguivo gia la persona
def checkIfYetFollowing(username_user_to_follow,cookies):

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookies
    }

    params = (
        ('__a', '1'),
    )

    ritorno = requests.get('https://www.instagram.com/'+username_user_to_follow+'/', headers=headers, params=params).content

    #ritorno e' ugiale a tru o fals nel caso in cui precedentemente seguivo gia o meno l'utente
    ritorno = ritorno[ritorno.find("followed_by_viewer\":") + len("followed_by_viewer\":") : ritorno.find("followed_by_viewer\":") + len("followed_by_viewer\":") + 4 ]
    if ritorno.__contains__("tru"):
        return True
    else:
        return False


def updateProcessing(username,value):
    url = url_bot + "/instatrack/updateProcessing.php?username=" + username + "&processing=" + str(value)
    requests.get(url)

def updateSctiptActive(username,valore):
    url = url_bot + "/instatrack/updateScriptActive.php?username=" + username + "&script_active=" + str(valore)
    requests.get(url)

def getUsersToFollow():
    url_get_all_user = url_bot + "/instatrack/instagram/getAllUser.php"
    return json.loads(requests.get(url_get_all_user).content)

#Update follow_unfollow nel database
def updateFollowUnfollowDatabase(username,follow_unfollow):
    url= url_bot + "/instatrack/updateFollowUnfollow.php?username="+username+"&follow_unfollow="+follow_unfollow
    requests.get(url)

#Agggiorno l'array sul database
def updateUserFollowed(userFollowed,username):

    url = url_bot + "/instatrack/updateUserFollowed.php"
    return_request = requests.post(url, data={'username': username, 'users_followed': userFollowed}).content

    return return_request

#Salvo id dell'utente nel database
def saveIdIntoDatabase(username,id):
    url = url_bot + "/instatrack/saveIdIntoDatabase.php?username="+username+"&id="+id
    requests.get(url)

#salvo i cookie di un relativo utente sul server
def seveCookieIntoServer(username,cookie):
    cookie =  base64.b64encode(str(cookie))
    url = url_bot + "/instatrack/saveCookie.php?username=" + str(username) +"&cookie="+str(cookie)
    requests.get(url)

#Questa funzione permette di settare il tempo di blocco
def setBlockTime(username,tempo_blocco_se_esce_errore,delta_t):
    print("Imposto il tempo di blocco per l'utente: " + username + " perche ha fatto troppe richueste")
    # Aggiorno ad attesa 10 minuti per l'utente a cui e' arrivato il blocco e aumento DT di 10 secondi
    updateTempoBlocco(username, tempo_blocco_se_esce_errore)
    #aumentoDelta t di 10 secondi
    #delta_t = int(delta_t) + 50
    #updateDeltaT(username, str(delta_t))




#prendo come input un numero random da 1 al numero massimo di persone che ho nel database di persone che posso
#seguire e facci ola richiesta pert farmene tornare 1 a caso
def getUserToFollwFromTarget(target,username):

    print( str(username) + " richiesta  al target: " + str(target))
    url = "http://www.utentidaseguire.eu/getUserToFollowFromUTENTI_DA_SEGUIRE.php?TARGET=" + str(target)
    return json.loads(requests.get(url).content)



#Ritorna quanti siano gli utenti registrati da quel thread
def countUserIntoDatabaseFromTread(thread):
    url = url_bot + "/instatrack/getCountUsersFromThread.php?THREAD="+str(thread)
    return requests.get(url).content


#Ritorna quanti siano gli utenti registrati totali
def countUserIntoDatabase():
    url = url_bot + "/instatrack/getCountUsers.php"
    return requests.get(url).content

#Seleziona un utente dal database con un preciso indice
def selectUserFromDatabase(index):
    url = url_bot + "/instatrack/getUserFromIndex.php?index=" +str(index)
    return json.loads(requests.get(url).content)


#Seleziona un utente dal database con un preciso indice
def selectUserFromDatabaseAndThread(index,thread):
    url = url_bot + "/instatrack/getUserFromIndexAndThread.php?index=" +str(index)+"&THREAD="+str(thread)
    return json.loads(requests.get(url).content)

#Ritorna il numero di utenti che sono nella tabella oin cui sono contenuti tutti
def getCountUsersToFollow():
    url = url_bot + "/instatrack/getCountUsersToFollow.php"
    return requests.get(url).content


#aggiorno nel mio databse la tupla con username: username e setto il tempo: time
def update_secondi_ultima_richiesta(username,time):
    url = url_bot + "/instatrack/updateSecondiUltimaRichiesta.php?username="+str(username)+"&time="+str(time)
    return requests.get(url).content

#funzione che aggiorna DT per quell'utente
def updateDeltaT(username,delta_t):
    url= url_bot + "/instatrack/updateDT.php?username="+str(username)+"&dt="+str(delta_t)
    return requests.get(url).content

#Aggiorno il tempo di blocco che deve attendere un utente prima che rinizi a mandare richieste
def updateTempoBlocco(username,tempo):
    url = url_bot + "/instatrack/updateTempoBlocco.php?username="+str(username)+"&tempo_blocco="+str(tempo)
    return requests.get(url).content

#Aggiorna il numere di richieste fatte, in questo modo dopo che un utente ne fa 100 posso
#diminuire il Delta T
def updateNumberRequestsDone(username,number_requests_done):
    url = url_bot + "/instatrack/updateNumberRequestsDone.php?username=" + str(username) + "&number_requests_done=" + str(number_requests_done)
    return requests.get(url).content

#Ottengo l id del utente attraverso lo username chiedendo ad instagram
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

def getIdFromUsernameToUnfollow(username):
    url = "http://www.utentidaseguire.eu/getIDFromUsername.php?username="+str(username)
    return requests.get(url).content


def updateDevePagare(username, value):
    url = url_bot + "/instatrack/updateDevePagare.php?username=" + str(username) + "&DEVE_PAGARE=" + str(value)
    return requests.get(url).content

#Parso la risposta da Instagram nel momento in cui ho mandato una richiesta, content_request_JSON e' il ritorno dela richiesta una volta mandata
#
#Nella richiesta di login: {"message": "unauthorized", "redirect_url": "/accounts/login/?next=/web/friendships/297458948/follow/", "status": "fail"} ->Login errato
#Nella richiesta di login: {"authenticated": false, "user": true, "status": "ok"}-> Login errato
#Nella richiesta di login: {"authenticated": true, "user": true, "userId": "6045478794", "oneTapPrompt": false, "status": "ok"}-> Se tutto e' andato a buon fine
#Nella richiesta di FOLLOW: {"result": "following", "status": "ok"} -> se andata a buonfine
#Nella richiesta di Follow {"message": "This action was blocked. Please try again later.", "status": "fail"} -> se devo bloccare per un po di clicli
#Nella richiesta di FOLLOW se l'utente cambia password e quindi deve risettare i coockie: {"message": "unauthorized", "redirect_url": "/accounts/login/?next=/web/friendships/365506590/follow/", "status": "fail"}
#Nella richiesta di LIKE se inizia con <!DOCTYPE html> allora non ha potuto mettere like perche la foto era nascosta
def parse_content_request(content_request, type_request,username,tempo_blocco_se_esce_errore,delta_t,email):

    if type_request == "LOGIN":
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return


        authenticated = str(content_request_JSON["authenticated"]).upper()

        #In questo caso mi sono loggato in maniera corretta.
        if authenticated == "FALSE":
            messaggio = "AUTENTICAZIONE NON RIUSCITA - L'utente:"+str(username) + " NON ha inserito credenziali corrette "
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            updatePasswordErrataAndProcessing(username,1,email)
        else:
            # MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
            messaggio = "INVIO EMAIL - L'utente:" + str(
                username) + " inizia i 4 giorni di prova"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

            #msg = "Ciao " + username + ",\n\nBenvenuto in instatrack.eu! \n Da oggi iniziano i 3 giorni di prova gratuiti!\nAlla fine del servizio potrai decidere se rinnovare ed iniziare a guadagnare con Instagram\n\n\n\n\n\nBuon lavoro,\nInstatrack.eu"
            #subject = "Instatrack.eu - Inizio Prova Gratuita"
            #sendMailToUser(email, msg, subject)

    elif type_request == "FOLLOW-UNFOLLOW":

        #Se la risposta contiene Attendi perche ne ho fatte troppe di fila allora setto il blocco time per quell'utente
        if content_request.content.__contains__("been temporarily") or content_request.content.__contains__("Please wait") or  content_request.content.__contains__("Attendi") or content_request.content.__contains__("This action")or content_request.content.__contains__("Sembra che") :
            messaggio = "BLOCCO - L'utente:" + str(
                username) + " ha fatto TROPPE richieste, bloccato per un po"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            setBlockTime(username, tempo_blocco_se_esce_errore, delta_t)

            msg = "ADMIN - L'utente " + username + ", è in blocco perche ha fatto troppe richeste"
            subject = "Instatrack.eu - ADMIN"
            sendMailToUser("21giulio21@gmail.com", msg, subject)
            return
        # Se la risposta contiene Sorry, you're following the max limit of accounts. You'll need to unfollow some accounts to start following more allora devo fare unfollow
        if content_request.content.__contains__("Sorry, you're following the max limit") :
            messaggio = "CAMBIO  - L'utente:" + str(
                username) + " ha fatto TROPPE richieste di FOLLOW, devo fargli fare UNFOLLOW"

            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            # Aggiorno il server dicendo che follow_unfollow e' zero
            follow_unfollow = "0"
            updateFollowUnfollowDatabase(username, follow_unfollow)

            msg = "ADMIN - L'utente " + username + ", ha fatto TROPPE richieste di FOLLOW, devo fargli fare UNFOLLOW"
            subject = "Instatrack.eu - ADMIN"
            sendMailToUser("21giulio21@gmail.com", msg, subject)

            return


        #se invecie contiene chechpoint vado ad incrementare il tempo_attesa_blocco a 10K
        if content_request.content.__contains__("checkpoint_required"):
            messaggio = "CHECK POINT REQUIRED - L'utente:" + str(
                username) + " è in checkpoint_required, lo blocco sperando che qualcuno lo sblocchi"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            setBlockTime(username, tempo_blocco_se_esce_errore, delta_t)

            msg = "ADMIN - L'utente " + username + ", è in checkpoint_required"
            subject = "Instatrack.eu - ADMIN"
            sendMailToUser("21giulio21@gmail.com", msg, subject)

            return

        #Se la risposta contiene unauthorized allora purche sia valida la data ma non va bene la password,
        #in particolare e' stata cambiata
        if content_request.content.__contains__("unauthorized"):
            messaggio = "CAMBIO PASSWORD - L'utente:" + str(
                username) + " ha cambiato password"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            updatePasswordErrataAndProcessing(username, 1, email)
            messaggio = "Ciao "+str(username)+", le credenziali del tuo accoint Instagram inserite precedentemente sono cambiate. Accedi a www.instatrack.eu per rimpostare le credenziali corrette."
            sendSMSToUser(email, messaggio)

        #Altrimenti puo accadere che ci sia la password errata perche puo aver cambiato password l'utente e devo rifare i coockie
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return

        #Controllo se la risposta contiene message
        if 'message' in content_request_JSON:
            message = str(content_request_JSON["message"]).upper()
            if message == "selectUserFromDatabaseAndThread":
                messaggio = "CAMBIO PASSWORD - L'utente:" + str(
                    username) + " ha cambiato password"
                scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
                updatePasswordErrataAndProcessing(username, 1,email)

    elif type_request == "LIKE":
        if content_request.content.__contains__("<!DOCTYPE html>"):
            print("Processo l'utente: "+username+" non ha messo like alla foto perche era un profilo privato")

        else:
            print("Processo l'utente: "+username+" ha messo like alla foto con esito: " + str(content_request.content))


def parse_content_request_for_LOGIN_THREAD_0(content_request, type_request,username,tempo_blocco_se_esce_errore,delta_t,email):

    if type_request == "LOGIN":
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return
        print("Processo la risposta: "+ str(content_request.content) )

        #Prima controllo se è andato in checkpoint
        if str(content_request_JSON).__contains__("checkpoint_required"):
            print("L'uente è in checkpoin, riprova piu tardi, mando la mail per avvertirlo")
            msg = "Ciao " + username + ",\n\nAccedi a Instagram per verificare il tuo account!\n\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
            subject = "Instatrack.eu - Accedi a Instagram"
            sendMailToUser(email, msg, subject)

            messaggio = "Ciao " + str(
                username) + ", Accedi a Instagram per verificare il tuo account."
            sendSMSToUser(email, messaggio)

            return 0


        #Qui controllo se lousername ho l'autenticazione a due fattori:
        if str(content_request_JSON).__contains__("two_factor_required"):

            messaggio = "LOGIN - l'account con USERNAME:" + username + " ha l'autenticazione a due fattori"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            msg = "Ciao " + username + ",\n\nAccedi a Instagram per rimuovere l'autenticazione a due fattori, altrimenti non possiamo processare il tuo account.\nUna volta processato puoi inserire nuovamente l'autenticazione a due fattori.\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
            subject = "Instatrack.eu - Accedi a Instagram"
            sendMailToUser(email, msg, subject)

            messaggio = "Ciao " + str(
                username) + ", Accedi a Instagram per rimuovere l'autenticazione a due fattori, altrimenti non possiamo processare il tuo account.\nUna volta processato puoi inserirla nuovamente"
            sendSMSToUser(email, messaggio)

            return 0



        authenticated = str(content_request_JSON["authenticated"]).upper()

        #In questo caso mi sono loggato in maniera corretta.
        if authenticated == "FALSE":

            messaggio = "Ciao " + str(
                username) + ", le tue credenziali risultano errate. Accedi al sito www.instatrack.eu per reinserirle correttamente."
            sendSMSToUser(email, messaggio)

            print("Autenticazione non riuscita")
            print(updatePasswordErrataAndProcessing(username,"1",email))
        else:
            # MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
            #print("Mando la mail a " + email + " per comunicare che da oggi iniziano i 4 giorni di prova")
            #msg = "Ciao " + username + ",\n\nBenvenuto in instatrack.eu! \n Da ora il tuo account è attivo."
            #subject = "Instatrack.eu - Inizio Abbonamento"
            #sendMailToUser(email, subject,msg)

            messaggio = "Ciao " + str(
                username) + ", la tua iscrizione e' andata a buon fine. Accedi alla nostra piattaforma www.instatrack.eu per gestire in tempo reale il tuo account!"
            sendSMSToUser(email, messaggio)



            newThread = random.randint(1,3)

            print("\n Autenticazione riuscita, cambio il thread da 0 a " + str(newThread)  )
            updateTreadFromUsername(username, newThread)
            #updateDeltaT(username,50)
            updateSctiptActive(username,1)


def updateTreadFromUsername(username,newThread):
    url = url_bot + "/instatrack/updateThread.php?username="+username+"&thread=" + str(newThread)
    print("RIsposta ottenuta quando cambio il thread: " + str(requests.get(url).content) + "\n")



#Questa funzione permette di mandare la mail in caso sia finita la prova o il pacchertto
def sendMailToUser(mail_to,messaggio,subject):
    response = requests.get(url_sms_mail + "/instatrack/send_MAIL/insert_mail_into_database.php?MESSAGGIO="+messaggio+"&EMAIL="+mail_to+"&OGGETTO="+subject)
    print(response.content)

#Questa funzione permette di mandare la mail in caso sia finita la prova o il pacchertto
def sendSMSToUser(email,messaggio):
    prefisso_numero = getPhoneNumberFromEmail(email)
    response = requests.get(url_sms_mail + "/instatrack/send_SMS/insert_sms_into_database.php?NUMERO_TELEFONICO="+str(prefisso_numero) +"&MESSAGGIO="+str(messaggio))
    #print(response.content)



####################################
#################################### Da qui in poi metto tutte le funzioni per i like automatici


def countPhotoIntoDatabase():
    url = url_bot + "/instatrack/likeautomatici/countPhotoIntoDatabase.php"
    return requests.get(url).content

def getIdPhotoNotLiked(max_like):
    url = url_bot + "/instatrack/likeautomatici/getPhoto.php?max_like="+str(max_like)
    return json.loads(requests.get(url).content)

def selectPhotoFromDatabase(index):
    url = url_bot + "/instatrack/likeautomatici/getPhotoFromIndex.php?index=" + str(index)
    return json.loads(requests.get(url).content)


#Per ogni utente si va a mettere sul database l'identificativo della foto e lo username della persona che ha messo la foto
def salvoSulDatabaseIdImmagineEUsernameDegliUtentiCheVoglionoLike(array_user_get_like):

    #Per ogni persone che vuole ricevere like prendo lo username e l'identificativo e la metto sul database
    for user_get_like in array_user_get_like:
        username_user_get_like = str(user_get_like["USERNAME"])
        idPrimaFoto = ottengoIdPrimaFotoDaUsername(username_user_get_like)

        print(username_user_get_like + " id:" + str(idPrimaFoto))

        if not str(idPrimaFoto).__contains__("lang="):# sono in questo caso se il profilo e' pubblico
            url = url_bot + "/instatrack/likeautomatici/saveUsernameAndIdImmagineIntoDatabase.php"
            payload = {'id_immagine': idPrimaFoto, 'username': username_user_get_like}
            return_request = requests.post(url, data=payload).content
            print("Salvo la foto di: " + str(username_user_get_like) + " con ID: " + idPrimaFoto)

        else:#sono in questo caso se il profilo e' privato
            print("Non posso prendere questo utente\n")

def updateUsersLiked(users_liked_string, id_immagine):
    payload = {'id_immagine': id_immagine, 'users_liked': users_liked_string}
    url = url_bot + "/instatrack/likeautomatici/updateUserLiked.php"
    return_request = requests.post(url, data=payload).content
    return return_request


#Questa funzione permette di cambiare il valore di GET_LIKE nel database
def updateGetLikeFromUsername(username,get_like):
    payload = {'username': username, 'get_like': get_like}
    url = url_bot + "/instatrack/likeautomatici/updateGetLikeFromUsername.php"
    return_request = requests.post(url, data=payload).content
    print(return_request)


#Questa funzione permette di cambiare il valore di SET_LIKE nel database
def updateSetLikeFromUsername(username,set_like):
    payload = {'username': username, 'set_like': set_like}
    url = url_bot + "/instatrack/likeautomatici/updateSetLikeFromUsername.php"
    return_request = requests.post(url, data=payload).content
    print(return_request)

def automaticLIKE(username, cookies_str, cookies_dict):

    #Questa variabile contiene il numero di LIKE massimo che si puo ottenere con il BOT
    max_like = 20

    # In questo array ho tutte le foto e tutte le persone che hanno messo like.
    numberPhotoIntoDatabase = int(countPhotoIntoDatabase())

    # In questo array inserisco tutte le foto e le persone che hanno messo like ma solo le foto che hanno un numero di like < max_like
    array_photo_to_auto_like = []

    # ciclo sul numero delle foto e inserisco nell'array array_photo_to_auto_like la foto che deve ottenere i like
    for index in range(0, int(numberPhotoIntoDatabase)):
        # Seleziono la tupla relativa all'utente
        photo = selectPhotoFromDatabase(index)

        id_photo = str(photo[0]['ID_IMMAGINE'])
        users_liked_string = str(photo[0]['USERS_LIKED'])
        users_liked_array = re.split(';', users_liked_string)
        username_immagine = str(photo[0]['USERNAME_IMMAGINE'])

        photo_dictionary = {
            "ID_IMMAGINE": id_photo,
            "USERS_LIKED_STRING": users_liked_string,
            "USERNAME_IMMAGINE": username_immagine,
        }

        print(
            "Processo la foto con id: " + id_photo + " dell'utente:" + username_immagine + " e ha come persone che hanno messo like: " + users_liked_string)

        # se il numero di persone che hanno messo like e' < max_like allora la inserisco in un array
        if len(users_liked_array) < max_like:
            array_photo_to_auto_like.append(
                photo_dictionary)  # array contenente tutte le foto che hanno len(users_liked_array) < max_like
            print("La foto con id: " + id_photo + " non ha raggiunto " + str(max_like) + " like")

    # Per ogni foto vado a far si che gli utenti gli mettano like
    for photo in array_photo_to_auto_like:

        # Per ogni imagine vado a prendere l'identificativo, l'array delle persone che hanno messo like e lo username
        # dell'utente che ha postato tale immagine
        id_photo = photo.get("ID_IMMAGINE")
        users_liked_string = photo.get("USERS_LIKED_STRING")
        users_liked_array = re.split(';', users_liked_string)
        username_get_immagine = photo.get("USERNAME_IMMAGINE")


        # Se lo username che deve mettere like è lo stesso di quello che lo deve ricevere deve continuare al prossimo
        if username_get_immagine == username:
            print("L'utente " + username + " non mette like a se stesso")
            continue

        # se lo username ha gia messo like non lo deve piu mettere e passo al prossimo
        if users_liked_array.__contains__(username):
            print(
                "L'utente: " + username + " ha gia messo like alla foto con id " + id_photo + " dell'utente:" + username_get_immagine)
        else:
            print(
                "L'utente: " + username + " deve mettere like alla foto con id " + id_photo + " dell'utente:" + username_get_immagine)


            content_request = richiestaLike(username_get_immagine, cookies_str, cookies_dict['csrftoken'])
            print(content_request.content)

            if content_request.content.__contains__("azione è stata bloccat"):
                return

            # Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_liked_string == "":
                users_liked_string = username + ";"

            else:
                users_liked_string = users_liked_string + username + ";"
            updateUsersLiked(users_liked_string, id_photo)


            break

################################# QUESTE FUNZIONI SERVONO PER IL LOG ##################

def getCurrentTime():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))


#QUesta funzione scrive nella cartella LOG il file
#Esempio di come deve essere chiamata:scrivoColoratoSuFile("prova.html", "hhhh", "green")
def scrivoColoratoSuFile(nomeFIle, testo, colore):

    #Ottengo l'ora di ora
    timestamp = getCurrentTime()
    with open( nomeFIle, "a") as myfile:
        print(colored(timestamp +" "+testo, colore))
        myfile.write('<p style="color: '+ colore+';">' +timestamp +" "+testo+'</p>')


#Questa funzione permette di eliminare una tupla dal database, in particolare elimina una mail
def removeEmailFromDatabase(id_mail):
    url = url_sms_mail + "/instatrack/send_MAIL/remove_email_from_database.php?ID=" + str(id_mail)
    return json.loads(requests.get(url,verify=False).content)

def removeSMSFromDatabase(id_sms):
    url = url_sms_mail + "/instatrack/send_SMS/remove_sms_from_database.php?ID=" + str(id_sms)
    return json.loads(requests.get(url).content)

#QUesta fnuzione mostra il numero di followers dallo username
def getCountFollowersFromUsername(username):
    headers = {
    'authority': 'www.instagram.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'mid=W4UpIQAEAAFq1cr_ml2C4FPWs8ot; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_cb=1; shbid=18440; shbts=1546613875.9463286; rur=FTW; csrftoken=9XKeMDWlkfpQmpvCbR2fiNRUQT2yJKFr; ds_user_id=1724745946; sessionid=1724745946%3Ae0F325eRVx05r0%3A14; urlgen="{\\"2.230.243.113\\": 12874}:1gfZji:ne0jYIxD0QXAfKgJKpO4vzEWpC8"',
    }

    response = str(requests.get('https://www.instagram.com/' + str(username), headers=headers).content)
    followers = str(response[response.find('<meta content="Follower: ') + len('<meta content="Follower: '):response.find(', seguiti:')])

    if len(followers) > 10 or len(followers) == 0:
        return "false"
    else:
        return followers

#Questa funzione permette di ottenere il numero di telefono a partire dalla mail relativa all'utente.
def getPhoneNumberFromEmail(email):
    url = "http://www.giuliovittoria.it/get_number_from_email.php?EMAIL=" + str(email)
    risposta =  json.loads(requests.get(url).content)
    NUMERO_TELEFONICO = risposta[0]["nphone"]
    PREFISSO = risposta[0]["prefix"]
    PREFISSO_NUMERO_TELEFONICO = PREFISSO + NUMERO_TELEFONICO
    return PREFISSO_NUMERO_TELEFONICO