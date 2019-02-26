#Questo file permette di ottenere la lista di username che hanno publicato nel giorno
import time

import instaloader
import datetime



from InstagramAPI import countUserIntoDatabase, selectUserFromDatabase

tempo_di_ora = str(time.time())
tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]


#questi sono i secondi in un giorno
secondi_indietro = 86400

#tempo da cui considero e inizio il round,
tempo_o = int(tempo_di_ora) - secondi_indietro

#ottengo tutti gli username che hanno script arrivo 1
array_username_che_hanno_publicato = []

#Queste credenziali sono di un profilo a caso che permette solamente di
#avere accesso ai post e dati dei p
username_IG = "marco_tani23"
password_IG = "21giulio21"


L = instaloader.Instaloader()
L.login(user=username_IG,passwd=password_IG)




numberUsersIntoDatabase = countUserIntoDatabase()

for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

    #tra un utente e l'altro lascio un po di attesa
    #time.sleep(0.3)

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




    if deve_pagare == "0" and password_errata == "0" and script_attivo == "1" and delta_t < 81:
        #Ottengo tutti i post dell'utente
        try:
            posts = instaloader.Profile.from_username(L.context, username).get_posts()

            # stoppo per 2 secondi
            time.sleep(1)

            for post in posts:
                data_publicazione = int(post.date.timestamp())

                if int(data_publicazione) > int(tempo_o):
                    array_username_che_hanno_publicato.append(username)
                    print(username)

                break

        except:
            print("Non riesco a prendere la foto di " + str(username))














