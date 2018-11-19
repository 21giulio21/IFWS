import datetime
import time


#Questa funzione permette di prendere in input lo username che diventa il nome del file e il messaggio da scrivere
def stampa(username,messaggio):

    #Prendo il timestamp
    ts = time.time()
    timestamp = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

    print(timestamp + " " + username + " " + messaggio)

    #Stampo su file il messaggio
    #with open("~/Dropbox/Git/IFWS/InstagramGetFollows/LOG/" + username +".txt" , "a") as myfile:
        #myfile.write(timestamp + " " + messaggio)
