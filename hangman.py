import random
from wordlist import wordlist
from images import progress


def main():
    print("Welcome to hangman! You get 11 guesses before the man is hanged! \nType 'stop' to quit.")

    global word_list
    global newlist
    word = str(random.choice(wordlist)).lower()
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
            break      

        print(play(guess))
        if play(guess) == word:
            print("You win!")
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