# JTSK-350111
# a4 p5.py
# Fezile Manana
# f.manana@jacobs-university.de

from math import pi

def volume(r):
    volume = 4/3 * pi * r*r*r
    return volume
    
r = input("Radius: ")
r = float(r)
result = volume(r)
print("The volume of your circle is", result)