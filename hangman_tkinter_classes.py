import random
from wordlist import wordlist
from wordlist_levels import seasy_words, easy_words, med_words, diff_words
from images import progress
import tkinter as tk
from tkinter import ttk


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hangman Game")
        self.topframe = ttk.Frame(self, padding = "0 15 0 0")
        self.topframe.grid(column = 0, row = 0)
        self.buttonsframe = ttk.Frame(self, padding = "10 5 10 5")
        self.buttonsframe.grid(column = 0, row = 1)
        self.bottomframe = ttk.Frame(self, padding = "5")
        self.bottomframe.grid(column = 0, row = 2)

        #Variables
        word = str(random.choice(wordlist)).lower()
        self.word = word
        self.newlist = list("-" * len(word))
        
        self.word_list = list(word)
        guesses = 0
        self.guesses = guesses

        #Progress Images
        imgzero = tk.PhotoImage(file = r"Images\Zero.png")
        imgone = tk.PhotoImage(file = r"Images\One.png")
        imgtwo = tk.PhotoImage(file = r"Images\Two.png")
        imgthree = tk.PhotoImage(file = r"Images\Three.png")
        imgfour = tk.PhotoImage(file = r"Images\Four.png")
        imgfive = tk.PhotoImage(file = r"Images\Five.png")
        imgsix = tk.PhotoImage(file = r"Images\Six.png")
        imgseven = tk.PhotoImage(file = r"Images\Seven.png")
        imgeight = tk.PhotoImage(file = r"Images\Eight.png")
        imgnine = tk.PhotoImage(file = r"Images\Nine.png")
        imgten = tk.PhotoImage(file = r"Images\Ten.png")
        imgeleven = tk.PhotoImage(file = r"Images\Eleven.png")

        #Labels
        self.progresslbl = ttk.Label(self.topframe, image = imgzero, borderwidth = 2, relief = "ridge")
        self.worddisplaylbl = ttk.Label(self.topframe, text = f"\n{'-' * len(word)}", font = (None, 15), padding = "10")

        #Letter Buttons
        btnA = ttk.Button(self.buttonsframe, text = "A", width = 2, command = lambda letter = "A", index = 0 : self.letterchoice(letter, index))
        btnB = ttk.Button(self.buttonsframe, text = "B", width = 2, command = lambda letter = "B", index = 1: self.letterchoice(letter, index))
        btnC = ttk.Button(self.buttonsframe, text = "C", width = 2, command = lambda letter = "C", index = 2: self.letterchoice(letter, index))
        btnD = ttk.Button(self.buttonsframe, text = "D", width = 2, command = lambda letter = "D", index = 3: self.letterchoice(letter, index))
        btnE = ttk.Button(self.buttonsframe, text = "E", width = 2, command = lambda letter = "E", index = 4: self.letterchoice(letter, index))
        btnF = ttk.Button(self.buttonsframe, text = "F", width = 2, command = lambda letter = "F", index = 5: self.letterchoice(letter, index))
        btnG = ttk.Button(self.buttonsframe, text = "G", width = 2, command = lambda letter = "G", index = 6: self.letterchoice(letter, index))
        btnH = ttk.Button(self.buttonsframe, text = "H", width = 2, command = lambda letter = "H", index = 7: self.letterchoice(letter, index))
        btnI = ttk.Button(self.buttonsframe, text = "I", width = 2, command = lambda letter = "I", index = 8: self.letterchoice(letter, index))
        btnJ = ttk.Button(self.buttonsframe, text = "J", width = 2, command = lambda letter = "J", index = 9: self.letterchoice(letter, index))
        btnK = ttk.Button(self.buttonsframe, text = "K", width = 2, command = lambda letter = "K", index = 10: self.letterchoice(letter, index))
        btnL = ttk.Button(self.buttonsframe, text = "L", width = 2, command = lambda letter = "L", index = 11: self.letterchoice(letter, index))
        btnM = ttk.Button(self.buttonsframe, text = "M", width = 2, command = lambda letter = "M", index = 12: self.letterchoice(letter, index))
        btnN = ttk.Button(self.buttonsframe, text = "N", width = 2, command = lambda letter = "N", index = 13: self.letterchoice(letter, index))
        btnO = ttk.Button(self.buttonsframe, text = "O", width = 2, command = lambda letter = "O", index = 14: self.letterchoice(letter, index))
        btnP = ttk.Button(self.buttonsframe, text = "P", width = 2, command = lambda letter = "P", index = 15: self.letterchoice(letter, index))
        btnQ = ttk.Button(self.buttonsframe, text = "Q", width = 2, command = lambda letter = "Q", index = 16: self.letterchoice(letter, index))
        btnR = ttk.Button(self.buttonsframe, text = "R", width = 2, command = lambda letter = "R", index = 17: self.letterchoice(letter, index))
        btnS = ttk.Button(self.buttonsframe, text = "S", width = 2, command = lambda letter = "S", index = 18: self.letterchoice(letter, index))
        btnT = ttk.Button(self.buttonsframe, text = "T", width = 2, command = lambda letter = "T", index = 19: self.letterchoice(letter, index))
        btnU = ttk.Button(self.buttonsframe, text = "U", width = 2, command = lambda letter = "U", index = 20: self.letterchoice(letter, index))
        btnV = ttk.Button(self.buttonsframe, text = "V", width = 2, command = lambda letter = "V", index = 21: self.letterchoice(letter, index))
        btnW = ttk.Button(self.buttonsframe, text = "W", width = 2, command = lambda letter = "W", index = 22: self.letterchoice(letter, index))
        btnX = ttk.Button(self.buttonsframe, text = "X", width = 2, command = lambda letter = "X", index = 23: self.letterchoice(letter, index))
        btnY = ttk.Button(self.buttonsframe, text = "Y", width = 2, command = lambda letter = "Y", index = 24: self.letterchoice(letter, index))
        btnZ = ttk.Button(self.buttonsframe, text = "Z", width = 2, command = lambda letter = "Z", index = 25: self.letterchoice(letter, index))

        #Other Buttons
        quit = ttk.Button(self.bottomframe, text = "Give Up", command = self.giveup)
        restart = ttk.Button(self.bottomframe, text = "Play Again", command = playagain)

        #Gridding
        self.progresslbl.grid(column = 0, row = 0)
        self.worddisplaylbl.grid(column = 0, row = 1)
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

        self.imglist = [imgzero, imgone, imgtwo, imgthree, imgfour, imgfive, imgsix, imgseven, imgeight, imgnine, imgten, imgeleven]
        self.buttons = [btnA, btnB, btnC, btnD, btnE, btnF, btnG, btnH, btnI, btnJ, btnK, btnL, btnM, btnN, btnO, btnP, btnQ, btnR, btnS, btnT, btnU, btnV, btnW, btnX, btnY, btnZ]

    

        
    def letterchoice(self, letter, index):
        letter = letter.replace("\"", "").lower()
        for i in range(len(self.word_list)):
            if self.word_list[i] == letter:
                self.newlist = self.newlist[:i] + [self.word_list[i]] + self.newlist[i+1:]
            else:
                self.newlist = self.newlist
        res = "".join(self.newlist)
        print(res)
        self.worddisplaylbl.config(text = f"\n{res}")
        self.disable(index)
        self.fail(letter)
        self.wincheck(res)
        
    def wincheck(self, x):
        if x == self.word:
            self.worddisplaylbl.config(text = "\nYou win!", font = (None, 15))

    def fail(self, y):
        if y not in self.word:
            self.guesses = self.guesses + 1
            self.progresslbl.config(image = self.imglist[self.guesses])
            if self.guesses == 11:
                self.worddisplaylbl.config(text = f'Sorry, you\'re hanged! \nThe word was "{self.word}"', font = (None, 15), justify = "center")
    
    def disable(self, index):
        self.buttons[index].config(state = "disabled")

    def giveup(self):
        self.worddisplaylbl.config(text = f'You have given up! \nThe word was "{self.word}".', font = (None, 15), justify = "center")

def playagain():
    Game()
    game.mainloop
        



if __name__ == "__main__":
    game = Game()
    game.mainloop()
    