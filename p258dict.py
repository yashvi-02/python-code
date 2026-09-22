students={1:"Ram", 2:"Jayul", 3:"Rahul",4:"Anjali",5:"Riya"}

marks={1:22,2:33,3:16,4:39,5:45}

print(students)
print(marks)

passed_students = [k for k, v in marks.items() if v > 20]
failed_students = [k for k, v in marks.items() if v <= 20]

print("Passed students count:", len(passed_students))
print("Failed students count:", len(failed_students))
    

