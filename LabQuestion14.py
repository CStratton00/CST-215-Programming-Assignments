import random

def handRatio(x):
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
    return fixedPoints

print(handRatio(10))