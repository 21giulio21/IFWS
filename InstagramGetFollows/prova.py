#QUesto file permette di fare una scansione giorno dei profili che utilizzano il bot.
#Per ogni profilo viene salvato: username, followers, followees e media.
import time

import requests
from requests import request

from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase

numberUsersIntoDatabase = countUserIntoDatabase()
print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti")

#Array di utenti che hanno script attivo, solo su questo array si fanno le statistiche
array_utenti_con_script_attivo = []

# Ora ciclo sul totale di persone che ho nel database
for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)

    username = str(user[0]['USERNAME'])
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])


    if script_attivo == "1":
        array_utenti_con_script_attivo.append(username)

print("Ho un totale di: " +  str(len(array_utenti_con_script_attivo)) + " utenti per cui fare le statistiche ")

#Per ogni utente di cui devo fare le statistiche devo chiedere i media,followees,followers
for utente in array_utenti_con_script_attivo:

    url_media = "https://www.elenarosina.com/instatrack/getPostsFromUser.php?username="
    url_followers = "https://www.elenarosina.com/instatrack/getFollowersFromUser.php?username="
    url_followees = "https://www.elenarosina.com/instatrack/getFolloweeFromUser.php?username="


    media       =   str(requests.get(url_media      + utente,verify=False).content)
    followers   =   str(requests.get(url_followers  + utente,verify=False).content)
    followees   =   str(requests.get(url_followees  + utente,verify=False).content)

    media = media.replace("'","")
    media = media.replace("b", "")

    followers = followers.replace("'", "")
    followers = followers.replace("b", "")

    followees = followees.replace("'", "")
    followees = followees.replace("b", "")

    time.sleep(1)

    print("Username: " + utente + " Followers: "+followers + " Follwees: " +followees)


    #Chiedo

