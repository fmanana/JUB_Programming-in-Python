# JTSK-350111
# a3 p10.py
# Fezile Manana
# f.manana@jacobs-university.de

def printing_frame(n, m, c):
    for i in range(n):
        for j in range(m):
            if(i == 0 or i == n-1):
                print(c, end = "")
            else:
                if(j == 0 or j == m-1):
                    print(c, end = "")
                else:
                    print(" ", end = "")
            
        print("")
        

print("Enter two integers then a char:")

n = int(input())
m = int(input())
c = input()

printing_frame(n, m, c)