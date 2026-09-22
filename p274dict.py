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
print("failed students:")
print("name", "marks", "Result")
for student, mark in marks.items():
    if mark < 18:
        print(student, mark, "Failed")