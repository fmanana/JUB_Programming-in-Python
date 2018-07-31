# JTSK-350111
# a5 p8.py
# Fezile Manana
# f.manana@jacobs-university.de

def overlapping(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
    return False

list1 = []
n = int(input("First list:\n"))
while n >= 0:
    list1.append(n)
    n = int(input())

list2 = []
m = int(input("Second list:\n"))
while m >= 0:
    list2.append(m)
    m = int(input())

if overlapping(list1, list2):
    print("The two list are overlapping.")
else:
    print("The two lists are not overlapping.")