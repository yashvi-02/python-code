list = [11, 12, 15, 22, 99, 77, 200, 66, 2]
total = 0
for i in list:
    if i%3 == 0:
        total = total + i
        print("total = ", total)

    