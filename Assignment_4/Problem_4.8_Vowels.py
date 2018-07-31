# JTSK-350111
# a4 p8.py
# Fezile Manana
# f.manana@jacobs-university.de

def count_vowels(s):
    s = s.lower()
    count = 0
    
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i ==  'o' or i == 'u':
            count += 1
    print("There are", count, "vowels in the string.")

str = input("Please enter a string: ")
count_vowels(str)