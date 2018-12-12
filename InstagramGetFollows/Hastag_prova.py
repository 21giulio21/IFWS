import sys
import threading
from time import sleep
import random
import  instaloader
import requests

target      =   "MILANO"#str(sys.argv[1])
hastag      =   "milano"#str(sys.argv[2]) #"pugilato"


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

       id = self.post.owner_id

       #id = self.post.owner_profile.userid
       #Controllo se quell'id e' gia presente nel database relativo a quel target
       #Se torna vero, torna indietro perche ho gia inserito quell'utente
       if controlloSeNelDBHoGiaUnUtenteConQuelIDETarget(id, target) == True:
           return


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

           print("Inserisco l'utente")




L = instaloader.Instaloader()
post_sporchi = L.get_hashtag_posts(hastag)

posts = []

#print("Post totali: " + str(len(post_sporchi)))

index = 0

#Prendo tutti i post del 2018
for post in post_sporchi:

    index = index + 1

    print("Processo il post - " +str(index)  )
    if str(post.date.year) == "2018":
        posts.append(post)

print("Post da processare totali nel 2018: " + str(len(posts)))

#mischio i post:
posts = random.shuffle(posts)


for post in posts:

    thread1 = myThread(post)
    thread1.start()

    sleep(0.8)


