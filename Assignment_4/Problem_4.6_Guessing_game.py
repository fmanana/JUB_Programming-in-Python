# JTSK-350111
# a4 p6.py
# Fezile Manana
# f.manana@jacobs-university.de

import random
random.seed()
minval = 0
maxval = 100
r = random.randint(minval, maxval)
found = False
guess = int(input("Enter your guess: "))
while not found:
    if guess == r:
        found = True
        print("Congratulations.")
    elif guess < r:
        print("Too small.")
        guess = int(input())
    else:
        print("Too big.")
        guess = int(input())