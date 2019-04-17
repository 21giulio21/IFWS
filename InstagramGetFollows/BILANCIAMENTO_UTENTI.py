
'''
Questa funzione permette di bilanciare i thread, in particolare permette di
far si che i vari utenti siano distribuiti uniformemente tra i thread
'''

#PROVESSO SOLAMENTE i seguenti thread, bilancio solo questi.
import json
import time
from random import randint

import requests
import schedule

from InstagramAPI import scrivoColoratoSuFile, updateTreadFromUsername


FILE_NAME = "BILANCIAMENTO.html"

#Questi sono i thread che voglio bilanciare
ARRAY_THREAD_DA_BILANCIARE = ["1","2","3","4","5","6","7", "8", "9", "10", "11" , "12", "13", "14", "15", "16"]
#ARRAY_THREAD_DA_BILANCIARE = ["1","2","3","4","5","6","7", "8", "9", "10", "11"]

#URL CHE restituisce il numero di utenti su quel hread
url_richesta_get_count_from_thread = "http://www.giuliovittoria.it/instatrack/BILANCIAMENTO_UTENTI_TRA_I_THREAD/getCountFromThread.php"



def BILANCIAMENTO_UTENTI_TRA_I_THREAD():


    #Questa variabile indica il totale di utenti
    UTENTI_TOTALI = 0



    for thread in ARRAY_THREAD_DA_BILANCIARE:
        #Invio al server i thread che devo bilanciare cosi ottengo la situazione attuale

        risposta = json.loads(requests.get(url_richesta_get_count_from_thread + "?THREAD=" + thread, verify=False).content)
        messaggio = "BILANCIAMENTO - THREAD: " + str(thread) + " COUNT: " + str(risposta)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
        time.sleep(2)

        if 'success' in risposta:
            messaggio = "BILANCIAMENTO - ERRORE nel bilanciamento dei thread, risposta: " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            return

        count = str(risposta[0]['COUNT'])

        UTENTI_TOTALI = UTENTI_TOTALI + int(count)

    MEDIA = int(UTENTI_TOTALI / len(ARRAY_THREAD_DA_BILANCIARE))

    #Mi faccio restituire tutti gli username che devo spostare

    #Qui dentro ho tutti gli username che devo processare
    USERNAME_UTENTI = []

    for my_thread in ARRAY_THREAD_DA_BILANCIARE:
        print("Utenti nel threrad: " + str(my_thread))
        url = "http://www.giuliovittoria.it/instatrack/BILANCIAMENTO_UTENTI_TRA_I_THREAD/getUsernameFromThread.php"
        utenti = json.loads(requests.get(url + "?THREAD=" + my_thread, verify=False).content)
        print(utenti)

        for utente in utenti:
            u = utente["USERNAME"]
            USERNAME_UTENTI.append(u)




    #in questo ciclo splitto tutti gli utenti nel thread
    for my_thread in ARRAY_THREAD_DA_BILANCIARE:

        cursore = 0
        while cursore < MEDIA:
            username_da_spostare = USERNAME_UTENTI.pop(0)
            print("Sposto lo username:" + str(username_da_spostare) + " sul thread: "+str(my_thread) )
            updateTreadFromUsername(username_da_spostare, str(my_thread))
            cursore = cursore + 1

    for utente_rimantente in USERNAME_UTENTI:
        min = int(ARRAY_THREAD_DA_BILANCIARE[0])
        max = int(ARRAY_THREAD_DA_BILANCIARE[len(ARRAY_THREAD_DA_BILANCIARE) - 1])
        print(min,max)

        rand_thread = randint(min, max)
        print("Sposto lo username che e' rimasto dentro:" + str(utente_rimantente) + " sul thread: " + str(rand_thread))
        updateTreadFromUsername(username_da_spostare, str(rand_thread))



BILANCIAMENTO_UTENTI_TRA_I_THREAD()

#schedule.every(5).hours.do
#schedule.every().second.do(BILANCIAMENTO_UTENTI_TRA_I_THREAD)

#while True:
    #schedule.run_pending()
    #time.sleep(3)

