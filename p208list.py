list= [11, 44, 500, 22, 99, 77]
even = []
odd = []
for i in range(len(list)):
    if i % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("Even indices:", even)
print("Odd indices:", odd)
