import requests
from InstagramAPI import follow
from InstagramAPI import getUsersToFollow
from InstagramAPI import login
import sys
import time




if __name__ == "__main__":
    print "starting requests"
    username = sys.argv[1]
    password = sys.argv[2]
    r = login(username,password)
    print r.content
    print "*****************************"
    cookies_dict = r.cookies.get_dict()
    cookies_str = ''.join(key + "=" + str(cookies_dict[key]) + "; " for key in cookies_dict)
    print(cookies_str[:-2])
    utenti = getUsersToFollow()
    for i in range(12000,13000):
        utente = utenti[i]
        print(username + " sta seguendo -> username : " + utente["USERNAME"] + " ID " + utente["ID"])
        follow(utente["ID"], utente["USERNAME"], cookies_str, cookies_dict['csrftoken'])
        time.sleep(30)
