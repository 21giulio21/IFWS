'''
Questo main permette di dare in input un nome ad esempio fedez
e scarico tutti gli id e i nomi delle persone che lo seguono
cosi ho la certezza che sono tutte persone vere e non capitano mai
nomi del tipo: 001 ecc..
'''

import requests
import re
import time
import json
import random


#fedez: 46071423
#fedex: 232257039



def follow(id,username):
    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'cookie': 'shbid=18815; rur=FRC; mid=Wv04-wAEAAHKaoK4SD8Hm37McmMb; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; fbsr_124024574287414=fZhVCJGuAHwRr0uEp_zZlp_hi0v-Ilb9mAChUJiR8Wc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURTS2YwWm00Ty1Hd1JkV09nZlRoR0lIUVg1SXJCcnJwQ2JVUEwxR3ZrWTdKdDNlR3FNU25jc3hmS1E2Q3FXNHVvYWl1M3JYZW9NSlZ6a1VwUEo1dHdodnBodjZ6N3ltTTZFTEN6OGdFdkF2dndrNU5qY1VjQzlZVjNrWUxQbHFnTkEtTTFuN0pmaWVKWWowRXFlU2RyZElreGJETzdIbUdyN01oeEUwQnZjUkhYTVd3Z1ptVFFuLVpNcWd0bnZoOWxHTWVtdjVqNmpKZ0hDbDBRbXlKV0xUTHNpN3p1MzRrb2RVYU00MUkybk5XbjhjeHVuMWpiT1d5dDRIM1planVXZkZpM3FkSnN6MW5GTzdrc1V3SXBQNjZlNkF1b2RJSGhjYkNnaHhDaHptbkE3Q0VLaUx3a3UyWi0ybkRjNjBub0dRbDNwa1hidDFMVWRmX2t6cXJxQyIsImlzc3VlZF9hdCI6MTUyNjU0NTA2NSwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1526544635\\054 \\"193.55.113.196\\": 2200}:1fJE6t:xLekT1cleCnK_R-H8MWYHIxSRik"',
        'x-csrftoken': 'F1cSYjQFyJ13hBayadSHigpivVa7PvTX',
        'x-instagram-ajax': '1b36312e9ac7',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/'+username+'/',
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/friendships/'+id+'/follow/', headers=headers)
    print(response.content)
    if str(response.content).__contains__("Quest"):
        print("Attendo 500 secondi")
        time.sleep(1000)






def unfollow():

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
        'cookie': 'csrftoken=lFhhLQoVs9oV50indCYzEq7IcgqDtWYe; shbid=18815; ds_user_id=819693525; rur=FRC; mid=WvmbbgAEAAGkE8-Iw_fd2dUvCtgG; sessionid=IGSC9796ca437fcfd6d36398ab15e9a206dec873970556b0fe021dc95ff271b319f1%3ATv29t528QoF7ZhOLnfv3eghfYFZwWSRt%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3At78X57JbUvMQlDmPz5isBb5F4xzbvugf%3A20cdd64da7cfe4973813334c7d0de224fab20e6de545dcecd280dc280e6daa35%22%2C%22last_refreshed%22%3A1526307694.726708889%7D; mcd=3; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=0_t2vXeIk8q8fy5LPXxymigkKjiDRJ3NzA3P_RwvM60.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURBZ1NxeElsU205a05RX2kwU04wUEZEaTJENEFnZkF2ZzBpeWd0SEQybC15NVF4Q2lIcVY5ZVJsN3IwbFdkRGUzclZyWDA2TmJNMlE1M2NpMGdfNTU2ZV9mMEhFZXhzdENaT2Jxd29BZ256OEVzU3lBV2Nsb2NyR0c4ODRmeWF6b21oVF9WUXhRTWstOE9VQlhKc2hUT2ZJOW4zeHd0OEgzUy1acnlmTHZsbHVlaUVRSmI0Y0xHUERrbTYya01xdlNmcC1vdnRjLU4xbmNseEVOMVZmb1AycXh1SE9wbWgtUWF2SkZGMXhCVXl2OFE3S0N5TzN3X3IwcnNJQkw3MFc5OGZERVk4b0pzb0lDaUZfRFFEblBDQ3ZQd3pVUXZ1ZlNpYXJGOG1NNzBDV3Y4TFhSVjI0c1l1RG9XUVhpQW4wN0x0Uy04eGFNQ2Z1WjBxcVhlQWhZZSIsImlzc3VlZF9hdCI6MTUyNjMwODMyNiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; shbts=1526308327.404692; urlgen="{\\"time\\": 1526307694\\054 \\"193.55.113.196\\": 2200}:1fIEWF:VLTfQwtdAehiKHQaTUTc3rPUepA"',
        'x-csrftoken': 'lFhhLQoVs9oV50indCYzEq7IcgqDtWYe',
        'x-instagram-ajax': '0fa00dc2cc1f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/fedez/',
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/friendships/232257039/unfollow/', headers=headers)

