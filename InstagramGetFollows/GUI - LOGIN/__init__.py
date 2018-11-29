from ScrolledText import ScrolledText
from Tkinter import *
from GUI.function import login_from_GUI

window = Tk()

window.title("INSTATRACK - LOGIN ")

window.geometry('1000x300')

lbl = Label(window, text="Voglio la LAMBORGHINI")

lbl.grid(column=0, row=0)

txt = ScrolledText(window, width=90, height=20)

txt.grid(column=0, row=1)

def clicked():
    login_from_GUI(txt)
    print("Premuto il pulsante")


btn = Button(window, text="LOGIN", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()