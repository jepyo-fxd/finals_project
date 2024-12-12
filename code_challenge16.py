A = {}

def accs():
    x = input("enter user: ")
    if x in A:
        print("acc already exist")
        
    else:
        A[x] = 0
        print(f"account already created for {x}")
        
def main():
    while True:
        print("type new for creation of acc")
        b = input("enter a command: ")
        if b == "new":
            accs()
            

main()
