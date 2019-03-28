#TODO User agent: Safari on ipad Vi_ci_78
import re
import time

import pynput
import pyautogui
from pip._vendor.distlib.compat import raw_input
from pynput.mouse import Button

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def click(x,y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

def clickDestro(x,y):
    mouse.position = (x, y)
    mouse.press(Button.right)
    time.sleep(0.1)
    mouse.release(Button.right)

def getPosition():
    time.sleep(0.3)
    posizione = str(mouse.position).split(',')
    x = re.sub('[^0-9]','', posizione[0])
    y = re.sub('[^0-9]','', posizione[1])


    return (x,y)


#lo username è vi_ci_79
def scrivi(array):
    for i in array:
        time.sleep(0.1)
        keyboard.press(i)
        time.sleep(0.1)
        keyboard.release(i)




for i in range(88,89):


    click(1889, 91)
    time.sleep(2)
    click(1732, 321)
    time.sleep(2)
    scrivi(list("www.instagram.com"))
    click(1506, 159)
    
    time.sleep(30)
    exit(1)
    click(1876, 217) # tolgo il banner

    x = int(getPosition()[0])
    y = int(getPosition()[1])
    raw_input("Vai sopra al campo email")
    print(x,y)
    click(x, y)
    email = "v"+str(i)+"@instatrack.eu"
    scrivi(list(email))
    time.sleep(1)
    x = int(getPosition()[0])
    y = int(getPosition()[1])
    raw_input("Vai sopra al campo Nome")
    click(x, y)
    print(x,y)
    username = "vi_ci_"+str(i)
    scrivi(list(username))
    click(x , y + 60)
    scrivi(list(username))
    time.sleep(1)
    click(x , y + 90)
    scrivi(list("21giulio21"))
    click(x , y + 130)
    time.sleep(1)
    click(1290, 665)
    time.sleep(1)
    click(1427, 807)
    time.sleep(2)
    click(1409, 856)
    time.sleep(8)
    click(1491, 840)
    time.sleep(3)
    click(1863, 233)
    
    print(getPosition())

    time.sleep(2)
    click(1878, 326)


    time.sleep(4)
    click(1441, 453)

    print(getPosition())

    time.sleep(4)
    click(1162, 471)
    time.sleep(4)

    click(221, 271) # apro download per poter sceglere la foto
    time.sleep(2)

    click(775, 461) # scelgo la foto
    time.sleep(4)
    print(getPosition())

    click(1633, 804)
    time.sleep(1)

    #ora chiudo la finestra di Instagram
    time.sleep(1)
    #click(1905, 33)
    #apro il tasto destro cosi posso eliminare la chacke
    time.sleep(3)
    clickDestro(1765, 379)
    time.sleep(1)
    click(1607, 728) # apro ispezione
    time.sleep(3)
    click(1801, 207)
    time.sleep(1)
    click(1794, 426)
    time.sleep(2)
    click(1815, 707)
    time.sleep(2)
    click(1894, 39)





print(getPosition())

