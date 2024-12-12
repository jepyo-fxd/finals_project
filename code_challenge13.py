for x in range (1,7):
    for a in range (6, x, -1):
        print(" ",end=" ")
    for a in range (x, 1, -1):
        print(a,end=" ")
    for b in range (1, x+1):
        print(b,end=" ")
    print() 

for x in range (5,0,-1):
    for a in range (6, x, -1):
        print(" ",end=" ")
    for a in range (x, 1 , -1):
        print(a,end=" ")
    for g in range (1,x+1):
        print(a,end=" ")
    print()