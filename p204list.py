list = [11, -44, 500, -22, -99, 77, 200, -66, 2]

for i in range(len(list)):
    if list[i] < 0:
        list[i] = 0

print(list)