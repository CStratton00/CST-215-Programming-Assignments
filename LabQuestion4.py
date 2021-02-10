A = True
B = True

def APT(): return "T" if(A == True) else "F"
def BPT(): return "T" if(B == True) else "F"
def abAND(): return "T" if(A and B) else "F"
def abOR(): return "T" if(A or B) else "F"
def abNAND(): return "T" if(not(A and B)) else "F"
def abNOR(): return "T" if(not(A or B)) else "F"
def abXOR(): return "T" if(A != B) else "F"
def aNOT(): return "T" if(not(A)) else "F"

print("<----------------------------->")
print("|           And Gate          |")
print("<----------------------------->")
print("| A = " + APT() + ", B = " + BPT() + " | A and B =  " + abAND() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A and B =  " + abAND() + " |")
A = False
B = True
print("| A = " + APT() + ", B = " + BPT() + " | A and B =  " + abAND() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A and B =  " + abAND() + " |")
print("<----------------------------->")

A = True
B = True

print("<----------------------------->")
print("|           OR Gate           |")
print("<----------------------------->")
print("| A = " + APT() + ", B = " + BPT() + " | A or B =   " + abOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A or B =   " + abOR() + " |")
A = False
B = True
print("| A = " + APT() + ", B = " + BPT() + " | A or B =   " + abOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A or B =   " + abOR() + " |")
print("<----------------------------->")

A = True
B = True

print("<----------------------------->")
print("|          NAND Gate          |")
print("<----------------------------->")
print("| A = " + APT() + ", B = " + BPT() + " | A nand B = " + abNAND() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A nand B = " + abNAND() + " |")
A = False
B = True
print("| A = " + APT() + ", B = " + BPT() + " | A nand B = " + abNAND() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A nand B = " + abNAND() + " |")
print("<----------------------------->")

A = True
B = True

print("<----------------------------->")
print("|           NOR Gate          |")
print("<----------------------------->")
print("| A = " + APT() + ", B = " + BPT() + " | A nor B =  " + abNOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A nor B =  " + abNOR() + " |")
A = False
B = True
print("| A = " + APT() + ", B = " + BPT() + " | A nor B =  " + abNOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A nor B =  " + abNOR() + " |")
print("<----------------------------->")

A = True
B = True

print("<----------------------------->")
print("|           XOR Gate         |")
print("<----------------------------->")
print("| A = " + APT() + ", B = " + BPT() + " | A xor B =  " + abXOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A xor B =  " + abXOR() + " |")
A = False
B = True
print("| A = " + APT() + ", B = " + BPT() + " | A xor B =  " + abXOR() + " |")
B = False
print("| A = " + APT() + ", B = " + BPT() + " | A xor B =  " + abXOR() + " |")
print("<----------------------------->")

A = True

print("<----------------->")
print("|     Not Gate    |")
print("<----------------->")
print("| A = " + APT() + " | A' =  " + aNOT() + " |")
A = False
print("| A = " + APT() + " | A' =  " + aNOT() + " |")
print("<----------------->")