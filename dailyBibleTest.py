from tkinter import *
import random

theBible = open("bible", "r")
allContent = theBible.read()
theBible.close()

megaList = allContent.split("\n")

selected = random.choice(megaList)
passage = selected.split("\t")

def createWindow():
    window = Tk()
    window.title(passage[0])
    window.geometry("900x500")

    Verse = Text(window, width = 100, font=("fixedsys", 10), bg="cyan", borderwidth = 0)
    Verse.insert('1.0', passage[0] + "\n\n" + passage[1])
    Verse.grid(row = 0, column = 0)
    
    window.configure(bg = "Cyan")
    window.mainloop()
    
createWindow()
