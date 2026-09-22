cubes={1: 1, 2: 8, 3: 27}
cubes1={4:64, 5:125}

cubes.update(cubes1)

print(cubes)
total=0
for (k,v) in cubes.items():
    total=total+v
print(total)

