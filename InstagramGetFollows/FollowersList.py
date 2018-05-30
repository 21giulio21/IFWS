import requests
import time

def find_end_cursor(content_originale,content):
    # Cerco end_cursor da mettere in input alla richiesta dopo
    content = content_originale[content_originale.find("end_cursor") + len("end_cursor") + 3: content.find("\"}")]
    end_cursor = content[:content.find("\"}")]
    return end_cursor

def findUsername(content_originale):
    content = content_originale
    for i in range(1, 50):
        index_username_start = content.find("\"username\"")
        s = content[index_username_start + len("\"username\"") + 2: index_username_start + len("\"username\"") + 80]
        username_1 = content[index_username_start + len("\"username\"") + 2: index_username_start + len(
            "\"username\"") + s.find("\"") + 2]
        content = content[content.find(username_1) + len(username_1):]
        with open("instagram.txt", "a") as myfile:
            myfile.write(username_1 + "\n")
        print(username_1)
    return find_end_cursor(content_originale, content)


headers = {
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; rur=FRC; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; sessionid=IGSC8ed527fc1cda43ac5555695cbba25d643a1f566c1a145452aeb5b67b12fb5305%3A17hUaA9Ul0DdZyAsj2Os4HkJ1yVzZfCg%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527681913.5427627563%7D; ig_cb=1; mcd=3; shbts=1527681922.7310588; urlgen="{\\"time\\": 1527681913\\054 \\"193.55.113.196\\": 2200}:1fNzr0:NCBvLS6u5whZsU3yaI4RUEU_pAU"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/fedex/followers/?hl=it',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': '7d2e902f70516f88fecb9fbea5eefd9d',
}

params = (
        ('query_hash', '37479f2b8209594dde7facb0d904896a'),
        ('variables', '{"id":"232257039","first":50}'),
)
    #Cerco tutti gli account
content_originale = str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)



for i in range(1,100000):
    time.sleep(5)
    headers = {
        'cookie': 'csrftoken=tpNpx90YcinKiWlaLcx3apvueW0OpZV9; shbid=18815; rur=FRC; mid=Ww6TeAAEAAHCATvZQX6W_Jih5thX; ds_user_id=819693525; sessionid=IGSC8ed527fc1cda43ac5555695cbba25d643a1f566c1a145452aeb5b67b12fb5305%3A17hUaA9Ul0DdZyAsj2Os4HkJ1yVzZfCg%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3Ap0rX7NmINkKdhHbEOdYn6Ku6bS6zoapm%3Ae88d7822ccb18324c4369523a052ca1680c61add19ecc6513c6466483123a6c0%22%2C%22last_refreshed%22%3A1527681913.5427627563%7D; ig_cb=1; mcd=3; urlgen="{\\"time\\": 1527681913\\054 \\"193.55.113.196\\": 2200}:1fNzrG:BBk8kXyGsKVfuEJZlRnRZPDCqzw"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.instagram.com/fedex/followers/?hl=it',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'dd1ca2d0c10e7e86ca9d1b12d789f5bb',
    }

    params = (
        ('query_hash', '37479f2b8209594dde7facb0d904896a'),
        ('variables', '{"id":"232257039","first":50,"after":"'+findUsername(content_originale)+'"}'),
    )

    response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
    content_originale =  response.content
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables=%7B%22id%22%3A%22232257039%22%2C%22first%22%3A12%2C%22after%22%3A%22AQDFNTQiGHGEEdaGk8AK6KgFyeSCDEqo8jzRBICgbK6ZylLpy6wJMXv7HH0Yg4Nm39WjZKd7RMyB1BpsmsjlfvgAq9ovZcQk2VGgf6MQaG3TWw%22%7D', headers=headers)
