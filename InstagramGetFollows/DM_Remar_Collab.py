import time

import schedule

from InstagramAPI import countUserIntoDatabase, selectUserFromDatabase, sendDMMessage

from enum import Enum     # for enum34, or the stdlib version

# Utilizzo un ENUM per andare a mappare i valori dei DIRECT,
#Animal = Enum('Animal', 'ant bee cat dog')
#Animal.ant  # returns <Animal.ant: 1>
#Animal['ant']  # returns <Animal.ant: 1> (string lookup)
#Animal.ant.name  # returns 'ant' (inverse lookup)
#COLLAB è il messaggio di collaborazione, REMARK quello per il remarketing e CLIENT è il messaggio da mandare al cliente
#chiedendo se conosce Instatrack e proponendo il prodotto
from InstagramAPI import sendDMMessageWithTAG

CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')
# "REMARK_0" sono quelli che hanno inserito il loro sito dentro al sito ma poi non hanno piu fatto ne prove ne neiente altro

''''
Questa funzione permette di mandare DM a tutti quelli che hanno il BOT spento da almeno 10 giorni,
in particolare sono tutti gli utenti che hanno finito la prova e poi sono rimasti li fermi

'''
def mandoDMRemark():

    tempo_di_ora = int((time.time()))
    print(tempo_di_ora)
    tempo_10_giorni_fa = int(tempo_di_ora) - 864000

    numberUsersIntoDatabase = countUserIntoDatabase()

    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        #tra un utente e l'altro lascio un po di attesa
        time.sleep(1)

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)
        username = str(user[0]['USERNAME'])
        script_attivo = str(user[0]['SCRIPT_ACTIVE'])
        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])
        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])


        # Tempo in uci deve finire lo script
        tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])

        if tempo_fine_iscrizione == "":
            continue




        if deve_pagare == "1" and int(tempo_fine_iscrizione) < tempo_10_giorni_fa :
            messaggio_b64 = "U29sbyBwZXIgdGUgZmlubyBhIGRvbWFuaSDDqCB2YWxpZG8gaWwgY29kaWNlIHNjb250byBYTEExNSAgcGVyIG90dGVuZXJlIHVubyBzY29udG8gZGVsIDE1JSBzdSBvZ25pIG5vc3RybyBwYWNjaGV0dG8gQSBWSVRBISEhIAoKU2NlZ2xpIHVubyBkZWkgcGFjY2hldHRpIHBlciBjb250aW51YXJlIGEgcmljZXZlcmUgRm9sbG93ZXJzIHJlYWxpIGl0YWxpYW5pIGluIHRhcmdldCBlIExpa2UgYSB0dXR0aSBpIHR1b2kgcG9zdC4gCgpBY2NlZGkgYWxsYSB0dWEgYXJlYSBwZXJzb25hbGUgcGVyIGF0dGl2YXJlIGlsIHNlcnZpemlvOiBodHRwczovL2FyZWF1dGVudGkuaW5zdGF0cmFjay5ldQ=="
            sendDMMessageWithTAG(username,messaggio_b64,"REMARK")
            print(username)


'''
Questa funzione permette di mandare il messaggio a tutti quelli che non hanno mai iniziato nessun abbonamento/prova
'''

def mandoDMAtuttiQuelloCheNonHannoMaiAcqquistatoUnPiano():
    messaggio_b64 = "SGFpIGluc2VyaXRvIGlsIHR1byBhY2NvdW50IEluc3RhZ3JhbSBzdWxsYSBub3N0cmEgcGlhdHRhZm9ybWEgcGVyIGluaXppYXJlIGEgY3Jlc2NlcmUgY29uIEZvbGxvd2VycyBlIExpa2UgcmVhbGksIGl0YWxpYW5pIGUgaW4gdGFyZ2V0LgoKQ29zYSBhc3BldHRpIGEgcHJvdmFyZSBpbCBub3N0cm8gc2Vydml6aW8/CgpTb2xvIHBlciB0ZSDDqCBhdHRpdm8gaWwgY29kaWNlIHNjb250byBBUEwxMCwgdmFsaWRvIGZpbm8gYSBkb21hbmksIHBlciB1bm8gc2NvbnRvIGRlbCAxMCUgc3Ugb2duaSBwYWNjaGV0dG8gQSBWSVRBISAKCnd3dy5pbnN0YXRyYWNrLmV1Cg=="

    numberUsersIntoDatabase = countUserIntoDatabase()

    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # tra un utente e l'altro lascio un po di attesa
        time.sleep(1)

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)
        username = str(user[0]['USERNAME'])
        script_attivo = str(user[0]['SCRIPT_ACTIVE'])
        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])
        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])

        # Tempo in uci deve finire lo script
        tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])

        if tempo_fine_iscrizione == "" and script_attivo == '0':
            sendDMMessageWithTAG(username, messaggio_b64, "REMARK_0")
            print(username)



#Questa funzione permette di mandare DM a tutti quelli che non hanno mai acquistato un piano ma
#Hanno solo inserito il loro account in Instatrack
#schedule.every().day.do(mandoDMAtuttiQuelloCheNonHannoMaiAcqquistatoUnPiano)
schedule.every(24).hours.do(mandoDMAtuttiQuelloCheNonHannoMaiAcqquistatoUnPiano)


#Funzione che manda a tutti quelli che hanno finito prove,abbonamento il DM di remark
schedule.every(24).hours.do(mandoDMRemark)


while True:
    schedule.run_pending()
    time.sleep(10)

