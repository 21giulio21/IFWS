import re
import time

from termcolor import colored
import datetime
from email.mime.text import MIMEText
import json
import smtplib
import random
from email.mime.multipart import MIMEMultipart
import requests

from InstagramAPI import countUserIntoDatabase, selectUserFromDatabase, scrivoColoratoSuFile, updateTreadFromUsername

'''
In questo file inserisco tutte le funzioni necessarie per:
1) Invio SMS
2) Invio Mail
3) Controllo deigli utenti che ci sono su ogni thread: Per ogni thread controllo il numero degli
utenti che ho, se sono sbilanciati li bilancio
4) Elimino tutti i contatti che hanno il tempo di fine iscrizione > 2 mesi

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
        print(colored(getCurrentTime(), 'green'), colored("SMS - SMS inviato", 'green'))
    else:
        print(colored(getCurrentTime(), 'red'), colored("SMS - Messaggio non inviato con il seguente errore: " + success, 'red'))
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
        print(colored(getCurrentTime(), 'red'), colored("SMS - " + str(risposta), 'red'))
        print(colored(getCurrentTime(), 'red'), colored("SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

        #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - Risposta ottenuta: " + str(risposta)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

    #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
    else:
        print(colored(getCurrentTime(), 'green'), colored("SMS - " + str(risposta), 'green'))

else:
    print(colored(getCurrentTime(), 'green'), colored("SMS - Ho un SMS da processare", 'green'))
    print(colored(getCurrentTime(), 'green'), colored("SMS - " + str(risposta), 'green'))

    #Mappo il messagio
    NUMERO_TELEFONICO = str(risposta[0]["NUMERO_TELEFONICO"])
    MESSAGGIO = str(risposta[0]["MESSAGGIO"])

    if checkNumeroTelefonico(NUMERO_TELEFONICO):
        print(colored(getCurrentTime(), 'green'), colored("SMS - Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO, 'green'))
        sendSMS(NUMERO_TELEFONICO, MESSAGGIO)
    else:
        print(colored(getCurrentTime(), 'red'), colored("SMS - Il numero telefonico non inizia con il +", 'red'))
        print(colored(getCurrentTime(), 'red'),
              colored("SMS - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

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
        print(colored(getCurrentTime(), 'red'), colored("MAIL - " + str(risposta), 'red'))
        print(colored(getCurrentTime(), 'red'), colored("MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

        #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO MAIL - Risposta ottenuta: " + str(risposta)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

    #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
    else:
        print(colored(getCurrentTime(), 'green'), colored( "MAIL - " + str(risposta), 'green'))

else:
    print(colored(getCurrentTime(), 'green'), colored("MAIL - Ho una MAIL da processare", 'green'))
    print(colored(getCurrentTime(), 'green'), colored("MAIL - " + str(risposta), 'green'))

    #Mappo il messagio
    EMAIL = str(risposta[0]["EMAIL"])
    MESSAGGIO = str(risposta[0]["MESSAGGIO"])
    OGGETTO = str(risposta[0]["OGGETTO"])


    if checkMailCorrect(EMAIL):
        print(colored(getCurrentTime(), 'green'), colored("MAIL - Invio messaggio:" + MESSAGGIO + " alla mail: " + EMAIL, 'green'))
        sendMailToUser(EMAIL, MESSAGGIO, OGGETTO)

    else:
        print(colored(getCurrentTime(), 'red'), colored("MAIL - Indirizzo mail non valido", 'red'))
        print(colored(getCurrentTime(), 'red'),
              colored("MAIL - Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO MAIL  - La mail non contiene la @  ("+str(EMAIL)+") "
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)



