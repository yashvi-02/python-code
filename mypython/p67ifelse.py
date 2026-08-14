print("press 1 for battery based toys.")
print("press 2 for key based toys.")
print("press 3 for electric-charing based toys.")
choice = int(input("enter your choice: "))
price = int(input("enter price of toy: "))
if choice ==1 and price >= 1000:
    discount = price-price*0.1
    print("total amt to pay after discount: ", discount)
elif choice ==2 and price >= 100:
    discount = price-price*0.05
    print("total amt to pay after discount: ", discount)
elif choice ==3 and price >= 500:
    discount = price-price*0.1
    print("total amt to pay after discount: ", discount)
else:
    print("no discount available")