#Funzione da non chiamare dal main, permette di andare a prendere la pagina instagram collegata al nome passato come parametro
#e prende l'id della persona
def getPage(nome):

    headers = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cache-control': 'max-age=0',
        'authority': 'www.instagram.com',
        'cookie': 'csrftoken=lFhhLQoVs9oV50indCYzEq7IcgqDtWYe; shbid=18815; ds_user_id=819693525; rur=FRC; mid=WvmbbgAEAAGkE8-Iw_fd2dUvCtgG; sessionid=IGSC9796ca437fcfd6d36398ab15e9a206dec873970556b0fe021dc95ff271b319f1%3ATv29t528QoF7ZhOLnfv3eghfYFZwWSRt%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3At78X57JbUvMQlDmPz5isBb5F4xzbvugf%3A20cdd64da7cfe4973813334c7d0de224fab20e6de545dcecd280dc280e6daa35%22%2C%22last_refreshed%22%3A1526307694.726708889%7D; mcd=3; fbm_124024574287414=base_domain=.instagram.com; shbts=1526309029.9915464; urlgen="{\\"time\\": 1526307694\\054 \\"193.55.113.196\\": 2200}:1fIEhZ:wKyKCP7ixpKxu_NZuUehI5oKGrI"; fbsr_124024574287414=ayQ08rt4SJMP25TFBfzXeesi14AvXSZ3yBlt0hKKlUw.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUIxLUw1VGptaFFFV0VYb2E3ejdrZFlpR1Nfai1KWjJsODZQN0JlV3djV3VUUVlONWdQQUtZbEVQNmV2UmZFNFBGZnRrZ0FLaHBoTTV6Tm1BLUlic0h6aGZNTmZKZVU4dkVwTVV5UHpXUWl0UUpsazMzeXVtSExZTHd4NG9VVlp1RWs2S2htQWRid3EwRGVVb3JqTVZvV0FycTgwaHpaODFLR1dDZmhGTW1RZUFIdFRXdHdWbER1ZDVOS1o3MTRIRkJjYUFIaE5iSUJMQW5uY1ZCZFVHUm1kSzhiMndOMTVVRlQ3SGhiNWdnUDBSMEE3ODk2U2FyaV85d0N3NTJvR0FxT3BXN0RSUDFKbXNhamFXN2lTZmZFSTVVRDhFVFFuY01WUTlRUnZoa2t5dUJYa0llWHYtWkQtUHE1VmZhZmkyaFptbDN2Mk1PakNvYXZ1ZnkwRHdkMSIsImlzc3VlZF9hdCI6MTUyNjMwOTUyNiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ',
    }

    response = requests.get('https://www.instagram.com/'+ nome +'/', headers=headers)
    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup
    html =  response.content
    parsed_html = BeautifulSoup(html)
    testo =  parsed_html.body.find('script', attrs={'type': 'text/javascript'}).text
    indiceInizio = testo.find("profilePage_") + "profilePage_".__len__()
    indiceFine = testo[indiceInizio:].find("\"")
    id = testo[indiceInizio:indiceInizio+indiceFine]
    if id.isnumeric():
        print(id + " " + nome)
        requests.get('http://2.230.243.113/foulo.php?id='+id+'&username='+ nome)


def ottengoIdDalUsername():
    # Ottengo la lista delle persone che sono seguite dal nome dato in input
    with open("namefile.txt") as f:
        for line in f:
            #time.sleep(3 + random.randint(2,6) )
            if line.__contains__("Immagine"):
                nome = re.findall(r'\S+', line)[4]
                getPage(nome)#li mando al server mio cosi posso poi vederli piu avanti

def ottengoDatiDalServerMio():
    return json.loads(requests.get("http://2.230.243.113/getFoulo.php").content)



if __name__ == "__main__":
    #ottengoIdDalUsername()
    data = ottengoDatiDalServerMio()
    numero_dati = len(data)
    indice = 0
    for i in range(2000,numero_dati):
        print(i)
        indice = indice +1
        #Dopo 20 secondi mi fermo per 20 secondi
        if indice % 4 == 0:
            time.sleep(20)

        id = data[i]["ID"]
        username = data[i]["USERNAME"]
        follow(id,username)
        time.sleep(15 +  random.randint(3,6))
