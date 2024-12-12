odd = 0
even = 0
sum = 0

for x in range (1, 11):
     num = int(input(f"\nEnter #{x}: "))
     sum += num
if (num % 2) == 0:
     num += sum == even
     print("even")
else:
    num += sum == odd
    print("odd")

print(f"\nThe sum of all given numbers is {sum}\n")
    
