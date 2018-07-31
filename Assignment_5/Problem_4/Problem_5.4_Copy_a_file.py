# JTSK-350111
# a5 p4.py
# Fezile Manana
# f.manana@jacobs-university.de

filename = input("Enter a file name: ")
f = open(filename, 'r')

newfile = open("copy.txt", 'w')

text = f.read()
newfile.write(text)