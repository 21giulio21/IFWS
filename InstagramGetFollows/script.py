import base64
import time
import ast
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
from random import randint
import re





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
        users_followed_array = re.split(';', user[user.find("u'USERS_FOLLOWED': u'")+len("u'USERS_FOLLOWED': u'"):user.find("', u'SCRIPT_ACTIVE'")])
        users_followed_string =  user[user.find("u'USERS_FOLLOWED': u'")+len("u'USERS_FOLLOWED': u'"):user.find("', u'SCRIPT_ACTIVE'")]

        #Controllo che siano settati i cookie dell'utente altrimenti li chiedo a instagram
        #facendo il login
        if len(cookie) == 0:
            username = "ginotani82324"
            password = "21giulio21"
            r = login(username, password)
            cookies_dict = r.cookies.get_dict()

            #Salvo la variabile cookies_dict sul server
            seveCookieIntoServer(username,cookies_dict)
        else:
            cookies_dict = ast.literal_eval(base64.b64decode(str(cookie)))

        #Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
        cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

        if len(id) == 0:
            id = getIDFromUsername(username)
            saveIdIntoDatabase(username, id)


        #controllo che sono al massimo di persone che posso seguire al giorno
        if len(users_followed_array) > 0: #max_requests:

            #Se sono al numero di persone massime imposto users_followed a 0
            # In questo modo inizio a fare richieste di unfollow
            follow_unfollow = 0

        #Se follow_unfollow e' 1 allora devo seguire una persona a caso tra tutte quelle  nel database
        if follow_unfollow == "1":

            #Ottengo il numero totale di persone che sono nella tabella degli utenti da seguire
            count_user_to_follow = getCountUsersToFollow()

            #Seleziono 1 utente tra 0 e count_user_to_follow da seguire
            random_number_user_to_follow = str(randint(1, int(count_user_to_follow)))
            user_to_follow = str(getRandomUserToFollow(random_number_user_to_follow))
            username_user_to_follow = user_to_follow[user_to_follow.find("u'USERNAME': u'") + len("u'USERNAME': u'"): user_to_follow.find("', u'ID':")]
            id_user_to_follow = user_to_follow[user_to_follow.find("', u'ID': u'") + len("', u'ID': u'"): user_to_follow.find("'}")]

            #Seguo la persona che ho scaricato
            follow(id_user_to_follow,username_user_to_follow,cookies_str,cookies_dict['csrftoken'])

            #Devo aggiundere l'utente alla stringa totale delle persone seguite
            users_followed_string = users_followed_string + ";" + username_user_to_follow
            updateUserFollowed(users_followed_string,username)

        else:


#TODO DA FARE!!
            # Devo fare richieste di UNFOLLOW
            username_to_unfollow = users_followed_array[0]
            id_to_unfollow = getIDFromUsername(username_to_unfollow)
            unfollow(id_to_unfollow,username_to_unfollow,cookies_str,cookies_dict['csrftoken'])
            users_followed_array.remove(users_followed_array[0])
            users_followed_string = ''.join(item for item in users_followed_array)
            updateUserFollowed(users_followed_string,username)






