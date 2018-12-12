import random
import time

from termcolor import colored
import datetime
from email.mime.text import MIMEText
import json
import smtplib
from email.mime.multipart import MIMEMultipart
import requests

from InstagramAPI import scrivoColoratoSuFile, countUserIntoDatabase, selectUserFromDatabase, updateTreadFromUsername

'''
In questo file inserisco tutte le funzioni necessarie all'invio di messaggi

I campi che controllo e' che il numero sia  con il + altrimenti restituisco un errore
'''


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


#questa funzione interroga il db e ottenere la prima mail da mandare
def ottengoMailDalDatabase():
    url = "http://www.elenarosina.com/instatrack/send_MAIL/get_mail_from_database.php"
    risposta = requests.get(url).content
    risposta_json = json.loads(risposta)
    return risposta_json


#questa funzione interroga il db per ottenere il primo SMS sa mandare
def ottengoSMSDalDatabase():
    url = "http://www.elenarosina.com/instatrack/send_SMS/get_sms_from_database.php"
    risposta = requests.get(url).content
    risposta_json = json.loads(risposta)
    return risposta_json

#Questo metodo permete di capire se il numero di telefono e' corretto
#Come unico controllo vedo se il numero inizia per +39
def checkNumeroTelefonico(numero_telefonico):
    if numero_telefonico.startswith("+"):
        return True
    else:
        return False

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
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

    else:
        messaggio = "SMS - Messaggio non inviato con il seguente errore: " + success
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - ERRORE nell'invio dell'SMS, risposta ottenuta da instatrack.eu/sms/sms.php: " + success
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)


#TODO: Rimuovere per inserire un qualcosa di figo
time.sleep(10)

##################### INIZIO SCRIPT PER SMS #####################
#QUESTA PARTE PERMETTE DI MANDARE SMS AGLI UTENTI


risposta = ottengoSMSDalDatabase();
#Ora controllo la risposta, se la risposta e' qualcosa di simile:
#{ "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
#Allora non devo proseguire perche non ho messaggi.
if 'success' in risposta:

    #Se la pagina php ha come risposta qualcosa che non sia: { "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
    #Allora mando la mail a me dicendo che ho un problema
    if risposta["reason"] != "Non ho SMS da prendere dal DB":


        messaggio = "SMS - " + str(risposta)
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        messaggio = "SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - Risposta ottenuta: " + str(risposta)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

    #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
    else:

        messaggio = "SMS - " + str(risposta)
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")
else:

    messaggio = "SMS - Ho un SMS da processare"
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

    messaggio = "SMS - " + str(risposta)
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")


    #Mappo il messagio
    NUMERO_TELEFONICO = str(risposta[0]["NUMERO_TELEFONICO"])
    MESSAGGIO = str(risposta[0]["MESSAGGIO"])

    if checkNumeroTelefonico(NUMERO_TELEFONICO):

        messaggio = "SMS - Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

        sendSMS(NUMERO_TELEFONICO, MESSAGGIO)



    else:


        messaggio = "SMS - Il numero telefonico non inizia con il +"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        messaggio = "SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - Il numero di telefono a cui voglio mandare l'SMS ("+str(NUMERO_TELEFONICO)+") non inizia con il + "
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

##################### FINE SCRIPT PER SMS #####################


##################### INIZIO SCRIPT PER MAIL #####################

risposta = ottengoMailDalDatabase()
#Ora controllo la risposta, se la risposta e' qualcosa di simile:
#{ "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
#Allora non devo proseguire perche non ho messaggi.



if 'success' in risposta:

    #Se la pagina php ha come risposta qualcosa che non sia: { "success":"failed", "reason":"Non ho MAIL da prendere dal DB" }
    #Allora mando la mail a me dicendo che ho un problema
    if risposta["reason"] != "Non ho MAIL da prendere dal DB":

        messaggio = "MAIL - " + str(risposta)
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        messaggio = "MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")



        #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO MAIL - Risposta ottenuta: " + str(risposta)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

    #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
    else:
        messaggio = "MAIL - " + str(risposta)
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

else:

    messaggio = "MAIL - Ho una MAIL da processare"
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

    messaggio = "MAIL - " + str(risposta)
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")


    #Mappo il messagio
    EMAIL = str(risposta[0]["EMAIL"])
    MESSAGGIO = str(risposta[0]["MESSAGGIO"])
    OGGETTO = str(risposta[0]["OGGETTO"])


    if checkMailCorrect(EMAIL):

        messaggio = "MAIL - Invio messaggio:" + MESSAGGIO + " alla mail: " + EMAIL
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

        sendMailToUser(EMAIL, MESSAGGIO, OGGETTO)

    else:
        messaggio = "MAIL - Indirizzo mail non valido"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")

        messaggio = "MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
        scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "red")


        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO MAIL  - La mail non contiene la @  ("+str(EMAIL)+") "
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)
################ INIZIO SCRIPT BILANCIAMENTO THREAD ############
#QUuesto parte solamente 1 volta su 200




numero_casuale = int(random.randint(0, 100))


if numero_casuale == 50:

    #Se sono qui dentro allora inizio il bilanciamento dei thread

    messaggio = "Inizio a spostare gli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")

    #In questa variabile inserisco il tempo di ora
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:-3]

    #scarico tute le tuple che ho nel database
    numberUsersIntoDatabase = countUserIntoDatabase()
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

        username = str(user[0]['USERNAME'])

        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])


        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])

        # Tempo in uci deve finire lo script
        tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])

        # mail dell'utente, utile perche contattiamo l'utente per
        # dirgli che e' da un mese che non accede
        email = str(user[0]['EMAIL'])

        thread = str(user[0]['THREAD'])

         #1) Se gli username hanno password errata / deve pagare = 1 allora li sposto sullo 0
        if int(thread) != 0 and (password_errata == '1' or deve_pagare == '1'):
            messaggio = "sposto l'utente: " + username + " sul thread 0"
            scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")
            updateTreadFromUsername(username, "0")

    messaggio = "Fine bilanciamento thread"
    scrivoColoratoSuFile("SMS_MAIL.html", messaggio, "green")




