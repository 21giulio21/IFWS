import json
import random

import instaloader
import requests

from InstagramAPI import scrivoColoratoSuFile



from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE

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

connection = CONNECTION_UTENTI_DA_SEGUIRE()

utenti = connection.fetchall("SELECT USERNAME,TARGET FROM UTENTI_DA_SEGUIRE ORDER BY RAND() LIMIT 1,4000")


for utente in utenti:
    USERNAME = str(utente[0])
    TARGET = str(utente[1])



    #url_controllo_se_username_esiste = "http://utentidaseguire.eu/getFollowersFromUsername.php?username=" + str(USERNAME)
    #risposta = str(requests.get(url_controllo_se_username_esiste, verify=False).content)
    #risposta = getCountFollowersFromUsername(USERNAME)
    #print("Username: " +str(USERNAME) +" "+ risposta)

    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context,USERNAME)
        userid = profile.userid

        messaggio = "PULIZIA_ACCOUNT - Tengo l'account con USERNAME:" + USERNAME + " e TARGET: " + str(
            TARGET) + " Instagram_ID:" + str(userid)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    except instaloader.exceptions.ProfileNotExistsException:

        messaggio = "PULIZIA_ACCOUNT - Elimino l'account con USERNAME:" + USERNAME + " e TARGET: " + str(
            TARGET)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
        print(rimuoviAccountUTENTI_DA_SEGUIRE(USERNAME))
        #connection.removeUserFromUTENTI_DA_SEGUIRE(USERNAME,TARGET)





