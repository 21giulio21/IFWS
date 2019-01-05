import requests

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


fol = getCountFollowersFromUsername("giulio_tavella")
print(fol)