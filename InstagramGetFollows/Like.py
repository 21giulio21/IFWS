import json
import random
import time

import requests

def ottengoIdPrimaFotoDaUsername(username):

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; shbid=14394; rur=PRN; mid=WwWZlQAEAAG_zXJpoNK1kd3gNgBY; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=jCMA3LcYOYgH0CKycMKs7kPBvhU86lRi0J7kKEUjBow.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURhRUpMWlBPQ1hCbVlqU2hJSE4xbENDR2VkbkZzT3VvRnZXaGxxUGxoRlh5TWQ5RnE5S19US0dNd25DLVVodGpSSEVGS1diNERNbVlfMG5WUjdZSkVlYjZ2Q3F4Z1pxd0RKNnNTbEs0MXhuWUhncklBNXVGS3lkMkZaRFJCMUswaGNQbmRscjhpMk92OE1fTjQwYmZ1ZEhBSEdTQURqb2N3eWFZUnNIOGhhV1N1QUhTYTVVeE5RcXBwZUFBeGJBWWdJUk00aFRYVUZtVDU1dzFqV3haNVZVTGVra25vZXFpTlpHWGEwblRrdjVFMVVEZERaNnhVTVRCODVwMW5DbEFwenFIZGJtS3lDN190NVpTdWV2eVdWUFFDT0JJMkxxZ2hYTGVCRnBfTUpidVpEZ29Fb0g0LW9maTVyNXRJX0dMV01TOGhSN2ZxcTIzZXVjUHVFdXdyVSIsImlzc3VlZF9hdCI6MTUyNzA5Mzk3MiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1527093653\\054 \\"91.253.85.98\\": 24608}:1fLWw5:CeahbLDKdr-qr7LIG_H6YV30jcg"',
    }

    response = str(requests.get('https://www.instagram.com/' + username + "/", headers=headers).content)
    posizione__typename = response.find("GraphImage")
    print(posizione__typename)
    stringa = response[posizione__typename + len("GraphImage") + 8  : posizione__typename + 100]
    posizione_id_foto = stringa.find("\"")

    return stringa[:posizione_id_foto]

def richiestaLike(username):

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
        'cookie': 'csrftoken=F1cSYjQFyJ13hBayadSHigpivVa7PvTX; ds_user_id=7752426221; sessionid=7752426221%3ALsQDV4YGLx4UYf%3A0; shbid=14394; rur=PRN; mid=WwWZlQAEAAG_zXJpoNK1kd3gNgBY; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=QspyVatIznnxGexjlFvxIcbyD5eC21K2YpvPkrhkIww.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUF1am0wWVNPM3IyYmt6dmE5WTBDT2F0a1NLb2hQYmRMYVFmNGdDSWd0ODJrekdmaVZGYUdlVXNkNTdoZXM4cWsyQlp4YjdYVTI2OFJoaXd5OTU1NEFrVzZkbzJ3MWVYdWw0QUlQQ1htOGp5OUdEQWhLcWNnZzlXQU9kQXZZR3o4QVhIck1jN0Z1aDhRcEwtemZtS1hYclIwOUlMelRYWkN5MVpZbVVDTUxCblB0YjJnODZmdmdyYUNTbjAwdEZzdEo2clEtN2RrSUpqWlpSZHZzRFByUWMyY1Y2LWRwZ3k1Y0o5V3hIZ2ptazU4dWNhNEk1anNKSGVKRDU2ZDI5YzdsT1UydzYxOGNrT1pnRVZNZkdROTlEWGN1akxWNjJ6S3VnWU5CRkc3cVJlU0RlVmNhMW1FSXd2ZlJvRzNLdzVUbnZGeG5hX0RpazEwQlBqdGZ6RGtJUiIsImlzc3VlZF9hdCI6MTUyNzA5Mzc0NiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; shbts=1527093914.6859105; urlgen="{\\"time\\": 1527093653\\054 \\"91.253.85.98\\": 24608}:1fLWt0:3P1PVXKoQrykMcm7zRxyRYVbmaA"',
        'x-csrftoken': 'F1cSYjQFyJ13hBayadSHigpivVa7PvTX',
        'x-instagram-ajax': 'd2dfd728ae44',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BjIEnJAgwYS/?taken-by=' + username,
        'authority': 'www.instagram.com',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/likes/'+ottengoIdPrimaFotoDaUsername(username)+'/like/', headers=headers)
    print(response.content)






def ottengoDatiDalServerMio():
    return json.loads(requests.get("http://2.230.243.113/getFoulo.php").content)


if __name__ == "__main__":
    data = ottengoDatiDalServerMio()
    numero_dati = len(data)
    indice = 0
    for i in range(1000, numero_dati):
        indice = indice + 1
        print("numero della persona a cui ho mandato la richiesta " + str(indice))
        # Dopo 20 secondi mi fermo per 20 secondi
        if indice % 4 == 0:
            time.sleep(20)

        id = data[i]["ID"]
        username = data[i]["USERNAME"]
        print("id persona = " + id + " username= " + username)
        richiestaLike(username)
        time.sleep(10)





