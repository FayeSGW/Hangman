from wordlist import wordlist
import random



def level(d):
    word = str(random.choice(wordlist)).lower()
    if d == "super easy":
        if len(word) == 3:
            return word
        else:
            level2(d)
    elif d == "easy":
        if len(word) == 4:
            return word
        else:
            level(d)
    elif d == "medium":
        if 4 <= len(word) <= 6:
            return word
        else:
            level(d)
    elif d == "difficult":
        if len(word) >= 7:
            return word
        else:
            level(d)
    else:
        return "Please input a valid level"

def level2(e):
    word = str(random.choice(wordlist)).lower()
    if e == "super easy":
        if len(word) == 3:
            return word
        else:
            level(e)

choice = input("Choose a difficulty: ").lower()
word = level(choice)
print(word)