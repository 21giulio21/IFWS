import MySQLdb


#Questa classe mi permette di interrogare il database
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



