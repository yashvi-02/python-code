total=0
while True:
    print("press 1 for pizza")
    print("press 2 for pasta")
    print("press 3 for burger")
    print("press 4 for pani puri")
    print("press 5 for exit")
    op = int(input("enter choice: "))
    if op == 1:
        qty = int(input("enter qty: "))
        bill = qty * 240
        total+=bill
        print("price is 240rs per pizza so your bill is: ", bill)
    elif op == 2:
        qty = int(input("enter qty: "))
        bill = qty * 300
        total+=bill
        print("price is 300rs per plate of pasta so your bill is: ", bill)
    elif op == 3:
        qty = int(input("enter qty: "))
        bill = qty * 350
        total+=bill
        print("price is 350rs per burger so your bill is: ", bill)
    elif op == 4:
        qty = int(input("enter qty: "))
        bill = qty * 30
        total+=bill
        print("price is 30rs per plate of pani puri so your bill is: ", bill)
    elif op == 5:
        grand_total = total
        print("Grand Total is:", grand_total)
        break



    

