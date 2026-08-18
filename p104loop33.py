while True:
    print("press 1 for square")
    print("press 2 for cube")
    print("press 3 for exit")
    op = int(input("enter choice:"))
    if op == 1:
        r = int(input("enter number: "))
        print(r*r)
    elif op == 2:
        r = int(input("enter number: "))
        print(r*r*r)
    elif op==3:
        print("bye")
        break
    else:
        print("invalid choice")
