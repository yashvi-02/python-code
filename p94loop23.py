l = int(input("enter limit: "))
sum = 0
for i in range (1,l+1):
    if i%2==0:
        print(i*i, end="+")
    elif i%2!=0:
        print(i*i*i, end="+")
        sum = sum + i
print("sum = ", sum)