import random
import re
import time

import schedule
from schedule import *

from termcolor import colored
import datetime
from email.mime.text import MIMEText
import json
import smtplib
from email.mime.multipart import MIMEMultipart
import requests



from InstagramAPI import scrivoColoratoSuFile, countUserIntoDatabase, selectUserFromDatabase, updateTreadFromUsername

'''
In Questo dile vado ad inserire tutte le statistiche nel database di: utentidaseguire.eu
'''

#FILE_NAME è il nome del file che è scritto!
FILE_NAME = "STATISTICHE.html"

#Controllo che il campo EMAIL contenga la chiocciola: @
def checkMailCorrect(EMAIL):
    if EMAIL.__contains__("@"):
        return True
    else:
        return False

#questa funzione manda la mail all'utente
def sendMailToUser(mail_to, messaggio, subject):
    mail_from = "instatrack.eu@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_from, "21giulio21")

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = subject
    msg.attach(MIMEText(messaggio, 'plain'))
    text = msg.as_string()

    # Mando la mail all'utente
    server.sendmail(mail_from, mail_to, text)

    # Mando la mail anche a me cosi capisco cosa sta sucedendo
    server.sendmail(mail_from, "21giulio21@gmail.com", text)


    server.quit()

def getCurrentTime():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))





##################### INIZIO - STATISTICHE #####################
#Questo script permette di effettuare una scansione dei profili che utilizzano il bot.
#Per ogni profilo viene salvato: username, followers, followees e media.




def STATISTICHE():
    numberUsersIntoDatabase = countUserIntoDatabase()
    messaggio = "Inizio il processo di creazione delle statistiche con un totale di utenti:"+str(numberUsersIntoDatabase)
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    utenti = json.loads(
        requests.get("https://www.elenarosina.com/instatrack/STATISTICHE/getUsernameAndTargetFromDatabase.php").text)

    for utente in utenti:
        username = utente["USERNAME"]
        target = utente["TARGET"]

        url_media = "https://www.elenarosina.com/instatrack/getPostsFromUser.php?username="
        url_followers = "https://www.elenarosina.com/instatrack/getFollowersFromUser.php?username="
        url_followees = "https://www.elenarosina.com/instatrack/getFolloweeFromUser.php?username="

        media = requests.get(url_media + username, verify=False).content.decode('utf-8')
        followers = requests.get(url_followers + username, verify=False).content.decode('utf-8')
        followees = requests.get(url_followees + username, verify=False).content.decode('utf-8')


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


#Inserisco qui dentro le code
schedule.every().second.do(STATISTICHE)



while True:
    schedule.run_pending()
    time.sleep(6)

