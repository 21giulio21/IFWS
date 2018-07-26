import instaloader
import requests


hastag = 'unige'

def saveUserAndIdIntoDatabase(id,username):
    response = requests.get("http://2.230.243.113/instagram/saveUserIntoDatabaseUSER_TO_FOLLOW_HASTAG.php?ID="+str(id)+"&USERNAME="+str(username)+"&TARGET=HASTAG"+hastag)
    print(response.content)

def geuUsernameFromId(id):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_id(L.context, int(id))
    print("username: " + profile.username + " id " + str(id))
    saveUserAndIdIntoDatabase(id, str(profile.username))

with open("username.txt", "r") as ins:

    for line in ins:
        geuUsernameFromId(line)
