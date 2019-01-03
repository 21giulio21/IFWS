import json
import random

import requests

from InstagramAPI import scrivoColoratoSuFile
from connection import CONNECTION

FILE_NAME = "PULIZIA_ACCOUNT.html"

def numeroDiUtentiDaSeguire():
    url = "http://utentidaseguire.eu/getCountUTENTI_DA_SEGUIRE.php"
    return requests.get(url,verify=False).content

#Seleziona un utente dal database con un preciso indice
def selezionaAccountDaSeguireFromIndex(index):
    url = "http://utentidaseguire.eu/getUTENTE_DA_SEGUIREFromIndex.php?index=" +str(index)
    return json.loads(requests.get(url,verify=False).content)

#Questa funzione permette di eliminare l'account
def rimuoviAccountUTENTI_DA_SEGUIRE(username):
    url = "http://utentidaseguire.eu/removeUserFromUTENTI_DA_SEGUIRE.php?USERNAME=" + str(username)
    return requests.get(url, verify=False).content

#Prendo il numero totale di account che ho:
numero_utenti_da_seguire = numeroDiUtentiDaSeguire()
print("Ho un totale di " + str(numero_utenti_da_seguire) + " utenti che devo gestire per mandare le richieste")

connection = CONNECTION()

utenti = connection.fetchall("SELECT USERNAME FROM UTENTI_DA_SEGUIRE ORDER BY RAND()")


for utente in utenti:
    USERNAME = str(utente[0])

    url_controllo_se_username_esiste = "http://utentidaseguire.eu/getFollowersFromUsername.php?username=" + str(USERNAME)
    risposta = str(requests.get(url_controllo_se_username_esiste, verify=False).content)
    print("Username: " +str(USERNAME) +" "+ risposta)

    if risposta.__contains__("false"):
        messaggio = " Username: " + USERNAME + " eliminato "
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
        risposta = rimuoviAccountUTENTI_DA_SEGUIRE(USERNAME)
        print(risposta)