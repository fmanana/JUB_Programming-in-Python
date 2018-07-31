# JTSK-350111
# a5 p7.py
# Fezile Manana
# f.manana@jacobs-university.de

lst = []
n = int(input("Add elements:\n"))

while n is not 0:
    lst.append(n)
    n = int(input())

lst.sort()
print("Max value: ", lst[-1])
print("Min value: ", lst[0])