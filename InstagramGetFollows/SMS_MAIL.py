# coding=utf-8


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

from connection import CONNECTION
from InstagramAPI import scrivoColoratoSuFile, countUserIntoDatabase, selectUserFromDatabase, updateTreadFromUsername, \
    removeEmailFromDatabase, removeSMSFromDatabase, countUserIntoDatabaseFromTread, selectUserFromDatabaseAndThread

'''
In questo file inserisco tutte le funzioni necessarie all'invio di messaggi

I campi che controllo e' che il numero sia  con il + altrimenti restituisco un errore
'''

#FILE_NAME e' il nome del file che e' scritto!
FILE_NAME = "SMS_MAIL.html"

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


#questa funzione interroga il db per ottenere il primo SMS sa mandare
def ottengoSMSDalDatabase():
    url = "http://www.utentidaseguire.eu/instatrack/send_SMS/get_sms_from_database.php"
    risposta = requests.get(url).content
    risposta_json = json.loads(risposta)
    return risposta_json

#Questo metodo permete di capire se il numero di telefono e' corretto
#Come unico controllo vedo se il numero inizia per +39
def checkNumeroTelefonico(numero_telefonico):
    if numero_telefonico.startswith("+"):
        return numero_telefonico
    else:
        return "+" + numero_telefonico

#Questa funzione prende come parametro il numero e il messaggio e invia il messaggio al numero
def sendSMS(numero,messaggio):
    #Questo e' un esempio di come dovrebbe essere la chiamata
    #risposta = requests.post("https://www.instatrack.eu/sms/sms.php", data={'numero': '+393426788719', 'messaggio': 'ELEFANTI INFINITI', 'password': 'yY3KKeSfzyHynay28eSfCpzqw5Xn7zYt'}).content
    #print(risposta)

    risposta = requests.post("https://www.instatrack.eu/sms/sms.php",
                             data={'numero': numero, 'messaggio': messaggio,
                                   'password': 'yY3KKeSfzyHynay28eSfCpzqw5Xn7zYt'}).content
    #La risposta e' in questo modo se e' andato tutto a buon fine: { "success":"success" }
    # altrimenti e' cosi: { "success":"failed", "reason":"SMS not sent" }
    success = json.loads(risposta)

    if success["success"] == "success":
        messaggio = "SMS - SMS inviato"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        messaggio = "SMS - Messaggio non inviato con il seguente errore: " + str(success)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - ERRORE nell'invio dell'SMS, risposta ottenuta da instatrack.eu/sms/sms.php: " + str(success)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

#QUESTA PARTE PERMETTE DI MANDARE SMS AGLI UTENTI
def SMS():
    connection = CONNECTION()

    # Chiedo quante mail ci sono
    num_row = connection.num_row("SELECT * FROM SMS_INSTATRACK LIMIT 0,1")
    if num_row == 0:
        # Se non ce ne sono allora finisce qui tutto
        messaggio = "SMS - Non ho nuovi SMS da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        # Altrimenti scarico l'SMS
        fetchall = connection.fetchall("SELECT * FROM SMS_INSTATRACK LIMIT 0,1")
        ID_MESSAGGIO = str(fetchall[0][0])
        NUMERO_TELEFONICO = str(fetchall[0][1])
        MESSAGGIO = str(fetchall[0][2])



        NUMERO_TELEFONICO = checkNumeroTelefonico(NUMERO_TELEFONICO)
        messaggio = "SMS - Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        #Invio il messaggio SMS
        sendSMS(NUMERO_TELEFONICO, MESSAGGIO)

        #Mando una mail a me dicendo che invio un SMS
        EMAIL = "21giulio21@gmail.com"
        OGGETTO = "NUOVO SMS"
        MESSAGGIO = "INVIO UN NUOVO SMS al numero: " + str(NUMERO_TELEFONICO) + " Testo:"+str(MESSAGGIO)
        sendMailToUser(EMAIL, MESSAGGIO, OGGETTO )

        # Elimino la mail che ho appena mandato
        removeSMSFromDatabase(ID_MESSAGGIO)




