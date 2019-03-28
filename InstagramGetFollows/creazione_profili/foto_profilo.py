import requests

headers = {
    'cookie': 'ig_cb=1; mid=XIU25gALAAEafhhxjJ8R7PbdfTro; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=xeqrO0rK2klWF40O5ptcIEneRscSYNBbXlmpUfY7mf0.eyJjb2RlIjoiQVFBbEgxODNYV3M4WUZHMjJnR2NKaHltQ094ejJSVFdZM1FYUGJINENRYm5PRG9ia01GcWcxNEdSTWNIODF1SjFHU0dwSDJ3RV9tNFltaHhzTnhtSzd1QzJWNnM2Y2ZQZmZGOFBfa0V4dzk3N25tMGJpanZFdWltay1saGJoanI4YXp5aERpV29XRHdFX3ZDNzFJQzhBNlVnTkRqTE9yYl9GT0YyTGJCeDdqUkpZSEhRc1BKd0U1YnV3Mks5RDVPNkFZekRuZGRoRmcwXzVocllTMTlVbXhtUC1QNEtvOVJrX2cya3kyc2ZDNVctLVVDbzZMMk1Tb2hDNTU2VzkzTDk3ZW9hcE1PNENwWHhRbC1sN2FTQWVfT0tLbWFHNDNXLWJMemh5T3h1ZC1BdHRzaWZ5MWIwWHcwc0k1aExUbnBkbE1xV1c0TnJkNXFfMmZEM29HNjFmcFdpbDBmTmNFWXRFV3owQzU3MFNqaWpkTmhJZUhWSlk3bXNQTGo1bndUTWVBIiwidXNlcl9pZCI6IjEwMDAxMTAwMDg1MTY4OSIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTUyMjM0NDI0fQ; csrftoken=oRIGgMKE3AuiPRBhZnf971dD7bAAulk8; ds_user_id=11622525273; sessionid=11622525273%3ABXzVMW3pZcz2ED%3A6; rur=ATN; urlgen="{\\"2001:b07:ac9:e9a2:8893:301e:f45d:f4de\\": 12874}:1h315y:1Xp7N-uiSrbZ5sgrOLHBdMovlxQ"',
    'origin': 'https://www.instagram.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-csrftoken': 'oRIGgMKE3AuiPRBhZnf971dD7bAAulk8',
    'x-ig-app-id': '936619743392459',
    'x-instagram-ajax': 'de81cb3fd9c4-hot',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryKiPH6SRo7YCxRolb',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/accounts/edit/',
    'authority': 'www.instagram.com',
}

data = '$------WebKitFormBoundaryKiPH6SRo7YCxRolb\\r\\nContent-Disposition: form-data; name="profile_pic"; filename="profilepic.jpg"\\r\\nContent-Type: image/jpeg\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryKiPH6SRo7YCxRolb--\\r\\n'

response = requests.post('https://www.instagram.com/accounts/web_change_profile_picture/', headers=headers, data=data)
print(response.content)