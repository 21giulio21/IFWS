import base64
import time
import ast
from LogFile import printFile
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
from random import randint

import re



delta_t = 100 #Perche ci sono 86400 secondi in un giorno e devo mandare massimo 300 richieste di follow o di unfollow al giorno
max_requests = 300

while True:

    print("Attendo DT")
    printFile("Attendo DT")

    #time.sleep(delta_t)
    print("Tempo DT passato, inizio lo script.")
    printFile("Tempo DT passato, inizio lo script.")

    #Chiedo quanti utenti ho nel database
    count = countUserIntoDatabase()
    print("Ho un totale di " + str(count) + " utenti che devo gestire per mandare le richieste")
    printFile("Ho un totale di " + str(count) + " utenti che devo gestire per mandare le richieste")


    #Ora ciclo sul totale di persone che ho nel database
    for index in range(0,int(count)): #Deve partire da 0

        time.sleep(10) #Tempo da attendere per ogni utente che viene provessato

        #Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

        #Prendo id della persona, se nullo lo chiedo a instagram
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


        print("Processo l'utente: " + username)
        printFile("Processo l'utente: " + username)

        #Se script_attivo e' 0 allora non devo fare nulla per quel user e passo allo user successivo
        if script_attivo == "0":
            print("L'utente: " + username + " ha script_attivo = 0 quindi non lo devo processare")
            printFile("L'utente: " + username + " ha script_attivo = 0 quindi non lo devo processare")
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


        #Se follow_unfollow e' 1 allora devo seguire una persona a caso tra tutte quelle  nel database
        if follow_unfollow == "1":

            print("Processo l'utente: " + username + " deve mandare richieste di follow")
            printFile("Processo l'utente: " + username + " deve mandare richieste di follow")

            #Ottengo il numero totale di persone che sono nella tabella degli utenti da seguire
            count_user_to_follow = getCountUsersToFollow()

            #Seleziono 1 utente tra 0 e count_user_to_follow da seguire
            random_number_user_to_follow = str(randint(1, int(count_user_to_follow)))
            user_to_follow = str(getUserToFollwFromTarget(random_number_user_to_follow))
            username_user_to_follow = user_to_follow[user_to_follow.find("u'USERNAME': u'") + len("u'USERNAME': u'"): user_to_follow.find("', u'ID':")]
            id_user_to_follow = user_to_follow[user_to_follow.find("', u'ID': u'") + len("', u'ID': u'"): user_to_follow.find("'}")]

            #Seguo la persona che ho scaricato e gli metto un like alla prima foto
            content_follow = follow(id_user_to_follow,username_user_to_follow,cookies_str,cookies_dict['csrftoken'])
            printFile(content_follow)
            print(content_follow)

            #Tale richiesta va a buon fine solo se il profilo non e' privato. Nel caso sia privato non funziona la richiesta di like
            #se il profilo e' publico funziona bene
            richiestaLike(username_user_to_follow,cookies_str,cookies_dict['csrftoken'])

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
                printFile(unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str, cookies_dict['csrftoken']))
                updateUserFollowed(users_followed_string, username)
            else:

                #Mando la richiesta di unfollow
                print("Processo l'utente: " + username + " username_user_to_unfollow " + username_user_to_unfollow)
                printFile("Processo l'utente: " + username + " username_user_to_unfollow " + username_user_to_unfollow)

                id_to_unfollow = getIDFromUsername(username_user_to_unfollow)
                unfollow(id_to_unfollow,username_user_to_unfollow,cookies_str,cookies_dict['csrftoken'])
                updateUserFollowed(users_followed_string,username)








