for x in range (6,1,-1):
    for a in range (x,1,-1):
        print(" ", end=" ")
    for b in range (x,7,1):
        print("*",end=" ")
    for c in range (x,6,1):
        print("*", end=" ")
    print()

for x in range (1,7):
    for a in range (1,x,1):
        print(" ", end=" ")
    for b in range (7, x, -1):
        print("*",end=" ")
    for c in range (6, x, -1):
        print("*", end=" ")
    print()