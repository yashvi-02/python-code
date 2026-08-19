def sum():
    x =  int(input("enter digits: "))
    total = 0
    while x > 0:
        digit = x%10
        total = total + digit
        x = x // 10
    print("sum of digits: ", total)
sum()
