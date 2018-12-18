import json
import time

import requests

#utenti = str(requests.get("https://www.elenarosina.com/instatrack/STATISTICHE/getUsernameFromDatabase.php",verify=False).content).replace("b'" , "").replace("" , "")
from InstagramGetFollows.InstagramAPI import scrivoColoratoSuFile

FILE_NAME = "prova_1.html"

utenti = json.loads(requests.get("https://www.elenarosina.com/instatrack/STATISTICHE/getUsernameAndTargetFromDatabase.php").text)

for utente in utenti:
    username = utente["USERNAME"]
    target = utente["TARGET"]



    url_media =     "https://www.elenarosina.com/instatrack/getPostsFromUser.php?username="
    url_followers = "https://www.elenarosina.com/instatrack/getFollowersFromUser.php?username="
    url_followees = "https://www.elenarosina.com/instatrack/getFolloweeFromUser.php?username="

    media = requests.get(url_media + username, verify=False).content.decode('utf-8')
    followers = requests.get(url_followers + username, verify=False).content.decode('utf-8')
    followees = requests.get(url_followees + username, verify=False).content.decode('utf-8')

    time.sleep(1)

    # Ottengo i secondi in modo da poter definire quando ho fatto il check
    timestamp = int(time.time())

    # Ora mando i dati al server

    # Url a cui mandare i dati
    url = "http://www.utentidaseguire.eu/STATISTICHE/saveUsernameFolloweesFollowersIntoDatabase.php"

    messaggio = " Username: " + username + " Followers: " + followers + " Follwees: " + followees
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
    risposta = requests.get(url + "?USERNAME=" + username + "&FOLLOWEES=" + str(followees) + "&FOLLOWERS=" + str(
        followers) + "&TARGET=" + target + "&TIMESTAMP=" + str(timestamp)).content

    success = json.loads(risposta)

    if success['success'] != 'success':
        messaggio = "STATISTICHE - ERRORE nel salvataggio della tupla di: " + str(username) + " " + str(risposta)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
