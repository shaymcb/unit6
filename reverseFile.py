#Shaylee McBride
#10May2018
#reverseFile.py

whichFile = input('Which File?' )
file = open(whichFile)

L=[]
for line in file:
    L.append(line.strip('\n'))

L.reverse()
for item in L:
    print(item)
    