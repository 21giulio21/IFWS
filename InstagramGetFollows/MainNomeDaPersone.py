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
    'cookie': 'csrftoken=0rcmqCEguMzQ2mdlAoDQ8tipUcly17B4; ds_user_id=7888680831; sessionid=IGSC57d8d858ba3aaf7ce45ae1dc7c32212d8a8295db743b3d1eaebfb134ab179314%3ALYQDJVCX3Fr2kd7XUfTvCRuD22mKxJ2m%3A%7B%22_auth_user_id%22%3A7888680831%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227888680831%3AOV6LLTxCPTOfvsPHpAqKk3TnJBDURk4m%3A90b6283516cda04d19801e18edd4414dddc50b4e5f2c20df33191432326bbd23%22%2C%22last_refreshed%22%3A1527620854.4057896137%7DIGSC910d7e05a5c4a2e15ca69322b054d6906e2e1f40ae35182eb870217c2f90ed7b%3A8PFs94s93ne49OcdFq50eatY3LMiR4TN%3A%7B%z%22%3A7888680831%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%227888680831%3AntcLhgS1v3fLXwfp2CWGSv4FvNuT2RZb%3A744411ddf1d8c7afdee4ed81fd638be2e4f31efefed83891768defefc1d31863%22%2C%22last_refreshed%22%3A1527620141.0235059261%7D; ig_cb=1; mid=Ww2iKAAEAAGUfOZDKB1J0sxmSXLr; mcd=3; rur=FRC; urlgen="{\\"time\\": 1527620141\\054 \\"91.253.159.25\\": 24608}:1fNjmf:SLC7FRX1WNcuR62vLucW_sDF22I"',
    'origin': 'https://www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': '0rcmqCEguMzQ2mdlAoDQ8tipUcly17B4',
    'x-instagram-ajax': '8958fe1e75ab',
    'authority': 'www.instagram.com',
    'referer': 'https://www.instagram.com/vvickyrehab/?hl=it',

	}



	response = requests.post('https://www.instagram.com/web/friendships/999307614/follow/', 	headers=headers)
	print(response.content)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.instagram.com/web/friendships/232257039/follow/?hl=en', headers=headers)







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






def ottengoDatiDalServerMio():
    return json.loads(requests.get("http://2.230.243.113/getFoulo.php").content)



if __name__ == "__main__":
	follow('','')




