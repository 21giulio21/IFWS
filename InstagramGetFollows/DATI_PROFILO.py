'''
Questo file permette di salvare sul DB di utendidaseguire.eu una tabella del tipo:
ID ID_PROFILO USERNAME URL_IMMAGINE FOLLOWERS FOLLOWEE POST
'''
import json
import sys
import time

import instaloader
import requests
import schedule

from InstagramAPI import scrivoColoratoSuFile

FILE_NAME = "DATI_PROFILO.html"


def getProfileData(USERNAME):

    profile_data = {}

    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context,USERNAME)
        profile_data["ID_INSTAGRAM"] = profile.userid
        profile_data["FOLLOWERS"] = profile.followers
        profile_data["FOLLOWEE"] = profile.followees
        profile_data["POST_NUMBER"] = profile.mediacount
        profile_data["URL"] = profile.profile_pic_url



        messaggio = "Dati di: " + str(USERNAME) + ": "+str(profile_data)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

        return profile_data

    except instaloader.exceptions.ProfileNotExistsException:

        messaggio = "Impossibile ottenere l' ID Instagram di: " + str(USERNAME)
        scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

def uploadDataIntoDb(USERNAME,ID_INSTAGRAM,FOLLOWERS,FOLLOWEE,POST_NUMBER,URL):
    url = "http://utentidaseguire.eu/instatrack/DATI_PROFILO/insertDatiProfilo.php?USERNAME="+str(USERNAME)+"&ID_INSTAGRAM="+str(ID_INSTAGRAM)+"&FOLLOWERS="+str(FOLLOWERS)+"&FOLLOWEE="+str(FOLLOWEE)+"&POST_NUMBER="+str(POST_NUMBER)+"&URL="+str(URL)
    risposta = requests.get(url).content
    print(risposta)

def coreFunction(username):
    dati_profilo = getProfileData(username)

    URL = dati_profilo["URL"]
    ID_INSTAGRAM = dati_profilo["ID_INSTAGRAM"]
    FOLLOWERS = dati_profilo["FOLLOWERS"]
    FOLLOWEE = dati_profilo["FOLLOWEE"]
    POST_NUMBER = dati_profilo["POST_NUMBER"]
    uploadDataIntoDb(username, ID_INSTAGRAM, FOLLOWERS, FOLLOWEE, POST_NUMBER, URL)

username = sys.argv[1]
coreFunction(username)


