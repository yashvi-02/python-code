held = int(input("enter number of classes held: "))
attended = int(input("enter number of classes attended: "))
attendance = (attended/held)*100
print("your attendance is: ", attendance)
if attendance>=75:
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam")