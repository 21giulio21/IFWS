import time

from InstagramAPI import countUserIntoDatabase, selectUserFromDatabase, sendDMMessage

from enum import Enum     # for enum34, or the stdlib version

# Utilizzo un ENUM per andare a mappare i valori dei DIRECT,
#Animal = Enum('Animal', 'ant bee cat dog')
#Animal.ant  # returns <Animal.ant: 1>
#Animal['ant']  # returns <Animal.ant: 1> (string lookup)
#Animal.ant.name  # returns 'ant' (inverse lookup)
#COLLAB è il messaggio di collaborazione, REMARK quello per il remarketing e CLIENT è il messaggio da mandare al cliente
#chiedendo se conosce Instatrack e proponendo il prodotto
CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')



print(CATEGORIA.COLLAB.name)


exit(0)
numberUsersIntoDatabase = countUserIntoDatabase()

for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    #tra un utente e l'altro lascio un po di attesa
    time.sleep(0.3)

    # Seleziono la tupla relativa all'utente
    user = selectUserFromDatabase(index)
    username = str(user[0]['USERNAME'])
    script_attivo = str(user[0]['SCRIPT_ACTIVE'])
    # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
    password_errata = str(user[0]['PASSWORD_ERRATA'])
    # deve_pagare e' a 1 solo se l'utente non ha pagato.
    deve_pagare = str(user[0]['DEVE_PAGARE'])

    #Ottendo dt in modo da non prendere tutti, ma solo chi paga dal medium in su
    delta_t = int(user[0]['DELTA_T'])




    if deve_pagare == "1":
        messaggio_b64 = "Q2lhbyEgCgpOb24gY2kgaGFpIHBpdSBmYXR0byBzYXBlcmUgbnVsbGEhIAoKVXRpbGl6emEgaWwgY29kaWNlIHNjb250byBIWVBFIHBlciBvdHRlbmVyZSB1bm8gc2NvbnRvIGRlbCAxMCUgc3Ugb2duaSBub3N0cm8gcGFjY2hldHRvIEEgVklUQSEhISAKCiBTY2VnbGkgdW5vIGRlaSBwYWNjaGV0dGkgcGVyIGNvbnRpbnVhcmUgYSByaWNldmVyZSBmb2xsb3dlcnMgcmVhbGkgaXRhbGlhbmkgaW4gdGFyZ2V0IGUgbGlrZSBhIHR1dHRpIGkgdHVvaSBwb3N0LiAKCkFjY2VkaSBhbGxhIHR1YSBhcmVhIHBlcnNvbmFsZSBwZXIgYXR0aXZhcmUgaWwgc2Vydml6aW86IGh0dHBzOi8vYXJlYXV0ZW50aS5pbnN0YXRyYWNrLmV1"
        sendDMMessage(username, messaggio_b64)
        print(username)

