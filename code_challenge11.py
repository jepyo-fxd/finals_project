for x in range (7,1,-1):
    for a in range (1, x + 1):
        print(" ", end=" ")
    for b in range (7, x, -1):
        print("*",end=" ")
    for c in range (6, x, -1):
        print("*", end=" ")
    print()

for x in range (1,7):
    for a in range (1, x +1):
        print(" ", end=" ")
    for b in range (4, x, -1):
        print("*",end=" ")
    for c in range (6, x, -1):
        print("*", end=" ")
    print()