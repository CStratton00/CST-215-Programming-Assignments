import random

x = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
y = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
z = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

Cartesian = []

for i in x:
    for j in y:
        for k in z:
            Cartesian.append([i, j, k])

print(Cartesian)