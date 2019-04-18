import requests



import requests
s = requests.Session()
#print(s.get("http://httpbin.org/ip", proxies={'http': 'http://45.43.133.83:3199'}).content)


proxies = { "http": "http://21giulio21-5jebr:obvJFmVEcf@168.80.230.47:3199",
            "https": "https://21giulio21-5jebr:obvJFmVEcf@168.80.230.47:3199",
        }

r = requests.get('http://httpbin.org/ip', proxies=proxies)
print(r.content)

