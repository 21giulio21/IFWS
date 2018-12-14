import random
import time
import schedule
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

#FILE_NAME è il nome del file che è scritto!
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
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        messaggio = "SMS - Messaggio non inviato con il seguente errore: " + success
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - ERRORE nell'invio dell'SMS, risposta ottenuta da instatrack.eu/sms/sms.php: " + success
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

#QUESTA PARTE PERMETTE DI MANDARE SMS AGLI UTENTI
def SMS():
    risposta = ottengoSMSDalDatabase();
    #Ora controllo la risposta, se la risposta e' qualcosa di simile:
    #{ "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
#   Allora non devo proseguire perche non ho messaggi.
    if 'success' in risposta:

        #Se la pagina php ha come risposta qualcosa che non sia: { "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
        #Allora mando la mail a me dicendo che ho un problema
        if risposta["reason"] != "Non ho SMS da prendere dal DB":


            messaggio = "SMS - " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            messaggio = "SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
            msg = "ERRORE NELL' INVIO SMS - Risposta ottenuta: " + str(risposta)
            subject = "ERRORE"
            email = "21giulio21@gmail.com"
            sendMailToUser(email, msg, subject)

        #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
        else:

            messaggio = "SMS - " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
    else:

        messaggio = "SMS - Ho un SMS da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        messaggio = "SMS - " + str(risposta)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


        #Mappo il messagio
        NUMERO_TELEFONICO = str(risposta[0]["NUMERO_TELEFONICO"])
        MESSAGGIO = str(risposta[0]["MESSAGGIO"])

        if checkNumeroTelefonico(NUMERO_TELEFONICO):

            messaggio = "SMS - Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

            sendSMS(NUMERO_TELEFONICO, MESSAGGIO)



        else:


            messaggio = "SMS - Il numero telefonico non inizia con il +"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            messaggio = "SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
            msg = "ERRORE NELL' INVIO SMS - Il numero di telefono a cui voglio mandare l'SMS ("+str(NUMERO_TELEFONICO)+") non inizia con il + "
            subject = "ERRORE"
            email = "21giulio21@gmail.com"
            sendMailToUser(email, msg, subject)


##################### INIZIO SCRIPT PER MAIL #####################
def MAIL():
    risposta = ottengoMailDalDatabase()
    #Ora controllo la risposta, se la risposta e' qualcosa di simile:
    #{ "success":"failed", "reason":"Non ho SMS da prendere dal DB" }
    #Allora non devo proseguire perche non ho messaggi.



    if 'success' in risposta:

        #Se la pagina php ha come risposta qualcosa che non sia: { "success":"failed", "reason":"Non ho MAIL da prendere dal DB" }
        #Allora mando la mail a me dicendo che ho un problema
        if risposta["reason"] != "Non ho MAIL da prendere dal DB":

            messaggio = "MAIL - " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            messaggio = "MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")



            #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
            msg = "ERRORE NELL' INVIO MAIL - Risposta ottenuta: " + str(risposta)
            subject = "ERRORE"
            email = "21giulio21@gmail.com"
            sendMailToUser(email, msg, subject)

        #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
        else:
            messaggio = "MAIL - " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:

        messaggio = "MAIL - Ho una MAIL da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        messaggio = "MAIL - " + str(risposta)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


        #Mappo il messagio
        EMAIL = str(risposta[0]["EMAIL"])
        MESSAGGIO = str(risposta[0]["MESSAGGIO"])
        OGGETTO = str(risposta[0]["OGGETTO"])


        if checkMailCorrect(EMAIL):

            messaggio = "MAIL - Invio messaggio:" + MESSAGGIO + " alla mail: " + EMAIL
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

            sendMailToUser(EMAIL, MESSAGGIO, OGGETTO)

        else:
            messaggio = "MAIL - Indirizzo mail non valido"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            messaggio = "MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")


            # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
            msg = "ERRORE NELL' INVIO MAIL  - La mail non contiene la @  ("+str(EMAIL)+") "
            subject = "ERRORE"
            email = "21giulio21@gmail.com"
            sendMailToUser(email, msg, subject)

################ Inizio a spostare gli utenti con: PSW errata / deve pagare = 1 su thread 0 ############
#Questo script permette di far si che tutti i profili con password errata = 1 o che hanno deve pagare = 1
#vengano spostati sul thread 0 in modo da non intasare gli altri
def SPOSTAMENTO_UTENTI():

    #Se sono qui dentro allora inizio il bilanciamento dei thread

    messaggio = "Inizio a spostare gli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

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
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            updateTreadFromUsername(username, "0")

    messaggio = "Fine spostamenti degli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

##################### INIZIO - BILANCIAMENTO DEI THREAD #####################




##################### FINE - BILANCIAMENTO DEI THREAD #####################




##################### INIZIO - STATISTICHE #####################
#Questo script permette di effettuare una scansione dei profili che utilizzano il bot.
#Per ogni profilo viene salvato: username, followers, followees e media.




def STATISTICHE():
    numberUsersIntoDatabase = countUserIntoDatabase()
    messaggio = "Inizio il processo di creazione delle statistiche con un totale di utenti:"+str(numberUsersIntoDatabase)
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


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

            #Ottengo i secondi in modo da poter definire quando ho fatto il check
            timestamp = int(time.time())

            #Ora mando i dati al server

            #Url a cui mandare i dati
            url = "https://www.elenarosina.com/instatrack/STATISTICHE/saveUsernameFolloweesFollowersIntoDatabase.php"

            messaggio = " Username: " + username + " Followers: "+followers + " Follwees: " +followees
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            risposta = requests.get(url + "?USERNAME=" + username + "&FOLLOWEES=" + str(followees) + "&FOLLOWERS=" + str(followers)+ "&TARGET=" + target + "&TIMESTAMP=" + str(timestamp)).content

            success = json.loads(risposta)

            if success['success'] != 'success' :
                messaggio = "STATISTICHE - ERRORE nel salvataggio della tupla di: " + str(username) + " " + str(risposta)
                scrivoColoratoSuFile(FILE_NAME, messaggio, "red")


#Inserisco qui dentro le code
schedule.every().second.do(SMS)
schedule.every().second.do(MAIL)

schedule.every().day.do(STATISTICHE)

schedule.every().day.do(SPOSTAMENTO_UTENTI)


while True:
    schedule.run_pending()
    time.sleep(6)

