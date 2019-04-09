'''
In questo file vado ad ottenere tutti i followers dell'account in questione e gli mando il relativo messaggio
'''
import time

import instaloader

from InstagramAPI import sendDMMessageWithTAG

username_to_get_followers = "viktoria_crttt"
username_to_login = "vittoriaangelici"
password_to_login = "21giulio21"

L = instaloader.Instaloader()
L.login(user=username_to_login,passwd=password_to_login)
followers = instaloader.Profile.from_username(L.context, username_to_get_followers).get_followers()

for seguace in followers:

    username_seguace = seguace.username
    id_seguace = seguace.userid
    messaggio_b64 = "Q2lhbywgY29ub3NjaSBJbnN0YXRyYWNrPwoKSW5zdGF0cmFjayDDqCBs4oCZdW5pY28gc2Vydml6aW8gZ2FyYW50aXRvIGVkIGFmZmlkYWJpbGUgY2hlIHRpIGNvbnNlbnRlIGRpIGF2ZXJlIHVuYSBjcmVzY2l0YSBjb3N0YW50ZSBzdWwgdHVvIHByb2ZpbG8gaW5zdGFncmFtIGNvbiBzZWd1YWNpIGl0YWxpYW5pLCByZWFsaSBlZCBpbiB0YXJnZXQuIAoKQXR0cmF2ZXJzbyBpbCBub3N0cm8gc2Vydml6aW8gb3R0aWVuaSBkYWkgNTAwIGFpIDE1MDAgTElLRSBzb3R0byBvZ25pIHNpbmdvbG8gcG9zdCBkYSB0ZSBwdWJibGljYXRvIGFsY3VuaSBkZWkgcXVhbGkgcHJvdmVuaWVudGkgZGEgdXRlbnRpIGNvbiBsYSBzcHVudGEgYmx1OiBxdWVzdG8gYXVtZW50ZXLDoCBlc3BvbmVuemlhbG1lbnRlIGxlIHR1ZSBwb3NzaWJpbGl0w6AgZGkgZmluaXJlIGluIEhvbWUhIAoKR3VhcmRhIGkgbm9zdHJpIHJpc3VsdGF0aSBzdSBhbGN1bmkgY2xpZW50aTogQGFsZXNzYW5kcm9naW5vXyBlICBAamF5Ymlfb2ZmaWNpYWwuCgpJbm9sdHJlIG1lbnNpbG1lbnRlIHNvbm8gZGlzcG9uaWJpbGkgZGVpIGNvZGljaSBzY29udG8gcGVyIHRlIGUgaSB0dW9pIGFtaWNpIQoKReKAmSBwb3NzaWJpbGUgcHJvdmFyZSBpbCBzZXJ2aXppbyBjb24gdW4gcGFjY2hldHRvIFBST1ZBIHNlZ3VlbmRvIHF1ZXN0byBsaW5rOgoKaHR0cDovL2JpdC5seS8yVXRObmwxCg=="
    risposta = str(sendDMMessageWithTAG(username_seguace, messaggio_b64, "CLIENT"))
    print(username_seguace , risposta)

    time.sleep(0.2)