#!/usr/bin/env python
# -*- coding: utf-8 -*-


import base64
import json
import time
import ast
from LogFile import printFile
from InstagramAPI import updateTempoBlocco
from InstagramAPI import comment
from InstagramAPI import update_secondi_ultima_richiesta
from InstagramAPI import updateFollowUnfollowDatabase
from InstagramAPI import updateUserFollowed
from InstagramAPI import ottengoURLImmagineProfilo
from InstagramAPI import saveIdIntoDatabase
from InstagramAPI import seveCookieIntoServer
from InstagramAPI import follow
from InstagramAPI import login
from InstagramAPI import updateURLImmagineProfilo
from InstagramAPI import unfollow
from InstagramAPI import updatePasswordErrataAndProcessing
from InstagramAPI import getRandomUserToFollow
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase
from InstagramAPI import getIDFromUsername
from InstagramAPI import getCountUsersToFollow
from InstagramAPI import richiestaLike
from InstagramAPI import updateDeltaT
from InstagramAPI import updateNumberRequestsDone
from InstagramAPI import updateProcessing
from random import randint
import re

#max_requests indica dopo quante richieste cambio da follow a unfollow,
#dopo 300 richieste di follow ne faccio 300 di unfollo e cosi via
max_requests = 300

#numero di richieste dopo il quale si decrementa il DT
number_requests_update_delta_t = 1000


tempo_blocco_se_esce_errore = 10000



