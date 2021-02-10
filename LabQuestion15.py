import random

def handRatio(x):
    fixedRatio = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fixedPoints = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, x):
        firstDeck = []
        secondDeck = []

        firstHand = []
        secondHand = []

        for i in range(1, 53):
            firstDeck.append(i)
            secondDeck.append(i)

        for i in range(0, 52):
            val_1 = random.choice(firstDeck)
            val_2 = random.choice(secondDeck)

            firstHand.append(val_1)
            secondHand.append(val_2)

            firstDeck.remove(val_1)
            secondDeck.remove(val_2)
        
        x = 0
        for i in range(0, 52):
            if(firstHand[i] == secondHand[i]):
                x += 1
        fixedPoints[x] += 1
    for i in range(0, 9):
        fixedRatio[i] = round(fixedPoints[i] / j, 2)
    return fixedRatio

ratio100 = handRatio(100)
ratio1000 = handRatio(1000)
ratio10000 = handRatio(10000)

print("Deck of 52 cards - 100 different card selections")
print("------------------------------------------------")
print("  Fixed Pts                         Percentage  ")
for i in range(0, 10):
    print("    ", i, "\t\t\t\t      ", ratio100[i])

print("Deck of 52 cards - 1000 different card selections")
print("-------------------------------------------------")
print("  Fixed Pts                          Percentage  ")
for i in range(0, 10):
    print("    ", i, "\t\t\t\t       ", ratio1000[i])

print("Deck of 52 cards - 10000 different card selections")
print("--------------------------------------------------")
print("  Fixed Pts                           Percentage  ")
for i in range(0, 10):
    print("    ", i, "\t\t\t\t        ", ratio10000[i])