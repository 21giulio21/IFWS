#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import base64
import datetime

from email.mime.text import MIMEText
from threading import *
import requests
import json
import itertools
import random
import time

from termcolor import colored


import re

from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE

url_bot = "http://www.giuliovittoria.it"
url_sms_mail = "http://www.utentidaseguire.eu"

FILE_NAME = "a.html"

comment_list=[  ["Complimenti","Bravo","Grande"],
                ["!",".","..","...","!","!!","!!!","!!!!"],
                ["Questa ","La tua","La"],
                ["foto", "fotografia", "immagine"],
                [" è veramente ", " è proprio ", " è davvero "," è "," secondo me è"],
                ["pazzesca", "unica", "sensazionale", "bellissima", "magnifica", "indimenticabile","meravigliosa", "straordinaria", "eccezionale", "magica","emozionante"],
                [" "," "," "," "," "," ","❤"," "],
                [".", "..", "...", "!", "!!", "!!!"," "]
                ]

'''

comment_list = [["\n"],
                ["Ciao ❄","Ciao!! ❄","Ciao!!! ❄","Buongiorno ❄","Buongiorno!! ❄","Buongiorno! ❄","Ehy! ❄","Ehy!!! ❄","Ehy!! ❄","Ehy ❄"],
                [" 🔥Aumenta i tuoi seguaci \n"],
                [" ▶️REALI \n"],
                [" ▶️ATTIVI \n "],
                [" ▶️100% IN TARGET"],
                [" 🚀 Collegati al sito per accedere alla PROMOZIONE LANCIO  \n"],
                [" ▶️ www.instatrack.eu"],
                [" Per info"," Per maggiori informazioni"],
                [" contattami in privato! 🎉"]
                ]

'''





# genera un commento a cauthenticated = str(content_request_JSON["authenticated"])aso usando le parole di comment_list
def generate_comment():
        c_list = list(itertools.product(*comment_list))

        repl = [("  ", " "), (" .", "."), (" !", "!")]
        res = " ".join(random.choice(c_list))
        for s, r in repl:
            res = res.replace(s, r)
        return res.capitalize()


def ottengoIdPrimaFotoDaUsername(username, cookies, csrf):
    # Genero random l'ip da cui viene fatto il login, deve esserequalcosa come: 64.1.3559.543
    primoNumero = random.randint(2, 100)
    secondoNumero = random.randint(2, 100)
    terzoNumero = random.randint(2, 100)
    quartoNumero = random.randint(2, 100)
    ip = str(str(primoNumero) + "." + str(secondoNumero) + "." + str(terzoNumero) + "." + str(quartoNumero) + ".")

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookies,

    }

    response = str(requests.get('https://www.instagram.com/' + username + "/", headers=headers).content)
    posizione__typename = response.find("GraphImage")
    stringa = response[posizione__typename + len("GraphImage") + 8  : posizione__typename + 100]
    posizione_id_foto = stringa.find("\"")

    return stringa[:posizione_id_foto]

def richiestaLike(username, cookies, csrf):

    user_agent_1 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'
    user_agent_2 = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36'



    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': 'd2dfd728ae44',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BjIEnJAgwYS/?taken-by=' + username,
        'authority': 'www.instagram.com',
        'content-length': '0',
        'user-agent': user_agent_1,

    }
    return requests.post('https://www.instagram.com/web/likes/'+ottengoIdPrimaFotoDaUsername(username,cookies, csrf) +'/like/', headers=headers)



#Permette di mettere un commento al media_id che gli passo
def comment(cookies, csrf,username_to_comment):
    # Genero random l'ip da cui viene fatto il login, deve esserequalcosa come: 64.1.3559.543
    primoNumero = random.randint(2, 100)
    secondoNumero = random.randint(2, 100)
    terzoNumero = random.randint(2, 100)
    quartoNumero = random.randint(2, 100)
    ip = str(str(primoNumero) + "." + str(secondoNumero) + "." + str(terzoNumero) + "." + str(quartoNumero) + ".")

    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': 'ac942a8a720f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/p/BkkwR3ihMUn/?taken-by=' + str(username_to_comment),
        'authority': 'www.instagram.com',
    }

    data = [
        ('comment_text', generate_comment()),
    ]

    return requests.post('https://www.instagram.com/web/comments/'+ottengoIdPrimaFotoDaUsername(username_to_comment,cookies, csrf)+'/add/', headers=headers, data=data).content




def follow(id, username, cookies, csrf,username_che_deve_fare_richiesta):

    connection = CONNECTION_UTENTI_DA_SEGUIRE()
    PROXY_DICTIONARY = connection.getProxiesFromDB(username_che_deve_fare_richiesta)
    print(username_che_deve_fare_richiesta , PROXY_DICTIONARY)



    #while PROXY_DICTIONARY.__contains__("error"):
    #    PROXY_DICTIONARY = connection.getProxiesFromDB()
    #    print("Attendo il proxy")
    #    time.sleep(10)



    proxy = PROXY_DICTIONARY["PROXY"]
    port = PROXY_DICTIONARY["PORT"]
    username_proxy = PROXY_DICTIONARY["USERNAME"]
    password_proxy = PROXY_DICTIONARY["PASSWORD"]

    # aggiorno l'ultimo utilizzo del proxy, cosi quel proxy potrà stare fermo per 60 secondi prima di fare una nuova richiesta
    connection.updateLAST_ROUNDFromDbPROXY(proxy)

    proxies = {"http": "http://" + username_proxy + ":" + password_proxy + "@" + proxy + ":" + port,
               "https": "https://" + username_proxy + ":" + password_proxy + "@" + proxy + ":" + port}

    headers = {
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': csrf,
        'x-instagram-ajax': '0fa00dc2cc1f',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/' + username,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        # 'user-agent':'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
    }

    return requests.post('https://www.instagram.com/web/friendships/' + str(id) + '/follow/', headers=headers,proxies=proxies,verify=False)





def follow_thread(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict,username,number_requests_done,tempo_blocco_se_esce_errore,delta_t,target,email):
    # Seguo la persona che ho scaricato e gli metto un like alla prima foto
    contet_request = follow(id_user_to_follow, username_user_to_follow, cookies_str, cookies_dict['csrftoken'],username)

    # In questo punto aumento la variabile:  number_requests_done di 1 e mando al server il nuovo valore di number_requests_done
    updateNumberRequestsDone(username, str(int(number_requests_done) + 1))

    print( str(username) + " FOLLOW :  " + username_user_to_follow + " " + str(
        contet_request.content) + " TARGET DELL?UTENTE CHE SEGUO: " + target)

    parse_content_request(contet_request, 'FOLLOW-UNFOLLOW', username, tempo_blocco_se_esce_errore, delta_t,
                          email)


def unfollow_thread(username_user_to_unfollow,cookies_str,cookies_dict,username,tempo_blocco_se_esce_errore,delta_t,email,users_followed_string):

    # chiedo al mio database di utenti li della persona con quell username
    try:
        id_to_unfollow = int(getIdFromUsernameToUnfollow(username_user_to_unfollow))
        id_to_unfollow = str(id_to_unfollow)

    #nel caso in cui non ci sia lo chiedo ad Instagram
    except:
        id_to_unfollow = getIDFromUsername(username_user_to_unfollow)




    content_request = unfollow(id_to_unfollow, username_user_to_unfollow, cookies_str, cookies_dict['csrftoken'])

    print("\n" + username + " UNFOLLOW " + username_user_to_unfollow + " id: " + str(id_to_unfollow) + " " + str(
        content_request.content) + "\n")

    parse_content_request(content_request, "FOLLOW-UNFOLLOW", username, tempo_blocco_se_esce_errore, delta_t, email)

    # Aggiorno il database, aggiorno ad ora il valore secondi_ultima_richiesta dell'utente che ha appena fatto la richiesta di follo
    update_secondi_ultima_richiesta(username, int(time.time()))
    updateUserFollowed(users_followed_string, username)




def unfollow(id,username, cookies, csrf):



    headers = {
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookies,
        'x-csrftoken': csrf,
        'x-instagram-ajax': '0fa00dc2cc1f',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/'+username+'/',
        'authority': 'www.instagram.com',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',

    }

    return requests.post('https://www.instagram.com/web/friendships/'+id+'/unfollow/', headers=headers)



