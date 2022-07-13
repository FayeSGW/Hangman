import random
from wordlist import wordlist
from wordlist_levels import seasy_words, easy_words, med_words, diff_words
from images import progress
import sys
from tkinter import *
from tkinter import ttk

class Game(Tk):
    def __init__(self):
        super().__init__()

        #GUI window
        self.title("Hangman Game")
        self.top = ttk.Frame(self)
        self.top.grid(column = 0, row = 0)
        self.buttons = ttk.Frame(self, padding = "10 5 10 5")
        self.buttons.grid(column = 0, row = 1)
        self.bottom = ttk.Frame(self, padding = "5")
        self.bottom.grid(column = 0, row = 2)

        #Progress Images
        self.zero = PhotoImage(file = r"Images\Zero.png")
        self.one = PhotoImage(file = r"Images\One.png")
        self.two = PhotoImage(file = r"Images\Two.png")
        self.three = PhotoImage(file = r"Images\Three.png")
        self.four = PhotoImage(file = r"Images\Four.png")
        self.five = PhotoImage(file = r"Images\Five.png")
        self.six = PhotoImage(file = r"Images\Six.png")
        self.seven = PhotoImage(file = r"Images\Seven.png")
        self.eight = PhotoImage(file = r"Images\Eight.png")
        self.nine = PhotoImage(file = r"Images\Nine.png")
        self.ten = PhotoImage(file = r"Images\Ten.png")
        self.eleven = PhotoImage(file = r"Images\Eleven.png")

        #Labels
        self.progress = ttk.Label(self.top, image = self.zero, borderwidth = 2, relief = "ridge")
        self.worddisplay = ttk.Label(self.top, text = "_ _ _ _ _", font = (None, 20), padding = "10")
        
        #Letter Buttons
        self.A = Button(self.buttons, text = "A", width = 2, command = self.button_click("A"))
        self.B = Button(self.buttons, text = "B", width = 2, command = self.button_click("B"))
        self.C = Button(self.buttons, text = "C", width = 2)
        self.D = Button(self.buttons, text = "D", width = 2)
        self.E = Button(self.buttons, text = "E", width = 2)
        self.F = Button(self.buttons, text = "F", width = 2)
        self.G = Button(self.buttons, text = "G", width = 2)
        self.H = Button(self.buttons, text = "H", width = 2)
        self.I = Button(self.buttons, text = "I", width = 2)
        self.J = Button(self.buttons, text = "J", width = 2)
        self.K = Button(self.buttons, text = "K", width = 2)
        self.L = Button(self.buttons, text = "L", width = 2)
        self.M = Button(self.buttons, text = "M", width = 2)
        self.N = Button(self.buttons, text = "N", width = 2)
        self.O = Button(self.buttons, text = "O", width = 2)
        self.P = Button(self.buttons, text = "P", width = 2)
        self.Q = Button(self.buttons, text = "Q", width = 2)
        self.R = Button(self.buttons, text = "R", width = 2)
        self.S = Button(self.buttons, text = "S", width = 2)
        self.T = Button(self.buttons, text = "T", width = 2)
        self.U = Button(self.buttons, text = "U", width = 2)
        self.V = Button(self.buttons, text = "V", width = 2)
        self.W = Button(self.buttons, text = "W", width = 2)
        self.X = Button(self.buttons, text = "X", width = 2)
        self.Y = Button(self.buttons, text = "Y", width = 2)
        self.Z = Button(self.buttons, text = "Z", width = 2)

        #Other Buttons
        self.quit = Button(self.bottom, text = "Give Up")
        self.restart = Button(self.bottom, text = "Play Again")

        #Gridding
        self.progress.grid(column = 0, row = 0)
        self.worddisplay.grid(column = 0, row = 1)
        self.A.grid(column = 0, row = 0)
        self.B.grid(column = 1, row = 0)
        self.C.grid(column = 2, row = 0)
        self.D.grid(column = 3, row = 0)
        self.E.grid(column = 4, row = 0)
        self.F.grid(column = 5, row = 0)
        self.G.grid(column = 6, row = 0)
        self.H.grid(column = 7, row = 0)
        self.I.grid(column = 8, row = 0)
        self.J.grid(column = 9, row = 0)
        self.K.grid(column = 10, row = 0)
        self.L.grid(column = 11, row = 0)
        self.M.grid(column = 12, row = 0)
        self.N.grid(column = 0, row = 1)
        self.O.grid(column = 1, row = 1)
        self.P.grid(column = 2, row = 1)
        self.Q.grid(column = 3, row = 1)
        self.R.grid(column = 4, row = 1)
        self.S.grid(column = 5, row = 1)
        self.T.grid(column = 6, row = 1)
        self.U.grid(column = 7, row = 1)
        self.V.grid(column = 8, row = 1)
        self.W.grid(column = 9, row = 1)
        self.X.grid(column = 10, row = 1)
        self.Y.grid(column = 11, row = 1)
        self.Z.grid(column = 12, row = 1)
        self.quit.grid(column = 0, row = 0)
        self.restart.grid(column = 0, row = 1)

    def button_click(self, letter):
        self.worddisplay.config(text = letter)

    

if __name__ == "__main__":
    game = Game()
    game.mainloop()