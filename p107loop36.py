total = 0
while True:
    print("press 1 for xerox")
    print("press 2 for typing")
    print("press 3 for exit")
    op = int(input("enter choice: "))
    if op == 1:
        page = int(input("enter number of pages: "))
        if page > 50:
            bill = page * 2
            total+=bill
            print ("2rs each, total", bill)
        else:
            bill = page * 4
            total+=bill
            print ("4rs each, total", bill)
    elif op == 2:
        page = int(input("enter number of pages: "))
        if page > 50:
            bill = page * 10
            total+=bill
            print ("10rs each, total", bill)
        else:
            bill = page * 15
            total+=bill
            print ("15rs each, total", bill)
    elif op == 3:
        grand_total = total
        print("grand total is: ", total)
        break
    

        


