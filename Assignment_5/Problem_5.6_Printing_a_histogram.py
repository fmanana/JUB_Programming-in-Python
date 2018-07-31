# JTSK-350111
# a5 p6.py
# Fezile Manana
# f.manana@jacobs-university.de

def histogram(lst):
    for i in range(len(lst)):
        for j in range(lst[i]):
            print("*", end = "")
        print(sep = "\n")

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

histogram(list)