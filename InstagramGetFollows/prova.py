import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMailToUser(mail_to, messaggio, subject):
    mail_from       = "info@instatrack.eu"
    password_from   = "21PC21pc"
    print("login1")
    server = smtplib.SMTP('smtps.aruba.it', 465)
    server.starttls()
    print("login")
    server.login(mail_from, password_from)
    print("login")
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

sendMailToUser("21giulio21@gmail.com","messaggio","ohh")