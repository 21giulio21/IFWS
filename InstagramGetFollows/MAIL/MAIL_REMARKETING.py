'''
In questo file vado a mandare
'''
import time

from InstagramAPI import sendSMSToUser, countUserIntoDatabase, sendSMSToUserWithTag, selectUserFromDatabase, \
    getPhoneNumberFromEmail, getLastPianoActived

#Questi 2 messaggi sono mandati a tutti i clienti che hanno inserito il loro account ma poi non hanno mai acquistato il pacchetto prova.
massaggio_01_1 = "Hai inserito il tuo account Instagram su Instatrack per crescere con Followers e Like reali, italiani e in target. Cosa aspetti a provare il nostro servizio?"
massaggio_01_2 = "Solo per te è attivo il codice sconto APL10, valido fino a domani, per uno sconto del 10% su ogni pacchetto A VITA!\nATTIVA SUBITO SU: www.instatrack.eu"

#Questi 2 messaggi sono mandati a tutti i clienti che hanno comprato la prova ma poi non sono piu andati avanti
massaggio_02_1 = "Hai terminato la prova gia da tempo e non hai ancora attivato un piano Instatrack."
massaggio_02_2 = "Solo per te fino a domani e' valido il codice sconto XLA15 per ottenere uno sconto del 15% su ogni nostro pacchetto A VITA! "
massaggio_02_3 = "Scegli uno dei pacchetti per continuare a ricevere Followers reali italiani e Like a tutti i tuoi post."
massaggio_02_4 = "Accedi alla tua area personale per attivare il servizio: https://areautenti.instatrack.eu"

#Qiesti messaggi devono essere mandati nel momento in cui devo scrivere a chi ha gia attivato un piano e poi l'ha termianto senza rinnovi
massaggio_03_1 = "Hai terminato il tuo piano Instatrack gia da tempo."
massaggio_03_2 = "Solo per te fino a domani e' valido il codice sconto XLA15 per ottenere uno sconto del 15% su ogni nostro pacchetto A VITA! "
massaggio_03_3 = "Scegli uno dei pacchetti per continuare a ricevere Followers reali italiani e Like a tutti i tuoi post."
massaggio_03_4 = "Accedi alla tua area personale per attivare il servizio: https://areautenti.instatrack.eu"


numberUsersIntoDatabase = countUserIntoDatabase()

for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # tra un utente e l'altro lascio un po di attesa
    #time.sleep(1)

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
    email = str(user[0]['EMAIL'])

    '''
    Entro in qui dentro solamente se l'utente non ha mai effettuato nessun pagamento verso Instatrack, quindi deve comunicare di
    comprare un pacchetto
    '''
    print(username,tempo_fine_iscrizione)
    if tempo_fine_iscrizione == "" and script_attivo == '0':
        try:
            print("Username: " + username + " - non ha mai comprato 1 piano ne prova")
            numero = getPhoneNumberFromEmail(email);
            sendSMSToUserWithTag(numero, massaggio_01_1, "01")
            sendSMSToUserWithTag(numero, massaggio_01_2, "0101")
            continue
        except:
            print("PRoblema con email: " + email)
            continue

    ''''
     Prima di mandare l'SMS controllo che l'utente si sia registrato almeno 10 giorni fa, non mando il messaggio a chi si e'
    registrato 9 giorni fa.

    In questo modo lascio passare un po di tempo dalla fine prova a quando arriverà l'SMS.
    '''

    #controllo l'ultimo abbonamento attivo sul profilo
    abbonamento_attivo = str(getLastPianoActived(str(username)))

    tempo_di_ora = int((time.time()))
    print(tempo_di_ora)
    tempo_10_giorni_fa = int(tempo_di_ora) - 864000


    if abbonamento_attivo.__contains__("Prova") and int(tempo_fine_iscrizione) < tempo_10_giorni_fa :
        print("Username: " + username + " - ultimo piano attivato è la prova")

        try:
            numero = getPhoneNumberFromEmail(email);
            sendSMSToUserWithTag(numero, massaggio_02_1, "02")
            sendSMSToUserWithTag(numero, massaggio_02_2, "0202")
            sendSMSToUserWithTag(numero, massaggio_02_3, "020202")
            sendSMSToUserWithTag(numero, massaggio_02_4, "02020202")
            continue
        except:
            print("PRoblema con email: " + email)
            continue
    elif (not abbonamento_attivo.__contains__("Prova") )and int(tempo_fine_iscrizione) < tempo_10_giorni_fa:
        #Se sono qui dentro allora significa che l'utente ha fatto un abbonamnto che non è la prova e poi ha terminato.

        print("Username: " + username + " - ultimo piano attivato NON è la prova")

        try:
            numero = getPhoneNumberFromEmail(email);
            sendSMSToUserWithTag(numero, massaggio_03_1, "03")
            sendSMSToUserWithTag(numero, massaggio_03_2, "0303")
            sendSMSToUserWithTag(numero, massaggio_03_3, "030303")
            sendSMSToUserWithTag(numero, massaggio_03_4, "03030303")
            continue
        except:
            print("PRoblema con email: " + email)
            continue


