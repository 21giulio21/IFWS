import sys
import threading
from time import sleep

import  instaloader
import requests

from InstagramAPI import getIDFromUsername

target      =   str(sys.argv[1])
hastag      =   str(sys.argv[2]) #"pugilato"



class myThread (threading.Thread):
   def __init__(self, follower):
      threading.Thread.__init__(self)
      self.follower = follower

   def run(self):
        self.function_thread()


   def function_thread(self):
       follower = self.follower
       followers = follower.followers


       # Se l'utente ha piu di 7k di followers non lo prendo neanche
       if int(followers) > 5000:
           print("L'utente:  ha piu di 5k followers, quindi non lo prendo nel nostro database")
           return

        #Controllo se la biografia è settata
       #biografia = str(follower.biography)


       mediacount = follower.mediacount
       if int(mediacount) > 8:

           is_private = follower.is_private

           if is_private == False :

               followees = follower.followees
               if int(followees) > int(followers):
                   id = follower.userid
                   username = follower.username
                   response = requests.get(
                       "http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=" + str(
                           id) + "&USERNAME=" + str(username) + "&TARGET=" + str(target))
                   print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(
                       target) + "\nmedia: " + str(mediacount) + "\nis_private" + str(
                       is_private) + "\nfollowers:" + str(
                       followers) + "\nfollowee:" + str(followees))
                   print(response.content)


               elif int(followees) < 1200 and int(followees) > 300:
                   id = follower.userid
                   username = follower.username
                   response = requests.get(
                       "http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=" + str(
                           id) + "&USERNAME=" + str(username) + "&TARGET=" + str(target))
                   print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(
                       target) + "\nmedia: " + str(mediacount) + "\nis_private" + str(
                       is_private) + "\nfollowers:" + str(
                       followers) + "\nfollowee:" + str(followees))
                   print(response.content)




L = instaloader.Instaloader()
posts = L.get_hashtag_posts(hastag)

for i in posts:

    username = i.owner_username
    profilo = instaloader.Profile.from_username(L.context, username)


    thread1 = myThread(profilo)
    thread1.start()
    #sleep(0.5)

