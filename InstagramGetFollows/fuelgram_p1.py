#QUesta funzione permette di ottenere il valore di GET_LIKE presente nella tabell REGISTRED_USERS
#Il valore di GET_LIKE e' il numero di round che quel profilo deve subire,
#Ad esempio se e' 2 quel profilo deve ricedere 2 giri di round di like
import json

import requests


def getGET_LIKE(username):
    url = "http://www.giuliovittoria.it/instatrack/LIKE_FUELGRAM/getGET_LIKE_From_DB.php?USERNAME=" + str(username)
    response = requests.get(url).content
    return json.loads(response)


#QUesto e' il valore del numero dei round da far mettere like a questo username
get_like = int(getGET_LIKE("InstatracK.eu")[0]["GET_LIKE"])
print(get_like)
