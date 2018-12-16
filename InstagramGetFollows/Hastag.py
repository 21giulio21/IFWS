import sys
import threading
from time import sleep

import  instaloader
import requests

target      =   str(sys.argv[1])
hastag      =   str(sys.argv[2]) #"pugilato"


URL_SALVATAGGIO_UTENTI = "http://www.utentidaseguire.eu/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php"


def controlloSeNelDBHoGiaUnUtenteConQuelIDETarget(id, target):
    # Faccio una richiueata al url: http://altridatabase.altervista.org/controlloSeNelDBHoGiaUnUtenteConQuelID.php?ID=1632792873    torna TRUE SE POSSO INSERIRE L?UTENTE
    url = "https://www.elenarosina.com/instatrack/saveUserToFollow/controlloSeNelDBHoGiaUnUtenteConQuelID.php?ID=" + str(id) + "&TARGET=" + target
    response = requests.get(url)
    if str(response.content).__contains__("TR"):
        return False
    else:
        print("ID Gia inserito " + str(id) + " con il target" + target)
        return True


class myThread (threading.Thread):
   def __init__(self, post):
      threading.Thread.__init__(self)
      self.post = post

   def run(self):
        self.function_thread()




   def function_thread(self):

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
                   response = requests.get(
                       URL_SALVATAGGIO_UTENTI + "?ID=" + str(
                           id) + "&USERNAME=" + str(username) + "&TARGET=" + str(target))
                   print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(
                       target) + "\nmedia: " + str(mediacount) + "\nis_private" + str(
                       is_private) + "\nfollowers:" + str(
                       followers) + "\nfollowee:" + str(followees))
                   print(response.content)


               elif int(followees) < 1200 and int(followees) > 300:
                   response = requests.get(
                       URL_SALVATAGGIO_UTENTI + "?ID=" + str(
                           id) + "&USERNAME=" + str(username) + "&TARGET=" + str(target))
                   print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(
                       target) + "\nmedia: " + str(mediacount) + "\nis_private" + str(
                       is_private) + "\nfollowers:" + str(
                       followers) + "\nfollowee:" + str(followees))
                   print(response.content)




L = instaloader.Instaloader()
posts = L.get_hashtag_posts(hastag)

index = 0

for post in posts:

    thread1 = myThread(post)
    thread1.start()

    index = index + 1
    print(index)

    sleep(1)


