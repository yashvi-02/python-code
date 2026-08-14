sugar = int(input("enter sugar level: "))
if sugar<80:
    print("sugar level is low")
elif sugar>=80 and sugar<=100:
    print("sugar level is normal")
else:
    print("sugar level is high")