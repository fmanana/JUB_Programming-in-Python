# JTSK-350111
# a3 p6.py
# Fezile Manana
# f.manana@jacobs-university.de

ch = input("Enter a character: ")
n = input("Enter an integer: ")

n = int(n)
ch = ord(ch)

for i in range(0, n + 1):
    asc = chr(ch+i)
    print(asc)