def login(username,password):
    headers = {
        'cookie': 'ig_cb=1; mid=W1nvMQAEAAFu2gGrVLf9bSIPaRj0; mcd=3; fbm_124024574287414=base_domain=.instagram.com; shbid=18815; rur=FRC; csrftoken=8PTQJQ7SinBSjbsmVnBExspM0dwYyNZ8; fbsr_124024574287414=8YD7u-K_rHKaSPA5xcY6uah59VJCd41My7qDi7TU_Hc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURTdTZuVG0zbVl2YXhPd2UwWXdnQ2JUVlZsM3VRTEltRzNmelk5cll6MlZEemhWQW1DejJONFpjUjN1NURKNjNSUndjSlBPU282dF9sNHlfN3U1eHE4TDNoMGFXUTNrUDc4YkFHM1JleFBSbjhoMzhXRFBpbjhBLWRYaTBtcER6MHJ1TE1LaUdsMUgzcmlDd2ZkV1UtTnMwX2Zld2VGelFBQXQyNnFMRGhMZTgtRnJfTVhIWXFGSFFrUnVJTmhZdGx2Tl9Gc254el9MOVlibWgwVTNJRllOYnM5VUFPaU9JdndPTWhwalR0Zm13NG5fRmduYlZ3VGV0TXpSbG9OdlZ1cGxZbGxDNGw4a3dqaDlTYW84dUdtUHJ4YUxQS2YzRjFGdUs5Y2ZzS1pkSFNOdE91LXdaaWVrWDl5M1Q0QkVITnpnZTNydzR2MllCTGNvRDFiNDBmRSIsImlzc3VlZF9hdCI6MTUzMjYyMDkxMCwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"91.252.132.111\\": 24608}:1hFm9x:xXRK6tvx7abPLhH_DxEQM3qfCyk"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '8PTQJQ7SinBSjbsmVnBExspM0dwYyNZ8',
        'pragma': 'no-cache',
        'x-instagram-ajax': 'f122ed33a26e',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
    }

    headers = {
        'cookie': 'ig_cb=1; mid=XKcLgQALAAFi390A3XpZPlfxaYIO; fbm_124024574287414=base_domain=.instagram.com; rur=FTW; shbid=18440; shbts=1554566136.2682383; csrftoken=SkGmpBuaSoi1YkBUs5CV88w8nUaUVqFr; urlgen="{\\"2.230.243.113\\": 12874\\054 \\"2001:b07:ac9:e9a2:e064:2a41:a68:f828\\": 12874\\054 \\"2001:b07:ac9:e9a2:a14b:a396:7b26:6a87\\": 12874}:1hDsck:QBJcmaRQ_fPwOJBbvByZeAO_YWY"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'SkGmpBuaSoi1YkBUs5CV88w8nUaUVqFr',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '712a6ca2c530',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; mid=XLSKXwALAAHH15QVw2n73vyLL0aI; fbm_124024574287414=base_domain=.instagram.com; shbid=18593; shbts=1555335788.3042486; rur=FTW; csrftoken=pIN059vKjUIiXN63sviXIsNjlpdGTEYu; fbsr_124024574287414=LCcumNG1OcgFdwtZOtrpcQhIRRUkBbM8RsA9zIuIDkY.eyJjb2RlIjoiQVFDVm9jaElaLTJtdGliUDVGTF9kYVZBUUxKdWxDVUhVeGNnTTV0UjhrUDl3T3NCZTRvZ3h1YVRyMFZZVkpyQlBKb3Bxc2xCTDZjQy1KRUEtSVg4QUFMc1g3Skk3T2V1dXc5M19kSDNtdTJkYlZaTGJodTUwZHJWNFZ2ZlVQVnpNQnFWV2hVM0tWZlJqeHRXRHlqZ2tIMzFsUXVhSV9lWW5iVThZblNmcGhTQ2syMnV2R19kNEwza2tXcElIU1BMYlVieFQ0MWoxMmZsUzBWRTVmeGVWYVJkZ2Y3ZVhWU0pDWWR6MlkzanRiSkhDdUhNaG9HM2ZHbFVzdnE5dExubGl1Qmw0WjQ2Mmd6WHZ5d0dKWmdhQlF3dFI2UExrWnB3dW9ZTXliUkRpYUNHYjNseVJkYkR1VFdKTkVVUjNxRmIwQ2JCOVZ0SjBDVzJKVVdnRld0SUswWjMiLCJ1c2VyX2lkIjoiMTE1NDAyMTE2MyIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTU1NDA3NTk2fQ; urlgen="{\\"2.230.243.113\\": 12874\\054 \\"91.253.26.123\\": 24608}:1hGKZP:fd6cCsvbet3OobUEBTy7Z7cfV68"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'pIN059vKjUIiXN63sviXIsNjlpdGTEYu',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; mid=XLSKXwALAAHH15QVw2n73vyLL0aI; fbm_124024574287414=base_domain=.instagram.com; shbid=18593; shbts=1555335788.3042486; rur=FTW; csrftoken=AUXlCWDsoXXPkGjslbZ32Ken7UPZJ4jR; fbsr_124024574287414=qCJ_b6DfuAXZymMDw-rult5Krr9Z9TYzxDSXCEl91l0.eyJjb2RlIjoiQVFCczg1Yk1UUkFTb3FOVWhuUlRPcjd5LUJEekpQSEFoOFFaeGNMMXhDRE4wUFpQejhONUV1eElEblZqd2tZeExGd1dxYWwxTG1fMFZUbzhrN1pGcnZXb3h2bHZmWmlYVzZLN3JnQlBNeGZnaUNMMF8yT1NxVXZ3TGlncWhXTlphWWNhNENSbk1VOXJXZGUzUlBhWVRzb3ppUVdlOUR4d1hDX05IYnlnNS1JaWt4VzVld0dkdGFabGl0MEZmeG5VYmpxM3hOOVp0OHNpa0NNS2ZDMkVsOFJqRUZ1TWE5SWpfQzBIUTlfb1dDcGs1M3I1eTNLbHBXbS0zc3BHNjBGX1pNbWJSWG1meFNlNmg1aldmdkxqY0NTTlVDVm1Ha1h1VFdOVHVNRlNQcUNlOFAzZnJIbFJQeVdnSjRNYXRwNEZGUGRLVEVCOFFscG8tamJXLS1QcDZJdHEiLCJ1c2VyX2lkIjoiMTE1NDAyMTE2MyIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTU1NDA4NDA2fQ; urlgen="{\\"2.230.243.113\\": 12874\\054 \\"91.253.26.123\\": 24608}:1hGKmR:1L093jFqFcGQ_92JYup0QTx3GVc"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'AUXlCWDsoXXPkGjslbZ32Ken7UPZJ4jR',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=ATN; csrftoken=aGA5zc78AVGcRNee3yejDFh0XJ0FfRO4; mid=XLWoxwALAAFoi37H6STUCHVPbx4H',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'aGA5zc78AVGcRNee3yejDFh0XJ0FfRO4',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }
    headers = {
        'origin': 'https://www.instagram.com',
        'x-mid': '11egzx1wfrixa1eyed2t17q688xpfbfjeb4jrlpe4hffgo1g8yn',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'jygHxJgBcShZmGCLmXvHEbVeUbMuuae0',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=ATN; csrftoken=c9CUdJdjRxRLPv2hRBVIiWOmRxr0whVk; mid=XLWuMAALAAFUNlqKivLJGuGkmY48',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'c9CUdJdjRxRLPv2hRBVIiWOmRxr0whVk',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=FTW; csrftoken=5oBcwvB3QZwihXr4vN2rgCBbq3JbBhKj; mid=XLWwMAALAAEDcFr-hAFxWWo9Xhi9',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '5oBcwvB3QZwihXr4vN2rgCBbq3JbBhKj',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=FTW; csrftoken=IEOhOWg5HINiL9SSzuFHUL4PAR51ZmUB; mid=XLWz8QALAAGGm38xn_OYpB6JJZXD',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'IEOhOWg5HINiL9SSzuFHUL4PAR51ZmUB',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=ASH; csrftoken=lyGsVowTaIOPpCHWnbfSPB5NgoeAsJcJ; mid=XLXJBQALAAHS98mTsDx4EP4ADZXe',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'lyGsVowTaIOPpCHWnbfSPB5NgoeAsJcJ',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; mid=XLXJBQALAAHS98mTsDx4EP4ADZXe; shbid=12922; shbts=1555417369.139812; rur=FRC; csrftoken=7loh7PlbUWw7qpaoC2se9mrn3O8U2Kz3; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=qxw1aTUPdvMoxGhoGVQtP2vu4w0uCvr4auclmmEtOmw.eyJjb2RlIjoiQVFEaFpMSHFrVnVhU1hySjhZOGhKY0VuX3QyTklrbEVaWGFORmQ3UUFNSDVXcHJpdWNhM19LVHFsRGdZNUZYN0x4WjFUSjVZemFwQk56MG9PLVFZWVlSV0lhRHFtMmVVdTNtZmJ0aHhXVmpQVGowT2kwaUlLYWE2YnprMkNxN0lGM0RoMmVzVFlmOHJrWkRJS3hSU19SVjRtWlVLWE5BVWt2eEtxU0k1V0RsVVk0WmFmYVVGTEJodzdRZUxZZ0VybUtpVDVhZDFBZk4yb0hsd3RYQlNrNDgzZU9iZFc3QlJWc3RvcmVJMVhhbjFkWDVuUlpaSDQxOXgzcE1yM0RYM05GN0ZvUlFsZzRfTHk4VkhPUzJnMllSUGN1UTYzNUdwSTNKaGd6cG9SeHpERUlGVkNYaEduUmNPME5PZEp4WGZGUmpfYWJVXzFtZXd4Q1ZvSzlrVEpPTmEiLCJ1c2VyX2lkIjoiMTE1NDAyMTE2MyIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTU1NDE4NTQzfQ; urlgen="{\\"91.253.33.167\\": 24608}:1hGNPz:yt-9Zx_jGXPpUp0SDGA0lMBJUgI"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '7loh7PlbUWw7qpaoC2se9mrn3O8U2Kz3',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': '645edb4d21a4',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
    }

    headers = {
        'cookie': 'ig_cb=1; rur=FRC; mid=XLclRQALAAHsabdTADUtEMiEe87y; csrftoken=gfyxKRwSXGyMg7RLzaDK7nqoaJMWWW0b',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'gfyxKRwSXGyMg7RLzaDK7nqoaJMWWW0b',
        'x-ig-app-id': '936619743392459',
        'pragma': 'no-cache',
        'x-instagram-ajax': 'fe333ffa075d',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?next=%2F__countess_elizabeth__%2F&source=logged_out_half_sheet',
    }

    data = {
        'username': username,
        'password': password,
        'queryParams': '{"source":"auth_switcher"}',
        'optIntoOneTap': 'false'
    }



    response = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)

    return response

