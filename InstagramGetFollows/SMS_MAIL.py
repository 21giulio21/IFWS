# coding=utf-8


import re
from random import randint

import instaloader
import schedule
from schedule import *

from termcolor import colored
import datetime
from email.mime.text import MIMEText
import json
import smtplib
from email.mime.multipart import MIMEMultipart
import requests
from InstagramAPI import scrivoColoratoSuFile
from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE
import postmarker as postmarker
from postmarker.core import PostmarkClient
from CLASSI.CLASSI import MAIL_POSTMARKAPP




from InstagramAPI import scrivoColoratoSuFile, countUserIntoDatabase, selectUserFromDatabase, updateTreadFromUsername, \
    removeEmailFromDatabase, removeSMSFromDatabase, countUserIntoDatabaseFromTread, selectUserFromDatabaseAndThread, \
    getLastPianoActived, updateDevePagare, updateSctiptActive

from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE

'''
In questo file inserisco tutte le funzioni necessarie all'invio di messaggi

I campi che controllo e' che il numero sia  con il + altrimenti restituisco un errore
'''

#FILE_NAME e' il nome del file che e' scritto!
FILE_NAME = "SMS_MAIL.html"

#Controllo che il campo EMAIL contenga la chiocciola: @
def checkMailCorrect(EMAIL):
    if EMAIL.__contains__("@"):
        return True
    else:
        return False

