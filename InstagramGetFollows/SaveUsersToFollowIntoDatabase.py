import instaloader
import requests
from time import sleep

import time


#Permette di scrivere i log su un file di testo
def myPrint(text):
    print(text)
    #with open("LOG/logSaveUsersToFollowIntoDatabase.txt", "a") as myfile:
    #   myfile.write(text + "\n")


# Get instance
L = instaloader.Instaloader()

target = "NATURE"
Users = ['hanwagofficial', 'slow_food_italia', 'visit_lazio', 'slowfood_international', 'vibramfivefingers',
          'gregorypacks', 'yourabruzzo', 'vaudesport']


# Login or load session
L.login('magic_host', '21giulio21')  # (login)

i = 0
followers_totali = 0
media = 0
for user in Users:
    profile = instaloader.Profile.from_username(L.context, user)
    followers = profile.followers
    myPrint("Followers totali del profilo " + str(user) + ": " + str(followers))
    followers_totali += followers
myPrint("Followers totali dei profili: "+ str(followers_totali))



for user in Users:
    profile = instaloader.Profile.from_username(L.context, user)
    # Print list of followers
    for follower in profile.get_followers():
        followers = follower.followers
        followees = follower.followees
        mediacount = follower.mediacount
        is_private = follower.is_private

        response = requests.get(
            "http://getfollowersoninstagram.altervista.org/saveUserIntoDatabaseUSER_TO_FOLLOW.php?ID=%s&USERNAME=%s&TARGET=%s&TYPE=%s&FOLLOWER=%s&FOLLOWEE=%s&MEDIA=%s&PRIVATE=%d" % (
            str(follower.userid), str(follower.username), target, '', followers, followees, mediacount,
            int(is_private)))

        i += 1
        myPrint(str(i) + ") Salvo il followers :" + str(follower.username) +" dell'utente " + str(user) )
        sleep(1)

    myPrint("Finito l'utente " + str(user))