#Questa funzione viene chiamata nel momento in cui un utente appena inserito ha sbagliato la password di instagram
#in particolare pre prima mette PASSWORD_SBAGLIATA a 1 nel database poi merre PROCESSING a 0 cosi lato app se ne accorge
def updatePasswordErrataAndProcessing(username,passwordErrata,email):
    updateSctiptActive(username,0)
    url = url_bot + "/instatrack/updatePasswordErrata.php?username=" + username + "&password_errata=" + str(passwordErrata)
    requests.get(url)
    updateProcessing(username,0)


    #MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
    print("Mando la mail a " + email + " per comunicare che la password Instagram e' errata")
    msg = "Ciao "+str(username)+",\n\nla password del tuo account Instagram e' errata.\nCollegati all'area utenti di Instatrack e inseriscila nuovamente per non perdere nuove occasioni.\n\nVisita https://areautenti.instatrack.eu\n\n\nIl Team di Instatrack."
    subject = "Instatrack - Password Instagram Errata"
    sendMailToUser(email, subject,msg)
    sendMailToUser("21giulio21@gmail.com", subject, msg)

#QUesta funzione prmette di capire se gia precedentemente seguivo una persona.
#Se gia seguivo una persona allora non rimando la richiesta
#QUesta funziona torna: true nel caso in cui precedentemente seguivo gia la persona
def checkIfYetFollowing(username_user_to_follow,cookies):

    headers = {
        'authority': 'www.instagram.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookies
    }

    params = (
        ('__a', '1'),
    )

    ritorno = requests.get('https://www.instagram.com/'+username_user_to_follow+'/', headers=headers, params=params).content

    #ritorno e' ugiale a tru o fals nel caso in cui precedentemente seguivo gia o meno l'utente
    ritorno = ritorno[ritorno.find("followed_by_viewer\":") + len("followed_by_viewer\":") : ritorno.find("followed_by_viewer\":") + len("followed_by_viewer\":") + 4 ]
    if ritorno.__contains__("tru"):
        return True
    else:
        return False

#Questa funzione permette di mandare direct message agli utenti
def sendDMMessage(username,testo):
    print("NON MANDO DM")
    #url = url_sms_mail + "/instatrack/send_DM/insert_DM_into_database.php?USERNAME=" + str(username) + "&MESSAGGIO=" + str(testo)
    #requests.get(url)

def sendDMMessageWithTAG(username,testo,tag):
    url = url_sms_mail + "/instatrack/send_DM/insert_DM_into_database_with_tag.php?USERNAME=" + str(username) + "&MESSAGGIO=" + str(testo)+ "&TAG=" + str(tag)
    return requests.get(url).content

def updateProcessing(username,value):
    url = url_bot + "/instatrack/updateProcessing.php?username=" + username + "&processing=" + str(value)
    requests.get(url)

def updateSctiptActive(username,valore):
    url = url_bot + "/instatrack/updateScriptActive.php?username=" + username + "&script_active=" + str(valore)
    requests.get(url)

def getUsersToFollow():
    url_get_all_user = url_bot + "/instatrack/instagram/getAllUser.php"
    return json.loads(requests.get(url_get_all_user).content)

#Update follow_unfollow nel database
def updateFollowUnfollowDatabase(username,follow_unfollow):
    url= url_bot + "/instatrack/updateFollowUnfollow.php?username="+username+"&follow_unfollow="+follow_unfollow
    requests.get(url)

#Agggiorno l'array sul database
def updateUserFollowed(userFollowed,username):

    url = url_bot + "/instatrack/updateUserFollowed.php"
    return_request = requests.post(url, data={'username': username, 'users_followed': userFollowed}).content

    return return_request

#Salvo id dell'utente nel database
def saveIdIntoDatabase(username,id):
    url = url_bot + "/instatrack/saveIdIntoDatabase.php?username="+username+"&id="+id
    requests.get(url)

#salvo i cookie di un relativo utente sul server
def seveCookieIntoServer(username,cookie):
    cookie =  base64.b64encode(str(cookie))
    url = url_bot + "/instatrack/saveCookie.php?username=" + str(username) +"&cookie="+str(cookie)
    requests.get(url)

#Questa funzione permette di settare il tempo di blocco
def setBlockTime(username,tempo_blocco_se_esce_errore,delta_t):
    print("Imposto il tempo di blocco per l'utente: " + username + " perche ha fatto troppe richueste")
    # Aggiorno ad attesa 10 minuti per l'utente a cui e' arrivato il blocco e aumento DT di 10 secondi
    updateTempoBlocco(username, tempo_blocco_se_esce_errore)
    #aumentoDelta t di 10 secondi
    #delta_t = int(delta_t) + 50
    #updateDeltaT(username, str(delta_t))




#prendo come input un numero random da 1 al numero massimo di persone che ho nel database di persone che posso
#seguire e facci ola richiesta pert farmene tornare 1 a caso
def getUserToFollwFromTarget(target,username):

    print( str(username) + " richiesta  al target: " + str(target))
    url = "http://www.utentidaseguire.eu/getUserToFollowFromUTENTI_DA_SEGUIRE.php?TARGET=" + str(target)
    return json.loads(requests.get(url).content)



#Ritorna quanti siano gli utenti registrati da quel thread
def countUserIntoDatabaseFromTread(thread):
    url = url_bot + "/instatrack/getCountUsersFromThread.php?THREAD="+str(thread)
    return requests.get(url).content


#Ritorna quanti siano gli utenti registrati totali
def countUserIntoDatabase():
    url = url_bot + "/instatrack/getCountUsers.php"
    return requests.get(url).content

