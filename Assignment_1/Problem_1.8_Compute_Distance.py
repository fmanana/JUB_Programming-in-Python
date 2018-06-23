"""
    350111
    a1_p8.py
    Fezile Manana
    f.manana@jacobs-university.de
"""

velocity = input("How fast are you going (in km/h): ")
time = input("How long does it take to get there (in hours): ")

velocity = float(velocity)
time = float(time)
print("Your destination is", velocity*time,"kilometres away")