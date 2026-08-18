l = int(input("enter limit: "))
sum = 0
for i in range (2,l):
    if i%2==0:
        print(i, end="+")
        sum = sum + i
print("sum = ", sum)

