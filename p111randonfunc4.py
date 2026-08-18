import random
positive = 0
negative = 0
for i in range (5):
    x=random.randint(-20,20)
    print(x)
    if x > 0:
        positive = positive + 1
    elif x < 0:
        negative = negative + 1
print("number of positive number: ", positive)
print("number of negative number: ", negative)