#Seleziona un utente dal database con un preciso indice
def selectUserFromDatabase(index):
    url = url_bot + "/instatrack/getUserFromIndex.php?index=" +str(index)
    return json.loads(requests.get(url).content)


#Seleziona un utente dal database con un preciso indice
def selectUserFromDatabaseAndThread(index,thread):
    url = url_bot + "/instatrack/getUserFromIndexAndThread.php?index=" +str(index)+"&THREAD="+str(thread)
    return json.loads(requests.get(url).content)

#Ritorna il numero di utenti che sono nella tabella oin cui sono contenuti tutti
def getCountUsersToFollow():
    url = url_bot + "/instatrack/getCountUsersToFollow.php"
    return requests.get(url).content


#aggiorno nel mio databse la tupla con username: username e setto il tempo: time
def update_secondi_ultima_richiesta(username,time):
    url = url_bot + "/instatrack/updateSecondiUltimaRichiesta.php?username="+str(username)+"&time="+str(time)
    return requests.get(url).content

#funzione che aggiorna DT per quell'utente
def updateDeltaT(username,delta_t):
    url= url_bot + "/instatrack/updateDT.php?username="+str(username)+"&dt="+str(delta_t)
    return requests.get(url).content

#Aggiorno il tempo di blocco che deve attendere un utente prima che rinizi a mandare richieste
def updateTempoBlocco(username,tempo):
    url = url_bot + "/instatrack/updateTempoBlocco.php?username="+str(username)+"&tempo_blocco="+str(tempo)
    return requests.get(url).content

#Aggiorna il numere di richieste fatte, in questo modo dopo che un utente ne fa 100 posso
#diminuire il Delta T
def updateNumberRequestsDone(username,number_requests_done):
    url = url_bot + "/instatrack/updateNumberRequestsDone.php?username=" + str(username) + "&number_requests_done=" + str(number_requests_done)
    return requests.get(url).content

#Ottengo l id del utente attraverso lo username chiedendo ad instagram
def getIDFromUsername(username):

    headers = {
        'authority': 'www.instagram.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; rur=FRC; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; sessionid=IGSC8ed527fc1cda43ac5555695cbba25d643a1f566c1a145452aeb5b67b12fb5305%3A17hUaA9Ul0DdZyAsj2Os4HkJ1yVzZfCg%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527681913.5427627563%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1527681913\\054 \\"193.55.113.196\\": 2200}:1fO1o7:2az6OzqMKD6FoWtZ4xZOuq8St1Q"',
    }

    response = str(requests.get('https://www.instagram.com/' + username, headers=headers).content)
    posizioneprofilePage_= response.find("profilePage_")
    inizio_id = response[posizioneprofilePage_ + len("profilePage_"):]
    id = unicode(str(inizio_id[:inizio_id.find("\"")]), 'utf-8')
    return id

def getIdFromUsernameToUnfollow(username):
    url = "http://www.utentidaseguire.eu/getIDFromUsername.php?username="+str(username)
    return requests.get(url).content


def updateDevePagare(username, value):
    url = url_bot + "/instatrack/updateDevePagare.php?username=" + str(username) + "&DEVE_PAGARE=" + str(value)
    return requests.get(url).content

#Parso la risposta da Instagram nel momento in cui ho mandato una richiesta, content_request_JSON e' il ritorno dela richiesta una volta mandata
#
#Nella richiesta di login: {"message": "unauthorized", "redirect_url": "/accounts/login/?next=/web/friendships/297458948/follow/", "status": "fail"} ->Login errato
#Nella richiesta di login: {"authenticated": false, "user": true, "status": "ok"}-> Login errato
#Nella richiesta di login: {"authenticated": true, "user": true, "userId": "6045478794", "oneTapPrompt": false, "status": "ok"}-> Se tutto e' andato a buon fine
#Nella richiesta di FOLLOW: {"result": "following", "status": "ok"} -> se andata a buonfine
#Nella richiesta di Follow {"message": "This action was blocked. Please try again later.", "status": "fail"} -> se devo bloccare per un po di clicli
#Nella richiesta di FOLLOW se l'utente cambia password e quindi deve risettare i coockie: {"message": "unauthorized", "redirect_url": "/accounts/login/?next=/web/friendships/365506590/follow/", "status": "fail"}
#Nella richiesta di LIKE se inizia con <!DOCTYPE html> allora non ha potuto mettere like perche la foto era nascosta
def parse_content_request(content_request, type_request,username,tempo_blocco_se_esce_errore,delta_t,email):

    if type_request == "LOGIN":
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return


        authenticated = str(content_request_JSON["authenticated"]).upper()

        #In questo caso mi sono loggato in maniera corretta.
        if authenticated == "FALSE":
            messaggio = "AUTENTICAZIONE NON RIUSCITA - L'utente:"+str(username) + " NON ha inserito credenziali corrette "
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            updatePasswordErrataAndProcessing(username,1,email)
        else:
            # MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
            messaggio = "INVIO EMAIL - L'utente:" + str(
                username) + " inizia i 4 giorni di prova"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

            #msg = "Ciao " + username + ",\n\nBenvenuto in instatrack.eu! \n Da oggi iniziano i 3 giorni di prova gratuiti!\nAlla fine del servizio potrai decidere se rinnovare ed iniziare a guadagnare con Instagram\n\n\n\n\n\nBuon lavoro,\nInstatrack.eu"
            #subject = "Instatrack.eu - Inizio Prova Gratuita"
            #sendMailToUser(email, msg, subject)

    elif type_request == "FOLLOW-UNFOLLOW":

        #Se la risposta contiene Attendi perche ne ho fatte troppe di fila allora setto il blocco time per quell'utente
        if content_request.content.__contains__("been temporarily") or content_request.content.__contains__("Please wait") or  content_request.content.__contains__("Attendi") or content_request.content.__contains__("This action")or content_request.content.__contains__("Sembra che") :
            messaggio = "BLOCCO - L'utente:" + str(
                username) + " ha fatto TROPPE richieste, bloccato per un po"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            setBlockTime(username, tempo_blocco_se_esce_errore, delta_t)

            msg = "ADMIN - L'utente " + username + ", è in blocco perche ha fatto troppe richeste"
            subject = "Instatrack.eu - ADMIN"
            #sendMailToUser("21giulio21@gmail.com", msg, subject)
            return
        # Se la risposta contiene Sorry, you're following the max limit of accounts. You'll need to unfollow some accounts to start following more allora devo fare unfollow
        if content_request.content.__contains__("Sorry, you're following the max limit") :
            messaggio = "CAMBIO  - L'utente:" + str(
                username) + " ha fatto TROPPE richieste di FOLLOW, devo fargli fare UNFOLLOW"

            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            # Aggiorno il server dicendo che follow_unfollow e' zero
            follow_unfollow = "0"
            updateFollowUnfollowDatabase(username, follow_unfollow)

            msg = "ADMIN - L'utente " + username + ", ha fatto TROPPE richieste di FOLLOW, devo fargli fare UNFOLLOW"
            subject = "Instatrack.eu - ADMIN"
            sendMailToUser("21giulio21@gmail.com", msg, subject)

            return


        #se invecie contiene chechpoint vado ad incrementare il tempo_attesa_blocco a 10K
        if content_request.content.__contains__("checkpoint_required"):
            messaggio = "CHECK POINT REQUIRED - L'utente:" + str(
                username) + " è in checkpoint_required, lo blocco sperando che qualcuno lo sblocchi"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            setBlockTime(username, tempo_blocco_se_esce_errore, delta_t)

            msg = "ADMIN - L'utente " + username + ", è in checkpoint_required"
            subject = "Instatrack.eu - ADMIN"
            sendMailToUser("21giulio21@gmail.com", msg, subject)

            return

        #Se la risposta contiene unauthorized allora purche sia valida la data ma non va bene la password,
        #in particolare e' stata cambiata
        if content_request.content.__contains__("unauthorized"):
            messaggio = "CAMBIO PASSWORD - L'utente:" + str(
                username) + " ha cambiato password"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
            updatePasswordErrataAndProcessing(username, 1, email)
            messaggio = "Ciao "+str(username)+",  le credenziali del tuo account Instagram inserite precedentemente sono cambiate.\nAccedi a https://areautenti.instatrack.eu per reimpostare le credenziali corrette."
            messaggio_b64 = "UHVydHJvcHBvIGhhaSBpbnNlcml0byBsYSBwYXNzd29yZCBlcnJhdGEgZGVsIHR1byBhY2NvdW50IGluc3RhZ3JhbSEKClRvcm5hIG5lbGxhIHR1YSBhcmVhIGNsaWVudGkgcGVyIHJlaW5zZXJpcmUgbGEgcGFzc3dvcmQgY29ycmV0dGE6IGh0dHA6Ly9hcmVhdXRlbnRpLmluc3RhdHJhY2suZXUg"

            sendDMMessage(username, messaggio_b64)
            sendSMSToUser(email, messaggio)

        #Altrimenti puo accadere che ci sia la password errata perche puo aver cambiato password l'utente e devo rifare i coockie
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return

        #Controllo se la risposta contiene message
        if 'message' in content_request_JSON:
            message = str(content_request_JSON["message"]).upper()
            if message == "selectUserFromDatabaseAndThread":
                messaggio = "CAMBIO PASSWORD - L'utente:" + str(
                    username) + " ha cambiato password"
                scrivoColoratoSuFile(FILE_NAME, messaggio, "red")
                updatePasswordErrataAndProcessing(username, 1,email)

    elif type_request == "LIKE":
        if content_request.content.__contains__("<!DOCTYPE html>"):
            print("Processo l'utente: "+username+" non ha messo like alla foto perche era un profilo privato")

        else:
            print("Processo l'utente: "+username+" ha messo like alla foto con esito: " + str(content_request.content))


