import time
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase
from InstagramAPI import getIDFromUsername
from InstagramAPI import getCountUsersToFollow
from random import randint





delta_t = 290 #Perche ci sono 86400 secondi in un giorno e devo mandare massimo 300 richieste di follow o di unfollow al giorno
max_requests = 300

while True:
    #time.sllep(delta_t)
    print("Tempo DT passato, inizio lo script.")

    #Chiedo quanti utenti ho nel database
    count = countUserIntoDatabase()
    print("Ho un totale di " + str(count) + " utenti")

    #Ora ciclo sul totale di persone che ho nel database
    for index in range(0,int(count)): #Deve partire da 0

        #Seleziono la tupla relativa all'utente
        user = str(selectUserFromDatabase(index))

        #Prendo id della persona, se nullo lo chiedo a instagram
        id = str(user[user.find(", u'ID': u'")+len(", u'ID': u'"):user.find("', u'FOLLOW_UNFOLLOW'")])
        username = str(user[user.find("u'USERNAME': u'")+len("u'USERNAME': u'"):user.find("', u'COOKIES'")])
        cookie = user[user.find("u'COOKIES': u'")+len("u'COOKIES': u'"):user.find("', u'PASSWORD_INSTAGRAM'")]
        follow_unfollow = user[user.find("u'FOLLOW_UNFOLLOW': u'")+len("u'FOLLOW_UNFOLLOW': u'"):user.find("'}]")]
        users_followed = user[user.find("u'USERS_FOLLOWED': u'")+len("u'USERS_FOLLOWED': u'"):user.find("', u'SCRIPT_ACTIVE'")]
        print(users_followed)


        #Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
        #facendo il login
        if len(cookie) == 0:
            print("cookie dell utente nullo")
            #TODO: cookie = ...

        if len(id) == 0:
            print("ID dell utente nullo")
            id = getIDFromUsername(username)

        #Se follow_unfollow e' 1 allora devo seguire una persona a caso tra tutte quelle  nel database
        if follow_unfollow == "1":

            #Ottengo il numero totale di persone che sono nella tabella degli utenti da seguire
            count_user_to_follow = getCountUsersToFollow()

            #Seleziono 1 utente tra 0 e count_user_to_follow da seguire
            random_user_to_follow = str(randint(1, int(count_user_to_follow)))

            print(random_user_to_follow)






        #Se il campo ID e' nullo allora chiedo l'id dell'utente a instagram
