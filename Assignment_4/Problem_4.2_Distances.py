# JTSK-350111
# a4 p2.py
# Fezile Manana
# f.manana@jacobs-university.de

def convert(miles):
    km = miles * 1.609344
    if miles < 0:
        print("Invalid input")
    elif miles == 1:
        print(miles, "mile = ", km, "kilometres")
    else:
        print(miles, "miles = ", km, "kilometres")

miles = input("Enter the number of miles: ")
miles = float(miles)
convert(miles)