def parse_content_request_for_LOGIN_THREAD_0(content_request, type_request,username,tempo_blocco_se_esce_errore,delta_t,email):

    if type_request == "LOGIN":
        # Converso in JSON la risposta in modo da capire quando e' andata a buon fine
        try:
            content_request_JSON = json.loads(content_request.content)
        except ValueError:
            return
        print("Processo la risposta: "+ str(content_request.content) )

        #Prima controllo se è andato in checkpoint
        if str(content_request_JSON).__contains__("checkpoint_required"):
            print("L'uente è in checkpoin, riprova piu tardi, mando la mail per avvertirlo")
            msg = "Ciao " + username + ",\n\nAccedi a Instagram per verificare il tuo account!\n\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
            subject = "Instatrack - Accedi a Instagram"
            sendMailToUser(email, msg, subject)

            messaggio = "Ciao " + str(
                username) + ", accedi subito ad Instagram per sbloccare il tuo account."

            sendSMSToUser(email, messaggio)

            return 0


        #Qui controllo se lousername ho l'autenticazione a due fattori:
        if str(content_request_JSON).__contains__("two_factor_required"):

            messaggio = "LOGIN - l'account con USERNAME:" + username + " ha l'autenticazione a due fattori"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")

            msg = "Ciao " + username + ",\n\nAccedi a Instagram per rimuovere l'autenticazione a due fattori, altrimenti non possiamo processare il tuo account.\nUna volta processato puoi inserire nuovamente l'autenticazione a due fattori.\n\n\n\n\n\nCordialmente,\nInstatrack.eu"
            subject = "Instatrack.eu - Accedi a Instagram"
            sendMailToUser(email, msg, subject)

            messaggio = "Ciao " + str(
                username) + ", accedi subito ad Instagram per rimuovere l'autenticazione a due fattori e continuare ad usare Instatrack. Una volta processato puoi inserirla nuovamente."

            messaggio_b64 = "Q2lhbywgYWNjZWRpIGEgSW5zdGFncmFtIHBlciByaW11b3ZlcmUgbCdhdXRlbnRpY2F6aW9uZSBhIGR1ZSBmYXR0b3JpLCBhbHRyaW1lbnRpIG5vbiBwb3NzaWFtbyBwcm9jZXNzYXJlIGlsIHR1byBhY2NvdW50LiBVbmEgdm9sdGEgcHJvY2Vzc2F0byBwdW9pIGluc2VyaXJsYSBudW92YW1lbnRlLg=="

            sendDMMessage(username, messaggio_b64)
            sendSMSToUser(email, messaggio)

            return 0



        authenticated = str(content_request_JSON["authenticated"]).upper()

        #In questo caso mi sono loggato in maniera corretta.
        if authenticated == "FALSE":

            messaggio = "Ciao " + str(
                username) + ", le credenziali del tuo account Instagram sono errate. Accedi al sito https://areautenti.instatrack.eu per aggiornarle."
            sendSMSToUser(email, messaggio)

            messaggio_b64 = "Q2lhbywgbGUgY3JlZGVuemlhbGkgZGVsIHR1byBhY2NvdW50IEluc3RhZ3JhbSByaXN1bHRhbm8gZXJyYXRlLiAKQWNjZWRpIGFsIHNpdG8gaHR0cHM6Ly9hcmVhdXRlbnRpLmluc3RhdHJhY2suZXUgcGVyIHJlaW5zZXJpcmxlIGNvcnJldHRhbWVudGUu"

            sendDMMessage(username, messaggio_b64)

            messaggio = "LOGIN  - " + "L'username " + str(username) + " ha inserito una psw errata"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "red")


            print(updatePasswordErrataAndProcessing(username,"1",email))
        else:
            # MANDO ANCHE LA MAIL alla persona, in questo modo ho la certezza che arriva!
            #print("Mando la mail a " + email + " per comunicare che da oggi iniziano i 4 giorni di prova")
            #msg = "Ciao " + username + ",\n\nBenvenuto in instatrack.eu! \n Da ora il tuo account è attivo."
            #subject = "Instatrack.eu - Inizio Abbonamento"
            #sendMailToUser(email, subject,msg)



            #Capisco che abbonamento ha l'utente, cosi poi posso mandargli il messaggio corretto
            abbonamento_attivo = str(getLastPianoActived(str(username)))

            #Mando i DM e SMS ai vari utenti in base al piano che hannp
            if abbonamento_attivo.__contains__("Prova"):
                messaggio_b64 = "SWwgcGlhbm8gUFJPVkEgw6ggY29ycmV0dGFtZW50ZSBhdHRpdmF0byBzdWwgdHVvIHByb2ZpbG8gcGVyIDQgZ2lvcm5pIGEgcGFydGlyZSBkYSBvcmEgISEKCkNvbiBxdWVzdG8gcGlhbm8gcG90cmFpIGNhcGlyZSBiZW5lIGlsIGZ1bnppb25hbWVudG8gZGVsIG5vc3RybyBwcm9kb3R0by4KClNlIGluIHF1ZXN0byBwZXJpb2RvIHB1YmJsaWNoaSB1bmEgZm90byBzYXLDoCB2aXNpYmlsZSBpbW1lZGlhdGFtZW50ZSBuZWxsYSBzZXppb25lIEVTUExPUkEgZGkgSW5zdGFncmFtIGluIG1vZG8gY2hlIHB1b2kgb3R0ZW5lcmUgbW9sdGlzc2ltaSBMSUtFISAKClJpY29yZGF0aSBjaGUgbmVsIHBpYW5vIFBST1ZBIG5vbiBwb3RyZWkgcmljZXZlcmUgbW9sdGkgZm9sbG93ZXJzIHBlcmNow6ggZGlhbW8gcHJlY2VkZW56YSBhIGNoaSBoYSBhY3F1aXN0YXRvIHVubyBkZWkgbm9zdHJpIHBpYW5pLgoKUGVyIHF1YWxzaWFzaSBpbmZvcm1hemlvbmUgcHVvaSBjb25zdWx0YXJlIGxhIHNlemlvbmUgRkFRIGRlbCBub3N0cm8gc2l0byB3ZWI6IGh0dHBzOi8vd3d3Lmluc3RhdHJhY2suZXUvI2ZhcQoKUHVvaSBjb250cm9sbGFyZSBpbiB0ZW1wbyByZWFsZSBpbCB0dW8gYWNjb3VudCBzZWd1ZW5kbyBxdWVzdG8gbGluazogaHR0cHM6Ly9hcmVhdXRlbnRpLmluc3RhdHJhY2suZXUgCg=="
                sendDMMessage(username, messaggio_b64)
                print("Aggiornamento GET_LIKE: 1 " + str(updateGetLikeFromUsername(username, '1')))

                inizio_prova_1 = "Il piano PROVA e' stato attivato sul tuo profilo. Sara' attivo per 4 giorni a partire da ora! Pubblica ora una foto per far si che finisca immediatamente nella sezione ESPLORA di Instagram attraverso il nostro servizio."
                inizio_prova_2 = "Ti ricordiamo che nel piano PROVA mostriamo solemtne il funzionamento del servizio, per ottenere veri risultati devi acquistare uno dei nostri piani!"
                inizio_prova_3 = "Per qualsiasi informazione non esitare a contattarci sulla nostra pagina Instagram ufficiale @instatrack.eu!"

                sendSMSToUser(email, inizio_prova_1)
                sendSMSToUser(email, inizio_prova_2)
                sendSMSToUser(email, inizio_prova_3)

            elif abbonamento_attivo.__contains__("Basic"):
                messaggio_b64 = "SWwgcGlhbm8gQkFTSUMgw6ggY29ycmV0dGFtZW50ZSBhdHRpdmF0byBzdWwgdHVvIHByb2ZpbG8hIQoKQ29uIHF1ZXN0byBwaWFubyBwb3RyYWkgc2NlZ2xpZXJlIHVuYSBkZWxsZSBub3N0cmUgY2F0ZWdvcmllIGEgY3VpIG1hbmRhcmUgcmljaGllc3RlIGRpIEZvbGxvdywgTGlrZSBlIENvbW1lbnRpIG9nbmkgZ2lvcm5vLgoKSW4gcXVlc3RvIHBpYW5vIG5vbiDDqCBpbmNsdXNhIGxhIGNyZXNjaXRhIGRlaSB0dW9pIHBvc3QsIGluIHBhcnRpY29sYXJlIG5vbiB2ZXJyYW5ubyBwdWJibGljYXRpIG5lbGxhIHNlemlvbmUgRVNQTE9SQSBkaSBJbnN0YWdyYW0uCgpTZSBzZWkgaW50ZXJlc3NhdG8gYSByaWNldmVyZSBhbmNoZSBMaWtlIGFpIHR1b2kgcG9zdCBhdHRyYXZlcnNvIGlsIG5vc3RybyBzZXJ2aXppbyB0aSBjb25zaWdsaWFtbyBkaSBzY2VnbGllcmUgc3VjY2Vzc2l2YW1lbnRlIHVuIHBpYW5vIE1FRElVTS4KClBlciBxdWFsc2lhc2kgaW5mb3JtYXppb25lIHB1b2kgY29uc3VsdGFyZSBsYSBzZXppb25lIEZBUSBkZWwgbm9zdHJvIHNpdG8gd2ViOiBodHRwczovL3d3dy5pbnN0YXRyYWNrLmV1LyNmYXEKClB1b2kgY29udHJvbGxhcmUgaW4gdGVtcG8gcmVhbGUgaWwgdHVvIGFjY291bnQgc2VndWVuZG8gcXVlc3RvIGxpbms6IGh0dHBzOi8vYXJlYXV0ZW50aS5pbnN0YXRyYWNrLmV1IAo="
                sendDMMessage(username, messaggio_b64)
                print("Aggiornamento GET_LIKE: 0 " + str(updateGetLikeFromUsername(username, '0')))

                inizio_basic_1 = "Il piano BASIC e' stato attivato sul tuo profilo! In questo piano non e' inclusa la crescita dei tuoi post, in particolare non verranno pubblicati nella sezione ESPLORA di Instagram."
                inizio_basic_2 = "Se sei interessato a ricevere anche Like ai tuoi post attraverso il nostro servizio ti consigliamo di scegliere successivamente un piano MEDIUM."
                inizio_basic_3 = "Per qualsiasi informazione puoi consultare la sezione FAQ del nostro sito web: https://www.instatrack.eu/#faq o scriverci sulla nostra pagina Instagram @instatrack.eu"
                inizio_basic_4 = "Puoi controllare in tempo reale il tuo account seguendo questo link: https://areautenti.instatrack.eu"

                sendSMSToUser(email, inizio_basic_1)
                sendSMSToUser(email, inizio_basic_2)
                sendSMSToUser(email, inizio_basic_3)
                sendSMSToUser(email, inizio_basic_4)



            elif abbonamento_attivo.__contains__("Medium"):
                messaggio_b64 = "SWwgcGlhbm8gTUVESVVNIMOoIGNvcnJldHRhbWVudGUgYXR0aXZhdG8gc3VsIHR1byBwcm9maWxvISEKCkNvbiBxdWVzdG8gcGlhbm8gcG90cmFpIHNjZWdsaWVyZSB1bmEgZGVsbGUgbm9zdHJlIGNhdGVnb3JpZSBhIGN1aSBtYW5kYXJlIHJpY2hpZXN0ZSBkaSBGb2xsb3csIExpa2UgZSBDb21tZW50aSBvZ25pIGdpb3Juby4KCkluIHF1ZXN0byBwaWFubyDDqCBpbmNsdXNhIGxhIGNyZXNjaXRhIGRlaSB0dW9pIHBvc3QsIGluIHBhcnRpY29sYXJlIHZlcnJhbm5vIHB1YmJsaWNhdGkgbmVsbGEgc2V6aW9uZSBFU1BMT1JBIGRpIEluc3RhZ3JhbSBmaW5vIGFsIHJhZ2dpdW5naW1lbnRvIGRpIDQwMCBMaWtlLgoKUGVyIHF1YWxzaWFzaSBpbmZvcm1hemlvbmUgcHVvaSBjb25zdWx0YXJlIGxhIHNlemlvbmUgRkFRIGRlbCBub3N0cm8gc2l0byB3ZWI6IGh0dHBzOi8vd3d3Lmluc3RhdHJhY2suZXUvI2ZhcQoKUHVvaSBjb250cm9sbGFyZSBpbiB0ZW1wbyByZWFsZSBpbCB0dW8gYWNjb3VudCBzZWd1ZW5kbyBxdWVzdG8gbGluazogaHR0cHM6Ly9hcmVhdXRlbnRpLmluc3RhdHJhY2suZXUgCg=="
                sendDMMessage(username, messaggio_b64)
                print("Aggiornamento GET_LIKE: 1 " + str(updateGetLikeFromUsername(username, '1')))

                inizio_medium_1 = "Il piano MEDIUM e' stato attivato sul tuo profilo! In questo piano e' inclusa la crescita dei tuoi post in particolare verranno pubblicati nella sezione ESPLORA di Instagram fino al raggiungimento di almeno 400 Like."
                inizio_medium_2 = "Per qualsiasi informazione puoi consultare la sezione FAQ del nostro sito web: https://www.instatrack.eu/#faq o contattarci direttamente sulla nostra pagina Instagram @instatrack.eu"
                inizio_medium_3 = "Puoi controllare in tempo reale il tuo account seguendo questo link: https://areautenti.instatrack.eu"

                sendSMSToUser(email, inizio_medium_1)
                sendSMSToUser(email, inizio_medium_2)
                sendSMSToUser(email, inizio_medium_3)



            elif abbonamento_attivo.__contains__("Large"):
                messaggio_b64 = "SWwgcGlhbm8gTEFSR0Ugw6ggY29ycmV0dGFtZW50ZSBhdHRpdmF0byBzdWwgdHVvIHByb2ZpbG8hIQoKQ29uIHF1ZXN0byBwaWFubyBwb3RyYWkgc2NlZ2xpZXJlIHVuYSBkZWxsZSBub3N0cmUgY2F0ZWdvcmllIGEgY3VpIG1hbmRhcmUgcmljaGllc3RlIGRpIEZvbGxvdywgTGlrZSBlIENvbW1lbnRpIG9nbmkgZ2lvcm5vLgoKSW4gcXVlc3RvIHBpYW5vIMOoIGluY2x1c2EgbGEgY3Jlc2NpdGEgZGVpIHR1b2kgcG9zdCwgaW4gcGFydGljb2xhcmUgdmVycmFubm8gcHViYmxpY2F0aSBuZWxsYSBzZXppb25lIEVTUExPUkEgZGkgSW5zdGFncmFtIGZpbm8gYWwgcmFnZ2l1bmdpbWVudG8gZGkgOTAwIExpa2UuCgpQZXIgcXVhbHNpYXNpIGluZm9ybWF6aW9uZSBwdW9pIGNvbnN1bHRhcmUgbGEgc2V6aW9uZSBGQVEgZGVsIG5vc3RybyBzaXRvIHdlYjogaHR0cHM6Ly93d3cuaW5zdGF0cmFjay5ldS8jZmFxCgpQdW9pIGNvbnRyb2xsYXJlIGluIHRlbXBvIHJlYWxlIGlsIHR1byBhY2NvdW50IHNlZ3VlbmRvIHF1ZXN0byBsaW5rOiBodHRwczovL2FyZWF1dGVudGkuaW5zdGF0cmFjay5ldSAK"
                sendDMMessage(username, messaggio_b64)
                print("Aggiornamento GET_LIKE: 2 " + str(updateGetLikeFromUsername(username, '2')))

                inizio_large_1 = "Il piano LARGE e' stato attivato sul tuo profilo! In questo piano e' inclusa la crescita dei tuoi post in particolare verranno pubblicati nella sezione ESPLORA di Instagram fino al raggiungimento di almeno 900 Like."
                inizio_large_2 = "Per qualsiasi informazione puoi consultare la sezione FAQ del nostro sito web: https://www.instatrack.eu/#faq o contattarci direttamente sulla nostra pagina Instagram @instatrack.eu"
                inizio_large_3 = "Puoi controllare in tempo reale il tuo account seguendo questo link: https://areautenti.instatrack.eu"

                sendSMSToUser(email, inizio_large_1)
                sendSMSToUser(email, inizio_large_2)
                sendSMSToUser(email, inizio_large_3)



            elif abbonamento_attivo.__contains__("Premium"):
                messaggio_b64 = "SWwgcGlhbm8gUFJFTUlVTSDDqCBjb3JyZXR0YW1lbnRlIGF0dGl2YXRvIHN1bCB0dW8gcHJvZmlsbyEhCgpDb24gcXVlc3RvIHBpYW5vIHBvdHJhaSBzY2VnbGllcmUgdW5hIGRlbGxlIG5vc3RyZSBjYXRlZ29yaWUgYSBjdWkgbWFuZGFyZSByaWNoaWVzdGUgZGkgRm9sbG93LCBMaWtlIGUgQ29tbWVudGkgb2duaSBnaW9ybm8uCgpJbiBxdWVzdG8gcGlhbm8gw6ggaW5jbHVzYSBsYSBjcmVzY2l0YSBkZWkgdHVvaSBwb3N0LCBpbiBwYXJ0aWNvbGFyZSB2ZXJyYW5ubyBwdWJibGljYXRpIG5lbGxhIHNlemlvbmUgRVNQTE9SQSBkaSBJbnN0YWdyYW0gZmlubyBhbCByYWdnaXVuZ2ltZW50byBkaSAxNTAwIExpa2UuCgpQZXIgcXVhbHNpYXNpIGluZm9ybWF6aW9uZSBwdW9pIGNvbnN1bHRhcmUgbGEgc2V6aW9uZSBGQVEgZGVsIG5vc3RybyBzaXRvIHdlYjogaHR0cHM6Ly93d3cuaW5zdGF0cmFjay5ldS8jZmFxCgpQdW9pIGNvbnRyb2xsYXJlIGluIHRlbXBvIHJlYWxlIGlsIHR1byBhY2NvdW50IHNlZ3VlbmRvIHF1ZXN0byBsaW5rOiBodHRwczovL2FyZWF1dGVudGkuaW5zdGF0cmFjay5ldSAK"
                sendDMMessage(username, messaggio_b64)
                print("Aggiornamento GET_LIKE: 3 " + str(updateGetLikeFromUsername(username, '3')))

                inizio_premium_1 = "Il piano PREMIUM e' stato attivato sul tuo profilo! In questo piano e' inclusa la crescita dei tuoi post in particolare verranno pubblicati nella sezione ESPLORA di Instagram fino al raggiungimento di almeno 1500 Like."
                inizio_premium_2 = "Per qualsiasi informazione puoi consultare la sezione FAQ del nostro sito web: https://www.instatrack.eu/#faq o contattarci direttamente sulla nostra pagina Instagram @instatrack.eu"
                inizio_premium_3 = "Puoi controllare in tempo reale il tuo account seguendo questo link: https://areautenti.instatrack.eu"

                sendSMSToUser(email, inizio_premium_1)
                sendSMSToUser(email, inizio_premium_2)
                sendSMSToUser(email, inizio_premium_3)


            #gli mando un po si LIKE all'ultima foto, in particolare faccio si di recuperare l'ultmo URL
            #e lo mando al db di utenti che devono ricevere LIKE, in questo modo gli faccio fare un round
            url = "inizio"+str(username)
            insertUserIntoFUELGRAM_ACCOUNT_RECEIVER_LIKE(username, url)


            #newThread = random.randint(1,10)

            #newThread = newThread
            print("\n Autenticazione riuscita"  )

            messaggio = "LOGIN  - " + "L'username " + str(username) + " si è loggato"
            scrivoColoratoSuFile(FILE_NAME, messaggio, "green")

            #updateTreadFromUsername(username, newThread)
            updateSctiptActive(username,1)


