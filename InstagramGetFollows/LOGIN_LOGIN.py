#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os

import requests
import base64
import time
import ast
import re

from InstagramAPI import parse_content_request_for_LOGIN_THREAD_0
from InstagramAPI import seveCookieIntoServer
from InstagramAPI import login

url_bot = "http://www.giuliovittoria.it"


##nel momento in cui un utente inizia la prova se l'iscrizione è avvenuta con successo allora devo andare a prendergli il media
#e inserirlo dentro alla tavella che fa si che gli arrivino like
import time


import requests


def insertUserIntoFUELGRAM_ACCOUNT_RECEIVER_LIKE(username,url_foto):
    #Inserisco la data di inserimento nel momento in cui inserisco la foto che dovra ricevere like!
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]
    url = "http://utentidaseguire.eu/instatrack/FUELGRAM_LIKE/insert_username_receive_like_from_database.php"
    response = requests.get(url + "?USERNAME=" + str(username) +"&URL=" + str(url_foto)+"&DATA_INSERIMENTO=" + str(tempo_di_ora) ).content
    print(response)


def recuperoUltimaFotoDellUtenteCheSiLogga(username):
    return "post iniziale"



#QUesta funzione indica quanti utenti devono iniziare la prova.
#In particolare mostra tutti gli account che hanno DEVE_PAGARE = 0, THREAD = 0 e PASSWORD_ERRATA = 0
def countUser_START_PROVA():
    url = url_bot + "/instatrack/getCountUser_START_PROVA.php"
    return requests.get(url).content


#Questa funzione seleziona Account per account di utnti che devono iniziare la prova
def selectUser_START_PROVA(index):
    url = url_bot + "/instatrack/getUser_START_PROVA.php?index=" +str(index)
    return json.loads(requests.get(url).content)




# numero di richieste dopo il quale si decrementa il DT
number_requests_update_delta_t = 1000

tempo_blocco_se_esce_errore = 500

# Passo come parametro dello script un tempo ad esmepio 30 in questo modo lo script ogni volta aspetta 3 secondi
tempo_passato_come_patametro = 5

# Definisce il pc su cui deve andare
thread_passato_come_patametro = 0


# print("Attendo DT")

# time.sleep(tempo_passato_come_patametro)
# print("Tempo DT passato, inizio lo script.")

# Chiedo quanti utenti ho nel database

# Chiedo quanti utenti ho nel database
numberUsersIntoDatabase = countUser_START_PROVA()
print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

# Ora ciclo sul totale di persone che ho nel database
for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUser_START_PROVA(index)

    id = str(user[0]['ID'])
    username = str(user[0]['USERNAME'])
    cookie = str(user[0]['COOKIES'])
    secondi_ultima_richiesta = str(user[0]['SECONDI_ULTIMA_RICHIESTA'])
    delta_t = str(user[0]['DELTA_T'])
    follow_unfollow = str(user[0]['FOLLOW_UNFOLLOW'])
    users_followed_string = str(user[0]['USERS_FOLLOWED'])
    users_followed_array = re.split(';', users_followed_string)
    password_instagram = user[0]['PASSWORD_INSTAGRAM'].encode('utf-8')
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])
    tempo_attesa_blocco = str(user[0]['TEMPO_ATTESA_BLOCCO'])

    # questa variabile indica le richieste fatte fino ad ora,
    # in particolare dopo 100 richieste diminuisco di 1 secondo DT relativo
    # all'utente, mentre appena esce scritto che devo aspettare qualche minuto per fare altre richieste
    # aumento DT di 1 secondo e attendo 10 minuti prima di fare una nuova richiesta
    number_requests_done = str(user[0]['NUMBER_REQUESTS_DONE'])

    # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
    password_errata = str(user[0]['PASSWORD_ERRATA'])

    # Qui inserisco il tempo in cui si e' iscritto al sito. In questo modo potendo solo dare 3 giorni di tempo come test se passano 3 giorni allora devom impostare
    # il valore: DEVE_PAGARE a 1 .
    tempo_iscrizione = str(user[0]['TEMPO_ISCRIZIONE'])

    # HA_PAGATO e' a 1 solo se l'utente ha pagato. in caso contrario e' 0.

    # deve_pagare e' a 1 solo se l'utente non ha pagato.
    deve_pagare = str(user[0]['DEVE_PAGARE'])

    # Tempo in uci deve finire lo script
    tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])

    # deve_pagare e' a 1 solo se l'utente non ha pagato.
    target = str(user[0]['TARGET'])

    # mail dell'utente
    email = str(user[0]['EMAIL'])

    print("Processo l'utente: " + username + " che ha una mail " + email)

    # Controllo il tempo_iscrizione, se sono passati 3 giorni allora deve pagare ossia impostare: DEVE_PAGARE a 1
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:-3]

    # Se la password e' errata non lo processo neanche e merro a 0 script_active nel caso fosse a 1
    if password_errata == '1':
        # print("Non processo l'utente: " + username + " perche ha la password errata")
        continue

    if deve_pagare == '1':
        # print("Non processo l'utente: " + username + " perche DEVE PAGARE")
        continue

    # Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
    # facendo il login
    if len(cookie) == 0:

        #Questo permette di avere sul
        os.system("py -3 C:\\Users\giulio.tavella\Dropbox\Git\IFWS\InstagramGetFollows\DATI_PROFILO.py " + str(username))
        content_request = login(username, password_instagram)
        retult = parse_content_request_for_LOGIN_THREAD_0(content_request, "LOGIN", username,
                                                          tempo_blocco_se_esce_errore, delta_t, email)

        # Se è 0 allora sono in checkpoint quindi non memorizzo il cookie
        if retult == 0:
            continue

        cookies_dict = content_request.cookies.get_dict()

        # Salvo la variabile cookies_dict sul server
        seveCookieIntoServer(username, cookies_dict)
    else:
        temp = base64.b64decode(str(cookie))
        cookies_dict = ast.literal_eval(temp)


