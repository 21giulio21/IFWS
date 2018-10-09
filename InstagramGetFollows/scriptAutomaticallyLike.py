#Questo script viene attivato tot di tempo e permette di ottenere tutte le persone che hanno SET_LIKE = 1 nel database
# e prende tutte le persone che hanno GET_LIKE = 1 sempre dal database.
# In questo modo ho due array uno di utente che mettono LIKE e uno di utenti che devono ricevere LIKE
# In questo modo lo script controlla se nell'ultimo giorno gli utenti con GET_LIKE hanno pubblicato una foto, se cosi e'
# allora tutti quelli nell'array di SET_LIKE gli mettono il like


import ast
import base64
import json
import time

import requests

from InstagramAPI import countUserIntoDatabaseFromTread
from InstagramAPI import selectUserFromDatabaseAndThread
from InstagramAPI import checkIfYetFollowing
from InstagramAPI import ottengoIdPrimaFotoDaUsername

# Chiedo quanti utenti ho nel database
from InstagramAPI import selectUserFromDatabase

from InstagramAPI import countUserIntoDatabase

from InstagramAPI import richiestaLike

numberUsersIntoDatabase = countUserIntoDatabase()
print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

#In questo array metto tutti i profili che devono mettere like
array_user_set_like = []

#In questo array metto tutti i profili che devono rivedere like
array_user_get_like = []



# Ora ciclo sul totale di persone che ho nel database
for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)

    id = str(user[0]['ID'])
    username = str(user[0]['USERNAME'])
    cookie = str(user[0]['COOKIES'])
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])
    tempo_attesa_blocco = str(user[0]['TEMPO_ATTESA_BLOCCO'])

    #Se questa variabile e' 1 allora quel username mette like questo username
    set_like = str(user[0]['SET_LIKE'])

    #Se questa variabile contiene il valore di 1 allora quell'username vuole ricevere like se ha publicato delle foto
    get_like = str(user[0]['GET_LIKE'])

    #Controllo per primo se lo username ha i cookie settati, se non li ha settati non viene processato
    if len(cookie) == 0:
        continue


    user_dictionary = {
        "ID":id,
        "USERNAME": username,
        "COOKIES": cookie,
        "USERNAME": username,
        "SET_LIKE": set_like,
        "GET_LIKE": get_like
    }

    if get_like == "1":
        array_user_get_like.append(user_dictionary)
    if set_like == "1":
        array_user_set_like.append(user_dictionary)

# Ora che tutti gli array sono stati settati allora inizio ad iterare sull'array di persone che vogliono i like
# e controllo se ha messo un post negli ultime ore
for user_set_like in array_user_set_like:

    username_user_set_like = str(user_set_like["USERNAME"])
    cookie_user_set_like = user_set_like["COOKIES"]

    temp = base64.b64decode(str(cookie_user_set_like))
    cookies_dict = ast.literal_eval(temp)
    # Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
    cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

    print(username_user_set_like + " Mette LIKE " )



    #Per ogni utente che vuole like processo quelli che vogliono mettere like e gli gaccio metterre il like
    for user_get_like in array_user_get_like:

        username_user_get_like = str(user_get_like["USERNAME"])

        #Se la persona che vuole like e' a stessa a mettere like non lo mette.
        if username_user_set_like == username_user_get_like:
            continue




        time.sleep(300)

        print(username_user_set_like + " METTE LIKE ALL' UTENTE " + username_user_get_like)
        idPrimaFoto = ottengoIdPrimaFotoDaUsername(username_user_get_like, cookies_str, cookies_dict['csrftoken'])
        content_request = richiestaLike(username_user_get_like, cookies_str, cookies_dict['csrftoken'])

        print("Processo le risposte, idPrimaFoto="+str(idPrimaFoto) + " richiesta_like="+str(content_request.content))