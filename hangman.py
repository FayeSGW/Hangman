import random
from wordlist import wordlist


def main():
    print("Welcome to hangman! You get 11 guesses before the man is hanged!")

    global word_list
    word = str(random.choice(wordlist)).lower()
    print(word)
    word_list = list(word)
    print("_" * len(word))
    
    global letters
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters2 = "".join(letters)
    print(f"Remaining Letters: {letters2}")

    guesses = 11
    global newlist
    newlist = list("_" * len(word))
    while guesses > 0:
        guess = input("Guess a letter: ").lower()
        print(play(guess))
        if guess not in word:
            guesses -=1
        print(f"Remaining Guesses: {guesses}")
        print(f"Remaining Letters: {remaining(guess)}")
        

def play(a):
    for i in range(len(word_list)):
        if word_list[i] == a:
            global newlist     
            newlist = newlist[:i] + [word_list[i]] + newlist[i+1:]
            
        else:
            newlist = newlist[:i] + [newlist[i]] + newlist[i+1:]          
    return "".join(newlist)

def remaining(l):
    if l in letters:
        ind = letters.index(l)
        letters.pop(ind)
        a = "".join(letters)
    return a

main()