#Shaylee McBride
#11May2018
#fileDemo.py - how to read a file

file = open('engmix.txt')

numWords = 0
for line in file:

    if line.strip()[0]=='s' and line.strip()[-1]=='m' and len(line.strip())>0:
        print(line.strip()) #strip gets rid of line break
    numWords += 1
    
print(numWords)
