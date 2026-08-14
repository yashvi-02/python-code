age = int(input("enter age: "))
gender = input("enter gender: ").lower()
days = int(input("enter days: "))
if age>=18 and age <= 30 and gender=="male":
    print("700 wages per day.")
elif age>=18 and age <= 30 and gender=="female":
    print("750 wages per day.")
elif age>=30 and age<= 40 and gender=="male":
    print("800 wages per day.")
elif age>=30 and age<= 40 and gender=="female":
    print("850 wages per day.")
else:
    print("other")