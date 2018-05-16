import requests
url_utente = "https://www.instagram.com/giulio_tavella/"
headers = {
    'origin': 'https://www.instagram.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.139 Chrome/66.0.3359.139 Safari/537.36',
    'cookie': 'shbid=18815; rur=FRC; mid=Wvw-LgAEAAFeGvt-y3z7sFfrYu5i; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=8BsyFYUSPP3m5xepzR030A7NTjoMUsfw; ds_user_id=7752426221; sessionid=7752426221%3ATAkVD94aec8M6E%3A10; fbsr_124024574287414=WGWIdbysFEYNIE1q_9As6gVQuN7CrV25WMJJ1El9eJQ.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUJCSW9DdksxcUQ5Y2xtRTJEMUtXRENQb3AzS3M4SjlaLTAtOWN5RjZsM0xTTGVJSjFKY3lkZ0FxaUctcFotM05DNUJFdnBTSkpNd08zdzEyVmoydUM3clFaeFBwZEd5R2c1Zm8xMmRDOFk2aVZFeWN0OHJSenRvUW9FTl9kR0M5OFllQlR0bUx2QVFkY0dfMEdZckw1c0tFRmJib19WbC1CTVNqeHVlTEJCMmRuQjh3WjlLd2FNTDdfZUJibFhJZ1VuZk1pMVRnRWJwcWNPU2xmVExfWXpJaVZaSTQyNmQ2aGxJb1VjWE1ZT2IxdWthd0xRSm44MnpfT19XRmxia2NjS0ZrdmlXb1BGanNfeEhBN0FBLUFteEN3bWFkcjE5ZkRGZXRFQmhmX1MxYUlxWnVxNFRON18tMlRnWU9hMnBxRGRURFI3Y2NrWFFKVW4xY3VUMExYayIsImlzc3VlZF9hdCI6MTUyNjQ4MTU4NiwidXNlcl9pZCI6IjExNTQwMjExNjMifQ; urlgen="{\\"time\\": 1526480430\\054 \\"193.55.113.196\\": 2200}:1fIxb8:YV5slo_jwOKRs8iz9UGINKEFHXY"',
    'x-csrftoken': '8BsyFYUSPP3m5xepzR030A7NTjoMUsfw',
    'x-instagram-ajax': 'f145b51a9723',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/p/BizCiLrlV3gd8hqX1VbE2GyWC-w8_py6C6Ret80/?taken-by=atreborgram',
    'authority': 'www.instagram.com',
    'content-length': '0',
}

response = requests.post(url_utente)
print(response.content)


