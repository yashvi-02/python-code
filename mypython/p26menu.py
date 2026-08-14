print("press 1 for pizza")
print("press 2 for pasta")
print("press 3 for burger")
print("press 4 for fries")
print("press 5 for garlic bread")

op=int(input("enter your option: "))
if op==1:
    print("pizza price is 400")
    qty=int(input("Enter qty =>"))
    print("bill = ",qty*400)
elif op==2:
    print("pasta price is 300")
    qty=int(input("enter qty: "))
    print("bill = ",qty*300)
elif op==3:
    print("burger price is 250")
    qty=int(input("enter qty: "))
    print("bill = ", qty*250)
elif op==4:
    print("fries price is 200")
    qty=int(input("enter qty: "))
    print("bill = ", qty*200)
elif op==5:
    print("garlic bread price is 150")
    qty=int(input("enter qty: "))
    print("bill = ", qty*150)



