list = [11, 44, 500, 22, 99, 77, 200, 66, 2]

even = 0
odd = 0

for i in list:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)

    