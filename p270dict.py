marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25
}
for key, value in marks.items():
    if value < 18:
        print(key, "failed")
    else:
        print(key, "passed")
count = 0
for key, value in marks.items():
    if value < 18:
        count += 1
print("number of passed students:", len(marks) - count)
    
