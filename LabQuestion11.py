def recursive(x, prev, mult, y):
    if x == 1:
        return [1] + y
    
    a = prev + (mult * 2)
    y.append(a)
    return recursive(x - 1, a, mult * 2, y)

def explicit(x):
    arr = [1]
    n = 2
    for i in range(1, x):
        n = n * 2
        arr.append(n + arr[-1])

    return arr

print("Recursive\tExplicit")
print("<--------------------->")

recursiveData = recursive(20, 1, 2, [])
explicitData = explicit(20)

for x in range(0, 20):
    print(recursiveData[x], "\t\t", explicitData[x])