import time
from InstagramAPI import countUserIntoDatabase
from InstagramAPI import selectUserFromDatabase



delta_t = 290 #Perche ci sono 86400 secondi in un giorno e devo mandare massimo 300 richieste di follow o di unfollow al giorno
max_requests = 300

while True:
    #time.sllep(delta_t)
    print("Tempo DT passato, inizio lo script.")

    #Chiedo quanti utenti ho nel database
    count = countUserIntoDatabase()
    print("Ho un totale di " + str(count) + " utenti")

    #Ora ciclo sul totale di persone che ho nel database
    for index in range(0,int(count)): #Deve partire da 0

        #Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

        #Se il campo ID e' nullo allora chiedo l'id dell'utente a instagram
