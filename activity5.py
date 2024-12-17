print("temperature conversion")
A1 = input("\ntype, celsius or fahrenheit: ")
if A1 == "celsius":
    print("\nfahrenheit to celsius")
    A = eval(input("enter temperature in fahrenheit:"))
    B = (A - 32) * 5
    C = B / 9
    print("\nthe conversion of ,",round(A,2),"degrees fahrenheit is,",round(C,2), "degrees celsius")
elif A1 == "fahrenheit":
    print("\ncelsius to fahrenheit")
    A2 = eval(input("enter temperature in celsius: "))
    B1 = (A2 * 9) / 5 
    C1 = B1 + 32
    print("\nthe conversion of, ",round(a,2),"degrees celsius is,",round(c,2),"degrees fahrenheit")

