import requests



def getPhoneNumberAndEmailFromUsername(username):
    inizio_stringa_telefono = '"telephone":"+39'
    fine_stringa_telefono = '"}\n            </script>\n'

    inizio_stringa_mail = '"email":"'
    fine_stringa_mail = '","telephone'

    url_instagram = "https://www.instagram.com/"
    username = "matteo_diamante_pr"
    risposta = str(requests.get(url_instagram + username).content)
    telefono = risposta[risposta.find(inizio_stringa_telefono) + len(inizio_stringa_telefono):]
    telefono = telefono[:10]
    email = risposta[risposta.find(inizio_stringa_mail) + len(inizio_stringa_mail):]
    email = email[:email.find(fine_stringa_mail)]
    print(email)
    print(telefono)
