#import instaloader
import json
import time
import datetime as dt

import requests

from InstagramAPI import getIDFromUsername

#Scarico esattamente tanti username che devono mettere like quanti quelli che devono riceverne
def getFuelgramAccountGetLike(quanti):
    response = requests.get("http://www.utentidaseguire.eu/instatrack/FUELGRAM_LIKE/get_username_get_like_from_database.php?QUANTI=" + str(quanti)).content
    return json.loads(response)

def getUsernameVolentereosiDiLike():
    response = requests.get("http://www.giuliovittoria.it/instatrack/LIKE_FUELGRAM/getUserToRegiveLikes.php").content
    return json.loads(response)

def insertUserIntoFUELGRAM_ACCOUNT_RECEIVER_LIKE(username,url_foto):
    #Inserisco la data di inserimento nel momento in cui inserisco la foto che dovra ricevere like!
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]
    url = "http://utentidaseguire.eu/instatrack/FUELGRAM_LIKE/insert_username_receive_like_from_database.php"
    response = requests.get(url + "?USERNAME=" + str(username) +"&URL=" + str(url_foto)+"&DATA_INSERIMENTO=" + str(tempo_di_ora) ).content
    print(response)

def scaricoUsernameCheHannoPubblicato(numeroUsernameDaScaricare):
    response = requests.get("http://www.utentidaseguire.eu/instatrack/FUELGRAM_LIKE/get_username_recive_like_from_database.php?QUANTI="+str(numeroUsernameDaScaricare)).content
    return json.loads(response)




#QUesta funzione permette di salvare nel database tutti gli url e gli username degli utenti che hanno pubblicato la foto nell ultime 24 ore
def salvoUsername_Foto_24H():
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]

    # questi sono i secondi in un giorno
    secondi_indietro = 86400

    # tempo da cui considero e inizio il round,
    tempo_o = int(tempo_di_ora) - secondi_indietro




    #Ottengo tutti gli username che vogliono like
    utenti_che_vogliono_like = getUsernameVolentereosiDiLike()

    for utente in utenti_che_vogliono_like:
        username = str(utente["USERNAME"])
        try:
            posts = instaloader.Profile.from_username(L.context, username).get_posts()

            #Controllo tra tutte le foto se c'e' ne almeno 1 nelle ultime 24 ore
            for post in posts:
                data_publicazione = int(post.date.timestamp())

                #Controllo che la data di publicazione della foto sia di almeno nelle ultime 24 ore
                if int(data_publicazione) > int(tempo_o):
                    print(username, post.url )


                    insertUserIntoFUELGRAM_ACCOUNT_RECEIVER_LIKE(username, post.url)

                break

        except:
            print("Non riesco a prendere la foto di " + str(username))

cookies = {
        'django_language': 'en-us',
        '_ga': 'GA1.2.79789760.1551402844',
        '_gid': 'GA1.2.1596153902.1551402844',
        '__stripe_mid': '8b7b92af-c341-44d4-814b-c8f812defe79',
        '__stripe_sid': '0cbff8c0-f30e-4f54-a784-9e6e94b9834d',
        'crisp-client%2Fsession%2Fc565f69a-cf98-45e4-9876-c35965c79ae3': 'session_01aa08f2-b84e-49a5-bb06-6be74fd74cc0',
        'crisp-client%2Fsession%2Fc565f69a-cf98-45e4-9876-c35965c79ae3%2Ffuelgram-36400-21giulio21%40gmail.com': 'session_01aa08f2-b84e-49a5-bb06-6be74fd74cc0',
    }

headers = {
        'Pragma': 'no-cache',
        'Origin': 'https://fuelgram.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Token 4aef61de50e8dc4d1ec05a93dd496d0068406837',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://fuelgram.com/app/autorounds',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}



def configurazioneSLOT(username_recive_likes,username_get_likes,ID_SLOT):
    IG_id_recive_likes = getIDFromUsername_PY3(username_recive_likes)
    IG_id_get_likes = getIDFromUsername_PY3(username_get_likes)

    print(IG_id_recive_likes , IG_id_get_likes)



    data = '{"receivers":[{"id":' + str(
        IG_id_recive_likes) + ',"niches":[],"avatar":"https://scontent-arn2-1.cdninstagram.com/vp/596d79cd95aa3f6e2939100d88c98040/5D26913E/t51.2885-19/51283637_2303526969862991_8685960324047699968_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","media_count":988,"follower_count":2891,"followed_count":1258,"username":"' + str(
        username_recive_likes) + '","status":"ok","user":36400}],"account":{"avatar":"https://scontent-arn2-1.cdninstagram.com/vp/6afb65ae6d429c015aaf458553bef513/5D1F0F14/t51.2885-19/52666869_2193616227556915_4300790339645472768_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","followed_count":0,"follower_count":17,"id":' + str(
        IG_id_get_likes) + ',"media_count":0,"status":"ok","user":36400,"username":"' + str(
        username_get_likes) + '"},"rounds":' + str(getRount()) + ',"extra":{},"active":true}'

    response = requests.post('https://fuelgram.com/api/users/36400/products/'+str(ID_SLOT)+'/settings/', headers=headers,
                             cookies=cookies, data=data)
    return response.content

#Aggiorno il valore di LAST_ROUND
def updateLAST_ROUND_username_get_likes(username_get_likes):
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]
    response = requests.get("http://www.utentidaseguire.eu/instatrack/FUELGRAM_LIKE/updateLAST_ROUND_username_get_likes.php?USERNAME="+str(username_get_likes)+"&LAST_ROUND="+str(tempo_di_ora))


