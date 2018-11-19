#Questo script viene attivato tot di tempo e permette di ottenere tutte le persone che hanno auto_like = 1 nel database
# e prende tutte le persone che hanno GET_LIKE = 1 sempre dal database.
# In questo modo ho due array uno di utente che mettono LIKE e uno di utenti che devono ricevere LIKE
# In questo modo lo script controlla se nell'ultimo giorno gli utenti con GET_LIKE hanno pubblicato una foto, se cosi e'
# allora tutti quelli nell'array di auto_like gli mettono il like


import ast
import base64
import json
import re
import time

import requests

from InstagramAPI import countUserIntoDatabaseFromTread, getIdPhotoNotLiked, countPhotoIntoDatabase, \
    selectPhotoFromDatabase, salvoSulDatabaseIdImmagineEUsernameDegliUtentiCheVoglionoLike, parse_content_request, \
    updateGetLikeFromUsername, updateSetLikeFromUsername
from InstagramAPI import selectUserFromDatabaseAndThread
from InstagramAPI import checkIfYetFollowing
from InstagramAPI import ottengoIdPrimaFotoDaUsername
from InstagramAPI import updateUsersLiked

# Chiedo quanti utenti ho nel database
from InstagramAPI import selectUserFromDatabase

from InstagramAPI import countUserIntoDatabase

from InstagramAPI import richiestaLike

#Ogni foto attraverso il nostro bot va a ricereve al massimo 20 like
max_like = 20



numberUsersIntoDatabase = countUserIntoDatabase()
print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

#In questo array metto tutti i profili che devono mettere like
array_user_auto_like = []

#In questo array metto tutti i profili che devono rivedere like
array_user_get_like = []


#QUesto for serve semplicemente per far si che un utente che ha script_attivo=1 allora puo solo ricevere like,
#Mentre quelli che hanno script_attivo=0 mettono like
for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)
    username = str(user[0]['USERNAME'])
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])

    auto_like = str(user[0]['AUTO_LIKE'])
    get_like = str(user[0]['GET_LIKE'])


    # Valori di auto_like=1 solo se l'utente ha la possibilita' di mettere like
    # Valori di get_like=1 solo se l'utente ha la possibilita' di mettere like
    #Quindi se ho script_attivo = 0 devo mettere auto_like=1 e get_like=0
    if script_attivo == "1" and auto_like == "1" :
        updateGetLikeFromUsername(username,0)
        updateSetLikeFromUsername(username,1)
    elif script_attivo == "1" and get_like == "1":
        updateGetLikeFromUsername(username, 1)
        updateSetLikeFromUsername(username, 0)


#QUesto For fa si che posso creare 2 array, uno che mette like e uno che li riceve
for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)
    id = str(user[0]['ID'])
    username = str(user[0]['USERNAME'])
    cookie = str(user[0]['COOKIES'])
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])
    password_errata = str(user[0]['PASSWORD_ERRATA'])


    tempo_attesa_blocco = str(user[0]['TEMPO_ATTESA_BLOCCO'])

    #Se questa variabile e' 1 allora quel username mette like questo username
    auto_like = str(user[0]['AUTO_LIKE'])

    #Se questa variabile contiene il valore di 1 allora quell'username vuole ricevere like se ha publicato delle foto
    get_like = str(user[0]['GET_LIKE'])


    #Controllo per primo se lo username ha i cookie settati, se non li ha settati non viene processato
    #Altra cosa, se ha la password errata non viene neanche inserito
    if len(cookie) == 0 or password_errata	=="1":
        continue

    user_dictionary = {
        "ID":id,
        "USERNAME": username,
        "COOKIES": cookie,
        "AUTO_LIKE": auto_like,
        "GET_LIKE": get_like
    }

    #Vado a mettere like solo se il profilo non va nel bot, altrimenti non mette like un profilo di cui sta andando il bot.
    if get_like == "1" and script_attivo == "1":
        array_user_get_like.append(user_dictionary)
    if auto_like == "1" and script_attivo == "0":
        array_user_auto_like.append(user_dictionary)


#In questo array ho tutte le foto e tutte le persone che hanno messo like.
numberPhotoIntoDatabase = int(countPhotoIntoDatabase())
print(numberPhotoIntoDatabase)

#In questo array inserisco tutte le foto e le persone che hanno messo like ma solo le foto che hanno un numero di like < max_like
array_photo_to_auto_like = []


#ciclo sul numero delle foto e inserisco nell'array array_photo_to_auto_like la foto che deve ottenere i like
for index in range(0, int(numberPhotoIntoDatabase)):
    # Seleziono la tupla relativa all'utente
    photo = selectPhotoFromDatabase(index)

    id_photo = str(photo[0]['ID_IMMAGINE'])
    users_liked_string = str(photo[0]['USERS_LIKED'])
    users_liked_array = re.split(';', users_liked_string)
    username_immagine = str(photo[0]['USERNAME_IMMAGINE'])

    photo_dictionary = {
        "ID_IMMAGINE": id_photo,
        "USERS_LIKED_STRING": users_liked_string,
        "USERNAME_IMMAGINE": username_immagine,
    }


    print("Processo la foto con id: " + id_photo + " dell'utente:"+username_immagine+" e ha come persone che hanno messo like: " + users_liked_string)

    #se il numero di persone che hanno messo like e' < max_like allora la inserisco in un array
    if len(users_liked_array) < max_like:
        array_photo_to_auto_like.append(photo_dictionary) # array contenente tutte le foto che hanno len(users_liked_array) < max_like
        print("La foto con id: " + id_photo + " non ha raggiunto " + str(max_like) + " like" )



#Per ogni foto vado a far si che gli utenti gli mettano like
for photo in array_photo_to_auto_like:

    #Per ogni imagine vado a prendere l'identificativo, l'array delle persone che hanno messo like e lo username
    #dell'utente che ha postato tale immagine
    id_photo = photo.get("ID_IMMAGINE")
    users_liked_string = photo.get("USERS_LIKED_STRING")
    users_liked_array = re.split(';', users_liked_string)
    username_get_immagine = photo.get("USERNAME_IMMAGINE")

   #In questo ciclo controllo se user_auto_like ossia l'utente che mette il like ha gi messo, attraverso il bot
    # il like, in tal caso non lo messo piu
    for user_auto_like in array_user_auto_like:

        username_auto_like = user_auto_like.get("USERNAME")
        print(username_auto_like)

        cookie_user_auto_like = user_auto_like.get("COOKIES")
        #se lo username ha gia messo like non lo deve piu mettere e passo al prossimo

        if users_liked_array.__contains__(username_auto_like):
            print("L'utente: " + username_auto_like + " ha gia messo like alla foto con id " +id_photo + " dell'utente:"+ username_get_immagine)
        else:
            print("L'utente: " + username_auto_like + " deve mettere like alla foto con id " +id_photo + " dell'utente:"+ username_get_immagine)

            temp = base64.b64decode(str(cookie_user_auto_like))
            cookies_dict = ast.literal_eval(temp)
            # Sia se ho ottenuto i cookie da instagram o dal mio server setto bene la variabile cookies_str
            cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)

            content_request = richiestaLike(username_get_immagine, cookies_str, cookies_dict['csrftoken'])
            print(content_request.content)

            if not str(content_request.content).__contains__("status\": \"ok"):
                print("Passo ad un altro account")
                array_user_auto_like.remove(user_auto_like)
                continue





            # Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_liked_string == "":
                users_liked_string = username_auto_like + ";"

            else:
                users_liked_string = users_liked_string + username_auto_like + ";"
            updateUsersLiked(users_liked_string, id_photo)

            time.sleep(5)

            break