#questa funzione manda la mail all'utente
def sendMailToUser(mail_to, messaggio, subject):
    mail_from = "instatrack.eu@gmail.com"
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_from, "21giulio21")

    #testo = '<html><head><title>Instatrack</title></head><body style="background: #dedede"><table style = "margin-left: auto; margin-right: auto; width: 630px;background: white"><tr style="background: black"><td><img style="width:200px;padding:12px;" src="https://www.instatrack.eu/wp-content/uploads/elementor/thumbs/LOGO-o0cwmexrbxfckrp1c0gy6hfkh6toa4h5vs0wjy2mbg.png"></td></tr><tr style="clear:both;"><td style="display: block;"><p style="padding:24px 24px 0px 24px;font-family: arial;">Ciao :)</p></td><td style="display: block;"><p style="font-family: arial; text-align: justify; line-height: 26px;padding:0px 24px 24px 24px;">è arrivata Nuova SEAT Tarraco, il primo grande SUV creato a Barcellona. Grazie ai suoi dispositivi sempre all\'avanguardia, è pronta a semplificarti la vita ogni giorno. Con il SEAT Virtual Cockpit, il SEAT Drive Profile, i fari Full LED e fino a 7 posti a disposizione, hai la sintesi perfetta tra sicurezza, tecnologia, design, e versatilità, a 199€ al mese.<br>In poche parole, tutto ciò che ti serve per non fermarti mai.</p></td><td style="display: block;padding:0px 24px 12px 24px;margin-bottom: 30px;font-family: arial;">Scoprila anche domenica</td><td style="width:300px;border-radius:25px;padding:6px; display: block; text-align: center; margin: 0 auto; margin-bottom: 20px"><a href="http://seat.bustomotorcompany.it/modelli/tarraco"><button style="width:300px; border-radius:25px;padding:12px;background: #e9515e; color:white">Scopri di più</button></a></td></tr></table></body></html>'

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = subject
    #TODO: msg.attach(MIMEText( messaggio, 'html'))
    msg.attach(MIMEText(messaggio, 'plain'))
    text = msg.as_string()

    # Mando la mail all'utente
    server.sendmail(mail_from, mail_to, text)

    # Mando la mail anche a me cosi capisco cosa sta sucedendo
    server.sendmail(mail_from, "21giulio21@gmail.com", text)


    server.quit()
    '''

def getCurrentTime():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))


#questa funzione interroga il db per ottenere il primo SMS sa mandare
def ottengoSMSDalDatabase():
    url = "http://www.utentidaseguire.eu/instatrack/send_SMS/get_sms_from_database.php"
    risposta = requests.get(url).content
    risposta_json = json.loads(risposta)
    return risposta_json

#Questo metodo permete di capire se il numero di telefono e' corretto
#Come unico controllo vedo se il numero inizia per +39
def checkNumeroTelefonico(numero_telefonico):
    if numero_telefonico.startswith("+"):
        return numero_telefonico
    else:
        return "+" + numero_telefonico

#Questa funzione prende come parametro il numero e il messaggio e invia il messaggio al numero
def sendSMS(numero,messaggio):
    #Questo e' un esempio di come dovrebbe essere la chiamata
    #risposta = requests.post("https://www.instatrack.eu/sms/sms.php", data={'numero': '+393426788719', 'messaggio': 'ELEFANTI INFINITI', 'password': 'yY3KKeSfzyHynay28eSfCpzqw5Xn7zYt'}).content
    #print(risposta)

    risposta = requests.post("https://www.instatrack.eu/sms/sms.php",
                             data={'numero': numero, 'messaggio': messaggio,
                                   'password': 'yY3KKeSfzyHynay28eSfCpzqw5Xn7zYt'}).content
    #La risposta e' in questo modo se e' andato tutto a buon fine: { "success":"success" }
    # altrimenti e' cosi: { "success":"failed", "reason":"SMS not sent" }
    success = json.loads(risposta)

    if success["success"] == "success":
        messaggio = "SMS - SMS inviato"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        messaggio = "SMS - Messaggio non inviato con il seguente errore: " + str(success)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

        # Invio a me stesso una mail dicendo che non possiamo mandare l' SMS.
        msg = "ERRORE NELL' INVIO SMS - ERRORE nell'invio dell'SMS, risposta ottenuta da instatrack.eu/sms/sms.php: " + str(success)
        subject = "ERRORE"
        email = "21giulio21@gmail.com"
        sendMailToUser(email, msg, subject)



def BILANCIAMENTO_UTENTI_TRA_I_THREAD():


    FILE_NAME = "BILANCIAMENTO.html"

    # Questi sono i thread che voglio bilanciare
    ARRAY_THREAD_DA_BILANCIARE = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

    # URL CHE restituisce il numero di utenti su quel hread
    url_richesta_get_count_from_thread = "http://www.giuliovittoria.it/instatrack/BILANCIAMENTO_UTENTI_TRA_I_THREAD/getCountFromThread.php"

    #Questa variabile indica il totale di utenti
    UTENTI_TOTALI = 0



    for thread in ARRAY_THREAD_DA_BILANCIARE:
        #Invio al server i thread che devo bilanciare cosi ottengo la situazione attuale

        risposta = json.loads(requests.get(url_richesta_get_count_from_thread + "?THREAD=" + thread, verify=False).content)
        time.sleep(5)

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



#QUESTA PARTE PERMETTE DI MANDARE SMS AGLI UTENTI
def SMS():

    connection = CONNECTION_UTENTI_DA_SEGUIRE()

    # Chiedo quante mail ci sono
    num_row = connection.num_row("SELECT * FROM SMS_INSTATRACK LIMIT 0,1")
    if num_row == 0:
        # Se non ce ne sono allora finisce qui tutto
        messaggio = "SMS - Non ho nuovi SMS da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        # Altrimenti scarico l'SMS
        fetchall = connection.fetchall("SELECT * FROM SMS_INSTATRACK LIMIT 0,1")
        ID_MESSAGGIO = str(fetchall[0][0])

        NUMERO_TELEFONICO = str(fetchall[0][1])
        MESSAGGIO = str(fetchall[0][2])



        NUMERO_TELEFONICO = checkNumeroTelefonico(NUMERO_TELEFONICO)
        messaggio = "SMS - Invio messaggio:" + MESSAGGIO + " al numero: " + NUMERO_TELEFONICO
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        #Invio il messaggio SMS
        sendSMS(NUMERO_TELEFONICO, MESSAGGIO)

        #Mando una mail a me dicendo che invio un SMS
        EMAIL = "21giulio21@gmail.com"
        OGGETTO = "NUOVO SMS"
        MESSAGGIO = "INVIO UN NUOVO SMS al numero: " + str(NUMERO_TELEFONICO) + " Testo:"+str(MESSAGGIO)
        sendMailToUser(EMAIL, MESSAGGIO, OGGETTO )

        # Elimino la mail che ho appena mandato
        removeSMSFromDatabase(ID_MESSAGGIO)





##################### INIZIO SCRIPT PER MAIL #####################
def MAIL():
    connection = CONNECTION_UTENTI_DA_SEGUIRE()


    #Chiedo quante mail ci sono
    num_row = connection.num_row("SELECT * FROM MAIL_INSTATRACK LIMIT 0,1")
    if num_row == 0:
        #Se non ce ne sono allora finisce qui tutto
        messaggio = "MAIL - Non ho nuove Mail da processare"
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    else:
        #Altrimenti scarico la mail
        fetchall = connection.fetchall("SELECT * FROM MAIL_INSTATRACK LIMIT 0,1")
        ID_MAIL = str(fetchall[0][0])
        EMAIL = str(fetchall[0][1])
        MESSAGGIO = str(fetchall[0][2])
        OGGETTO = str(fetchall[0][3])

        sendMailToUser(EMAIL,MESSAGGIO,OGGETTO)

        messaggio = "MAIL - Ho una MAIL da processare con Mail:" + EMAIL + " Messaggio: "+str(MESSAGGIO) + " Oggetto:"+OGGETTO
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        #Elimino la mail che ho appena mandato
        removeEmailFromDatabase(ID_MAIL)



################ Mando una mail contenente tutti gli username che hanno postato nelle 24h ############
def mandoEmailPerGliUtentiCheHannoPostato():
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]

    # questi sono i secondi in un giorno
    secondi_indietro = 86400

    # tempo da cui considero e inizio il round,
    tempo_o = int(tempo_di_ora) - secondi_indietro

    # ottengo tutti gli username che hanno script arrivo 1
    array_username_che_hanno_publicato = []

    # Queste credenziali sono di un profilo a caso che permette solamente di
    # avere accesso ai post e dati dei p

    L = instaloader.Instaloader()

    # Ottengo gli identificativi di chi mettete/riceve i like
    numberUsersIntoDatabase = countUserIntoDatabase()

    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # tra un utente e l'altro lascio un po di attesa
        time.sleep(0.3)

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)
        username = str(user[0]['USERNAME'])
        script_attivo = str(user[0]['SCRIPT_ACTIVE'])
        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])
        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])

        # Ottendo dt in modo da non prendere tutti, ma solo chi paga dal medium in su
        delta_t = int(user[0]['DELTA_T'])

        if deve_pagare == "0" and password_errata == "0" and script_attivo == "1" and delta_t < 81:
            # Ottengo tutti i post dell'utente
            try:
                posts = instaloader.Profile.from_username(L.context, username).get_posts()

                # stoppo per 2 secondi
                time.sleep(0)

                for post in posts:
                    data_publicazione = int(post.date.timestamp())

                    if int(data_publicazione) > int(tempo_o):
                        array_username_che_hanno_publicato.append(username)
                        print(username)

                    break

            except:
                print("Non riesco a prendere la foto di " + str(username))

        # Stringa che contiene tutti gli username separati da un \n
    stringa_username = ""
    for a in array_username_che_hanno_publicato:
        abbonamento_attivo = str(getLastPianoActived(str(a)))
        stringa_username = stringa_username  +"\n" + a + " - " + abbonamento_attivo
        print("UU ", stringa_username)

    EMAIL = "21giulio21@gmail.com"
    OGGETTO = "UTENTI POSTANTI FOTO - ELEFANTI"
    MESSAGGIO = stringa_username
    sendMailToUser(EMAIL, MESSAGGIO, OGGETTO)


################ Inizio a spostare gli utenti con: PSW errata / deve pagare = 1 su thread 0 ############
#Questo script permette di far si che tutti i profili con password errata = 1 o che hanno deve pagare = 1
#vengano spostati sul thread 0 in modo da non intasare gli altri
def SPOSTAMENTO_UTENTI():

    FILE_NAME = "SPOSTAMENTO_UTENTI.html"

    #Se sono qui dentro allora inizio il bilanciamento dei thread

    messaggio = "Sposto gli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

    # Chiedo quanti utenti ho nel database
    numberUsersIntoDatabase = countUserIntoDatabase()
    print("Ho un totale di " + str(numberUsersIntoDatabase) + " utenti che devo gestire per mandare le richieste")

    # Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabase(index)

        id = str(user[0]['ID'])
        username = str(user[0]['USERNAME'])
        cookie = str(user[0]['COOKIES'])
        follow_unfollow = str(user[0]['FOLLOW_UNFOLLOW'])
        users_followed_string = str(user[0]['USERS_FOLLOWED'])
        users_followed_array = re.split(';', users_followed_string)
        script_attivo = str(user[0]['SCRIPT_ACTIVE'])
        tempo_attesa_blocco = str(user[0]['TEMPO_ATTESA_BLOCCO'])

        # PASSWORD_ERRATA e' a 1 se la password di instagram e' sbagliata
        password_errata = str(user[0]['PASSWORD_ERRATA'])

        # Qui inserisco il tempo in cui si e' iscritto al sito. In questo modo potendo solo dare 3 giorni di tempo come test se passano 3 giorni allora devom impostare
        # il valore: DEVE_PAGARE a 1 .
        tempo_iscrizione = str(user[0]['TEMPO_ISCRIZIONE'])

        # deve_pagare e' a 1 solo se l'utente non ha pagato.
        deve_pagare = str(user[0]['DEVE_PAGARE'])



        # mail dell'utente
        email = str(user[0]['EMAIL'])

        thread = str(user[0]['THREAD'])




        #print(THREAD)
         #1) Se gli username hanno password errata allora li sposto sullo 0
        if  thread != '0' and password_errata == '1' :
            messaggio = "sposto l'utente: " + username + " sul thread 0"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            updateTreadFromUsername(username, "0")
        #Solamente se rispetta queste condizioni allora sposto gli utenti, altrimenti no.
        elif thread != '0' and deve_pagare == '1' and len(users_followed_array) == 0:
            messaggio = "sposto l'utente: " + username + " sul thread 0"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")
            updateTreadFromUsername(username, "0")


    messaggio = "Fine spostamenti degli utenti con: PSW errata / deve pagare = 1 su thread 0"
    scrivoColoratoSuFile(FILE_NAME, messaggio, "green")


'''
1) Faccio si che tutti quelli che sono sul thread 0 abbiano script attivo = 0
2) Faccio si che tutti quelli che sono sul thread 0 e hanno la data di fine pagamento passato gli diventi DEVE_PAGARE = 1
'''
def ordineInTHread_0():

    thread_passato_come_patametro = "0"

    # Chiedo quanti utenti ho nel database
    numberUsersIntoDatabase = countUserIntoDatabaseFromTread(thread_passato_come_patametro)

    # Ora ciclo sul totale di persone che ho nel database
    for index in range(0, int(numberUsersIntoDatabase)):  # Deve partire da 0

        # Seleziono la tupla relativa all'utente
        user = selectUserFromDatabaseAndThread(index, thread_passato_come_patametro)

        username = str(user[0]['USERNAME'])


        # Tempo in uci deve finire lo script
        tempo_fine_iscrizione = str(user[0]['TEMPO_FINE_ISCRIZIONE'])


        tempo_di_ora = int((time.time()))


        if tempo_fine_iscrizione == "" or tempo_fine_iscrizione.__contains__("-"):
            continue

        print( username + " " + tempo_fine_iscrizione)


        if int(tempo_fine_iscrizione) < tempo_di_ora:
            print("Modifico i dati per: " +username )
            updateDevePagare(username,"1")
            updateSctiptActive(username,"0")

############################################# INIZIO DATI PROFILO ######################################################


def getProfileData(USERNAME):

    profile_data = {}

    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context,USERNAME)
        profile_data["ID_INSTAGRAM"] = profile.userid
        profile_data["FOLLOWERS"] = profile.followers
        profile_data["FOLLOWEE"] = profile.followees
        profile_data["POST_NUMBER"] = profile.mediacount
        profile_data["URL"] = profile.profile_pic_url



        messaggio = "Dati di: " + str(USERNAME) + ": "+str(profile_data)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        return profile_data

    except instaloader.exceptions.ProfileNotExistsException:

        messaggio = "Impossibile ottenere l' ID Instagram di: " + str(USERNAME)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")



#Scarico tutti gli username presenti in giuliovittoria.it
def downloadAllUsername():
    url = "http://www.giuliovittoria.it/instatrack/DATI_PROVILO/getAllUsername.php"
    risposta = requests.get(url).content
    return json.loads(risposta)

def uploadDataIntoDb(USERNAME,ID_INSTAGRAM,FOLLOWERS,FOLLOWEE,POST_NUMBER,URL):
    url = "http://utentidaseguire.eu/instatrack/DATI_PROFILO/insertDatiProfilo.php?USERNAME="+str(USERNAME)+"&ID_INSTAGRAM="+str(ID_INSTAGRAM)+"&FOLLOWERS="+str(FOLLOWERS)+"&FOLLOWEE="+str(FOLLOWEE)+"&POST_NUMBER="+str(POST_NUMBER)+"&URL="+str(URL)
    risposta = requests.get(url).content
    print(risposta)
'''
Questa funzione è il core di tutto questo script:
1) Scarica gli username degli utenti che sono nel DB giuliovittoria
2) Per ogni username scarica tutte le informazioni necessarie
'''
def core_function():

    utenti = downloadAllUsername()

    for utente in utenti:
        username = utente["USERNAME"]
        dati_profilo =getProfileData(username)

        URL = dati_profilo["URL"]
        ID_INSTAGRAM = dati_profilo["ID_INSTAGRAM"]
        FOLLOWERS = dati_profilo["FOLLOWERS"]
        FOLLOWEE = dati_profilo["FOLLOWEE"]
        POST_NUMBER = dati_profilo["POST_NUMBER"]
        uploadDataIntoDb(username,ID_INSTAGRAM,FOLLOWERS,FOLLOWEE,POST_NUMBER,URL)



############################################# FINE DATI PROFILO ######################################################


#Questa funzione permette di mandare le mail attraverso POSTMARKAPP
def sendMailWIthPOSTMARKAPP():
    CONNECTION = CONNECTION_UTENTI_DA_SEGUIRE()

    try:

        #l'oggetto che ritorna è un oggetto di tipo MAIL_POSTMARKAPP, bisogna scorporarlo e poi mandare la mail
        mail_postmarkapp = CONNECTION.getMailFromDb_POSTMARKAPP()[0]
    except:
        messaggio = "POSMARKAPP MAIL - NON HO MAIL DA PROCESSARE"
        scrivoColoratoSuFile("a.html", messaggio, "red")
        return



    #Creo l'oggetto postmark
    postmark = PostmarkClient(server_token='f6cd8fa0-db9d-45b1-8f3e-20052de2ec9a')

    try:
        #Invio la mail
        postmark.emails.send(
            From='info@instatrack.eu',
            To=mail_postmarkapp.EMAIL,
            Subject=mail_postmarkapp.OGGETTO,
            HtmlBody=mail_postmarkapp.MESSAGGIO_TEMPLATE
        )

        messaggio = "POSMARKAPP MAIL - Mail inviata ad " + str(mail_postmarkapp.EMAIL) + " con il messaggio: " + str(
            mail_postmarkapp.MESSAGGIO)
        scrivoColoratoSuFile("a.html", messaggio, "green")

    except:
        messaggio = "POSMARKAPP MAIL - Mail NON INVIATA -> " + str(mail_postmarkapp.EMAIL) + " con il messaggio: " + str(
            mail_postmarkapp.MESSAGGIO)
        scrivoColoratoSuFile("a.html", messaggio, "red")

    #A precindere che l'ha mandata o meno la cencello dal DB
    #Rimuovo la mail appena mandata, recupero la mail attraverso il suo ID.
    CONNECTION.removeEmailFromDb_POSTMARKAPP(mail_postmarkapp.ID)



#Inserisco qui dentro le code
schedule.every().second.do(SMS)
schedule.every().second.do(MAIL)
schedule.every().second.do(sendMailWIthPOSTMARKAPP)
schedule.every().day.do(SPOSTAMENTO_UTENTI)
schedule.every(1).hours.do(mandoEmailPerGliUtentiCheHannoPostato)
schedule.every(48).hours.do(BILANCIAMENTO_UTENTI_TRA_I_THREAD)
schedule.every(48).hours.do(ordineInTHread_0)
schedule.every(5).hours.do(core_function)


while True:
    schedule.run_pending()
    time.sleep(10)


