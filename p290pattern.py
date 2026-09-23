num = int(input("enter limit: "))
for i in range(num):
    for j in range(num):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print(" ")
   