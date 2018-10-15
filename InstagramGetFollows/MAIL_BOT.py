#QUESTO FILE PERMETTE DI CONTROLLARE IL DATABASE DELLE EMAIL, E NEL CASO IN CUI CI SIA UNA NUOVA MAIL DA MANDARE ESEGUE
import time
from email.mime.text import MIMEText


import json
import smtplib
from email.mime.multipart import MIMEMultipart
import requests

#questa funzione interroga il db e ottenere la prima mail da mandare
def ottengoMailDalDatabase():
    url = "http://www.elenarosina.com/instatrack/send_MAIL/get_mail_from_database.php"
    return json.loads(requests.get(url).content)

#questa funzione manda la mail all'utente
def sendMailToUser(mail_to, messaggio, subject):
    mail_from = "instatrack.eu@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_from, "21giulio21")

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = subject
    msg.attach(MIMEText(messaggio, 'plain'))
    text = msg.as_string()

    # Mando la mail all'utente
    server.sendmail(mail_from, mail_to, text)

    # Mando la mail anche a me cosi capisco cosa sta sucedendo
    server.sendmail(mail_from, "21giulio21@gmail.com", text)
    server.sendmail(mail_from, "m.denurchis@gmail.com", text)

    server.quit()


#DA QUI IL SISTEMA VIENE MESSO IN LOOP
while True:

    time.sleep(5)


    #RICHIEDO AL DATABASE MAIL SE CE UN NUOVO INDIRIZZO MAIL
    temp=ottengoMailDalDatabase()
    email=temp[0]['EMAIL']
    messaggio=temp[0]['MESSAGGIO']
    oggetto=temp[0]['OGGETTO']

    sendMailToUser(email,messaggio,oggetto)

    print("Mail mandata all'indirizzo mail " + email)

