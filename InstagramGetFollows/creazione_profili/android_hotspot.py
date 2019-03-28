#In questo file posso accendere/spegnere l'hotspot dell telefono
#comando 1: adb shell am start -n com.android.settings/.TetherSettings
#comando2: adb shell input tap 200 250
#comando3: adb shell input tap 200 250
import os
import time
import requests
import urllib


def sono_connesso():
    try:
        url = "https://www.google.com"
        requests.get(url)
        status = "Connected"
    except:
        status = "Not connected"
    return status
def acceddoConnessioneBloothod():
    time.sleep(1)
    os.system("adb shell input tap 200 600")
    time.sleep(1)
    os.system("adb shell input tap 200 300")
    time.sleep(1)
    os.system("adb shell input tap 200 1100")
    time.sleep(3)
    os.system("adb shell input tap 100 100")

def acceddoConnessioneWIFI():
    time.sleep(1)
    os.system("adb shell input tap 900 300")
    time.sleep(1)

def spengoConnessioneWIFI():
    time.sleep(1)
    os.system("adb shell input tap 900 300")
    time.sleep(1)


def insertUserGET_LIKE_intoDatabase(username):
    url = "http://utentidaseguire.eu/instatrack/FUELGRAM_LIKE/insert_user_GET_LIKE_into_database.php?USERNAME=" + str(
            username)
    return requests.get(url).content

def creazioneProfiloInstagram(email,username):




    headers = {
        'cookie': 'ig_cb=1; mid=XAA98gALAAEsMBVLUBqkv5uh7wcw; mcd=3; fbm_124024574287414=base_domain=.instagram.com; datr=mnh6XImQGHX_ZwtCOpydL9pN; shbid=15567; shbts=1551997510.79551; csrftoken=Cwi36GSDU5yb4hs2h1bgI7YvPo6nfjea; fbsr_124024574287414=ScuZqPcHDOfeGir_YiEDDhNPuiY39ruLYjmZn1XItRg.eyJjb2RlIjoiQVFBVkljeE9GNFYxU0E1bVh3THUtR0Y4eFkwWElIbDFWWU1WcVBtbzM3LXVfQnNDalUxWkxtU3RIb3JBUWQ4SXZjcUQxWG1wb1BVYUZLeWRSTkszUldhV2w0aHhBOFd3d1Frb0JSM0hfaklhR0lhSWgzMFNoUnV1bnpTLXR3RTlwbXZBNjlERURBLXdQUWVuZ1pLaUlKVkkwWThhdTJXY3hjc2RNVmpaaDVHeTJYOWVMckhyekFBd0dtYTdUcXUzRUZFdUUtczZudFluN01GZFY2ZEtEbzIydUdnek1zTnMwNjhpMnFKb0tYNEVHNUhnWG1aUnNyb3lEQlB6Zm1NRWJ4bERfeEExTnpfZHVJQm01d1Q4Skcya3U3WUdRRVhVV0FTWUg2Y1RQRG9rNWRZNTZVUkNjYkxvd0ZrLWlnNnFFS25ZZHduS3FiSWlnMmtmd2F3OWszNnUiLCJ1c2VyX2lkIjoiMTAwMDExMDAwODUxNjg5IiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1NTIwNTU4NjJ9; rur=FTW; urlgen="{\\"80.84.97.22\\": 12428\\054 \\"91.253.189.164\\": 24608}:1h2Gf5:UmCsy0VHcZJRMHONQ90YMzbxH_o"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'Cwi36GSDU5yb4hs2h1bgI7YvPo6nfjea',
        'x-ig-app-id': '936619743392459',
        'x-instagram-ajax': '6fd3989c69a9',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'authority': 'www.instagram.com',
    }


    data = {
        'email': email ,
        'password': '21giulio21',
        'username': username,
        'first_name': 'ariana_rilanini21345',
        'client_id': 'XAA98gALAAEsMBVLUBqkv5uh7wcw',
        'seamless_login_enabled': '1',
        'gdpr_s': '[0,2,0,null]',
        'tos_version': 'eu',
        'opt_into_one_tap': 'false'
    }

    #insertUserGET_LIKE_intoDatabase(username)
    response = requests.post('https://www.instagram.com/accounts/web_create_ajax/', headers=headers, data=data)
    print(response.content)

import time

import pynput
from pynput.mouse import Button

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def click(x,y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    time.sleep(0.5)
    mouse.release(Button.left)


def spengoAccendoWifi():
    click(981, 640)
    time.sleep(5)
    click(981, 640)




for i in range(55,100):
    print("Imposto la modalita aereo")
    # qui devo mettere il telefono in modalita' aereo
    os.system("adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    time.sleep(1)
    os.system("adb shell input tap 200 250")


    time.sleep(15)
    print("Tolgo la modalita aereo")

    #ora aspetto un po di tempo prima di togliere la modalita' aereo
    os.system("adb shell input tap 200 250")

    time.sleep(10)


    print("Accendo l'hotspot del telefono ")
    os.system("adb shell am start -n com.android.settings/.TetherSettings")
    time.sleep(3)

    ##Accendo il thetering USB
    #print("Attendo Thetering USB")
    #os.system("adb shell input tap 200 850")

    ##Accendo il thetering Bloothod
    #print("Attendo Thetering USB")
    #acceddoConnessioneBloothod()

    print("Attendo Thetering WIFI")
    acceddoConnessioneWIFI()
    time.sleep(10)

    print("Attendo Spengo/Riaccendo il wifi del PC")
    spengoAccendoWifi()
    time.sleep(10)




    print("Attendo che il PC si connetta al wifi del telefono")

    while sono_connesso()!= "Connected":
        print("Attendo altri 5 secondi")
        time.sleep(5)

    #accendo il wifi del mac
    print("Accendo il wifi del mac")
    time.sleep(15)

    ## qui devo creare il profilo con il pc

    username = "vincenzo_ernesto_aliberti_A" + str(i)
    email = "v" +str(i)+"@instatrack.eu"
    print("Creao il profilo " , username,email)
    time.sleep(3)
    creazioneProfiloInstagram(email,username )

    spengoConnessioneWIFI()
    time.sleep(2)




