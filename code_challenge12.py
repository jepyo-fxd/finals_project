for x in range (1,5):
    for a in range (5, x, -1):
        print(" ", end=" ")
    for b in range (1, x + 1):
        print("*",end=" ")
    for c in range (1, x+1):
        print("*", end=" ")
    print() 

for d in range (0,4):
    for e in range (4, 0, -1):
        print(" ", end=" ")
    for f in range (2,4):
        print("*",end=" ")
    for g in range (4,0,-1):
        print("  ",end=" ")
    print()