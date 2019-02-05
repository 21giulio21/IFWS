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
from InstagramAPI import automaticLIKE
import threading
from threading import *
import re
import sys

# max_requests indica dopo quante richieste cambio da follow a unfollow,
# dopo 300 richieste di follow ne faccio 300 di unfollo e cosi via
#max_requests = 250

# numero di richieste dopo il quale si decrementa il DT


number_requests_update_delta_t = 1000

tempo_blocco_se_esce_errore = 500

#Passo come parametro dello script un tempo ad esmepio 30 in questo modo lo script ogni volta aspetta 3 secondi
tempo_passato_come_patametro =  int(sys.argv[1])

#Definisce il pc su cui deve andare
thread_passato_come_patametro = int(sys.argv[2])




print("\nAttendo DT")

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

    #QUesta variabile se è a 1 allora l'utente manda la richiesta di follow
    auto_follow = str(user[0]['AUTO_FOLLOW'])

    # QUesta variabile se è a 1 allora l'utente manda la richiesta di commenta
    auto_comment = str(user[0]['AUTO_COMMENT'])

    # Se è 1 allora bisogna che l'utente metta like.
    auto_like = str(user[0]['AUTO_LIKE'])



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

    # deve_pagare e' a 1 solo se l'utente non ha pagato.
    deve_pagare = str(user[0]['DEVE_PAGARE'])

    # Tempo in uci deve finire lo script
    tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])
    # deve_pagare e' a 1 solo se l'utente non ha pagato.
    target = str(user[0]['TARGET'])

    # mail dell'utente
    email = str(user[0]['EMAIL'])

    # Massimo numero di richieste che l'utente deve fare
    max_requests = int(user[0]['MAX_REQUESTS'])


    # Controllo il tempo_iscrizione, se sono passati 3 giorni allora deve pagare ossia impostare: DEVE_PAGARE a 1
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:-3]

    if len(tempo_iscrizione) > 4:  # Se l'utente non ha pagato e l'ho inserito dal sito internet
        if tempo_fine_iscrizione < tempo_di_ora and deve_pagare == "0":  # Se sono passati 3 giorni come prova oppure è passato il tempo per cui ha pagato
            # Aggiorno il valore dell'utente DEVE_PAGARE in questo modo compare un banner sul sito per farlo pagare.

            messaggio = "DEVE PAGARE - Mando la mail per comunicarlo"
            stampa(username, messaggio)

            # GLi mando la mail dicendo che deve pagare
            msg = "Ciao " + username + ",\n\nIl tuo abbonamento e' scaduto!\nAccedi al sito instatrack.eu per rinnovare il servizio.\n\nNon perdere l'occasione di guadagnare con Instagram\n\n\n\n\nA presto,\nInstatrack.eu"
            subject = "Instatrack.eu - Abbonamento scaduto"
            sendMailToUser(email, msg, subject)


            updateSctiptActive(username, 0)  # Metto sctipt_attivo = 0
            updateDevePagare(username, 1)  # Imposto che deve pagare



    # Se la password e' errata non lo processo neanche e merro a 0 script_active nel caso fosse a 1
    if password_errata == '1':
        messaggio = "PASSWORD ERRATA - Non processo questo utente"
        stampa(username, messaggio)

        if script_attivo == '1':
            updateSctiptActive(username, 0)
            continue
        continue

    # Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
    # facendo il login
    if len(cookie) == 0:
        content_request = login(username, password_instagram)
        parse_content_request(content_request, "LOGIN", username, tempo_blocco_se_esce_errore, delta_t, email)
        cookies_dict = content_request.cookies.get_dict()

        # Salvo la variabile cookies_dict sul server
        seveCookieIntoServer(username, cookies_dict)
    else:
        temp = base64.b64decode(str(cookie))
        cookies_dict = ast.literal_eval(temp)

    # Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
    cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)
    # Controllo che deve fermarsi se ho un tempo di blocco attivo, in particolare se ho tempo_attesa_blocco > 0 devo continuare  senza processarlo
    if int(tempo_attesa_blocco) > 0:
        tempo_attesa_blocco = int(tempo_attesa_blocco) - 1
        updateTempoBlocco(username, str(tempo_attesa_blocco))

        messaggio = "BLOCCO - Utente in blocco per ancora:" + str(tempo_attesa_blocco) + " cicli"
        stampa(username, messaggio)
        continue

    # Controllo che secondi_ultima_richiesta + delta_t sia maggiore di ora, se lo e' allora devo processare
    # altrimenti non devo processare
    tempo_ora = int(time.time())

    if int(secondi_ultima_richiesta) + int(delta_t) > tempo_ora:
        #messaggio = "DT NON PASSATO - Non processo questo utente perche non è passato il DT"
        #stampa(username, messaggio)
        continue

    # Se script_attivo e' 0 allora devo smettere di seguire tutti quelli che sono nell'array di persone che seguo
    if script_attivo == "0" and len(users_followed_array) > 1:

        # Devo prendere un utente che seguiva questo utente e mandare la richiesta di UNFOLLOW per far si che le persone che segue siano le stesse di quella che
        # seguiva prima del bot

    # Faccio in modo che la stringa contenente tutti gli user che seguo che e' sul mio database sia
        # ben fatta, in particolare che non ci siano situazioni in cui ho user;user;user;
        # in questo caso andrebbe tolto l'ultimo ;

        users_followed_array_temp = users_followed_array
        for i in users_followed_array_temp:
            if i == "":
                users_followed_array.remove(i)

        # elimino il primo user che ho seguito
        username_user_to_unfollow = users_followed_array.pop(0)

        # Costruisco nuovamente la stringa da mandare al mio server
        for i in range(0, len(users_followed_array)):
            if i == 0:
                users_followed_string = users_followed_array[i] + ";"
            elif i == len(users_followed_array) - 1:
                users_followed_string = users_followed_string + users_followed_array[i]
            else:
                users_followed_string = users_followed_string + users_followed_array[i] + ";"

        if len(users_followed_array) == 0:
            users_followed_string = ""
            # mando la richiesta di unfollow all'utente come thread
            unfollow_thread(
                username_user_to_unfollow, cookies_str, cookies_dict
                , username, tempo_blocco_se_esce_errore, delta_t, email, users_followed_string)


            continue
        else:

            # Mando la richiesta di unfollow
            # mando la richiesta di unfollow all'utente come thread
            unfollow_thread(
                username_user_to_unfollow, cookies_str, cookies_dict
                , username, tempo_blocco_se_esce_errore, delta_t, email, users_followed_string)


        continue

    if len(id) == 0:
        messaggio = "CHIEDO ID A INSTAGRAM"
        stampa(username, messaggio)


        id = getIDFromUsername(username)
        saveIdIntoDatabase(username, id)

    # Imposto a 1 perche non va con 0 comunque ogni volta riempie il campo user_followed e lo svuota
    if len(users_followed_array) == 1 and script_attivo == "1":
        # Devo iniziare a seguire

        messaggio = "INIZIO A CON LE RICHIESTE DI FOLLOW"
        stampa(username, messaggio)

        follow_unfollow = str('1')
        updateFollowUnfollowDatabase(username, str(follow_unfollow))

    #Se seguo un numero di persone pari al massimo di quelle che devo seguire allora deo fare un unfollow
    if ((len(users_followed_array) == max_requests) or (len(users_followed_array) > max_requests)) and script_attivo == "1":  # max_requests:

        messaggio = "MASSIMO UTENTI SEGUITI - imposto follow_unfollow a 0"
        stampa(username, messaggio)


        # Se sono al numero di persone massime imposto users_followed a 0
        # In questo modo inizio a fare richieste di unfollow
        follow_unfollow = "0"
        # Aggiorno il server dicendo che follow_unfollow e' zero
        updateFollowUnfollowDatabase(username, follow_unfollow)




    #Se non seguo ancora il numero massimo di persone
    if follow_unfollow == "1" and script_attivo == "1" and (len(users_followed_array) < max_requests):



        #Se devo mettere follow
        if auto_follow == "1":
            # Mi faccio tornare un utente da seguire con stesso target
            # dell'utente che sto processando. Questo è realizzato dal php

            user_to_follow = getUserToFollwFromTarget(target,username)
            id_user_to_follow = str(user_to_follow[0]["ID"])
            username_user_to_follow = str(user_to_follow[0]["USERNAME"])
            target = str(user_to_follow[0]["TARGET"])

            # Controllo se la persona è gia precedentemente stata seguita
            if checkIfYetFollowing(username_user_to_follow, cookies_str) == True:
                messaggio = "UTENTE GIA SEGUITO - Ho gia seguito questo utente quindi mando la richiesta ad un altro"
                stampa(username, messaggio)
                continue

            #mando la richiesta di follow all'utente come thread
            follow_thread(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict,username,number_requests_done,tempo_blocco_se_esce_errore,delta_t,target,email)


            # Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_followed_string == "":
                users_followed_string = username_user_to_follow + ";"

            else:
                users_followed_string = users_followed_string + username_user_to_follow + ";"

            #aggiorno il database

            if not users_followed_string.endswith(";"):
                users_followed_string = users_followed_string + ";"

            updateUserFollowed(users_followed_string, username)

        # Tale richiesta va a buon fine solo se il profilo non e' privato. Nel caso sia privato non funziona la richiesta di like
        # se il profilo e' publico funziona bene
        # Se set_like è uno allora con probabilità 1 / 4 mettero un like
        if auto_like == "1":

            #Prendo un utente dal database a cui mettere like
            #user_to_follow = getUserToFollwFromTarget(target, username)
            #id_user_to_follow = str(user_to_follow[0]["ID"])
            #username_user_to_follow = str(user_to_follow[0]["USERNAME"])
            #target = str(user_to_follow[0]["TARGET"])


            # Faccio in modo che con probabilità 1/4 metta like quindi non verra messo sempre, in modo
            # tale da aumentare il nuemro di richiueste di follow
            #random_number = random.randint(1, 20)

            # Solamente se random_number è 1 allora mando una richiesta di like, in questo modo sono sicuro che
            # ho la probabilità di 1/3 di mettere like. quindi non dovrebbe bloccarlo.
            #if random_number == 5:

                ''' Se scommento qui mette like alla prima foto dell'utente a cui si hanno mandato la richesta di FOLLOW
                print("Processo l'utente: " + username + " mette like  alla foto di " + username_user_to_follow)
                content_request = richiestaLike(username_user_to_follow, cookies_str, cookies_dict['csrftoken'])
                parse_content_request(content_request, 'LIKE', username, tempo_blocco_se_esce_errore, delta_t,email)
                '''
                #In questo caso metto like alle persone che hanno AUTO_LIKE a 1
                #automaticLIKE(username, cookies_str, cookies_dict)




            #else:
                #print("Processo l'utente: " + username + " non mette il like, forse la prossima volta ?")

        # Metto un commento all'ultima foto con probabilità 1/4 in questo modo non verrà bloccato l'account
        if auto_comment == "1":
            # Faccio in modo che con probabilità 1/4 commenta quindi non verra messo sempre, in modo
            # tale da aumentare il nuemro di richiueste di follow
            random_number = random.randint(1,4)
            if random_number == 2:

                risposta_commento = comment(cookies_str, cookies_dict['csrftoken'], username_user_to_follow)

                messaggio = "COMMENTA FOTO - Commento la foto di " + username_user_to_follow +" "+risposta_commento
                stampa(username, messaggio)

            else:
                messaggio = "COMMENTA FOTO - Commento la prossima volta"
                stampa(username, messaggio)
        else:
            print(" ")

        # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
        update_secondi_ultima_richiesta(username, int(time.time()))



    elif script_attivo == "1" and follow_unfollow == "0":

        print("sssssssssss")

        # Faccio in modo che la stringa contenente tutti gli user che seguo che e' sul mio database sia
        # ben fatta, in particolare che non ci siano situazioni in cui ho user;user;user;
        # in questo caso andrebbe tolto l'ultimo ;

        users_followed_array_temp = users_followed_array
        for i in users_followed_array_temp:
            if i == "":
                users_followed_array.remove(i)

        # elimino il primo user che ho seguito
        username_user_to_unfollow = users_followed_array.pop(0)

        print("DOVREI FARE UNFOLLOW DI: " + username_user_to_unfollow)

        # Costruisco nuovamente la stringa da mandare al mio server
        for i in range(0, len(users_followed_array)):
            if i == 0:
                users_followed_string = users_followed_array[i] + ";"
            elif i == len(users_followed_array) - 1:
                users_followed_string = users_followed_string + users_followed_array[i]
            else:
                users_followed_string = users_followed_string + users_followed_array[i] + ";"

        if len(users_followed_array) == 0:

            users_followed_string = ""
            unfollow_thread(
                username_user_to_unfollow, cookies_str, cookies_dict
                , username, tempo_blocco_se_esce_errore, delta_t, email, users_followed_string)

        else:



            if not users_followed_string.endswith(";"):
                users_followed_string = users_followed_string + ";"
            # mando la richiesta di unfollow all'utente come thread

            unfollow_thread(
                username_user_to_unfollow,cookies_str,cookies_dict
                ,username,tempo_blocco_se_esce_errore,delta_t,email,users_followed_string)


        #In questo caso riparto da capo
        if (len(users_followed_array) == max_requests) or (len(users_followed_array) < max_requests) :
            updateFollowUnfollowDatabase(username,"1")




