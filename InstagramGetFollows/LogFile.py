

#Permette di scrivere i log su un file di testo
def printFile(text):
    with open("LOG/logScript2.txt", "a") as myfile:
        myfile.write(text + "\n")
