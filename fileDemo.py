#Shaylee McBrdie
#9May2018
#fileDemo.py - how to read a file

file = open('engmix.txt')


numWords = 0
for line in file:
    if 'shay' in line:
        print(line.strip()) #strip gets rid of line break
    numWords += 1
    
print(numWords)

