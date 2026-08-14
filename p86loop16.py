l = int(input("enter limit:"))
div = int(input("enter divisible: "))
count = 0
total = 0
for i in range(1,l):
    if i%div == 0:
        count += 1
        total += i
        print(i)
print("count:", count)
print("total:", total)
