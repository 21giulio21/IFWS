import time

import pynput
from pynput.keyboard import Key
from pynput.mouse import Button


mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def click(x,y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    time.sleep(0.5)
    mouse.release(Button.left)

def premiTab():
    keyboard.press(Key.shift_r)
    #time.sleep(0.5)
    keyboard.press()



def getPosition():
    time.sleep(2)
    print('The current pointer position is {0}'.format(
        mouse.position))

def pasteMailDestinazione():
    #accountfake@instatrack.eu
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    time.sleep(0.5)
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(0.2)
def scrivi(array):
    for i in array:
        time.sleep(0.1)
        keyboard.press(i)
        time.sleep(0.1)
        keyboard.release(i)


for i in range (124,1000):

    #Premo su aggiungi Aliaswww.instagram.
    click(343, 237)
    time.sleep(1)

    click(492, 324)
    scrivi(list("f"+str(i)))

    time.sleep(0.3)
    click(600, 344)
    time.sleep(0.3)

    pasteMailDestinazione()
    click(540, 374)

    time.sleep(2)








'''
# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release


'''