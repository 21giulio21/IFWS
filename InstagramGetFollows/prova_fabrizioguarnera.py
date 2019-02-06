#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base64
import time
import ast
import random
import thread
import time


from InstagramAPI import updateTempoBlocco, follow_thread, unfollow_thread, sendSMSToUser
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
import re
import sys




C1 = ""
C2 = ""
array_to_get_like = []

for thread_I in range(1,21):

    numberUsersIntoDatabase = countUserIntoDatabaseFromTread(thread_I)

    # Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabaseAndThread(index,thread_I)

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

        if script_attivo == "1":
            array_to_get_like.append(username)



        if username == "fabrizioguarnera__":
            temp = base64.b64decode(str(cookie))
            cookies_dict = ast.literal_eval(temp)
            cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

            C1 = cookies_str
            C2 = cookies_dict['csrftoken']


print(array_to_get_like)

for username in array_to_get_like:

    print("fabrizioguarnera__ mette like a " + str(username))
    print(richiestaLike(username,C1, C2).content)
    time.sleep(100)


