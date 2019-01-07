import MySQLdb


#Questa classe mi permette di interrogare il database
from UTENTE_DA_SEGUIRE import UTENTE_DA_SEGUIRE


class CONNECTION:
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




