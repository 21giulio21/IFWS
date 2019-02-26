import sys

from RICERCA_INFLUENCER_ISTANZA import RICERCA_INFLUENCER_ISTANZA


#Prendo username - password dalla console
username = str(sys.argv[1]) #"djinfiewj2"
password = str(sys.argv[2]) #"21giulio21"
username_profilo_target = str(sys.argv[3]) #"giacomohawkman"

#Cerco tra i followers del profilo: username_profilo_target
RICERCA_INFLUENCER_ISTANZA(username,password).salvoProfiloNelDatabase(username_profilo_target)




