import instaloader
import requests
import sys
from time import sleep
import random
import threading
import time
import sys
import threading

''''
Questo file permette di salvare USERNAME e ID dentro al database
In partcolare in base ai parametri in ingresso posso cambiare la modalità di salvataggio
Posso salvare:
1) Followers di username
2) Username che hanno messo media con ceti #

'''

'''
La variabile MODALITA può essere valorizzata:
1) FOLLOWERS -> in questo caso prendo i followers di un username
2) FOLLOWERS_PARAMETERS -> in questo caso prendo tutti i followers di un username con i parametri
3) HASTAG -> In questo caso prendo tutti gli username con i parametri che hanno messo quel #
'''
MODALITA = str(sys.argv[1])


#QUesta variabile contiene il valore relativo al target
TARGET  = str(sys.argv[2])


#Questa classe permette di parallelizzare

class myThread (threading.Thread):
   def __init__(self, post):
      threading.Thread.__init__(self)
      self.post = post

   def saveUserIntoDatabase(self,id,username):
        response = requests.get("https://www.elenarosina.com/instatrack/saveUserToFollow/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=" + str(
                id) + "&USERNAME=" + str(username) + "&TARGET=" + str(TARGET))
        print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(TARGET))
        print(response.content)

   def run(self):

       id = self.post.owner_profile.userid
       username = self.post.owner_profile.username
       followers = self.post.owner_profile.followers
       followees = self.post.owner_profile.followees



       # Se l'utente ha piu di 7k di followers non lo prendo neanche
       if int(followers) > 5000:
           print("L'utente:  ha piu di 5k followers, quindi non lo prendo nel nostro database")
           return

        #Controllo se la biografia e' settata
       #biografia = str(follower.biography)


       mediacount = self.post.owner_profile.mediacount
       if int(mediacount) > 8:

           is_private = self.post.owner_profile.is_private

           if is_private == False :

               if int(followees) > int(followers):




               elif int(followees) < 1200 and int(followees) > 300:
                   response = requests.get(
                       "https://www.elenarosina.com/instatrack/saveUserToFollow/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=" + str(
                           id) + "&USERNAME=" + str(username) + "&TARGET=" + str(target))
                   print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(
                       target) + "\nmedia: " + str(mediacount) + "\nis_private" + str(
                       is_private) + "\nfollowers:" + str(
                       followers) + "\nfollowee:" + str(followees))
                   print(response.content)











#Questa funzione permette di prendere gli username che hanno publicato tutte le foto
#con l'#selezionato e metterle dentro gl database, gli username vengono selezionati
#se rispettano i parametri
def GET_FOLLOWERS_FROM_HASTAG():

    hastag = str(sys.argv[3])

    L = instaloader.Instaloader()
    posts = L.get_hashtag_posts(hastag)

    index = 0

    for post in posts:
        thread1 = myThread(post)
        thread1.start()

        index = index + 1
        print(index)

        sleep(1)


#Questa funzione permette di prendere gli username che seguono un particolare username
# e metterle dentro gl database, gli username vengono selezionati
#se rispettano i parametri
def GET_FOLLOWERS_FROM_FOLLOWERS_PARAMETERS():
    return

if MODALITA     ==  "HASTAG":
    GET_FOLLOWERS_FROM_HASTAG()

elif MODALITA   ==  "FOLLOWERS_PARAMETERS":
    GET_FOLLOWERS_FROM_FOLLOWERS_PARAMETERS()


