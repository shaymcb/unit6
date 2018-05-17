#Shaylee McBride
#17May2018
#warmup17.py

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if 'm' in line and 'c' in line and 'b' in line and 'r' in line and 'i' in line and 'd' in line and 'e' in line:
        print(line)
