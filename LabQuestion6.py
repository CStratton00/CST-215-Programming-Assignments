import random

def GCD(x, y):
    while(x != y):
        if(x > y):
            x = x - y
        elif(y > x):
            y = y - x
    return x

for i in range(1, 100):
    a = random.randint(1, 9999999)
    b = random.randint(1, 9999999)
    print(a, "  ", b, " ", GCD(a, b))