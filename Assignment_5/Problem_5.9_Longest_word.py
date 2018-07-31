# JTSK-350111
# a5 p9.py
# Fezile Manana
# f.manana@jacobs-university.de

def longest_word(lst):
    longest = -1
    for word in lst:
        if len(word) > longest:
            longest = len(word)
    print(longest)

text = input()
w_list = text.split()

longest_word(w_list)