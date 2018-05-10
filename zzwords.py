#Shaylee McBride
#9May2018
#fileDemo.py - how to read a file

file = open('engmix.txt')

for line in file:
    if 'zz' in line:
        print(line.strip()) #strip gets rid of line break


