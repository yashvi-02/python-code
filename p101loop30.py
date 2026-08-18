l = int(input("enter limit: "))
i = 1
while i <= l:
        if i % 2 != 0:
                print(i, "is odd")
        elif i % 2 == 0:
                print(i, "i even")
        i = i + 1