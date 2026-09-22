students={1:"Ram", 2:"Jayul", 3:"Rahul",4:"Anjali",5:"Riya"}

marks={1:22,2:33,3:16,4:39,5:45}

print(students)
print(marks)
choice = int(input("enter your choice: "))
if choice == 1:
    print("students passed")
elif choice == 2:
    print("students failed")
elif choice == 3:
    print("both passed and failed")
else:
    print("error")
