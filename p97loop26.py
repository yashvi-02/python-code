l = int(input("enter limit: "))
sum = 0
for i in range (l,0,-1):
    print(i, end="*")
    sum = sum + i
print("sum = ", sum)