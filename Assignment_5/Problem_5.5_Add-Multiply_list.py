# JTSK-350111
# a5 p5.py
# Fezile Manana
# f.manana@jacobs-university.de

def add(lst, val):
    newlist = lst[:]
    for i in range(len(lst)):
        newlist[i] += val    
    return newlist

def multiply(lst, val):
    newlist = lst[:]
    for i in range(len(lst)):
        newlist[i] = newlist[i] * val
    return newlist

n = int(input("Enter an integer: "))

list_f = []
for i in range(n):
    list_f.append(float(input()))

list_1 = add(list_f, 1.5)
list_2 = multiply(list_f, 5)
print(list_f)
print(list_1)
print(list_2)