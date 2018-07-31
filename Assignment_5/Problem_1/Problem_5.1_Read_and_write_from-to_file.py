# JTSK-350111
# a5 p1.py
# Fezile Manana
# f.manana@jacobs-university.de

f = open("input.txt", 'r')

for cursor in f:
    list = cursor

f.close()

product = ord(list[0]) * ord(list[1])
print(product)