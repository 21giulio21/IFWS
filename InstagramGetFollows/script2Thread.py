#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base64
import time
import ast
import random
from InstagramAPI import sendMailToUser
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
from InstagramAPI import checkIfYetFollowing

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

#Definisco il numero massimo di richieste che devo fare
max_requests = int(sys.argv[3])

while True:

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
        commenta = str(user[0]['COMMENTA'])

        # questa variabile indica le richieste fatte fino ad ora,
        # in particolare dopo 100 richieste diminuisco di 1 secondo DT relativo
        # all'utente, mentre appena esce scritto che devo aspettare qualche minuto per fare altre richieste
        # aumento DT di 1 secondo e attendo 10 minuti prima di fare una nuova richiesta
        number_requests_done = str(user[0]['NUMBER_REQUESTS_DONE'])

        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])

        # Se è 1 allora bisogna che l'utente metta like.
        set_like = str(user[0]['SET_LIKE'])

        # Qui inserisco il tempo in cui si e' iscritto al sito. In questo modo potendo solo dare 3 giorni di tempo come test se passano 3 giorni allora devom impostare
        # il valore: DEVE_PAGARE a 1 .
        tempo_iscrizione = str(user[0]['TEMPO_ISCRIZIONE'])

        # HA_PAGATO e' a 1 solo se l'utente ha pagato. in caso contrario e' 0.
        ha_pagato = str(user[0]['HA_PAGATO'])

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

        if ha_pagato == "0" and len(tempo_iscrizione) > 5:  # Se l'utente non ha pagato e l'ho inserito dal sito internet
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
                    msg = "Ciao " + username + ",\n\nL'abbonamento sul tuo account e' staduto, collegati al sito www.instatrack.eu per scegliere il pacchetto più adatto a te!\n\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
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
            parse_content_request(content_request, "LOGIN", username, tempo_blocco_se_esce_errore, delta_t,email)
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
            print("Username " + username + " ancora in blocco per un totale di cicli: " + str(tempo_attesa_blocco))
            continue

        # Controllo che secondi_ultima_richiesta + delta_t sia maggiore di ora, se lo e' allora devo processare
        # altrimenti non devo processare
        tempo_ora = int(time.time())

        if int(secondi_ultima_richiesta) + int(delta_t) > tempo_ora:
            print("Processo l'utente: " + username + " NON deve mandare richieste perche non e' ancora passato il suo DT")
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
                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str,
                                           cookies_dict['csrftoken'])
                print("Mando una richiesta di UNFOLLOW a " + str(
                    username_user_to_unfollow) + " per eliminare tutti gli utenti che ho seguito con lo script, " + str(
                    content_request.content))

                parse_content_request(content_request, "FOLLOW-UNFOLLOW", username, tempo_blocco_se_esce_errore,
                                      delta_t,email)

                # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
                update_secondi_ultima_richiesta(username, int(time.time()))
                updateUserFollowed(users_followed_string, username)
                continue
            else:

                # Mando la richiesta di unfollow

                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str,
                                           cookies_dict['csrftoken'])

                print(
                    "Mando una richiesta di UNFOLLOW a " + username_user_to_unfollow + " per eliminare tutti gli utenti che ho seguito con lo script, " + str(
                        content_request.content))

                parse_content_request(content_request, "FOLLOW-UNFOLLOW", username, tempo_blocco_se_esce_errore,
                                      delta_t,email)

                update_secondi_ultima_richiesta(username, int(time.time()))
                updateUserFollowed(users_followed_string, username)

            continue

        if len(id) == 0:
            print(
                "Processo l'utente: " + username + " non ha l'id settato, lo chiedo a Instagram e lo salvo sul mio database")

            id = getIDFromUsername(username)
            saveIdIntoDatabase(username, id)

        # Imposto a 1 perche non va con 0 comunque ogni volta riempie il campo user_followed e lo svuota
        if len(users_followed_array) == 1 and script_attivo == "1":
            # Devo iniziare a seguire

            print("Processo l'utente: " + username + " non segue ancora nessuno, deve iniziare a seguire gente")

            follow_unfollow = str('1')
            updateFollowUnfollowDatabase(username, str(follow_unfollow))

        # controllo che sono al massimo di persone che posso seguire al giorno
        if len(users_followed_array) > max_requests and script_attivo == "1":  # max_requests:

            print(
                "Processo l'utente: " + username + " segue gia il numero massimo di user giornalieri, ora bisogna iniziare a fare unfollow")

            # Se sono al numero di persone massime imposto users_followed a 0
            # In questo modo inizio a fare richieste di unfollow
            follow_unfollow = str("0")

            # Aggiorno il server dicendo che follow_unfollow e' zero
            updateFollowUnfollowDatabase(username, follow_unfollow)

        # numero di richieste che si devono fare prima di diminuire il DT: 1000 per ogni utente
        if int(number_requests_done) > number_requests_update_delta_t and script_attivo == "1":
            # Entro qui dentro dopo 100 richieste per ogni utente fatte
            # In questo modo diminuisco DT per quell'utente perche ne ho gia fatte 100
            # delta_t = int(delta_t) - 1
            # updateDeltaT(username,str(delta_t))
            print("Aggiorno Delta T per l'utente " + username + " perche e arrivato a " + str(
                number_requests_update_delta_t) + " richieste mandate")

            # aggiorno a 0 il numero di richieste mandate perche ho gia diminuito delta t
            # updateNumberRequestsDone(username, "0")

        # Se follow_unfollow e' 1 allora devo seguire una persona a caso tra tutte quelle  nel database
        if follow_unfollow == "1" and script_attivo == "1":

            print("Processo l'utente: " + username + " deve mandare richieste di follow")


            # Mi faccio tornare un utente da seguire con stesso target
            # dell'utente che sto processando. Questo è realizzato dal php

            user_to_follow = getUserToFollwFromTarget(target)
            id_user_to_follow = str(user_to_follow[0]["ID"])
            username_user_to_follow = str(user_to_follow[0]["USERNAME"])
            target = str(user_to_follow[0]["TARGET"])

            #Controllo se la persona è gia precedentemente stata seguita
            if checkIfYetFollowing(username_user_to_follow,cookies_str) == True:
                print("L'utente " + str(username) + " seguiva gia lo username: " + str(username_user_to_follow))
                continue


            # Seguo la persona che ho scaricato e gli metto un like alla prima foto
            contet_request = follow(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict['csrftoken'])

            # In questo punto aumento la variabile:  number_requests_done di 1 e mando al server il nuovo valore di number_requests_done
            updateNumberRequestsDone(username, str(int(number_requests_done) + 1))

            print("Richiesta di FOLLOW mandata a:  " + username_user_to_follow + " " + str(contet_request.content) + " TARGET DELL?UTENTE CHE SEGUO: " + target )

            parse_content_request(contet_request, 'FOLLOW-UNFOLLOW', username, tempo_blocco_se_esce_errore, delta_t,email)

            # Tale richiesta va a buon fine solo se il profilo non e' privato. Nel caso sia privato non funziona la richiesta di like
            # se il profilo e' publico funziona bene
            # Se set_like è uno allora con probabilità 1 / 4 mettero un like
            if set_like == "1":
                # Faccio in modo che con probabilità 1/4 metta like quindi non verra messo sempre, in modo
                # tale da aumentare il nuemro di richiueste di follow
                random_number = random.randint(1, 4)

                ''' Per far andare l'auto like devo solo scommentare questo

                # Solamente se random_number è 2 allora mando una richiesta di like, in questo modo sono sicuro che
                # ho la probabilità di 1/4 di mettere like. quindi non dovrebbe bloccarlo.
                if random_number == 2:
                    print("Processo l'utente: " + username + " mette like  alla foto di " + username_user_to_follow)
                    content_request = richiestaLike(username_user_to_follow, cookies_str, cookies_dict['csrftoken'])
                    parse_content_request(content_request, 'LIKE', username, tempo_blocco_se_esce_errore, delta_t,email)
                else:
                    print("Processo l'utente: " + username + " non mette il like, forse la prossima volta ?")
                
                '''
            # Metto un commento all'ultima foto con probabilità 1/4 in questo modo non verrà bloccato l'account
            if commenta == "1":
                # Faccio in modo che con probabilità 1/4 commenta quindi non verra messo sempre, in modo
                # tale da aumentare il nuemro di richiueste di follow
                random_number = random.randint(1, 4)
                if random_number == 2:
                    print("Processo l'utente: " + username + " commenta la foto di " + username_user_to_follow)
                    print(comment(cookies_str, cookies_dict['csrftoken'], username_user_to_follow))
                else:
                    print("Processo l'utente: " + username + " non commenta, forse la prossima volta ?")
            else:
                print(
                    "Processo l'utente: " + username + " NON commenta la foto di " + username_user_to_follow + " perchè non ha COMMENTA a 1")

            # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
            update_secondi_ultima_richiesta(username, int(time.time()))

            # Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_followed_string == "":
                users_followed_string = username_user_to_follow + ";"

            else:
                users_followed_string = users_followed_string + username_user_to_follow + ";"
            updateUserFollowed(users_followed_string, username)

        elif script_attivo == "1" and follow_unfollow == "0":
            print("Processo l'utente: " + username + " deve mandare richieste di unfollow")
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
                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str,cookies_dict['csrftoken'])
                print("UNFOLLOW " + username_user_to_unfollow + " " + str(
                    content_request))

                parse_content_request(content_request, 'FOLLOW-UNFOLLOW', username, tempo_blocco_se_esce_errore,
                                      delta_t,email)

                # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
                update_secondi_ultima_richiesta(username, int(time.time()))
                updateUserFollowed(users_followed_string, username)

            else:

                # Mando la richiesta di unfollow


                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str,
                                           cookies_dict['csrftoken'])
                print("Processo l'utente: " + username + " username_user_to_unfollow " + username_user_to_unfollow + " " + str(content_request.content))

                parse_content_request(content_request, "FOLLOW-UNFOLLOW", username, tempo_blocco_se_esce_errore,
                                      delta_t,email)

                # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
                update_secondi_ultima_richiesta(username, int(time.time()))
                updateUserFollowed(users_followed_string, username)







