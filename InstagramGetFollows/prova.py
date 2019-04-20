from InstagramAPI import sendMailToUser

email = "21giulio21@gmail.com"

print("Mando la mail a " + email + " per comunicare che la password Instagram e' errata")

msg = "Ciao "+str("ugo")+",\n\nla password del tuo account Instagram e' errata.\nCollegati all'area utenti di Instatrack e inseriscila nuovamente per non perdere nuove occasioni.\n\nVisita https://areautenti.instatrack.eu\n\n\nIl Team di Instatrack."

subject = "Instatrack - Password Instagram Errata"
sendMailToUser(email, subject,msg)


