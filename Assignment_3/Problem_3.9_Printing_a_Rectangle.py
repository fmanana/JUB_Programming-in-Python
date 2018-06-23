# JTSK-350111
# a3 p9.py
# Fezile Manana
# f.manana@jacobs-university.de

def print_rectangle(n, m, c):
    for i in range(m):
        for j in range(n):
            print(c, end = "")
        print("")


print("Enter two integers then a chracter:")
n = int(input())
m = int(input())
c = input()

print_rectangle(n, m, c)