def updateTreadFromUsername(username,newThread):
    url = url_bot + "/instatrack/updateThread.php?username="+username+"&thread=" + str(newThread)
    print("RIsposta ottenuta quando cambio il thread: " + str(requests.get(url).content) + "\n")



#Questa funzione permette di mandare la mail in caso sia finita la prova o il pacchertto
def sendMailToUser(mail_to,messaggio,subject):
    response = requests.get(url_sms_mail + "/instatrack/send_MAIL/insert_mail_into_database.php?MESSAGGIO="+messaggio+"&EMAIL="+mail_to+"&OGGETTO="+subject)
    print(response.content)


#Questa funzione permette di mandare la mail in caso sia finita la prova o il pacchertto
def sendSMSToUser(email,messaggio):
    prefisso_numero = getPhoneNumberFromEmail(email)
    response = requests.get(url_sms_mail + "/instatrack/send_SMS/insert_sms_into_database.php?NUMERO_TELEFONICO="+str(prefisso_numero) +"&MESSAGGIO="+str(messaggio))


def sendSMSToUserWithTag(prefisso_numero, messaggio,tag):
    response = requests.get(url_sms_mail + "/instatrack/send_SMS/insert_SMS_into_database_with_tag.php?NUMERO_TELEFONICO=" + str(
        prefisso_numero) + "&MESSAGGIO=" + str(messaggio) + "&TAG=" + str(tag))