#AGGIORNO IL VALORE DI DONE
def updateDONE_username_recive_likes(username_recive_likes):
    url = "http://www.utentidaseguire.eu/instatrack/FUELGRAM_LIKE/updateDONE_username_recive_likes.php?USERNAME="
    response = requests.get(url + username_recive_likes )

#Questa funzione permette di ritornare il round corretto a partire dall'orario che è ora!
def getRount():
    ora_del_giorno = int(dt.datetime.now().hour)
    if   12 <= ora_del_giorno <= 15:
        print("Imposto round delle 14:00")
        return '["13:30"]'
    elif   16 <= ora_del_giorno <= 18:
        print("Imposto round delle 17:00")
        return '["16:30"]'
    elif   19 <= ora_del_giorno <= 21:
        print("Imposto round delle 20:00")
        return '["19:30"]'
    elif   22 <= ora_del_giorno <= 23 or ora_del_giorno == 0:
        print("Imposto round delle 23:00")
        return '["22:30"]'
    elif   0 <= ora_del_giorno <= 3:
        print("Imposto round delle 2:00")
        return '["01:30"]'
    elif   4 <= ora_del_giorno <= 11:
        print("Imposto round delle 11:00")
        return '["10:30"]'
    else:
        print("BHO")
        return '["10:30"]'

def getIDFromUsername_PY3(username):

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
    id = str(inizio_id[:inizio_id.find("\"")])
    return id

# Queste credenziali sono di un profilo a caso che permette solamente di
    # avere accesso ai post e dati dei p
username_IG = "instatrack.eu"
password_IG = "vikagiulio2121"





#Questi sono tutti gli identificativi delle slot comprate
array_ID_SLOT = []
array_ID_SLOT.append("276794")
array_ID_SLOT.append("276793")
array_ID_SLOT.append("286830")
array_ID_SLOT.append("286833")
array_ID_SLOT.append("276794")
array_ID_SLOT.append("280188")
array_ID_SLOT.append("276792")
array_ID_SLOT.append("276791")
array_ID_SLOT.append("286831")
array_ID_SLOT.append("268891")
array_ID_SLOT.append("286835")
array_ID_SLOT.append("280186")
array_ID_SLOT.append("286834")




'''
Salvo nel database tutti gli URL, Username ecc di quelli che hanno pubblicato fino a 24 ore prima
'''

#TODO
#salvoUsername_Foto_24H()

'''
Una volta che ho inserito tutti gli url e i relativi username nel mio database ritorno tanti username quanti
il numero di slot al massimo.
In questo modo per ogni utente che ha pubblicato posso mandargli i like.
'''

#Avendo comprato un tot di slot di autoround posso solamente interagire con quelle, scarico tanti
#username quante sono le slot che ho comprato
numero_slot_comprate = 12

#Scarico gli username che devono ricevere like, al massimo quante slot ho
username_da_mettere_like = scaricoUsernameCheHannoPubblicato(numero_slot_comprate)

#In base a quanto username devono ricevere like scarico il numero di persone che dovrenno mettere,
#in particolare se 4 persone devon oricevere, 4 devono metterne per loro
numero_username_che_devono_mettere_like = len(username_da_mettere_like)

#Scarico gli username che devono mettere like
username_che_metono_like = getFuelgramAccountGetLike(numero_username_che_devono_mettere_like)


#Ora facciamo un for che va da 0 al numero di persone da processare e riempiamo le slot
for index in range(0,len(username_da_mettere_like)):

    time.sleep(2)

    username_recive_likes = username_da_mettere_like[index]["USERNAME"]
    username_get_likes = username_che_metono_like[index]["USERNAME"]

    print(username_recive_likes,username_get_likes)
    risposta = str(configurazioneSLOT(username_recive_likes,username_get_likes,array_ID_SLOT[index]))

    #Se la risposta dice che un account deve essere validato mando una mail a me dicendo che devo verificare l'account
    if risposta.__contains__("challenge_verification_required"):
        print("Devo verificare l'account: " + username_get_likes)

    print(risposta)

    #ora imposto che il profilo username_get_likes ha messo like ora quindi non dovra piu mettere like per un po
    updateLAST_ROUND_username_get_likes(username_get_likes)

    #Aggiorno il valore DONE dello username username_recive_likes una volta che l'ho impostato
    updateDONE_username_recive_likes(username_recive_likes)

