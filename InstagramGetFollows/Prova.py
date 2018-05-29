import requests

headers = {
    'cookie': 'shbid=18815; ds_user_id=819693525; mid=WwvBIAAEAAH03rDJUvvqUFkP8kdd; ig_cb=1; csrftoken=oUZOpTYZzoBjdXSbreBES9jriVcM7ECq; rur=FRC; sessionid=IGSCeeb6de56742c9ce8ab9462f0984c296a39c0cc6671ce8234c72b9ab95c909406%3A7EwrYOXGltOjNn4P9sZYoony1DcgxH6U%3A%7B%22_auth_user_id%22%3A819693525%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_platform%22%3A4%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22819693525%3AUUzNSEb8qiyM7T6qzD2c1rg3HkERwWwd%3A37de8bf5e846d80fdcc9252f908456c87c56927cd92e9d8ffcb66ac221774189%22%2C%22last_refreshed%22%3A1527517869.2403335571%7D; mcd=3; shbts=1527518069.6854541; urlgen="{\\"time\\": 1527517869\\054 \\"193.55.113.196\\": 2200}:1fNJED:2noIWWfNVzxEBaVK_lY98CbvaF0"',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.instagram.com/fedez/followers/',
    'authority': 'www.instagram.com',
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-gis': '3e90d1df8701ec6dae50ac5c0c398acf',
}

params = (
    ('query_hash', '37479f2b8209594dde7facb0d904896a'),
    ('variables', '{"id":"46071423","first":40,"after":"AQBKacnYhpz3lzH--ixZj_UuTtDRuYxyde92S2jf9H8yyLUtyehIUbV9edPqGkqKB-emoE3x5aUee1feVCXlfshGCY9jnURL0pRh6Nki-WwAgA"}'),
)

response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params)
print(response.content)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.instagram.com/graphql/query/?query_hash=37479f2b8209594dde7facb0d904896a&variables=%7B%22id%22%3A%2246071423%22%2C%22first%22%3A12%2C%22after%22%3A%22AQBKacnYhpz3lzH--ixZj_UuTtDRuYxyde92S2jf9H8yyLUtyehIUbV9edPqGkqKB-emoE3x5aUee1feVCXlfshGCY9jnURL0pRh6Nki-WwAgA%22%7D', headers=headers)
