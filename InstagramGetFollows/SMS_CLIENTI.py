#from enum import Enum
from connection_utenti_da_seguire import CONNECTION_UTENTI_DA_SEGUIRE
from InstagramAPI import sendSMSToUserWithTag

#CATEGORIA = Enum('CATEGORIA', 'COLLAB REMARK CLIENT')

prefisso_numero = "+393381243473"
messaggio = "Ciao, conosci Instatrack?\nInstatrack e' l’unico servizio garantito ed affidabile che ti consente di avere una crescita costante sul tuo profilo instagram.\nAttraverso il nostro servizio ottieni dai 200 ai 1000 LIKE sotto ogni singolo post da te pubblicato alcuni dei quali provenienti da utenti con la spunta blu.\nGuarda i nostri risultati su alcuni clienti: @alessandrogino_ e  @jaybi_official.\nProva il nostro servizio:\nwww.instatrack.eu"

tag =  "Pd"
c = CONNECTION_UTENTI_DA_SEGUIRE()

utenti_da_contattare = c.getUTENTI_DA_CONTATTARE()
print(utenti_da_contattare)
sendSMSToUserWithTag(prefisso_numero, messaggio,tag)


