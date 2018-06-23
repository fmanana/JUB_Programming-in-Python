# JTSK-350111
# a2 p5.py
# Fezile Manana
# f.manana@jacobs-university.de

minutes = input("Minutes: ")
minutes = int(minutes)

if(minutes < 0):
    print("Invalid input!")
else:
    hours = minutes//60
    print(hours, "hrs", minutes%60, "mins")