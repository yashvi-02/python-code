marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20
}
print(marks)


print("Passed students:")
for key, student in marks.items():
	status = "Passed" if marks[key] > 20 else "Failed"
	print(student, status)