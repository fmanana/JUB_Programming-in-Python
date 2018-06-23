"""
    350111
    a1_p5.py
    Fezile Manana
    f.manana@jacobs-university.de
"""

name = input("Please enter your name: ")
age = input("Please enter your age: ")

age = int(age)
print("Hi " +name, " welcome to our program.")

if(age >= 21):
    print(age, "wow that's really old!")
else:
    print("You're still young.")