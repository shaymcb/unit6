#Shaylee McBride
#10May2018
#longestDictionaryWord.py

file = open('engmix.txt')

longest = 0
for line in file:
    if len(line.strip()) > longest:
        longest = len(line.strip())
        word = line.strip()

print(word)