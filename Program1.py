## Collin Stratton

i = 0
j = 0
k = 0

def TF(x): return "1" if(x == 1) else "0"
def aSum(x, y): return 1 if((x or y) and not((x and y))) else 0
def carry(x, y): return 1 if(x and y) else 0

## Half Adder

print("<----------------------------->")
print("|          Half Adder         |")
print("<----------------------------->")
print("|    Inputs    |    Outputs   |")
print("|___i___|___j__|_Carry_|__Sum_|")
print("|   "+TF(i)+"   |   "+TF(j)+"  |   "+TF(carry(i, j))+"   |   "+TF(aSum(i, j))+"  |")
j = 1
print("|   "+TF(i)+"   |   "+TF(j)+"  |   "+TF(carry(i, j))+"   |   "+TF(aSum(i, j))+"  |")
i = 1
j = 0
print("|   "+TF(i)+"   |   "+TF(j)+"  |   "+TF(carry(i, j))+"   |   "+TF(aSum(i, j))+"  |")
j = 1
print("|   "+TF(i)+"   |   "+TF(j)+"  |   "+TF(carry(i, j))+"   |   "+TF(aSum(i, j))+"  |")
print("<----------------------------->")

i = 0
j = 0

## Full Adder

print("<------------------------------------>")
print("|              Full Adder            |")
print("<------------------------------------>")
print("|       Inputs       |    Outputs    |")
print("|___i___|___j___|__k__|_Carry_|__Sum_|")
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 0
j = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 0
j = 0
i = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 0
j = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
k = 1
print("|   "+TF(i)+"   |   "+TF(j)+"   |  "+TF(k)+"  |   "+TF(carry(i, j)+carry(k, aSum(i, j)))+"   |   "+TF(aSum(aSum(i, j), k))+"  |")
print("<------------------------------------>")

## Parallel Adder
a = 0
b = 1
c = 1

d = 1
e = 1
f = 0

z = aSum(c, f)
y = aSum(aSum(b, e), carry(c, f))
x = aSum(aSum(a, d), carry(b, e) or carry(aSum(b, e), carry(c, f)))
w = carry(a, d) or carry(aSum(a, d), carry(b, e) or carry(aSum(b, e), carry(c, f)))

print("("+TF(w)+" "+TF(x)+" "+TF(y)+" "+TF(z)+")")