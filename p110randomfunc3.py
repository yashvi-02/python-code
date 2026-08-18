import random
correct = 0
wrong = 0
for i in range (5):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    sum = num1 + num2
    print("num1:", num1)
    print("num2:", num2)
    usum = (int(input("sum:")))
    if usum == sum:
        print("correct")
        correct = correct + 1
    else:
        print("wrong")
        wrong = wrong + 1
print("number of correct answers: ", correct)
print("number of wrong answers: ", wrong)
