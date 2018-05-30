
import requests
import re

#Funzione da non chiamare dal main, permette di andare a prendere la pagina instagram collegata al nome passato come parametro
#e prende l'id della persona
def getPage(nome):

	cookies = {
    'csrftoken': 'gbFYDDECFb7zkLbMN5yTR2iF6nMgTtJQ',
    'ds_user_id': '819693525',
    'sessionid': 'IGSC13fd980dbdaf73c3dcefac967306c70084186884457fcdc0be8b0d8ff6a3e8aa%3AxF8ille8sA0B6MAZjlulegBXh4EofoDo%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3AiJhOivcaW4oXkkZI2Jix32dA9WhLLqXL%3A20df30023ab984daf85ae50e4916278986eccdeec0870a6a87161f3dbc4d58bc%22%2C%22last_refreshed%22%3A1526631731.6816165447%7D',
    'mid': 'Wv6NMwAEAAHR532pOD8RTWGf_4Hu',
    'rur': 'ASH',
    'urlgen': '{\\"time\\": 1527689685\\054 \\"193.55.113.198\\": 2200}:1fO1sF:Kt6BrsJcRWAF6BPhlthUoM3p9hg',
	}

   	headers = 
   	{
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'www.instagram.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
   	}

	response = requests.get('https://www.instagram.com/'+ nome +'/', headers=headers, cookies=cookies)

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
    ottengoIdDalUsername('instagram_fisso_mio.txt')
