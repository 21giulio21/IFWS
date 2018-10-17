import instaloader
import requests
import sys
from time import sleep

import time


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



for user in ustenti_da_cui_prendere_followers:
    profile = instaloader.Profile.from_username(L.context, user)
    # Print list of followers
    for follower in profile.get_followers():
        username = follower.username
        followers = follower.followers
        followees = follower.followees
        mediacount = follower.mediacount
        viewable_story = follower.has_viewable_story
        is_private = follower.is_private

        #Se l'utente ha piu di 7k di followers non lo prendo neanche
        if int(followers) > 7000:
            print("L'utente: "+username + " ha piu di 7k followers, quindi non lo prendo nel nostro database")
            continue

        if int(followees) > int(followers) and viewable_story == True and int(mediacount) > 3:
            print("Username: " + str(username) + " followers: " + str(followers) + " followees: "+ str(followees) + " viewable_story: "+str(viewable_story) + " mediacount: " + str(mediacount) + " is_private: " + str(is_private))
            response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=%s&USERNAME=%s&TARGET=%s" % (str(follower.userid), str(follower.username), target))
            print("Inserisco in altridatabase con Target " + str(target) + " \n")
            print(response.content)
            myPrint(str(i) + ") Salvo il followers :" + str(follower.username) + " dell'utente " + str(user))

        if int(followees) > 400 and viewable_story == True and int(mediacount) > 3:
            print("Username: " + str(username) + " followers: " + str(followers) + " followees: "+ str(followees) + " viewable_story: "+str(viewable_story) + " mediacount: " + str(mediacount) + " is_private: " + str(is_private))
            response = requests.get("http://altridatabase.altervista.org/saveUserIntoDatabaseUTENTI_DA_SEGUIRE.php?ID=%s&USERNAME=%s&TARGET=%s" % (str(follower.userid), str(follower.username), target))
            print("Inserisco in altridatabase con Target " + str(target) + " \n")
            print(response.content)
            myPrint(str(i) + ") Salvo il followers :" + str(follower.username) + " dell'utente " + str(user))

        print("Processo l'utente :" + str(i))
        i += 1


    myPrint("Finito l'utente " + str(user))

