l = int(input("enter limit: "))
sum = 0
for i in range (0,l):
    print(i, end="*")
    sum = sum + i
print("sum = ",sum)