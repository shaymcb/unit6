#Shaylee McBride
#11May2018
#longShort.py

file = open('engmix.txt')

letters = 'abcdefghijklmnopqrstuvwxyz'
shortList = ['thiswouldbeaverylongshortestword']*26 #store a long word for all 26 letters
longList = ['']*26

for line in file:
    line = line.strip()
    
    if len(line) > 0:
        firstletter = line[0].lower() #safety
    
    if firstletter in letters: #safety
        pos = letters.index(firstletter)  #first letter position in letter list
        
        if len(shortList[pos]) > len(line):  #if word in list right now for letter longer than this word, replace it
            shortList[pos] = line
            
        if len(longList[pos]) < len(line):
            longList[pos] = line

for i in range(26):
    print(shortList[i],'/',longList[i])
