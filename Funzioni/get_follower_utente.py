import instaloader
import requests
from time import sleep
import time

#Permette di scrivere i log su un file di testo
def printFile(text):
    with open("logFollowers.txt", "a") as myfile:
        myfile.write(str(text) + "\n")


def checkType(follower,follows,media):
                
                if follows == 0 or follower / follows > 2:
                    is_selebgram = True
                    is_fake_account = False
                    printFile('   >>>This is probably Selebgram account')
                    return 'Fake'
                elif follower == 0 or follows / follower > 2:
                    is_fake_account = True
                    is_selebgram = False
                    printFile('   >>>This is probably Fake account')
                    return 'Fake'

                else:
                    is_selebgram = False
                    is_fake_account = False
                    printFile('   >>>This is a normal account')
                    

                if media > 0 and follows / media < 10 and follower / media < 10:
                    is_active_user = True
                    printFile('   >>>This user is active')
                    return 'Attivo'

                else:
                    is_active_user = False
                    printFile('   >>>This user is passive')
                    return 'Passivo'

                


# Get instance
L = instaloader.Instaloader()
Natura=[ 'hanwagofficial' ]
# Login or load session
L.login('magic_host', '21giulio21')        # (login)
#L.interactive_login(USER)      # (ask password on terminal)
#L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)

# Obtain profile metadata

i=0
totale=0
media=0
for id in Natura:
    profile = instaloader.Profile.from_username(L.context, id)
    followers=profile.followers
    printFile(str(followers))
    totale+=followers
print(totale)
for id in Natura:
    profile = instaloader.Profile.from_username(L.context, id)
    # Print list of followers
    
    for follower in profile.get_followers():
            start=time.time()
            followers=follower.followers
            followees=follower.followees
            mediacount=follower.mediacount
            checkTypeFollowee=checkType(followers,followees,mediacount)
            printFile(checkTypeFollowee)
            response = requests.get("http://getfollowersoninstagram.altervista.org/saveUserIntoDatabaseUSER_TO_FOLLOW.php?ID=%s&USERNAME=%s&TARGET=%s&TYPE=%s&FOLLOWER=%s&FOLLOWEE=%s&MEDIA=%s"%(str(follower.userid),str(follower.username),'Natura',checkTypeFollowee,followers,followees,mediacount))

            i+=1
            printFile((i/totale)*100)
            printFile(response)
            sleep(1)
            media+= (time.time()-start)
            printFile(media/i)

            printFile((totale-i)*(media/i))
    printFile(id)

