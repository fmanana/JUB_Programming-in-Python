# JTSK-350111
# a2 p4.py
# Fezile Manana
# f.manana@jacobs-university.de

C = input("Temperature in Celcius: ")

while(C != 'quit'):
    C = float(C)
    F = (9/5)*C + 32
    if(F < 32):
        print(F,"F (cold)")
    elif(F > 104):
        print(F, "F (hot)")
    else:
        print(F, "F")
    C = input("Temperature in Celsius: ")