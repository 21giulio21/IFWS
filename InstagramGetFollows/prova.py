#QUesto file permette di fare una scansione giorno dei profili che utilizzano il bot.
#Per ogni profilo viene salvato: username, followers, followees e media.
import time

import requests

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
    target = str(user[0]['TARGET'])

    if script_attivo == "1":
        user_dictionary = {
            "USERNAME": username,
            "TARGET": target
        }
        array_utenti_con_script_attivo.append(user_dictionary)

print("Ho un totale di: " +  str(len(array_utenti_con_script_attivo)) + " utenti per cui fare le statistiche ")

#Per ogni utente di cui devo fare le statistiche devo chiedere i media,followees,followers
for utente in array_utenti_con_script_attivo:

    username = utente["USERNAME"]
    target = utente["TARGET"]

    url_media = "https://www.elenarosina.com/instatrack/getPostsFromUser.php?username="
    url_followers = "https://www.elenarosina.com/instatrack/getFollowersFromUser.php?username="
    url_followees = "https://www.elenarosina.com/instatrack/getFolloweeFromUser.php?username="


    media       =   str(requests.get(url_media      + username,verify=False).content)
    followers   =   str(requests.get(url_followers  + username,verify=False).content)
    followees   =   str(requests.get(url_followees  + username,verify=False).content)

    media = media.replace("'","")
    media = media.replace("b", "")

    followers = followers.replace("'", "")
    followers = followers.replace("b", "")

    followees = followees.replace("'", "")
    followees = followees.replace("b", "")

    time.sleep(1)
    #Creo il
    ora = time.strftime("%H:%M:%S")
    data = str(time.strftime("%d/%m/%Y"))

    tempo = data + " - " + ora

    print( tempo + " Username: " + username + " Followers: "+followers + " Follwees: " +followees)

    #Chiedo

