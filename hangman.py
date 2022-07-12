from random_word import RandomWords
import re

r = RandomWords()

def main():
    print("Welcome to hangman! You get 11 guesses before the man is hanged!")

    global wordlist
    word = str(r.get_random_word()).lower()
    print(word)
    wordlist = list(word)
    print("_" * len(word))
    

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    guesses = 0
    global newlist
    newlist = list("_" * len(word))
    while guesses < 11:
        guess = input("Guess a letter: ").lower()
        print(play(guess))
        if guess not in word:
            guesses +=1
        print(guesses)

def play(a):
    for i in range(len(wordlist)):
        if wordlist[i] == a:
            l = a
            global newlist     
            
            newlist = newlist[:i] + [wordlist[i]] + newlist[i+1:]
        else:
            l = "_"
            newlist = newlist[:i] + [newlist[i]] + newlist[i+1:]
            
        
        
    return "".join(newlist)


main()