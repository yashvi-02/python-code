l = int(input("enter limit: "))
sum = 0
for i in range (1,l+1):
    print(i*i*i, end="+")
    sum = sum + i
print("sum = ", sum)