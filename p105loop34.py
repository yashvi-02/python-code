while True:
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for multiplication")
    print("press 4 for division")
    print("press 5 for tata")
    op = int(input("enter choice: "))
    if op == 1:
        num1 = int(input("enter number 1: "))
        num2 = int(input("enter number 2:"))
        print("sum = ", num1+num2)
    elif op == 2:
        num1 = int(input("enter number 1: "))
        num2 = int(input("enter number 2:"))
        print("difference = ", num1-num2)
    elif op == 3:
        num1 = int(input("enter number 1: "))
        num2 = int(input("enter number 2:"))
        print("product = ", num1*num2)
    elif op == 4:
        num1 = int(input("enter number 1: "))
        num2 = int(input("enter number 2:"))
        print("division = ", num1/num2)
    elif op == 5:
        print("byeee")
    else:
        print("invalid choice")

