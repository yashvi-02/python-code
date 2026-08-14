balance = int(input("enter your balance: "))
withdrawal = int(input("enter withdrawal amount: "))
if withdrawal<=balance:
    print("withdrawal successful")
    print("remaining balance: ", balance-withdrawal)
else:
    print("insufficient balance")