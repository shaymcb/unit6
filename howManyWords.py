#Shaylee McBride
#10May18
#howManyWords - how many words of each length there are

file = open('engmix.txt')

L = [0]*21
for line in file:
    L[len(line.strip())-1] += 1


num = 1
for item in L:
    print(num,'letter words:',item)
    num += 1