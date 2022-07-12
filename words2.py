supereasy = []
easy = []
medium = []
difficult = []

with open("newwords.txt") as file:
    for line in file:
        if len(line) == 4:
            supereasy.append(line.rstrip())
        elif len(line) == 5:
            easy.append(line.rstrip())
        elif 6 <= len(line) <= 7:
            medium.append(line.rstrip())
        else:
            difficult.append(line.rstrip())

SE = open("wordlist_supereasy.py", "w")
for word in supereasy:
    SE.write(f"'{word}', ")
SE.close()

E = open("wordlist_easy.py", "w")
for word in easy:
    E.write(f"'{word}', ")
E.close()

M = open("wordlist_medium.py", "w")
for word in medium:
    M.write(F"'{word}', ")
M.close()

D = open("wordlist_difficult.py", "w")
for word in difficult:
    D.write(f"'{word}', ")
D.close()