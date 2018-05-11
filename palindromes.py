#Shaylee McBride
#10May2018
#palindromes.py

file = open('engmix.txt')

def palindrome(word):
    palindrome = ""
    for i in range(-1,-1*len(word)-1,-1):
        palindrome += word[i]
    return palindrome
    
for line in file:
    if len(line.strip())>1 and line.strip()[0] == line.strip()[-1]:
        if line.strip() == palindrome(line.strip()):
            print(line.strip())
    
