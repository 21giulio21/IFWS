
import instaloader
import requests
import sys
from time import sleep
import random
import threading
import time

# Questo file permette di inserire nel database tutti i profili che rispettano queste condizioni
#
#
#


class myThread (threading.Thread):
   def __init__(self, follower):
      threading.Thread.__init__(self)
      self.follower = follower

   def run(self):
        self.function_thread()


   def function_thread(self):
       follower = self.follower

       id = follower.userid
       username = follower.username
       response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET="+str(target))
       print("Inserisco l'utente: " + str(username) + " in altridatabase con Target " + str(target))
       print(response.content)



#Permette di scrivere i log su un file di testo
def myPrint(text):
    print(text)
    #with open("LOG/logSaveUsersToFollowIntoDatabase.txt", "a") as myfile:
    #   myfile.write(text + "\n")

# Get instance
L = instaloader.Instaloader()

username = str(sys.argv[1])
password = str(sys.argv[2])
target = str(sys.argv[3])
ustenti_da_cui_prendere_followers = str(sys.argv[4]).split(',')



print("Prendo followers fa questi username")
for i in ustenti_da_cui_prendere_followers:
    print(i)

print("Inizio lo script con username: " + username +" password " + password+ " target: " + target+ " utenti da cui prendere followers: " + str(ustenti_da_cui_prendere_followers)  )
L.login(user=username,passwd=password)
i = 0
followers_totali = 0
media = 0
for user in ustenti_da_cui_prendere_followers:
    profile = instaloader.Profile.from_username(L.context, user)
    followers = profile.followers
    myPrint("Followers totali del profilo " + str(user) + ": " + str(followers))
    followers_totali += followers
myPrint("Followers totali dei profili: "+ str(followers_totali))

random.shuffle(ustenti_da_cui_prendere_followers)


for user in ustenti_da_cui_prendere_followers:
    profile = instaloader.Profile.from_username(L.context, user)
    # Print list of followers
    for follower in profile.get_followers():
        i += 1
        print(i)
        # Create new threads
        thread1 = myThread(follower)
        thread1.start()

        sleep(1)


