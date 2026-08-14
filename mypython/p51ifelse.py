year = int(input("enter number of years of service: "))
if year>5:
    salary = int(input("enter salary: "))
    print("bonus: ", salary+salary*5/100)
else:
    print("no bonus")