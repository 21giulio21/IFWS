#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base64
import time
import ast
import random
import thread
import time
from function import stampa

from InstagramAPI import updateTempoBlocco, follow_thread, unfollow_thread
from InstagramAPI import comment
from InstagramAPI import update_secondi_ultima_richiesta
from InstagramAPI import updateFollowUnfollowDatabase
from InstagramAPI import updateUserFollowed
from InstagramAPI import saveIdIntoDatabase
from InstagramAPI import seveCookieIntoServer
from InstagramAPI import follow
from InstagramAPI import login
from InstagramAPI import unfollow
from InstagramAPI import getUserToFollwFromTarget
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase
from InstagramAPI import getIDFromUsername
from InstagramAPI import getCountUsersToFollow
from InstagramAPI import richiestaLike
from InstagramAPI import updateDevePagare
from InstagramAPI import updateNumberRequestsDone
from InstagramAPI import updateSctiptActive
from InstagramAPI import parse_content_request
from InstagramAPI import countUserIntoDatabaseFromTread
from InstagramAPI import selectUserFromDatabaseAndThread
from InstagramAPI import checkIfYetFollowing
from InstagramAPI import sendMailToUser
from InstagramAPI import getIdFromUsernameToUnfollow
import threading
from threading import *
import base64
import time
import ast
import random
from InstagramAPI import sendMailToUser, parse_content_request_for_LOGIN_THREAD_0
from InstagramAPI import updateTempoBlocco
from InstagramAPI import comment
from InstagramAPI import update_secondi_ultima_richiesta
from InstagramAPI import updateFollowUnfollowDatabase
from InstagramAPI import updateUserFollowed
from InstagramAPI import saveIdIntoDatabase
from InstagramAPI import seveCookieIntoServer
from InstagramAPI import follow
from InstagramAPI import login
from InstagramAPI import unfollow
from InstagramAPI import getUserToFollwFromTarget
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase
from InstagramAPI import getIDFromUsername
from InstagramAPI import getCountUsersToFollow
from InstagramAPI import richiestaLike
from InstagramAPI import updateDevePagare
from InstagramAPI import updateNumberRequestsDone
from InstagramAPI import updateSctiptActive
from InstagramAPI import parse_content_request
from InstagramAPI import countUserIntoDatabaseFromTread
from InstagramAPI import selectUserFromDatabaseAndThread
import re
import sys







# max_requests indica dopo quante richieste cambio da follow a unfollow,
# dopo 300 richieste di follow ne faccio 300 di unfollo e cosi via
#max_requests = 250

# numero di richieste dopo il quale si decrementa il DT
number_requests_update_delta_t = 1000

tempo_blocco_se_esce_errore = 500

#Passo come parametro dello script un tempo ad esmepio 30 in questo modo lo script ogni volta aspetta 3 secondi
tempo_passato_come_patametro =  5

#Definisce il pc su cui deve andare
thread_passato_come_patametro = 0

#Definisco il numero massimo di richieste che devo fare
max_requests = 200

while True:

    print("Attendo DT")

    time.sleep(tempo_passato_come_patametro)
    print("Tempo DT passato, inizio lo script.")

    # Chiedo quanti utenti ho nel database
    numberUsersIntoDatabase = countUserIntoDatabaseFromTread(thread_passato_come_patametro)
    print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

    # Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabaseAndThread(index,thread_passato_come_patametro)

        id = str(user[0]['ID'])
        username = str(user[0]['USERNAME'])
        cookie = str(user[0]['COOKIES'])
        secondi_ultima_richiesta = str(user[0]['SECONDI_ULTIMA_RICHIESTA'])
        delta_t = str(user[0]['DELTA_T'])
        follow_unfollow = str(user[0]['FOLLOW_UNFOLLOW'])
        users_followed_string = str(user[0]['USERS_FOLLOWED'])
        users_followed_array = re.split(';', users_followed_string)
        password_instagram = str(user[0]['PASSWORD_INSTAGRAM'])
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

        #mail dell'utente
        email = str(user[0]['EMAIL'])


        print("Processo l'utente: " + username + " che ha una mail " + email)


        # Controllo il tempo_iscrizione, se sono passati 3 giorni allora deve pagare ossia impostare: DEVE_PAGARE a 1
        tempo_di_ora = str(time.time())
        tempo_di_ora = tempo_di_ora[:-3]

        if len(tempo_iscrizione) > 5:  # Se l'utente non ha pagato e l'ho inserito dal sito internet
            if tempo_fine_iscrizione < tempo_di_ora and deve_pagare == "0":  # Se sono passati 3 giorni come prova oppure è passato il tempo per cui ha pagato
                # Aggiorno il valore dell'utente DEVE_PAGARE in questo modo compare un banner sul sito per farlo pagare.
                print("Processo l'utente: " + username + " deve pagare")
                updateSctiptActive(username, 0) #Metto sctipt_attivo = 0
                updateDevePagare(username, 1) # Imposto che deve pagare

                #se è stata settata la mail allora manda la mail con scritto che deve poagare
                if len(email) > 3:
                    print("Mando la mail all'utente " +str(username) + " per avvertire che bisogna pagare")

                    # mando la mail che l'utente deve pagare, preparo la mail e la invio, invio anche una copia al miop
                    #Indirizzo cosi so sempre cosa accade!
                    msg = "Ciao " + username + ",\n\nL'abbonamento sul tuo account è staduto, collegati al sito www.instatrack.eu per scegliere il pacchetto più adatto a te!\n\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
                    subject = "Instatrack.eu - Fine Prova"
                    sendMailToUser(email,msg,subject)

        # Se la password e' errata non lo processo neanche e merro a 0 script_active nel caso fosse a 1
        if password_errata == '1':
            print("Non processo l'utente: " + username + " perche ha la password errata")
            if script_attivo == '1':
                updateSctiptActive(username, 0)
                continue
            continue

        # Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
        # facendo il login
        if len(cookie) == 0:
            content_request = login(username, password_instagram)


            retult = parse_content_request_for_LOGIN_THREAD_0(content_request, "LOGIN", username, tempo_blocco_se_esce_errore, delta_t,email)

            #Se è 0 allora sono in checkpoint quindi non memorizzo il cookie
            if retult == 0:
                continue

            cookies_dict = content_request.cookies.get_dict()

            # Salvo la variabile cookies_dict sul server
            seveCookieIntoServer(username, cookies_dict)
        else:
            temp = base64.b64decode(str(cookie))
            cookies_dict = ast.literal_eval(temp)

