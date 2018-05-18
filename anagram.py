#Shaylee McBride
#17May2018
#anagram.py

file = open('engmix.txt')

def count(word):
    for letter in word:
        if letter not in lists('letters'):
            lists('letters').append(letter)
            lists('counts').append(1)
        else:
            pos = letterList.index(letter)
            lists('counts')[pos] += 1


if __name__ == '__main__':
    data = {}
    lists('letters') = []
    lists('counts') = []
    
    L = []
    
    count('that')
    print(lists('counts'))
    print(lists('letters')
"""
    original = input('enter word: ')
    for line in file:
        if len(line.strip()) == len(original):
            L.append(line.strip())
    
    for word in L:
        i = 0
        for letter in letterList:
            if word.count(letter) != countList(letterList.index(letter)):
                L[i] = ''
                i += 1
    
    print(L)
     """   
