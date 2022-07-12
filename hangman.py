import random
from wordlist import wordlist
from wordlist_levels import seasy_words, easy_words, med_words, diff_words
from images import progress


def main():
    print("Welcome to hangman! You get 11 guesses before the man is hanged! \nType 'stop' to quit.")
    print("Difficulty options: \nSuper Easy (SE): words 3 letters long \nEasy (E): words 4 letters long \nMedium (M): words 5-6 letters long \nDifficult (D): words >6 letters long \nRandom (R): words random length")
    
    levels = ["super easy", "easy", "medium", "difficult", "random", "se", "e", "m", "d", "r"]
    
    while True:
        choice = input("Choose a difficulty: ").lower()
        if choice in levels:
            word = level(choice)
            break
        else:
            print("Please input a valid difficulty")
            continue
    
    global word_list
    global newlist
    word_list = list(word)
    newlist = list("_" * len(word))
    print("".join(newlist))
    
    global letters
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(f"Remaining Letters: {''.join(letters)}")

    guesses = 11
    
    while guesses >= 0:
        guess = input("Guess a letter: ").lower()
        if guess == "stop":
            print(f"You have given up! The word was: {word}")
            break      

        print(play(guess))
        if play(guess) == word:
            print("Congratulations, you win!")
            break
        else:
            if guess not in letters: 
                print(f"You've already guessed that letter! Try again. \nRemaining Letters: {remaining(guess)}")
            elif guess in letters and guess in word:
                print(f"Remaining Letters: {remaining(guess)}")
            elif guess not in word:
                guesses -= 1
                if guesses == 0:
                    print(f"{hanging(guesses)} \nSorry, you lose! \nThe word was: {word}")
                    break
                else:
                    print(f"Nope, no {guess}! \nRemaining Guesses: {guesses}")
                    print(hanging(guesses))
                    print(f"Remaining Letters: {remaining(guess)}")

def level(d):
    if d == "super easy" or d == "se":
        return str(random.choice(seasy_words)).lower()
    elif d == "easy" or d == "e":
        return str(random.choice(easy_words)).lower()
    elif d == "medium" or d == "m":
        return str(random.choice(med_words)).lower()
    elif d == "difficult" or d == "d":
        return str(random.choice(diff_words)).lower()
    elif d == "random" or d == "r":
        return str(random.choice(wordlist)).lower()
    
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
        return "".join(letters)
    else:
        return "".join(letters)

def hanging(x):
    image = progress[x]
    return image
    
main()