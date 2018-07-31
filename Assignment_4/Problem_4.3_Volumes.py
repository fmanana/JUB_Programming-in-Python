# JTSK-350111
# a4 p3.py
# Fezile Manana
# f.manana@jacobs-university.de

def to_liter(gallon, cup):
    liters = (gallon*3.7854) + (cup*0.2366)
    return liters

gallon = input("Gallons: ")
cup = input("Cups: ")
gallon = float(gallon)
cup = float(cup)

result = to_liter(gallon, cup)
print("The conversion is", result, "litres")