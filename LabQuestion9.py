firstTerm = int(input("First term in the arithmetic sequence: "))
difference = int(input("Value to iterate the sequence by: "))
numberTerms = int(input("Number of terms to display: "))

for i in range(0, numberTerms):
    print(firstTerm)
    firstTerm = firstTerm + difference