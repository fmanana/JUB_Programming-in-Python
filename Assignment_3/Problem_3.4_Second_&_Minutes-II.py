# JTSK-350111
# a3 p4.py
# Fezile Manana
# f.manana@jacobs-university.de

var = input()
var = int(var)

for i in range (1, var+1):
    if i is 1:
        print(i, "minute = ", 60*i, "seconds")
    else:
        print(i, "minutes = ", 60*i, "seconds")