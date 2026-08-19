def rev():
    x = int(input("enter a number: "))
    reverse = 0
    while x > 0:
        digit = x%10
        reverse = reverse * 10 + digit
        x = x // 10

    print("Reverse:", reverse)


rev()
