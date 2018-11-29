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
    updateGetLikeFromUsername, updateSetLikeFromUsername, updateTempoBlocco
from InstagramAPI import selectUserFromDatabaseAndThread
from InstagramAPI import checkIfYetFollowing
from InstagramAPI import ottengoIdPrimaFotoDaUsername
from InstagramAPI import updateUsersLiked

# Chiedo quanti utenti ho nel database
from InstagramAPI import selectUserFromDatabase

from InstagramAPI import countUserIntoDatabase

from InstagramAPI import richiestaLike

#Ogni foto attraverso il nostro bot va a ricereve al massimo 20 like



numberUsersIntoDatabase = countUserIntoDatabase()
print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

#In questo array metto tutti i profili che devono mettere like
array_user_auto_like = []

#In questo array metto tutti i profili che devono rivedere like
array_user_get_like = []



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


    #Controllo per primo se lo username ha i cookie settati, se non li ha settati non viene processato
    #Altra cosa, se ha la password errata non viene neanche inserito
    if len(cookie) == 0 or password_errata	=="1":
        continue

    user_dictionary = {
        "ID":id,
        "USERNAME": username,
        "COOKIES": cookie,
        "AUTO_LIKE": auto_like
    }

    #Riempio l'array con tutte le persone che dovranno ricevere like
    if auto_like == "1" and script_attivo == "1":
        array_user_auto_like.append(user_dictionary)

print("Totale utenti che dovranno ricevere like: " + str(len(array_user_auto_like)))


#Per ogni username salvo l'id della relativa immagine su cui gli utenti metteranno like
salvoSulDatabaseIdImmagineEUsernameDegliUtentiCheVoglionoLike(array_user_auto_like)
