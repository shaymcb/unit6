#Shaylee McBride
#17May2018
#anagram.py

file = open('engmix.txt')

L = []
original = input('enter word: ')

for line in file:
    if len(line.strip()) == len(original):
        L.append(line.strip())

i = 0
while i <= len(L):
    for letter in original:
        if letter not in L[i]:
            L.remove(L[i])
            i -= 1

print(L)
    
