# JTSK-350111
# a5 p2.py
# Fezile Manana
# f.manana@jacobs-university.de

f = open("numbers.txt", 'r')

sum = 0
for index in f:
    sum += int(index)

print(sum)