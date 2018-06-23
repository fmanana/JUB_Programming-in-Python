# JTSK-350111
# a3 p7.py
# Fezile Manana
# f.manana@jacobs-university.de

ch = input("Enter a character: ")
n = input("Enter an integer: ")

n = int(n)
ch = ord(ch)

while (not (ch >= 65 and ch <= 90) or not (n >= 0 and n <= 32)):
    ch = input("Enter a character: ")
    n = input("Enter an integer: ")
    n = int(n)
    ch = ord(ch)

for i in range(0, n + 1):
    asc = chr(ch+i)
    print(asc, end = '')

print("\n")
