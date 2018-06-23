# JTSK-350111
# a3 p1.py
# Fezile Manana
# f.manana@jacobs-university.de

char = input("Enter a character: ")
asc = ord(char) #ASCII value of char

if(asc >= 97 and asc <= 122):
    print("lower case")
else:
    print("not lower case")