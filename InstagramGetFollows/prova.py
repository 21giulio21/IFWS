import time

import requests
from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE

connection = CONNECTION_UTENTI_DA_SEGUIRE()
PROXY_DICTIONARY = connection.getProxiesFromDB()

while PROXY_DICTIONARY.__contains__("error"):

    PROXY_DICTIONARY = connection.getProxiesFromDB()
    print("Attendo il proxy")
    time.sleep(10)



proxy  = PROXY_DICTIONARY["PROXY"]
port = PROXY_DICTIONARY["PORT"]
username_proxy = PROXY_DICTIONARY["USERNAME"]
password_proxy = PROXY_DICTIONARY["PASSWORD"]


168.81.22.148
proxies = { "http": "http://"+username_proxy+":"+password_proxy+"@"+proxy+":" + port,
            "https": "https://"+username_proxy+":"+password_proxy+"@"+proxy+":" + port,
        }

r = requests.get('http://httpbin.org/ip', proxies=proxies)
print(proxy, r.content)
connection.updateLAST_ROUNDFromDbPROXY(proxy)


