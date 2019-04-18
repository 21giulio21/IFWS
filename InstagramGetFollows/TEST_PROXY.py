import requests

proxies = { "http": "http://21giulio21-vaccn:F2QwNdBrYJ@168.81.22.148:3199",
            "https": "https://21giulio21-vaccn:F2QwNdBrYJ@168.81.22.148:3199",
        }

print(requests.get('http://httpbin.org/ip', proxies=proxies).content)