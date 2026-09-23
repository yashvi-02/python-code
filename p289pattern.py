num = int(input("enter limit: "))
for i in range(num):
    if i % 2 == 0:
        print("1" * num)
    else:
        print("0" * num)