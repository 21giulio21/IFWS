#Questo script2 a differenza di script ha la possibilita di gestire il DT per ogni utente. In particolare ogni utente manda una richiesta
# in tempi diversi rispetto agli altri

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
from InstagramAPI import getRandomUserToFollow
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase
from InstagramAPI import getIDFromUsername
from InstagramAPI import getCountUsersToFollow
from InstagramAPI import richiestaLike
from random import randint

import re





delta_t = 30 #Perche ci sono 86400 secondi in un giorno e devo mandare massimo 300 richieste di follow o di unfollow al giorno
delta_attesa = 180
counter_before_error = 0

while True:

    print("Attendo DT")
    time.sleep(delta_t)
    print("DT passato")

    #Chiedo quanti utenti ho nel database
    count = countUserIntoDatabase()
    print("Ho un totale di " + str(count) + " utenti che devo gestire per mandare le richieste")
    printFile("Ho un totale di " + str(count) + " utenti che devo gestire per mandare le richieste")


    #Ora ciclo sul totale di persone che ho nel database
    for index in range(0,int(count)): #Deve partire da 0

        #Seleziono la tupla relativa all'utente
        user = str(selectUserFromDatabase(index))

        #Prendo id della persona, se nullo lo chiedo a instagram
        id = str(user[user.find(", u'ID': u'")+len(", u'ID': u'"):user.find("', u'FOLLOW_UNFOLLOW'")])
        username = str(user[user.find("u'USERNAME': u'")+len("u'USERNAME': u'"):user.find("', u'COOKIES'")])
        cookie = user[user.find("u'COOKIES': u'")+len("u'COOKIES': u'"):user.find("', u'PASSWORD_INSTAGRAM'")]
        password_instagram = user[user.find("u'PASSWORD_INSTAGRAM': u'") + len("u'PASSWORD_INSTAGRAM': u'"):user.find("', u'USERS_FOLLOWED'")]


        print("Processo l'utente: " + username)
        if not username.__contains__("ginotani82324"):
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


        #Ottengo il numero totale di persone che sono nella tabella degli utenti da seguire
        count_user_to_follow = getCountUsersToFollow()

        #Seleziono 1 utente tra 0 e count_user_to_follow da seguire
        random_number_user_to_follow = str(randint(1, int(count_user_to_follow)))
        user_to_follow = str(getRandomUserToFollow(random_number_user_to_follow))
        username_user_to_follow = user_to_follow[user_to_follow.find("u'USERNAME': u'") + len("u'USERNAME': u'"): user_to_follow.find("', u'ID':")]
        id_user_to_follow = user_to_follow[user_to_follow.find("', u'ID': u'") + len("', u'ID': u'"): user_to_follow.find("'}")]

        #Seguo la persona che ho scaricato e gli metto un like alla prima foto
        risposta = str(follow(id_user_to_follow,username_user_to_follow,cookies_str,cookies_dict['csrftoken']))
        print(risposta)
        counter_before_error += 1




        if risposta.__contains__("Please wait a few minutes before you try again"):
            time.sleep(delta_attesa)
            delta_t = delta_t + 1
            with open("loginstagram.txt", "a") as myfile:
                myfile.write("SOno passate " + str(counter_before_error)+" richieste prima dell'errore DT e' " + str(delta_t) + "\n")
                counter_before_error = 0

