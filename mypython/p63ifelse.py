amt = int(input("enter the payable amt: "))
if amt >= 3000:
    discount = amt-500
    print("discount applied: ", discount)
else:
    print("no discount available")