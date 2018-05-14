
file = open('engmix.txt')
"""
word = input('Enter a word: ')

inDictionary = False
for line in file:
    if word == line.strip():
        inDictionary = True
        print(word,'is in the dictionary')
        break
if inDictionary == False:
    print(word,'is not in the dictionary')
"""
"""
dictionaryList = []

for line in file:
    dictionaryList.append(line.strip())

num = int(input('Enter a number: '))
print(dictionaryList[num])
"""
"""
for line in file:
    print(line.strip()+'!')
"""

letter = input('Enter letter: ')

most = 0
for line in file:
    if line.strip().count(letter) > most:
        most = line.strip().count(letter)
        word = line.strip()
    
print(word,'has',most,letter+"'s")
    