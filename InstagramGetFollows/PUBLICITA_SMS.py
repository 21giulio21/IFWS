import pandas as pd
import requests
import xlrd


from InstagramAPI import scrivoColoratoSuFile, countUserIntoDatabase, selectUserFromDatabase, updateTreadFromUsername


'''
Questo file permette di andare a mandare SMS in automatico alle persone presenti nel database degl incluencer.
'''

file_name ="/home/giulioportatile/Scrivania/DATABASE CONTATTI.xlsx"
sheet =  "DATABASE"
url_sms_mail = "http://www.utentidaseguire.eu"

df = pd.read_excel(io=file_name, sheet_name=sheet)
username = df.head(990)["USERNAME"]
telefono = df.head(990)["TELEFONO"]

for i in range(0,990):
    try:
        print(username[i] , telefono[i])
        messaggio = "Ciao "+str(username[i])+ ",\nVuoi  che ogni tua foto finisca nella sezione ESPLORA di Instagram ?\nVieni a provare il servizio su www.instatrack.eu"
        print(messaggio)

        prefisso_numero = "+39"+str(telefono[i])
        response = requests.get(url_sms_mail + "/instatrack/send_SMS/insert_sms_into_database.php?NUMERO_TELEFONICO=" + str(prefisso_numero) + "&MESSAGGIO=" + str(messaggio))
        print(response.content)

    except:
        print("EEEEE")