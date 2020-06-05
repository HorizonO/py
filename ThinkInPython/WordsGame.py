file = open("words.txt")
for line in file:
    word = line.strip()
    if len(word)>19:
        print(word)
