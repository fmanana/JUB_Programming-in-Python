# JTSK-350111
# a3 p3.py
# Fezile Manana
# f.manana@jacobs-university.de

var = input()
var = int(var)
i = 1
while i <= var:
    if i is 1:
        print(i, "minute = ", 60*i, "seconds")
    else:
        print(i, "minutes = ", 60*i, "seconds")
    i += 1