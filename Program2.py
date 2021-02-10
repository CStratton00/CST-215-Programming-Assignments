import random

def GCD(x, y):
    while x != y:
        if x > y:
            x = x - y
        elif y > x:
            y = y - x
    return x

def Euclidian(a, b):
    x = 1
    y = 0
    
    x1 = 0
    y1 = 1

    aNew = a
    bNew = b

    while(bNew != 0):
        q = aNew // bNew

        holdA = aNew
        x2 = x
        y2 = y

        aNew = bNew
        x = x1
        y = y1

        bNew = holdA % bNew
        x1 = x2 - q * x1
        y1 = y2 - q * y1

    return f'{a} * ({x}) + {b}*({y}) = {aNew}'


for i in range(0, 100):
    x = random.randint(1, 999)
    y = random.randint(1, 999)

    if(GCD(x, y) == 1):
        if(x > y):
            print(str(x) + "\t" + str(y) + "\t" + str(GCD(x, y)) + "\t" + str(Euclidian(x, y)))
        else :
            print(str(y) + "\t" + str(x) + "\t" + str(GCD(y, x)) + "\t" + str(Euclidian(y, x)))
    else:
        if(x > y):
            print(str(x) + "\t" + str(y) + "\t" + str(GCD(x, y)))
        else:
            print(str(y) + "\t" + str(x) + "\t" + str(GCD(y, x)))