####################################
#################################### Da qui in poi metto tutte le funzioni per i like automatici


def countPhotoIntoDatabase():
    url = url_bot + "/instatrack/likeautomatici/countPhotoIntoDatabase.php"
    return requests.get(url).content

def getIdPhotoNotLiked(max_like):
    url = url_bot + "/instatrack/likeautomatici/getPhoto.php?max_like="+str(max_like)
    return json.loads(requests.get(url).content)

def selectPhotoFromDatabase(index):
    url = url_bot + "/instatrack/likeautomatici/getPhotoFromIndex.php?index=" + str(index)
    return json.loads(requests.get(url).content)


#Per ogni utente si va a mettere sul database l'identificativo della foto e lo username della persona che ha messo la foto
def salvoSulDatabaseIdImmagineEUsernameDegliUtentiCheVoglionoLike(array_user_get_like):

    #Per ogni persone che vuole ricevere like prendo lo username e l'identificativo e la metto sul database
    for user_get_like in array_user_get_like:
        username_user_get_like = str(user_get_like["USERNAME"])
        idPrimaFoto = ottengoIdPrimaFotoDaUsername(username_user_get_like)

        print(username_user_get_like + " id:" + str(idPrimaFoto))

        if not str(idPrimaFoto).__contains__("lang="):# sono in questo caso se il profilo e' pubblico
            url = url_bot + "/instatrack/likeautomatici/saveUsernameAndIdImmagineIntoDatabase.php"
            payload = {'id_immagine': idPrimaFoto, 'username': username_user_get_like}
            return_request = requests.post(url, data=payload).content
            print("Salvo la foto di: " + str(username_user_get_like) + " con ID: " + idPrimaFoto)

        else:#sono in questo caso se il profilo e' privato
            print("Non posso prendere questo utente\n")

