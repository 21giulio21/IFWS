
import requests
import re

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

def ottengoIdDalUsername(pathFile):
    # Ottengo la lista delle persone che sono seguite dal nome dato in input
    with open(pathFile) as f:
        for line in f:
            getPage(line)#li mando al server mio cosi posso poi vederli piu avanti


if __name__ == "__main__":
    ottengoIdDalUsername('instagram.txt')