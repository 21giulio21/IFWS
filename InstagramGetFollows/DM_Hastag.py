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

    messaggio_b64 = "Q2lhbywgY29ub3NjaSBJbnN0YXRyYWNrPwoKSW5zdGF0cmFjayDDqCBs4oCZdW5pY28gc2Vydml6aW8gZ2FyYW50aXRvIGVkIGFmZmlkYWJpbGUgY2hlIHRpIGNvbnNlbnRlIGRpIGF2ZXJlIHVuYSBjcmVzY2l0YSBjb3N0YW50ZSBzdWwgdHVvIHByb2ZpbG8gaW5zdGFncmFtIGNvbiBzZWd1YWNpIGl0YWxpYW5pLCByZWFsaSBlZCBpbiB0YXJnZXQuIAoKQXR0cmF2ZXJzbyBpbCBub3N0cm8gc2Vydml6aW8gb3R0aWVuaSBkYWkgNTAwIGFpIDE1MDAgTElLRSBzb3R0byBvZ25pIHNpbmdvbG8gcG9zdCBkYSB0ZSBwdWJibGljYXRvIGFsY3VuaSBkZWkgcXVhbGkgcHJvdmVuaWVudGkgZGEgdXRlbnRpIGNvbiBsYSBzcHVudGEgYmx1OiBxdWVzdG8gYXVtZW50ZXLDoCBlc3BvbmVuemlhbG1lbnRlIGxlIHR1ZSBwb3NzaWJpbGl0w6AgZGkgZmluaXJlIGluIEhvbWUhIAoKR3VhcmRhIGkgbm9zdHJpIHJpc3VsdGF0aSBzdSBhbGN1bmkgY2xpZW50aTogQGFsZXNzYW5kcm9naW5vXyBlICBAamF5Ymlfb2ZmaWNpYWwuCgpJbm9sdHJlIG1lbnNpbG1lbnRlIHNvbm8gZGlzcG9uaWJpbGkgZGVpIGNvZGljaSBzY29udG8gcGVyIHRlIGUgaSB0dW9pIGFtaWNpIQoKReKAmSBwb3NzaWJpbGUgcHJvdmFyZSBpbCBzZXJ2aXppbyBjb24gdW4gcGFjY2hldHRvIFBST1ZBIHNlZ3VlbmRvIHF1ZXN0byBsaW5rOgoKaHR0cDovL2JpdC5seS8yVXRObmwxCg=="
    risposta = str(sendDMMessageWithTAG(username_post, messaggio_b64, tag))
    if risposta.__contains__("DM gia mandato in precedenza"):
        time.sleep(10)
    else:
        time.sleep(2700)
