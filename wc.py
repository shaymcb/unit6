#Shaylee McBride
#16May2018
#wc.py - lines, words, characters

whatFile = input('What file: ')
file = open(whatFile)

lines = 0
words = 0
chars = 0
for line in file:
    line = line.strip()
    lines += 1
    words += line.count(' ')+1
    for word in line:
        for char in word:
            chars += 1

print(lines,words,chars)