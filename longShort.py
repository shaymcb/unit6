#Shaylee McBride
#11May2018
#longShort.py

file = open('engmix.txt')

letters = 'abcdefghijklmnopqrstuvwxyz'
shortList = ['averrryyyyylloooonngggwoorrrrrdddddoommg']*27
longList = ['']*27

for line in file:
    line = line.strip()
    
    if len(line) > 0:
        firstletter = line[0].lower()
    
    if firstletter in letters:
        pos = letters.index(firstletter)  #first letter position
        word = line
        
        if len(shortList[pos]) > len(word):
            shortList[pos] = word
            
        if len(longList[pos]) < len(word):
            longList[pos] = word

for i in range(26):
    print(shortList[i],'/',longList[i])
