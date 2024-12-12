name = input("Your name: ")
grocery = input("Do you want to buy? (yes or no): ")
if grocery.lower() == 'yes':
    print("\nTHIS IS OUR PRODUCTS: \nMILK TEA - $100 \nFRUIT SHAKE - $120 \nICE CREAM - $150")
    quanti = eval(input("\nHow many MILK TEA you want to buy? "))
    price1 = (quanti * 100)
    quanti2 = eval(input("\nHow many FRUIT SHAKE you want to buy? "))
    price2 = (quanti2 * 120)
    quanti3 = eval(input("\nHow many ICE CREAM you want to buy? "))
    price3 = (quanti3 * 150)
    total = price1 + price2 + prijefce3
    tax = round(total * 0.123)
    ttax = round(total + tax)
    id = input("\nDo you have Senior/Student/PWD ID? (yes or no): ")
    if id.lower() == 'yes': 
        discount = round(ttax * 0.052)
    else: 	
	    discount = 0
         
print(f"\nGood day {name}!, you ordered {quanti}pcs of MILK TEA, {quanti2}pcs of FRUIT SHAKE and {quanti3}pcs of ICE CREAM with a price of ${total} with 12.3% of tax with a total of ${ttax}.")
money = eval(input("\nPlease type the amount you'll give: $"))
if money >= ttax:
    change = round(money - ttax + discount)
    print(f"\n\t\t\t==RECEIPT== \nQty.     Description           Amount\n{quanti}x  ---- MILK TEA ($100) ------ ${price1} \n{quanti2}x  ---- FRUIT SHAKE ($120) ----- ${price2} \n{quanti3}x  ---- ICE CREAM ($150) --- ${price3} \n\t SUBTOTAL ------------ ${total} \n\t SALES TAX (12.3%) --- ${tax} \n\t TOTAL --------------- ${ttax} \n\t AMOUNT OF PAY ------- ${money}\n\t DISCOUNT (5.2%) ----- ${discount} \n\t CHANGE -------------- ${change} \n\t\t ==THANK YOU FOR SHOPPING!==")
else:
    money<= ttax
    print("\ninsufficient amount, please try again.\n")
      

