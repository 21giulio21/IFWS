import requests
import json


def get_lista_immagini(username):
#Restituisce la lista delle foto caricate su instagram dall'utente (username)
#Per usarla bisogna aver effettuato il login
 url_image='https://www.instagram.com/p/%s/'
 s=requests.Session()
 t=s.get('https://www.instagram.com/%s/?__a=1'%username)
 j=json.loads(t.text)
 listaImmagini=[]
 data=list(j['graphql']['user']['edge_owner_to_timeline_media']['edges'])
 for d in data:
  listaImmagini.append(url_image % (d['node']['shortcode']))
 return listaImmagini