while True:

    print("Attendo DT")
    printFile("Attendo DT")

    #time.sleep(20)
    print("Tempo DT passato, inizio lo script.")
    printFile("Tempo DT passato, inizio lo script.")

    #Chiedo quanti utenti ho nel database
    numberUsersIntoDatabase = countUserIntoDatabase()
    print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")
    printFile("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")


    #Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)): #Deve partire da 0

        #Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

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
        url_immagine_profilo = str(user[0]['URL_IMMAGINE_PROFILO'])

        # questa variabile indica le richieste fatte fino ad ora,
        # in particolare dopo 100 richieste diminuisco di 1 secondo DT relativo
        # all'utente, mentre appena esce scritto che devo aspettare qualche minuto per fare altre richieste
        # aumento DT di 1 secondo e attendo 10 minuti prima di fare una nuova richiesta
        number_requests_done = str(user[0]['NUMBER_REQUESTS_DONE'])


        #Processing va settato a 0 se ho fatto un login corretto
        processing = str(user[0]['PROCESSING'])


        #PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])


        print("Processo l'utente: " + username)
        printFile("Processo l'utente: " + username)

        #inserisco per primo l'url della immagine profilo della persona
        if url_immagine_profilo == "":
            print("Inserisco l'url dell'immagine profilo dell'utente: " + username)
            printFile("Inserisco l'url dell'immagine profilo dell'utente: " + username)
            url = ottengoURLImmagineProfilo(username)
            updateURLImmagineProfilo(username,url)
            continue

        #Se script_attivo e' 0 allora non devo fare nulla per quel user e passo allo user successivo
        if script_attivo == "0":
            print("L'utente: " + username + " ha script_attivo = 0 quindi non lo devo processare")
            printFile("L'utente: " + username + " ha script_attivo = 0 quindi non lo devo processare")
            continue

        #Controllo che secondi_ultima_richiesta + delta_t sia maggiore di ora, se lo e' allora devo processare
        #altrimenti non devo processare
        tempo_ora = int(time.time())


        #Controllo che deve fermarsi se ho un tempo di blocco attivo, in particolare se ho tempo_attesa_blocco > 0 devo continuare  senza processarlo
        if int(tempo_attesa_blocco) > 0:
            tempo_attesa_blocco = int(tempo_attesa_blocco) - 1
            updateTempoBlocco(username,str(tempo_attesa_blocco))
            print("Username " + username + " ancora in blocco per un totale di cicli: " + str(tempo_attesa_blocco))
            continue

        if int(secondi_ultima_richiesta) + int(delta_t) > tempo_ora:
            print("L'utente " + username + " NON deve mandare richieste perche non e' ancora passato il suo DT")
            continue



        #Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
        #facendo il login
        if len(cookie) == 0:
            r = login(username, password_instagram)
            cookies_dict = r.cookies.get_dict()

            #Salvo la variabile cookies_dict sul server
            seveCookieIntoServer(username,cookies_dict)
        else:
            cookies_dict = ast.literal_eval(base64.b64decode(str(cookie)))

        #Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
        cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

        if len(id) == 0:

            print("Processo l'utente: " + username + " non ha l'id settato, lo chiedo a Instagram e lo salvo sul mio database")
            printFile("Processo l'utente: " + username + " non ha l'id settato, lo chiedo a Instagram e lo salvo sul mio database")

            id = getIDFromUsername(username)
            saveIdIntoDatabase(username, id)

        #Imposto a 1 perche non va con 0 comunque ogni volta riempie il campo user_followed e lo svuota
        if len(users_followed_array) == 1:
            #Devo iniziare a seguire

            print("Processo l'utente: " + username + " non segue ancora nessuno, deve iniziare a seguire gente")
            printFile("Processo l'utente: " + username + " non segue ancora nessuno, deve iniziare a seguire gente")


            follow_unfollow = str('1')
            updateFollowUnfollowDatabase(username, str(follow_unfollow))

        #controllo che sono al massimo di persone che posso seguire al giorno
        if len(users_followed_array) > max_requests: #max_requests:

            print("Processo l'utente: " + username + " segue gia il numero massimo di user giornalieri, ora bisogna iniziare a fare unfollow")
            printFile("Processo l'utente: " + username + " segue gia il numero massimo di user giornalieri, ora bisogna iniziare a fare unfollow")

            #Se sono al numero di persone massime imposto users_followed a 0
            # In questo modo inizio a fare richieste di unfollow
            follow_unfollow = str("0")

            #Aggiorno il server dicendo che follow_unfollow e' zero
            updateFollowUnfollowDatabase(username, follow_unfollow)


        #In questo punto aumento la variabile:  number_requests_done di 1:
        number_requests_done = int(number_requests_done) + 1

        #Mando al server il nuovo valore di number_requests_done
        updateNumberRequestsDone(username,str(number_requests_done))

        #numero di richieste che si devono fare prima di diminuire il DT: 1000 per ogni utente
        if int(number_requests_done) > number_requests_update_delta_t:
            #Entro qui dentro dopo 100 richieste per ogni utente fatte
            #In questo modo diminuisco DT per quell'utente perche ne ho gia fatte 100
            delta_t = int(delta_t) - 1
            updateDeltaT(username,str(delta_t))
            print("Aggiorno Delta T per l'utente " + username + " perche e arrivato a "+str(number_requests_update_delta_t)+" richieste mandate")

            #aggiorno a 0 il numero di richieste mandate perche ho gia diminuito delta t
            updateNumberRequestsDone(username, str(0))


        #Se follow_unfollow e' 1 allora devo seguire una persona a caso tra tutte quelle  nel database
        if follow_unfollow == "1":

            print("Processo l'utente: " + username + " deve mandare richieste di follow")
            printFile("Processo l'utente: " + username + " deve mandare richieste di follow")

            #Ottengo il numero totale di persone che sono nella tabella degli utenti da seguire
            count_user_to_follow = getCountUsersToFollow()

            #Seleziono 1 utente tra 0 e count_user_to_follow da seguire
            random_number_user_to_follow = str(randint(1, int(count_user_to_follow)))
            user_to_follow = str(getRandomUserToFollow(random_number_user_to_follow))
            username_user_to_follow = user_to_follow[user_to_follow.find("u'USERNAME': u'") + len("u'USERNAME': u'"): user_to_follow.find("', u'ID':")]
            id_user_to_follow = user_to_follow[user_to_follow.find("', u'ID': u'") + len("', u'ID': u'"): user_to_follow.find("'}")]

            #Seguo la persona che ho scaricato e gli metto un like alla prima foto
            content_follow = follow(id_user_to_follow,username_user_to_follow,cookies_str,cookies_dict['csrftoken'])

            printFile(content_follow)
            print("Richiesta di FOLLOW mandata a: username_user_to_follow " + content_follow)

            content_follow_JSON = json.loads(content_follow)


            if content_follow.__contains__("Please wait a few minutes before you try again"):
                updateTempoBlocco(username,tempo_blocco_se_esce_errore)
                # aumentoDelta t di 10 secondi
                delta_t = int(delta_t) + 10
                updateDeltaT(username, str(delta_t))
                continue

            elif processing == "1":
                if 'message' in  content_follow_JSON:
                    #Caso in cui ho sbagliato la password
                    print("Errore, password dello username " + username + " ERRATA ")
                    #mando sul server il valore di PASSWORD ERRATA a 1 cosi dall'app me ne posso accordere e rimettere la password
                    updatePasswordErrataAndProcessing(username,1)
                    continue
                else:
                    #Caso in cui va tutto bene: Se ho PROCESSING a 1 devo metterlo a 0
                    updateProcessing(username,0)


            #Tale richiesta va a buon fine solo se il profilo non e' privato. Nel caso sia privato non funziona la richiesta di like
            #se il profilo e' publico funziona bene
            print(richiestaLike(username_user_to_follow,cookies_str,cookies_dict['csrftoken']))

            #Metto un commento all'ultima foto
            print("Commento")
            print(comment(cookies_str, cookies_dict['csrftoken'], username_user_to_follow))


            #Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
            update_secondi_ultima_richiesta(username, int(time.time()))

            #Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_followed_string == "":
                users_followed_string =  username_user_to_follow + ";"

            else:
                users_followed_string = users_followed_string +username_user_to_follow + ";"
            updateUserFollowed(users_followed_string,username)

        else:
            print("Processo l'utente: " + username + " deve mandare richieste di unfollow")
            printFile("Processo l'utente: " + username + " deve mandare richieste di unfollow")

            #Faccio in modo che la stringa contenente tutti gli user che seguo che e' sul mio database sia
            #ben fatta, in particolare che non ci siano situazioni in cui ho user;user;user;
            #in questo caso andrebbe tolto l'ultimo ;
            users_followed_array_temp = users_followed_array
            for i in users_followed_array_temp:
                if i == "":
                    users_followed_array.remove(i)

            #elimino il primo user che ho seguito
            username_user_to_unfollow = users_followed_array.pop(0)

            #Costruisco nuovamente la stringa da mandare al mio server
            for i in range(0,len(users_followed_array)):
                if i == 0:
                    users_followed_string = users_followed_array[i] + ";"
                elif i == len(users_followed_array)-1:
                    users_followed_string = users_followed_string + users_followed_array[i]
                else:
                    users_followed_string = users_followed_string + users_followed_array[i] + ";"

            if len(users_followed_array) == 0:
                users_followed_string = ""
                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_unfollow = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str, cookies_dict['csrftoken'])
                printFile(content_unfollow)
                print(content_unfollow)


                if content_unfollow.__contains__("Please wait a few minutes before you try again"):

                    #Aggiorno ad attesa 10 minuti per l'utente a cui e' arrivato il blocco e aumento DT di 10 secondi
                    updateTempoBlocco(username, tempo_blocco_se_esce_errore)

                    #aumentoDelta t di 10 secondi
                    delta_t = int(delta_t) + 10
                    updateDeltaT(username,str(delta_t))


                # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
                update_secondi_ultima_richiesta(username, int(time.time()))
                updateUserFollowed(users_followed_string, username)
            else:

                #Mando la richiesta di unfollow
                print("Processo l'utente: " + username + " username_user_to_unfollow " + username_user_to_unfollow)
                printFile("Processo l'utente: " + username + " username_user_to_unfollow " + username_user_to_unfollow)

                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                content_unfollow = unfollow(id_to_unfollow,username_user_to_unfollow,cookies_str,cookies_dict['csrftoken'])

                printFile(content_unfollow)
                print(content_unfollow)


                if content_unfollow.__contains__("Please wait a few minutes before you try again"):
                    # Aggiorno ad attesa 10 minuti per l'utente a cui e' arrivato il blocco e aumento DT di 10 secondi
                    updateTempoBlocco(username, tempo_blocco_se_esce_errore)

                    # aumentoDelta t di 10 secondi
                    delta_t = int(delta_t) + 10
                    updateDeltaT(username, str(delta_t))

                # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
                update_secondi_ultima_richiesta(username, int(time.time()))

                updateUserFollowed(users_followed_string,username)







