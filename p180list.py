list = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
value = int(input("Enter greater than value: "))
for num in list:
    if num > value:
        print(num, end=" ")