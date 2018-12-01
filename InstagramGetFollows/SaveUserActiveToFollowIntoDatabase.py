import sys
import threading
import time

import instaloader
import requests


class myThread (threading.Thread):
   def __init__(self, follower):
      threading.Thread.__init__(self)
      self.follower = follower

   def run(self):
        self.function_thread()


   def function_thread(self):
       follower = self.follower
       followers = follower.followers
       username = follower.username
       # Se l'utente ha piu di 7k di followers non lo prendo neanche
       if int(followers) > 5000:
           print("L'utente: " + username + " ha piu di 5k followers, quindi non lo prendo nel nostro database")
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













target      =  "INFLUENCER_MONDIALE" #str(sys.argv[1])
username      =  "chiaraferragni" #str(sys.argv[2]) #"pugilato"



L = instaloader.Instaloader()
posts = instaloader.Profile.from_username(L.context, username).get_posts()

for post in posts:

    print(post.date)


    likes = post.get_likes()
    
    for like in likes:

        thread1 = myThread(like)
        thread1.start()
        time.sleep(2)



