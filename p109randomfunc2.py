import random
num1 = random.randint(1,50)
num2 = random.randint(1,50)
sum = num1 + num2
print("num1: ", num1)
print("num2: ", num2)
usum = (int(input("sum: ")))
if usum == sum:
    print("correct")
else:
    print("wrong")
