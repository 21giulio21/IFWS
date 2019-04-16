import sys
import time
from enum import Enum

import instaloader

from InstagramAPI import sendDMMessageWithTAG

CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')


hastag = "naturaitaliana" #str(sys.argv[1])
L = instaloader.Instaloader()
posts = L.get_hashtag_posts(hastag)


for post in posts:

    username_post = post.owner_username
    url_post = post.url
    tag = CATEGORIA.CLIENT.name
    testo = ""

    print(username_post, url_post)

    messaggio_b64 = "Q2lhbywgY29ub3NjaSBJbnN0YXRyYWNrPwoKSW5zdGF0cmFjayDDqCBpbCBudW92byBzZXJ2aXppbyBjaGUgdGkgY29uc2VudGUgZGkgYXZlcmUgdW5hIGNyZXNjaXRhIGNvc3RhbnRlIHN1bCB0dW8gcHJvZmlsbyBpbnN0YWdyYW0gY29uIHNlZ3VhY2kgaXRhbGlhbmksIHJlYWxpIGVkIGluIHRhcmdldC4gCgpBdHRyYXZlcnNvIGlsIG5vc3RybyBzZXJ2aXppbyBvdHRpZW5pIGRhaSA1MDAgYWkgMTUwMCBMSUtFIHNvdHRvIG9nbmkgc2luZ29sbyBwb3N0IGRhIHRlIHB1YmJsaWNhdG8gYWxjdW5pIGRlaSBxdWFsaSBwcm92ZW5pZW50aSBkYSB1dGVudGkgY29uIGxhIHNwdW50YSBibHU6IHF1ZXN0byBhdW1lbnRlcsOgIGVzcG9uZW56aWFsbWVudGUgbGUgdHVlIHBvc3NpYmlsaXTDoCBkaSBmaW5pcmUgaW4gSG9tZSEgCgpHdWFyZGEgaSBub3N0cmkgcmlzdWx0YXRpIHN1IGFsY3VuaSBjbGllbnRpOiBAYWxlc3NhbmRyb2dpbm9fIGUgQHZpa3RvcmlhY29ydGUuCgpJbm9sdHJlIG1lbnNpbG1lbnRlIHNvbm8gZGlzcG9uaWJpbGkgZGVpIGNvZGljaSBzY29udG8gcGVyIHRlIGUgaSB0dW9pIGFtaWNpIQoKReKAmSBwb3NzaWJpbGUgcHJvdmFyZSBpbCBzZXJ2aXppbyBjb24gdW4gcGFjY2hldHRvIFBST1ZBIHNlZ3VlbmRvIHF1ZXN0byBsaW5rOgoKaHR0cDovL2JpdC5seS8yVXRObmwxCg=="
    risposta = str(sendDMMessageWithTAG(username_post, messaggio_b64, tag))

    if risposta.__contains__("DM gia mandato in precedenza"):
        time.sleep(0)
        print("DM gia mandato in precedenza")
    else:
        time.sleep(0)
