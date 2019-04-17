from InstagramGetFollows.InstagramAPI import sendMailToUser

msg = "Ciao \n\nla password del tuo account Instagram e’ errata.\nCollegati all’area utenti di Instatrack e inseriscila nuovamente per non perdere nuove occasioni.\n\nVisita https://areautenti.instatrack.eu\n\n\nIl Team di Instatrack."
subject = "Instatrack.eu - Password Instagram Errata"
email = "21giulio21@gmail.com"
sendMailToUser(email, subject,msg)