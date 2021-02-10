uInput = int(input("Enter a value for the Collaz Sequence: "))
iterations = 0

while(uInput != 1):
    if(uInput % 2 == 0):
        uInput = int(uInput/2)
        print(uInput)
        iterations = iterations + 1
    else:
        uInput = int((uInput * 3) + 1)
        print(uInput)
        iterations = iterations + 1

print("Number of iterations: ", iterations)