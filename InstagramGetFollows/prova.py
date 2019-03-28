from InstagramAPI import sendSMSToUser

inizio_large_1 = "Il piano LARGE e' attivo sul tuo profilo! In questo piano e' inclusa la crescita dei tuoi post in particolare verranno pubblicati nella sezione ESPLORA di Instagram fino al raggiungimento di almeno 900 Like."
inizio_large_2 = "Per qualsiasi informazione puoi consultare la sezione FAQ del nostro sito web: https://www.instatrack.eu/#faq o contattarci direttamente sulla nostra pagina Instagram @instatrack.eu"
inizio_large_3 = "Puoi controllare in tempo reale il tuo account seguendo questo link: https://areautenti.instatrack.eu"

fine_prova_1 = "La tua prova di Instatrack e' terminata!\nScegli uno dei pacchetti per continuare a ricevere Followers reali italiani in target e Like a tutti i tuoi post!"
fine_prova_2 = "Ti ricordo che se vuoi continuare a ricevere Followers e Like devi scegliere un piano MEDIUM o superiore, il piano BASIC non include l'aumento di Like nei tuoi post!"
fine_prova_3 = "Utilizza il codice sconto HYPE, valido fino a domani, per uno sconto del 10% su ogni pacchetto A VITA! Riattiva immadietamente il servizio: http://bit.ly/instatrack10"

i = "me.giuliotavella@gmail.com"

sendSMSToUser(i,inizio_large_1)
sendSMSToUser(i,inizio_large_2)
sendSMSToUser(i, inizio_large_3)

