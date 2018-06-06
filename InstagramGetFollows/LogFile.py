

#Permette di scrivere i log su un file di testo
def printFile(text):
    with open("loginstagram.txt", "a") as myfile:
        myfile.write(text + "\n")