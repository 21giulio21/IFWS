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



def writeToFIleAllUsersToUnfollow():

    headers = {
        'pragma': 'no-cache',
        'cookie': 'csrftoken=kzhnCxTTMNcKqmcnIzItNO2AUuD7fWlK; shbid=18815; rur=FRC; mid=W1RylQAEAAH5JaMUhqG2ayFfFT9S; ds_user_id=819693525; sessionid=IGSC2ca26b47e37a210f08669a862ca2efbbff5053caf87ddf5ef338e36972107ba0%3AgCgZqIdtVuCMi3sb32t9M1aMPxSWXLnx%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ADJcqY0MGaC0Ubl7p3s5adpKpjTGfvWJd%3Abe6fbe0257aee3d66c7c74b7f00e113adb82111935919abaf8d24a9fec6e978a%22%2C%22last_refreshed%22%3A1532261014.1639788151%7D; ig_cb=1; mcd=3; shbts=1532261356.7046137; urlgen="{\\"time\\": 1532261028\\054 \\"91.252.42.170\\": 24608}:1fhDAr:Cxv3eGXQioodmKWAr-czG06ZH0Q"',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'x-requested-with': 'XMLHttpRequest',
        'x-instagram-gis': 'd41a558092d3ac856ca28cfea25a460a',
        'referer': 'https://www.instagram.com/giulio_tavella/following/',
    }

    params = (
        ('query_hash', '9335e35a1b280f082a47b98c5aa10fa4'),
        ('variables', '{"id":"819693525","first":24}'),
    )

    content_request =  str(requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params).content)
    usernameToUnfollow = content_request[content_request.find("username") + len("username\":\""):content_request.find("\",\"full_name\"")]
    idToUnfollow = getIDFromUsername(usernameToUnfollow)



    headers = {
        'cookie': 'csrftoken=kzhnCxTTMNcKqmcnIzItNO2AUuD7fWlK; shbid=18815; rur=FRC; mid=W1RylQAEAAH5JaMUhqG2ayFfFT9S; ds_user_id=819693525; sessionid=IGSC2ca26b47e37a210f08669a862ca2efbbff5053caf87ddf5ef338e36972107ba0%3AgCgZqIdtVuCMi3sb32t9M1aMPxSWXLnx%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3ADJcqY0MGaC0Ubl7p3s5adpKpjTGfvWJd%3Abe6fbe0257aee3d66c7c74b7f00e113adb82111935919abaf8d24a9fec6e978a%22%2C%22last_refreshed%22%3A1532261014.1639788151%7D; ig_cb=1; mcd=3; shbts=1532262307.7787287; urlgen="{\\"time\\": 1532261028\\054 \\"91.252.42.170\\": 24608}:1fhDQB:qsmWL6Imrd9aEH2gIploahdSprk"',
        'origin': 'https://www.instagram.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'kzhnCxTTMNcKqmcnIzItNO2AUuD7fWlK',
        'pragma': 'no-cache',
        'x-instagram-ajax': '314b21580dde',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.instagram.com',
        'referer': 'https://www.instagram.com/giulio_tavella/following/',
        'content-length': '0',
    }

    response = requests.post('https://www.instagram.com/web/friendships/'+str(idToUnfollow)+'/unfollow/', headers=headers)
    print("UNFOLLOW " + str(usernameToUnfollow) + " " + str(response.content))
for i in range(0,3000):
    writeToFIleAllUsersToUnfollow()
    time.sleep(100)
