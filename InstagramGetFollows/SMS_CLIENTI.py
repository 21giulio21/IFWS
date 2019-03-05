#from enum import Enum
import time

from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE
from InstagramAPI import sendSMSToUserWithTag

#CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')
from InstagramAPI import countUserIntoDatabase, selectUserFromDatabase

prefisso_numero = ""
messaggio = "A grande richiesta ancora 100 pacchetti Instatrack in promozione del 10% a VITA utilizzando il codice sconto APL10.\nAttiva subito la promo: www.instatrack.eu"

tag =  "CLIENT"
c = CONNECTION_UTENTI_DA_SEGUIRE()

#Inserisco in questo array tutti gli utenti da contattare
utenti_da_contattare = c.getUTENTI_DA_CONTATTARE()

#Inserisco in questo array tutti i contatto che ho gia io nel database che utilizzano Instatrack
utenti_utilizzatori_instatrack = []


#Ottengo tutti gli username che stanno utilizzando Instatrack, in questo modo posso toglierli dall'array di utenti da contattare
numberUsersIntoDatabase = countUserIntoDatabase()

for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)
    username = str(user[0]['USERNAME'])
    utenti_utilizzatori_instatrack.append(username)
    time.sleep(0.2)
    print("X - " + username)

print("Ho finito il download dei miei contatti")

for utente in utenti_da_contattare:
    username = utente.username
    followers = utente.followers
    mail = utente.mail
    telefono = utente.telefono

    print("Inserisco l'utente " + username + " come utente da contattare")

    if utenti_utilizzatori_instatrack.__contains__(username):
        print("Non contatto " + username + " perche gia usa Instatrack")
    else:
        sendSMSToUserWithTag(telefono, messaggio,tag)


