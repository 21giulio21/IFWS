from InstagramAPI import scrivoColoratoSuFile
from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE
import postmarker as postmarker
from postmarker.core import PostmarkClient
from CLASSI.CLASSI import MAIL_POSTMARKAPP

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
            HtmlBody=mail_postmarkapp.MESSAGGIO
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

sendMailWIthPOSTMARKAPP()




