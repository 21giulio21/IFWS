import time

import MySQLdb


#Questa classe mi permette di interrogare il database
from CLASSI.CLASSI import MAIL_POSTMARKAPP
from UTENTE_DA_CONTATTARE import UTENTE_DA_CONTATTARE

from UTENTE_DA_SEGUIRE import UTENTE_DA_SEGUIRE


class CONNECTION_UTENTI_DA_SEGUIRE:
  def __init__(self):

      self.db = MySQLdb.connect(host="146.66.111.144",  # your host, usually localhost
                           user="utentida_foulo",  # your username
                           passwd="21giulio21",  # your password
                           db="utentida_foulo")  # name of the data base

      # you must create a Cursor object. It will let
      #  you execute all the queries you need
      self.cur = self.db.cursor()



  def fetchall(self,query):
      # Use all the SQL you like
      self.cur.execute(query)

      # print all the first cell of all the rows
      return self.cur.fetchall()

  def num_row(self,query):
      # Use all the SQL you like
      self.cur.execute(query)

      # print all the first cell of all the rows
      return self.cur.rowcount

  def query(self,query):
      # Use all the SQL you like
      return self.cur.execute(query)

  def getUserToFollowFromTarget(self,target):
      query         =   "SELECT * FROM UTENTI_DA_SEGUIRE WHERE TARGET = '" +str(target)+"' ORDER BY RAND() LIMIT 1"
      self.cur.execute(query)
      fetch         =   self.cur.fetchall()

      if self.cur.rowcount == 0:

          query = "SELECT * FROM UTENTI_DA_SEGUIRE WHERE TARGET = 'INFLUENCER_ITALIANO' ORDER BY RAND() LIMIT 1"
          self.cur.execute(query)
          fetch = self.cur.fetchall()

          id_instagram = str(fetch[0][1])
          username = str(fetch[0][2])
          target = str(fetch[0][3])
          return UTENTE_DA_SEGUIRE(id_instagram, username, target)

      else:
        id_instagram  =   str(fetch[0][1])
        username      =   str(fetch[0][2])
        target        =   str(fetch[0][3])
        return UTENTE_DA_SEGUIRE(id_instagram,username,target)


  def insertUserIntoDatabaseUTENTI_DA_SEGUIRE(self,username,id_instagram,target):
      query = "INSERT INTO UTENTI_DA_SEGUIRE (USERNAME, ID, ID_INTERNO, TARGET) VALUES ('"+str(username)+"', '"+str(id_instagram)+"', NULL, '"+str(target)+"')"
      return self.cur.execute(query)

  def removeUserFromUTENTI_DA_SEGUIRE(self,username,target):
      query = "DELETE FROM `UTENTI_DA_SEGUIRE` WHERE `UTENTI_DA_SEGUIRE`.`USERNAME` = '"+str(username)+"' AND `UTENTI_DA_SEGUIRE`.`TARGET` = '" + str(target)+"'"
      return self.cur.execute(query)

  #con questa funzione trovo tutti gli utenti che posso contattare
  def getUTENTI_DA_CONTATTARE(self):
      query = "SELECT * FROM UTENTI_DA_CONTATTARE"
      self.cur.execute(query)
      fetch = self.cur.fetchall()

      #Inserisco qui dentro tutti gli utenti da ocntattare predenti nel DB
      utenti_da_contattare= []

      for utente in fetch:
        USERNAME = str(utente[0])
        FOLLOWERS = str(utente[1])
        MAIL = str(utente[2])
        TELEFONO = str(utente[3])

        #Ritorno tutti gli utente presenti del DB
        utenti_da_contattare.append(UTENTE_DA_CONTATTARE(USERNAME,FOLLOWERS,MAIL,TELEFONO))
      return utenti_da_contattare

  ##Ottengo una mail alla volta dal DB per ottenere le mail per postkarkapp

  def getMailFromDb_POSTMARKAPP(self):
      query = "SELECT * FROM `MAIL_POSTMARKAPP` LIMIT 1"
      self.cur.execute(query)
      fetch = self.cur.fetchall()

      # Inserisco qui dentro tutti gli utenti da ocntattare predenti nel DB
      mail = []

      for utente in fetch:
          ID = str(utente[0])
          EMAIL = str(utente[1])
          OGGETTO = str(utente[2])
          MESSAGGIO = str(utente[3])

          # Ritorno tutti gli utente presenti del DB
          mail.append(MAIL_POSTMARKAPP(ID, EMAIL, OGGETTO,MESSAGGIO))

      return mail

  def removeEmailFromDb_POSTMARKAPP(self,ID):

      query = """DELETE FROM MAIL_POSTMARKAPP WHERE ID =   """ + str(ID)

      print(query)
      print(self.cur.execute( query))
      self.db.commit()

#Questa funzione permette di tornare il proxy
  def getProxiesFromDB(self,username_instagram):

    #Ottengo l'ora di ora
    #tempo_di_ora = str(time.time())
    #tempo_di_ora = tempo_di_ora[:-3]

    '''
    Prendo il proxy che ha fatto l'ultima richiesta almeno 100 secondi fa
    '''
    #tempo_che_posso_prendere_proxy = int(tempo_di_ora) - 100

    query = "SELECT * FROM PROXIES WHERE USERNAME_INSTAGRAM = '" + str(username_instagram) + "' LIMIT 1"

    self.cur.execute(query)
    fetch = self.cur.fetchall()

    PROXY_DICTIONARY = {
        "PROXY": "",
        "PORT": "",
        "USERNAME": "",
        "PASSWORD": "",

    }
    #Controllo se e' tornato almeno 1 proxy
    if len(fetch) == 0:
        return "{'error':'No proxy ready'}"

    for utente in fetch:
        PROXY_DICTIONARY["PROXY"] = str(utente[1])
        PROXY_DICTIONARY["PORT"] = str(utente[2])
        PROXY_DICTIONARY["USERNAME"] = str(utente[3])
        PROXY_DICTIONARY["PASSWORD"] = str(utente[4])


    return PROXY_DICTIONARY

  def updateLAST_ROUNDFromDbPROXY(self,proxy):

      tempo_di_ora = str(time.time())
      tempo_di_ora = tempo_di_ora[:-3]

      query = "UPDATE `PROXIES` SET `LAST_ROUND` = '"+str(tempo_di_ora)+"' WHERE `PROXIES`.`PROXY` =  '" + str(proxy) + "'"

      self.cur.execute(query)
      self.db.commit()







