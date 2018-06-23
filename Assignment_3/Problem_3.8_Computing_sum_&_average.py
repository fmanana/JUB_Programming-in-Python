# JTSK-350111
# a3 p8.py
# Fezile Manana
# f.manana@jacobs-university.de

arr = []
for i in range(0, 10):
    x = int(input())

    if(x == -9):
        break
    
    arr.append(x)

sum = 0
counter = 0
for i in arr:
    sum += i
    counter += 1

average = sum/counter
print("Sum:", sum)
print("Average:", average)