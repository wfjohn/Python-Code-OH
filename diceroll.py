import random

#Find random num between 1 and six using random
#Do it 10 times
#Count how many times a number was rolled

DICE_ROLLS_REQUIRED = 10
total = [0, 0, 0, 0, 0, 0]
i = 0
while i < DICE_ROLLS_REQUIRED:
    i += 1
    roll = (random.randrange(1, 7))
    total[roll-1] += 1

i = -1
while i < len(total) - 1:
    i += 1
    if total[i] == 1:
        amount = "time"
    else:
        amount = "times"
    results = "Dice rolled {}, {} {}".format(i + 1, total[i], amount)
    print(results)

