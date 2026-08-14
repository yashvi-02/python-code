age = int(input("enter age: "))
gender = input("enter gender: ").lower()
if gender == "female":
    print("you have to work in urban area only")
elif gender == "male" and age>=20 and age<=40:
    print("you can work anywhere")
elif gender == "male" and age>=40 and age<=60:
    print("you can work anywhere")
else:
    print("ERROR")