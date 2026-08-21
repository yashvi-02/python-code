india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = str(input("enter city: "))
if city == "mumbai" or city == "banglore" or city == "chennai" or city =="delhi" :
    print("india")
elif city == "lahore"or city == "karachi" or city == "islamabad":
    print("pakistan")
elif city == "dhaka"or city == "khulna" or city == "rangpur":
    print("bangladesh")

