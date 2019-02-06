import json
import random

import requests


FILE_NAME = "puliziaAccount.html"
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
    return json.loads(requests.get(url, verify=False).content)

#Prendo il numero totale di account che ho:
numero_utenti_da_seguire = numeroDiUtentiDaSeguire()
print("Ho un totale di " + str(numero_utenti_da_seguire) + " utenti che devo gestire per mandare le richieste")

# Ora ciclo sul totale di persone che ho nel database
'''
index = int(random.randint(1,int(numero_utenti_da_seguire)))
user = selezionaAccountDaSeguireFromIndex(index)

id = str(user[0]['ID'])
username = str(user[0]['USERNAME'])
target = str(user[0]['TARGET'])

url_controllo_se_username_esiste = "http://utentidaseguire.eu/getFollowersFromUsername.php?username="+str(username)
risposta = str(requests.get(url_controllo_se_username_esiste,verify=False).content)
print(risposta)

if risposta.__contains__("false"):
    messaggio = " Username: " + username + " eliminato "
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
    risposta = rimuoviAccountUTENTI_DA_SEGUIRE(username)
    print(risposta)
'''