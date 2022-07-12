
words = []

with open("words.txt") as file:
    for line in file:
        if line[0].isupper():
            pass
        elif "'" in line:
            pass
        elif len(line) < 4:
            pass
        else:
            words.append(line.rstrip())

new = open("newwords.txt", "w")
for word in words:
    new.write(word + "\n")
new.close()

