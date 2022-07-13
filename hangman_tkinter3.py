import random
from wordlist import wordlist
from wordlist_levels import seasy_words, easy_words, med_words, diff_words
from images import progress
import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hangman Game")
root.top = ttk.Frame(root)
root.top.grid(column = 0, row = 0)
root.buttons = ttk.Frame(root, padding = "10 5 10 5")
root.buttons.grid(column = 0, row = 1)
root.bottom = ttk.Frame(root, padding = "5")
root.bottom.grid(column = 0, row = 2)

word = str(random.choice(wordlist)).lower()
newlist = list("-" * len(word))
word_list = list(word)


#Progress Images
imgzero = PhotoImage(file = r"Images\Zero.png")
imgone = PhotoImage(file = r"Images\One.png")
imgtwo = PhotoImage(file = r"Images\Two.png")
imgthree = PhotoImage(file = r"Images\Three.png")
imgfour = PhotoImage(file = r"Images\Four.png")
imgfive = PhotoImage(file = r"Images\Five.png")
imgsix = PhotoImage(file = r"Images\Six.png")
imgseven = PhotoImage(file = r"Images\Seven.png")
imgeight = PhotoImage(file = r"Images\Eight.png")
imgnine = PhotoImage(file = r"Images\Nine.png")
imgten = PhotoImage(file = r"Images\Ten.png")
imgeleven = PhotoImage(file = r"Images\Eleven.png")

#Labels
progresslbl = ttk.Label(root.top, image = imgzero, borderwidth = 2, relief = "ridge")
worddisplaylbl = ttk.Label(root.top, text = f"{'-' * len(word)}", font = (None, 20), padding = "10")


buttons = []
print(buttons)


def letterchoice(letter, index):
    global word_list
    letter = letter.replace("\"", "").lower()
    for i in range(len(word_list)):
        if word_list[i] == letter:
            global newlist
            newlist = newlist[:i] + [word_list[i]] + newlist[i+1:]
        else:
            newlist = newlist
    res = "".join(newlist)
    worddisplaylbl.config(text = res)
    disable(index)
    
    
   

def giveup():
    worddisplaylbl.config(text = f'You have given up! \nThe word was "{word}".', font = (None, 15), justify = CENTER)


#Letter Buttons

btnA = Button(root.buttons, text = "A", width = 2, command = lambda letter = "A", index = 0 : letterchoice(letter, index))
btnB = Button(root.buttons, text = "B", width = 2, command = lambda letter = "B", index = 1: letterchoice(letter, index))
btnC = Button(root.buttons, text = "C", width = 2, command = lambda letter = "C", index = 2: letterchoice(letter, index))
btnD = Button(root.buttons, text = "D", width = 2, command = lambda letter = "D", index = 3: letterchoice(letter, index))
btnE = Button(root.buttons, text = "E", width = 2, command = lambda letter = "E", index = 4: letterchoice(letter, index))
btnF = Button(root.buttons, text = "F", width = 2, command = lambda letter = "F", index = 5: letterchoice(letter, index))
btnG = Button(root.buttons, text = "G", width = 2, command = lambda letter = "G", index = 6: letterchoice(letter, index))
btnH = Button(root.buttons, text = "H", width = 2, command = lambda letter = "H", index = 7: letterchoice(letter, index))
btnI = Button(root.buttons, text = "I", width = 2, command = lambda letter = "I", index = 8: letterchoice(letter, index))
btnJ = Button(root.buttons, text = "J", width = 2, command = lambda letter = "J", index = 9: letterchoice(letter, index))
btnK = Button(root.buttons, text = "K", width = 2, command = lambda letter = "K", index = 10: letterchoice(letter, index))
btnL = Button(root.buttons, text = "L", width = 2, command = lambda letter = "L", index = 11: letterchoice(letter, index))
btnM = Button(root.buttons, text = "M", width = 2, command = lambda letter = "M", index = 12: letterchoice(letter, index))
btnN = Button(root.buttons, text = "N", width = 2, command = lambda letter = "N", index = 13: letterchoice(letter, index))
btnO = Button(root.buttons, text = "O", width = 2, command = lambda letter = "O", index = 14: letterchoice(letter, index))
btnP = Button(root.buttons, text = "P", width = 2, command = lambda letter = "P", index = 15: letterchoice(letter, index))
btnQ = Button(root.buttons, text = "Q", width = 2, command = lambda letter = "Q", index = 16: letterchoice(letter, index))
btnR = Button(root.buttons, text = "R", width = 2, command = lambda letter = "R", index = 17: letterchoice(letter, index))
btnS = Button(root.buttons, text = "S", width = 2, command = lambda letter = "S", index = 18: letterchoice(letter, index))
btnT = Button(root.buttons, text = "T", width = 2, command = lambda letter = "T", index = 19: letterchoice(letter, index))
btnU = Button(root.buttons, text = "U", width = 2, command = lambda letter = "U", index = 20: letterchoice(letter, index))
btnV = Button(root.buttons, text = "V", width = 2, command = lambda letter = "V", index = 21: letterchoice(letter, index))
btnW = Button(root.buttons, text = "W", width = 2, command = lambda letter = "W", index = 22: letterchoice(letter, index))
btnX = Button(root.buttons, text = "X", width = 2, command = lambda letter = "X", index = 23: letterchoice(letter, index))
btnY = Button(root.buttons, text = "Y", width = 2, command = lambda letter = "Y", index = 24: letterchoice(letter, index))
btnZ = Button(root.buttons, text = "Z", width = 2, command = lambda letter = "Z", index = 25: letterchoice(letter, index))

buttons = [btnA, btnB, btnC, btnD, btnE, btnF, btnG, btnH, btnI, btnJ, btnK, btnL, btnM, btnN, btnO, btnP, btnQ, btnR, btnS, btnT, btnU, btnV, btnW, btnX, btnY, btnZ]

def disable(index):
    buttons[index].config(state = "disabled")

#Other Buttons
quit = Button(root.bottom, text = "Give Up", command = giveup)
restart = Button(root.bottom, text = "Play Again")

#Gridding
progresslbl.grid(column = 0, row = 0)
worddisplaylbl.grid(column = 0, row = 1)
btnA.grid(column = 0, row = 0)
btnB.grid(column = 1, row = 0)
btnC.grid(column = 2, row = 0)
btnD.grid(column = 3, row = 0)
btnE.grid(column = 4, row = 0)
btnF.grid(column = 5, row = 0)
btnG.grid(column = 6, row = 0)
btnH.grid(column = 7, row = 0)
btnI.grid(column = 8, row = 0)
btnJ.grid(column = 9, row = 0)
btnK.grid(column = 10, row = 0)
btnL.grid(column = 11, row = 0)
btnM.grid(column = 12, row = 0)
btnN.grid(column = 0, row = 1)
btnO.grid(column = 1, row = 1)
btnP.grid(column = 2, row = 1)
btnQ.grid(column = 3, row = 1)
btnR.grid(column = 4, row = 1)
btnS.grid(column = 5, row = 1)
btnT.grid(column = 6, row = 1)
btnU.grid(column = 7, row = 1)
btnV.grid(column = 8, row = 1)
btnW.grid(column = 9, row = 1)
btnX.grid(column = 10, row = 1)
btnY.grid(column = 11, row = 1)
btnZ.grid(column = 12, row = 1)
quit.grid(column = 0, row = 0)
restart.grid(column = 0, row = 1)





if __name__ == "__main__":
    root.mainloop()