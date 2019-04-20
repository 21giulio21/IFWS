import requests

proxies = { "http": "http://21giulio21-y8nk7:zUIRM3BlOX@181.177.76.114:3199",
            "https": "https://21giulio21-y8nk7:zUIRM3BlOX@181.177.76.114:3199",
        }

print(requests.get('http://httpbin.org/ip', proxies=proxies).content)