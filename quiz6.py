#Shaylee McBride
#21May2018
#quiz6.py

file = open('engmix.txt')
"""
#program 1
letter = input('Enter letter: ')

for line in file:
    if line.strip().count(letter) == 4:
        print(line.strip())
"""
"""
#program 2
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break
"""
"""
#program 3
num = int(input('Enter a number: '))
letter = input('Enter a letter: ')

for line in file:
    line = line.strip()
    if len(line) == num:
        if line[0] == letter:
            print(line)
"""
"""
#program 4
L = []

for line in file:
    if len(line.strip()) >= 10:
        L.append(line.strip())

print(L[7999])
"""

#program 5
mostvowels = 0
vowelword = ''

for line in file:
    line = line.strip().lower()
    vowels = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')
    if vowels > mostvowels:
        mostvowels = vowels
        vowelword = line

print(vowelword, 'has',mostvowels,'vowels.')










