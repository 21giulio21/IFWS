import json

from termcolor import colored
import requests
import datetime


'''
In questo file inserisco tutte le funzioni necessarie all'invio di messaggi

I campi che controllo e' che il numero sia  con il + altrimenti restituisco un errore
'''

def getCurrentTime():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))

#questa funzione interroga il db per ottenere il primo SMS sa mandare
def ottengoSMSDalDatabase():
    url = "http://www.elenarosina.com/instatrack/send_SMS/get_sms_from_database.php"
    if
    temp = json.loads(requests.get(url).content)

    ID_MESSAGGIO = temp[0]['ID_MESSAGGIO']
    NUMERO_TELEFONICO = temp[0]['NUMERO_TELEFONICO']
    MESSAGGIO = temp[0]['MESSAGGIO']

    return

#def sendSMS(numero,messaggio):

    #Controllo che il nuemro di telefono inizia per +
    #Questo e' un esempio di come dovrebbe essere la chiamata
    #risposta = requests.post("https://www.instatrack.eu/sms/sms.php", data={'numero': '+393426788719', 'messaggio': 'ELEFANTI INFINITI', 'password': 'yY3KKeSfzyHynay28eSfCpzqw5Xn7zYt'}).content
    #print(risposta)



print(colored(getCurrentTime(), 'green') , colored("Inizio controllo", 'green') )
print(ottengoSMSDalDatabase())
print(colored('hello', 'red'), colored('world', 'green'))