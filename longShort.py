#Shaylee McBride
#11May2018
#longShort.py

file = open('engmix.txt')

letters = 'abcdefghijklmnopqrstuvwxyz'
shortList = ['averrryyyyylloooonngggwoorrrrrdddddoommg']*27
longList = ['']*27

for line in file:
    if len(line.strip()) > 0:
        pos = letters.index(line.strip()[0])  #first letter position
        word = line.strip()
        
        if len(shortList[pos]) > len(word):
            shortList[pos] = word
            
        if len(longList[pos]) < len(word):
            longList[pos] = word

print(longList[10])