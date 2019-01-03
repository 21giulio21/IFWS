
'''
Questa funzione permette di bilanciare i thread, in particolare permette di
far si che i vari utenti siano distribuiti uniformemente tra i thread
'''

#PROVESSO SOLAMENTE i seguenti thread, bilancio solo questi.
import json
import time

import requests
import schedule

from InstagramAPI import scrivoColoratoSuFile, updateTreadFromUsername


FILE_NAME = "BILANCIAMENTO.html"

#Questi sono i thread che voglio bilanciare
ARRAY_THREAD_DA_BILANCIARE = ["1","2","3","4","5","6","7","8"]

#Questo e' un array accociativo in cui come chiave ho il thread e come valore
#ho il numero di ustenti su quel thread
ARRAY_THREAD_COUNT = {}

#URL CHE restituisce il numero di utenti su quel hread
url_richesta = "http://utentidaseguire.eu/instatrack/BILANCIAMENTO_UTENTI_TRA_I_THREAD/getCountFromThread.php"


def BILANCIAMENTO_UTENTI_TRA_I_THREAD():

    #Questa variabile deve contenere il numero di utenti da posstare
    totale_utenti_da_spostare = 0

    #soglia indica l'errore, maggiore e' la soglia e piu i thread sono bilanciati a caso
    SOGLIA = 1

    for thread in ARRAY_THREAD_DA_BILANCIARE:
        #Invio al server i thread che devo bilanciare cosi ottengo la situazione attuale

        risposta = json.loads(requests.get(url_richesta+"?THREAD=" + thread,verify=False).content)
        time.sleep(5)

        if 'success' in risposta:
            messaggio = "BILANCIAMENTO - ERRORE nel bilanciamento dei thread, risposta: " + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            return

        count = str(risposta[0]['COUNT'])
        ARRAY_THREAD_COUNT[thread] = count
        totale_utenti_da_spostare = totale_utenti_da_spostare + int(count)

    media = int(totale_utenti_da_spostare / len(ARRAY_THREAD_DA_BILANCIARE))

    messaggio = "Utenti su cui si fanno spostamenti: "+ str(totale_utenti_da_spostare) + " media:" + str(media)
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


    #Individuo tutti i thread che hanno piu utenti della metia + soglia
    array_thread_sovra_soglia = []

    # Individuo tutti i thread che hanno meno utenti della metia - soglia
    array_thread_sotto_soglia = []


    for thread in ARRAY_THREAD_DA_BILANCIARE:

        if int(ARRAY_THREAD_COUNT[thread]) > media + SOGLIA:
            array_thread_sovra_soglia.append(thread)

        elif int(ARRAY_THREAD_COUNT[thread]) < media - SOGLIA:
            array_thread_sotto_soglia.append(thread)


    if (len(array_thread_sovra_soglia) > 0) and (len(array_thread_sotto_soglia) > 0):
        thread_sovra_soglia = array_thread_sovra_soglia.pop()
        thread_sotto_soglia = array_thread_sotto_soglia.pop()

        #ottengo un username tra i thread che ne hanno di piu
        url = "http://www.utentidaseguire.eu/instatrack/BILANCIAMENTO_UTENTI_TRA_I_THREAD/getUsernameFromThread.php"
        risposta = json.loads(requests.get(url + "?THREAD=" + thread_sovra_soglia, verify=False).content)
        time.sleep(5)

        if 'success' in risposta:
            messaggio = "Errore nella richiesta all'url("+url+"), risposta:" + str(risposta)
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            return

        username_da_spostare = risposta[0]["USERNAME"]
        updateTreadFromUsername(username_da_spostare,thread_sotto_soglia)

        messaggio = "Utente " + username_da_spostare + " spostato sul thread " + str(thread_sotto_soglia)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")





schedule.every(5).hours.do(BILANCIAMENTO_UTENTI_TRA_I_THREAD)

while True:
    schedule.run_pending()
    time.sleep(100)

