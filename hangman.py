import random
import sys
from wordlist import wordlist


def main():
    print("Welcome to hangman! You get 11 guesses before the man is hanged! \nType 'stop' to quit.")

    global word_list
    global newlist
    word = str(random.choice(wordlist)).lower()
    print(word)
    word_list = list(word)
    newlist = list("_" * len(word))
    print("".join(newlist))
    
    print(remaining("-"))

    guesses = 11
    
    while guesses > 0:
        guess = input("Guess a letter: ").lower()
        if guess == "stop":
            sys.exit()
        elif guess not in word:
            guesses -=1
        

        print(play(guess))
        if play(guess) == word:
            print("You win!")
            break
        else:
            print(f"Remaining Guesses: {guesses}")
            print(remaining(guess))
        

def play(a):
    for i in range(len(word_list)):
        if word_list[i] == a:
            global newlist     
            newlist = newlist[:i] + [word_list[i]] + newlist[i+1:]
            
        else:
            newlist = newlist[:i] + [newlist[i]] + newlist[i+1:]          
    return "".join(newlist)

def remaining(l):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if l == "-":
        a = f'Remaining Letters: {"".join(letters)}'
    elif l in letters:
        ind = letters.index(l)
        letters.pop(ind)
        a = f'Remaining Letters: {"".join(letters)}'
    elif l not in letters:
        a = "You've already guessed that letter! Try again."
    return a

main()