import instaloader
import requests

from InstagramAPI import scrivoColoratoSuFile



class RICERCA_INFLUENCER_ISTANZA:

  #TODO: Qui devo inserire tutti i parametri per il costruttore...
  def __init__(self,username,password):

    self.FILE_NAME = "RICERCA_INFLUENCER.html"

    #followers minimi e massimi che deve avere la persona presunta Influencer
    self.followers_minimi = 300
    self.followers_massimi = 50000

    #numeri di media minimi e massimi che deve avere la persona presunta Influencer
    self.media_minimi = 10
    self.media_massimi = 10000

    #Questa variabile indica se l'utente ha le storie attive
    self.storie_attive = True

    # Questa variabile indica se l'utente ha il profilo pubblico
    self.profilo_pubblico = True

    # Questa variabile indica se l'utente che cerco deve avere una mail nella descrizione
    self.presenza_email_nella_descrizione = True

    # Questa variabile indica se l'utente che cerco ha delle storie in evidenza
    self.presenza_highlight_rells = True

    #In questo caso cerco di capire se il profilo ha la spunta blu o meno
    self.presenza_spunta_blu = False

    #Credenziali di un profilo per il login ad Instaloader
    self.username = username
    self.password = password

  def ottengoNumeroDiTelefonoDaUsername(self,username):
    inizio_stringa_telefono = '"telephone":"+39'

    url_instagram = "https://www.instagram.com/"
    risposta = str(requests.get(url_instagram + username, verify=False).content)

    telefono = risposta[risposta.find(inizio_stringa_telefono) + len(inizio_stringa_telefono):]
    telefono = str(telefono[:10])

    if len(telefono) > 11 or telefono.__contains__("html"):
      messaggio = "RICERCA INFLUENCER - USERNAME:" + username + " Telefono non valido"
      scrivoColoratoSuFile(self.FILE_NAME, messaggio, "red")
    else:
      messaggio = "RICERCA INFLUENCER - USERNAME:" + username + " Telefono: " + str(telefono)
      scrivoColoratoSuFile(self.FILE_NAME, messaggio, "green")
      return telefono

  def ottengoEmailDaUsername(self,username):
    inizio_stringa_mail = '"email":"'
    fine_stringa_mail = '","telephone'

    url_instagram = "https://www.instagram.com/"
    risposta = str(requests.get(url_instagram + username, verify=False).content)

    email = risposta[risposta.find(inizio_stringa_mail) + len(inizio_stringa_mail):]
    email = str(email[:email.find(fine_stringa_mail)])

    if len(email) > 30 or email.__contains__("l>\n<html"):
      messaggio = "RICERCA INFLUENCER - USERNAME:" + username + " Email non valida"
      scrivoColoratoSuFile(self.FILE_NAME, messaggio, "red")
    else:
      messaggio = "RICERCA INFLUENCER - USERNAME:" + username + " Email: " + str(email)
      scrivoColoratoSuFile(self.FILE_NAME, messaggio, "green")
      return email



  #quESTA FUNZIONE PERMETTE DI SALVARE PROFILI iNSTAGRAM SUL DATABASE INTERNO CHE HO IO,
  #PER OGNI USERNAME SI SALVA IL RELATIVO CONTATTO TELEFONICO E LA MAIL
  def salvoProfiloNelDatabase(self,username_profilo_target):


    L = instaloader.Instaloader()
    L.login(user=self.username, passwd=self.password)
    profile = instaloader.Profile.from_username(L.context, username_profilo_target)

    for follower in profile.get_followers():
      if self.controllo_se_il_profilo_rispetta_i_canoni(follower) == True:
        email    =  self.ottengoEmailDaUsername(follower.username)
        telefono =  self.ottengoNumeroDiTelefonoDaUsername(follower.username)
        username =  follower.username
        followers = follower.followers

        #Se i followers sono minori di 10k allora:
        if int(followers) < 10000 and telefono is not None:
          print(username,telefono,email,followers)
          print(self.salvaContatto(username,telefono,email,followers))
        elif int(followers) > 10000:
          print(username, telefono, email, followers)
          print(self.salvaContatto(username, telefono, email, followers))




  def salvaContatto(self,username,telefono,email,followers):
    url = "http://www.utentidaseguire.eu/instatrack/SalvataggioInfluencer/salvoInfluencerIntoUTENTI_DA_CONTATTARE.php?USERNAME="+str(username)+"&FOLLOWERS="+str(followers)+"&EMAIL="+str(email)+"&TELEFONO="+str(telefono)
    return requests.get(url,verify=False).content

  def controllo_se_il_profilo_rispetta_i_canoni(self,follower):

    #Controllo se l'utente ha piu di 10k di followers
    followers_profilo_target = int(follower.followers)
    if  followers_profilo_target > self.followers_minimi and followers_profilo_target < self.followers_massimi:

      #Controllo il numero di media che stia tra i parametri dati
      media_profilo_target = int(follower.mediacount)
      if media_profilo_target > self.media_minimi and media_profilo_target < self.media_massimi:

        # Controllo che le storie siano viibili
        storie_attive_profilo_target = follower.has_public_story
        if storie_attive_profilo_target == self.storie_attive:

          #controllo che il profilo sia pubblico
          profilo_pubblico_profilo_target = not follower.is_private
          if profilo_pubblico_profilo_target == self.profilo_pubblico:

            return True




