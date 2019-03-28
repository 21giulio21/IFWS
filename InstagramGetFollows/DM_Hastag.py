import sys
import time
from enum import Enum

import instaloader

from InstagramAPI import sendDMMessageWithTAG

CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')


hastag = "bicipiti" #str(sys.argv[1])
L = instaloader.Instaloader()
posts = L.get_hashtag_posts(hastag)


for post in posts:

    username_post = post.owner_username
    url_post = post.url
    tag = CATEGORIA.CLIENT.name
    testo = ""

    print(username_post, url_post)

    messaggio_b64 = "Q2lhbywgY29ub3NjaSBJbnN0YXRyYWNrPwoKSW5zdGF0cmFjayDDqCBs4oCZdW5pY28gc2Vydml6aW8gZ2FyYW50aXRvIGVkIGFmZmlkYWJpbGUgY2hlIHRpIGNvbnNlbnRlIGRpIGF2ZXJlIHVuYSBjcmVzY2l0YSBjb3N0YW50ZSBzdWwgdHVvIHByb2ZpbG8gaW5zdGFncmFtIGNvbiBzZWd1YWNpIGl0YWxpYW5pLCByZWFsaSBlZCBpbiB0YXJnZXQuIAoKQXR0cmF2ZXJzbyBpbCBub3N0cm8gc2Vydml6aW8gb3R0aWVuaSBkYWkgNTAgYWkgNTAwIExJS0Ugc290dG8gb2duaSBzaW5nb2xvIHBvc3QgZGEgdGUgcHViYmxpY2F0byBhbGN1bmkgZGVpIHF1YWxpIHByb3ZlbmllbnRpIGRhIHV0ZW50aSBjb24gbGEgc3B1bnRhIGJsdTogcXVlc3RvIGF1bWVudGVyw6AgZXNwb25lbnppYWxtZW50ZSBsZSB0dWUgcG9zc2liaWxpdMOgIGRpIGZpbmlyZSBpbiBIb21lISAKCkd1YXJkYSBpIG5vc3RyaSByaXN1bHRhdGkgc3UgYWxjdW5pIGNsaWVudGk6IEBhbGVzc2FuZHJvZ2lub18gZSAgQGpheWJpX29mZmljaWFsLgoKSW5vbHRyZSBtZW5zaWxtZW50ZSBzb25vIGRpc3BvbmliaWxpIGRlaSBjb2RpY2kgc2NvbnRvIHBlciB0ZSBlIGkgdHVvaSBhbWljaSEKCkXigJkgcG9zc2liaWxlIHByb3ZhcmUgaWwgc2Vydml6aW8gY29uIHVuIHBhY2NoZXR0byBQUk9WQSBzZWd1ZW5kbyBxdWVzdG8gbGluazoKCnd3dy5pbnN0YXRyYWNrLmV1Cg=="
    risposta = str(sendDMMessageWithTAG(username_post, messaggio_b64, tag))
    if risposta.__contains__("DM gia mandato in precedenza"):
        time.sleep(10)
    else:
        time.sleep(2700)
