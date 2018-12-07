import json

from termcolor import colored
import requests
import datetime

from InstagramAPI import sendMailToUser

'''
In questo file inserisco tutte le funzioni necessarie all'invio di messaggi

I campi che controllo e' che il numero sia  con il + altrimenti restituisco un errore
'''

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
        print(colored(getCurrentTime(), 'green'), colored("SMS inviato", 'green'))
    else:
        print(colored(getCurrentTime(), 'red'), colored("Messaggio non inviato con il seguente errore: " + success, 'red'))
        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - ERRORE nell'invio dell'SMS, risposta ottenuta da instatrack.eu/sms/sms.php: " + success
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)



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
        print(colored(getCurrentTime(), 'red'), colored(risposta, 'red'))
        print(colored(getCurrentTime(), 'red'), colored("Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

        #Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - Risposta ottenuta: " + str(risposta)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

    #Entro dentro l'else solamente se risposta["reason"] == "Non ho SMS da prendere dal DB". In questo scrivo che non ho SMS da processare
    else:
        print(colored(getCurrentTime(), 'green'), colored(risposta, 'green'))

else:
    print(colored(getCurrentTime(), 'green'), colored("Ho un SMS da processare", 'green'))
    print(colored(getCurrentTime(), 'green'), colored(risposta, 'green'))

    #Mappo il messagio
    NUMERO_TELEFONICO = str(risposta[0]["NUMERO_TELEFONICO"])
    MESSAGGIO = str(risposta[0]["MESSAGGIO"])

    if checkNumeroTelefonico(NUMERO_TELEFONICO):
        print(colored(getCurrentTime(), 'green'), colored("Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO, 'green'))
        sendSMS(NUMERO_TELEFONICO, MESSAGGIO)
    else:
        print(colored(getCurrentTime(), 'red'), colored("Il numero telefonico non inizia con il +", 'red'))
        print(colored(getCurrentTime(), 'red'),
              colored("Invio la mail all'indirizzo: 21giulio21@gmail.com dicendo che ho un errore", 'red'))

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - Il numero di telefono a cui voglio mandare l'SMS ("+str(NUMERO_TELEFONICO)+") non inizia con il + "
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)

##################### FINE SCRIPT PER SMS #####################


##################### INIZIO SCRIPT PER MAIL #####################