##################### INIZIO SCRIPT PER MAIL #####################
def MAIL():
    connection = CONNECTION()


    #Chiedo quante mail ci sono
    num_row = connection.num_row("SELECT * FROM MAIL_INSTATRACK LIMIT 0,1")
    if num_row == 0:
        #Se non ce ne sono allora finisce qui tutto
        messaggio = "MAIL - Non ho nuove Mail da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        #Altrimenti scarico la mail
        fetchall = connection.fetchall("SELECT * FROM MAIL_INSTATRACK LIMIT 0,1")
        ID_MAIL = str(fetchall[0][0])
        EMAIL = str(fetchall[0][1])
        MESSAGGIO = str(fetchall[0][2])
        OGGETTO = str(fetchall[0][3])

        sendMailToUser(EMAIL,MESSAGGIO,OGGETTO)

        messaggio = "MAIL - Ho una MAIL da processare con Mail:" + EMAIL + " Messaggio: "+str(MESSAGGIO) + " Oggetto:"+OGGETTO
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        #Elimino la mail che ho appena mandato
        removeEmailFromDatabase(ID_MAIL)



################ Inizio a spostare gli utenti con: PSW errata / deve pagare = 1 su thread 0 ############
#Questo script permette di far si che tutti i profili con password errata = 1 o che hanno deve pagare = 1
#vengano spostati sul thread 0 in modo da non intasare gli altri
def SPOSTAMENTO_UTENTI():

    FILE_NAME = "SPOSTAMENTO_UTENTI.html"

    #Se sono qui dentro allora inizio il bilanciamento dei thread

    messaggio = "Sposto gli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    # Chiedo quanti utenti ho nel database
    numberUsersIntoDatabase = countUserIntoDatabase()
    print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

    # Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

        id = str(user[0]['ID'])
        username = str(user[0]['USERNAME'])
        cookie = str(user[0]['COOKIES'])
        follow_unfollow = str(user[0]['FOLLOW_UNFOLLOW'])
        users_followed_string = str(user[0]['USERS_FOLLOWED'])
        users_followed_array = re.split(';', users_followed_string)
        script_attivo = str(user[0]['SCRIPT_ACTIVE'])
        tempo_attesa_blocco = str(user[0]['TEMPO_ATTESA_BLOCCO'])

        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])

        # Qui inserisco il tempo in cui si e' iscritto al sito. In questo modo potendo solo dare 3 giorni di tempo come test se passano 3 giorni allora devom impostare
        # il valore: DEVE_PAGARE a 1 .
        tempo_iscrizione = str(user[0]['TEMPO_ISCRIZIONE'])

        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])



        # mail dell'utente
        email = str(user[0]['EMAIL'])

        thread = str(user[0]['THREAD'])




        #print(THREAD)
         #1) Se gli username hanno password errata allora li sposto sullo 0
        if  thread != '0' and password_errata == '1' :
            messaggio = "sposto l'utente: " + username + " sul thread 0"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            updateTreadFromUsername(username, "0")
        #Solamente se rispetta queste condizioni allora sposto gli utenti, altrimenti no.
        elif thread != '0' and deve_pagare == '1' and len(users_followed_array) == 0:
            messaggio = "sposto l'utente: " + username + " sul thread 0"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            updateTreadFromUsername(username, "0")


    messaggio = "Fine spostamenti degli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


##################### INIZIO - BILANCIAMENTO DEI THREAD #####################




##################### FINE - BILANCIAMENTO DEI THREAD #####################



#Inserisco qui dentro le code
schedule.every().second.do(SMS)
schedule.every().second.do(MAIL)
schedule.every().day.do(SPOSTAMENTO_UTENTI)

while True:
    schedule.run_pending()
    time.sleep(10)

