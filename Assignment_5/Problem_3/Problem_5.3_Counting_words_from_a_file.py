# JTSK-350111
# a5 p3.py
# Fezile Manana
# f.manana@jacobs-university.de

filename = input("File: ")
f = open(filename, 'r')

count = 1
for line in f:
    list = line.split()
    print("Line: ", count, "\tWord count: ", len(list))
    count += 1