def updateUsersLiked(users_liked_string, id_immagine):
    payload = {'id_immagine': id_immagine, 'users_liked': users_liked_string}
    url = url_bot + "/instatrack/likeautomatici/updateUserLiked.php"
    return_request = requests.post(url, data=payload).content
    return return_request


#Questa funzione permette di cambiare il valore di GET_LIKE nel database
def updateGetLikeFromUsername(username,get_like):
    url = "http://www.giuliovittoria.it/instatrack/LIKE_FUELGRAM/updateGET_LIKE.php?USERNAME=" + username + "&GET_LIKE=" + str(get_like)
    return requests.get(url).content


#Questa funzione permette di cambiare il valore di SET_LIKE nel database
def updateSetLikeFromUsername(username,set_like):
    payload = {'username': username, 'set_like': set_like}
    url = url_bot + "/instatrack/likeautomatici/updateSetLikeFromUsername.php"
    return_request = requests.post(url, data=payload).content
    print(return_request)

def automaticLIKE(username, cookies_str, cookies_dict):

    #Questa variabile contiene il numero di LIKE massimo che si puo ottenere con il BOT
    max_like = 20

    # In questo array ho tutte le foto e tutte le persone che hanno messo like.
    numberPhotoIntoDatabase = int(countPhotoIntoDatabase())

    # In questo array inserisco tutte le foto e le persone che hanno messo like ma solo le foto che hanno un numero di like < max_like
    array_photo_to_auto_like = []

    # ciclo sul numero delle foto e inserisco nell'array array_photo_to_auto_like la foto che deve ottenere i like
    for index in range(0, int(numberPhotoIntoDatabase)):
        # Seleziono la tupla relativa all'utente
        photo = selectPhotoFromDatabase(index)

        id_photo = str(photo[0]['ID_IMMAGINE'])
        users_liked_string = str(photo[0]['USERS_LIKED'])
        users_liked_array = re.split(';', users_liked_string)
        username_immagine = str(photo[0]['USERNAME_IMMAGINE'])

        photo_dictionary = {
            "ID_IMMAGINE": id_photo,
            "USERS_LIKED_STRING": users_liked_string,
            "USERNAME_IMMAGINE": username_immagine,
        }

        print(
            "Processo la foto con id: " + id_photo + " dell'utente:" + username_immagine + " e ha come persone che hanno messo like: " + users_liked_string)

        # se il numero di persone che hanno messo like e' < max_like allora la inserisco in un array
        if len(users_liked_array) < max_like:
            array_photo_to_auto_like.append(
                photo_dictionary)  # array contenente tutte le foto che hanno len(users_liked_array) < max_like
            print("La foto con id: " + id_photo + " non ha raggiunto " + str(max_like) + " like")

    # Per ogni foto vado a far si che gli utenti gli mettano like
    for photo in array_photo_to_auto_like:

        # Per ogni imagine vado a prendere l'identificativo, l'array delle persone che hanno messo like e lo username
        # dell'utente che ha postato tale immagine
        id_photo = photo.get("ID_IMMAGINE")
        users_liked_string = photo.get("USERS_LIKED_STRING")
        users_liked_array = re.split(';', users_liked_string)
        username_get_immagine = photo.get("USERNAME_IMMAGINE")


        # Se lo username che deve mettere like è lo stesso di quello che lo deve ricevere deve continuare al prossimo
        if username_get_immagine == username:
            print("L'utente " + username + " non mette like a se stesso")
            continue

        # se lo username ha gia messo like non lo deve piu mettere e passo al prossimo
        if users_liked_array.__contains__(username):
            print(
                "L'utente: " + username + " ha gia messo like alla foto con id " + id_photo + " dell'utente:" + username_get_immagine)
        else:
            print(
                "L'utente: " + username + " deve mettere like alla foto con id " + id_photo + " dell'utente:" + username_get_immagine)


            content_request = richiestaLike(username_get_immagine, cookies_str, cookies_dict['csrftoken'])
            print(content_request.content)

            if content_request.content.__contains__("azione è stata bloccat"):
                return

            # Devo aggiundere l'utente alla stringa totale delle persone seguite
            if users_liked_string == "":
                users_liked_string = username + ";"

            else:
                users_liked_string = users_liked_string + username + ";"
            updateUsersLiked(users_liked_string, id_photo)


            break

################################# QUESTE FUNZIONI SERVONO PER IL LOG ##################

def getCurrentTime():
    now = datetime.datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M"))


#QUesta funzione scrive nella cartella LOG il file
#Esempio di come deve essere chiamata:scrivoColoratoSuFile("prova.html", "hhhh", "green")
def scrivoColoratoSuFile(nomeFIle, testo, colore):

    #Ottengo l'ora di ora
    timestamp = getCurrentTime()
    print(colored(timestamp + " " + testo, colore))
   # with open( nomeFIle, "a") as myfile:
    #    myfile.write('<p style="color: '+ colore+';">' +timestamp +" "+testo+'</p>')


#Questa funzione permette di eliminare una tupla dal database, in particolare elimina una mail
def removeEmailFromDatabase(id_mail):
    url = url_sms_mail + "/instatrack/send_MAIL/remove_email_from_database.php?ID=" + str(id_mail)
    return json.loads(requests.get(url,verify=False).content)

def removeSMSFromDatabase(id_sms):
    url = url_sms_mail + "/instatrack/send_SMS/remove_sms_from_database.php?ID=" + str(id_sms)
    return json.loads(requests.get(url).content)

#QUesta fnuzione mostra il numero di followers dallo username
def getCountFollowersFromUsername(username):
    headers = {
    'authority': 'www.instagram.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'mid=W4UpIQAEAAFq1cr_ml2C4FPWs8ot; mcd=3; fbm_124024574287414=base_domain=.instagram.com; ig_cb=1; shbid=18440; shbts=1546613875.9463286; rur=FTW; csrftoken=9XKeMDWlkfpQmpvCbR2fiNRUQT2yJKFr; ds_user_id=1724745946; sessionid=1724745946%3Ae0F325eRVx05r0%3A14; urlgen="{\\"2.230.243.113\\": 12874}:1gfZji:ne0jYIxD0QXAfKgJKpO4vzEWpC8"',
    }

    response = str(requests.get('https://www.instagram.com/' + str(username), headers=headers).content)
    followers = str(response[response.find('<meta content="Follower: ') + len('<meta content="Follower: '):response.find(', seguiti:')])

    if len(followers) > 10 or len(followers) == 0:
        return "false"
    else:
        return followers

#Questa funzione permette di ottenere il numero di telefono a partire dalla mail relativa all'utente.
def getPhoneNumberFromEmail(email):
    url = "http://www.giuliovittoria.it/get_number_from_email.php?EMAIL=" + str(email)
    risposta =  json.loads(requests.get(url).content)
    NUMERO_TELEFONICO = risposta[0]["nphone"]
    PREFISSO = risposta[0]["prefix"]
    PREFISSO_NUMERO_TELEFONICO = PREFISSO + NUMERO_TELEFONICO
    return PREFISSO_NUMERO_TELEFONICO


'''
Questa funziona mostra l'ultimo abbonamento attivo
in particolare ritorna:
"" (stringa vuota) se la persona non ha mai fatta abbonamento oppure se la abbiamo inserita senza farla pagare dal sito
Large - se l' ultimo abbonamento attivo dell username è Large
Basic - se l'ultimo abbonamento attivo è Basic
'''
def getLastPianoActived(username):
    url_get_all_user = "https://areautenti.instatrack.eu/api.php?k=DASCR$%Etrfd&acc="+str(username)
    return requests.get(url_get_all_user).content


#Queta funzione permette di andare ad inserire tutti gli account + url nel db per far si che poi vengano estratti per un round
def insertUserIntoFUELGRAM_ACCOUNT_RECEIVER_LIKE(username,url_foto):
    #Inserisco la data di inserimento nel momento in cui inserisco la foto che dovra ricevere like!
    tempo_di_ora = str(time.time())
    tempo_di_ora = tempo_di_ora[:tempo_di_ora.find(".")]
    url = "http://utentidaseguire.eu/instatrack/FUELGRAM_LIKE/insert_username_receive_like_from_database.php" + "?USERNAME=" + str(username) +"&URL=" + str(url_foto)+"&DATA_INSERIMENTO=" + str(tempo_di_ora)
    print(url)
    response = requests.get(url).content
    print(response)
