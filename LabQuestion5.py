total = 0
number = input("Enter a integer: ")

value = int(number)
while(value > 0):
    if(value % 2 == 1):
        total += 1
    value = int(value / 2)

binary = bin(int(number))[2:]
print("(" + str(total) + ", " + str(binary) + ")")
