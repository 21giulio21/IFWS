import requests
import base64
import requests
import time

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
    id = str(inizio_id[:inizio_id.find("\"")])
    return id



def unfollw():


    #Ottengo i primi 24 che seguo e ne prendo 1

    headers = {
        'pragma': 'no-cache',
        'cookie': 'mid=W2MaRwAEAAFRBmtwITPHl2lN9cn3; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; datr=PKN6W-keB-dHGIzDbTv5Z51-; csrftoken=5a2VFQiu4y5pTzldlrfFznAwnBGEfQ2y; shbid=4294; ds_user_id=6374451695; sessionid=IGSC97217a987a9356856fe6d42f49dfb813275bb639722069c1df8b842431a0eba2%3AqEpWEscTZsmlSJUnuNsiNcx9W1Uluequ%3A%7B%22_auth_user_id%22%3A6374451695%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%226374451695%3AUya4R8y8f4At9JfacirW2XbWPF8RR53a%3A62231ebbe7c43399024f0bba6408d8ecd671840ec7edd2b3bf5f3b1ddde05c76%22%2C%22last_refreshed%22%3A1534769728.9096515179%7D; rur=ATN; fbsr_124024574287414=sZoYf3WemGclsH3-8CGvHY7qQcL_Fl3U5_x2NoT7_DQ.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFVdW1iSWQ0aTFaaXZUSExYdkxoTHJlNFNkeEZuNExpMFVrQjJhenNoVkc2d0pkYWxyaG9DTEg1M3M1RHRxMFRMazBDNzJFNGQ2Q2F4cnpXVWFKcTNocWhST0o1NW5oTG1DMGR1anJCUFJzQkQ2VUU3NU1adWZsUUxKVmlNN2x6OXNNNjRrZmhJMXVOMGxjVGh4ZUVkbUlvYV9OZE5zcmpxN3F0Qm1SYXZnT3NsR3BNc0loQXdVLW5qbWctWDdyWnBrM2I2RkdnN1IwUFNyTEFqZ05ETkZpNWc2UHlDZ2lWYUVnUXhNTGN0bDA0eGpxY08wckF3MThYbDliUFVxaWlDT3FJSnpLeWV0dHlnTC1veWx4QldzQVcwbFFoXzl6VS1sLXlucjJJa0RNVERNYXM3bF9FSHdpeDk1b3Uwei1uWllmdjJ2UjVtZVpKenRDdE5OTnY4VCIsImlzc3VlZF9hdCI6MTUzNDc2OTczMSwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"37.227.59.128\\": 24608}:1frjiz:i-DhFUQYUXIiiIpah9upPjrZ7rs"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'ffbdaa4416896b3c821c9a0f96adb7f1',
        'referer': 'https://www.instagram.com/dietabarfitalia/following/',
    }

    params = (
        ('query_hash', 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'),
        ('variables', '{"id":"6374451695","include_reel":true,"first":24}'),
    )

    content_request =  str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)
    usernameToUnfollow = content_request[content_request.find("username") + len("username\":\""):content_request.find("\",\"full_name\"")]
    idToUnfollow = getIDFromUsername(usernameToUnfollow)

    #Ottengo username - identificativo e faccio unfollow

    headers = {
        'cookie': 'mid=W2MaRwAEAAFRBmtwITPHl2lN9cn3; mcd=3; ig_cb=1; fbm_124024574287414=base_domain=.instagram.com; datr=PKN6W-keB-dHGIzDbTv5Z51-; csrftoken=5a2VFQiu4y5pTzldlrfFznAwnBGEfQ2y; shbid=4294; ds_user_id=6374451695; sessionid=IGSC97217a987a9356856fe6d42f49dfb813275bb639722069c1df8b842431a0eba2%3AqEpWEscTZsmlSJUnuNsiNcx9W1Uluequ%3A%7B%22_auth_user_id%22%3A6374451695%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%226374451695%3AUya4R8y8f4At9JfacirW2XbWPF8RR53a%3A62231ebbe7c43399024f0bba6408d8ecd671840ec7edd2b3bf5f3b1ddde05c76%22%2C%22last_refreshed%22%3A1534769728.9096515179%7D; rur=ATN; fbsr_124024574287414=sZoYf3WemGclsH3-8CGvHY7qQcL_Fl3U5_x2NoT7_DQ.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFVdW1iSWQ0aTFaaXZUSExYdkxoTHJlNFNkeEZuNExpMFVrQjJhenNoVkc2d0pkYWxyaG9DTEg1M3M1RHRxMFRMazBDNzJFNGQ2Q2F4cnpXVWFKcTNocWhST0o1NW5oTG1DMGR1anJCUFJzQkQ2VUU3NU1adWZsUUxKVmlNN2x6OXNNNjRrZmhJMXVOMGxjVGh4ZUVkbUlvYV9OZE5zcmpxN3F0Qm1SYXZnT3NsR3BNc0loQXdVLW5qbWctWDdyWnBrM2I2RkdnN1IwUFNyTEFqZ05ETkZpNWc2UHlDZ2lWYUVnUXhNTGN0bDA0eGpxY08wckF3MThYbDliUFVxaWlDT3FJSnpLeWV0dHlnTC1veWx4QldzQVcwbFFoXzl6VS1sLXlucjJJa0RNVERNYXM3bF9FSHdpeDk1b3Uwei1uWllmdjJ2UjVtZVpKenRDdE5OTnY4VCIsImlzc3VlZF9hdCI6MTUzNDc2OTczMSwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"37.227.59.128\\": 24608}:1frjkE:-QNU2hLolLm3GuH5phzEwegRXLk"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '5a2VFQiu4y5pTzldlrfFznAwnBGEfQ2y',
        'pragma': 'no-cache',
        'x-instagram-ajax': '6c1f67754dc0',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/dietabarfitalia/following/',
        'content-length': '0',
    }

    link = 'https://www.instagram.com/web/friendships/'+str(idToUnfollow)+'/unfollow/'
    print(link)

    response = requests.post(link, headers=headers)
    print("UNFOLLOW " + str(usernameToUnfollow) + " " + str(response.content))
for i in range(0,3000):
    unfollw()
    time.sleep(30)
