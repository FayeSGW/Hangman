words = []

with open("newwords.txt") as file:
    for line in file:
        words.append(line.rstrip())

new = open("wordlist.py", "w")
for word in words:
    new.write(f"'{word}', ")
new.close()