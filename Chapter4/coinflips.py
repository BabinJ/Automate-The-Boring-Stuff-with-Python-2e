import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    outcomes = []
    for flip in range(100):
        flipVal = random.randint(0,1)
        if flipVal == 0:
            coinSide = 'H'
        else:
            coinSide = 'T'
        outcomes.append(coinSide)
    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(outcomes) - 5):
        if (outcomes[i]==outcomes[i+1]==outcomes[i+2]==outcomes[i+3]==outcomes[i+4]==outcomes[i+5]):
            numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 10000)) # Book has (number of streaks / 100), but I think /10000 makes more sense given the number of iterations