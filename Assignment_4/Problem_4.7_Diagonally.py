# JTSK-350111
# a4 p7.py
# Fezile Manana
# f.manana@jacobs-university.de

str = input("Enter a string: ")

counter = 0
for i in str:
    for j in range (counter):
        print(" ", end = "")
    print(i)
    counter += 1