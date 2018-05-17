#Shaylee McBride
#17May2018
#anagram.py

file = open('engmix.txt')

L = []
original = input('enter word: ')

for line in file:
    L.append(line.strip())

for letter in original:
    for word in L:
        if letter not in word:
            L.remove(word)

print(L)
    
