list = ["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]
count = 0
for x in list:
    if len(x) > 3:
        count = count + 1
print("Number of strings with length greater than 3:", count)