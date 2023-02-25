import random

#Find random num between 1 and six using random
#Do it 10 times
#Count how many times a number was rolled

DICE_ROLLS_REQUIRED = 10
total = [0, 0, 0, 0, 0, 0]
i = 0
while i < DICE_ROLLS_REQUIRED:
    i += 1
    roll = (random.randrange(1, 7))      ### unnecessary brackets around the random call
    total[roll-1] += 1

i = -1
while i < len(total) - 1:                ### this is better implemented with a for loop using range() to set the length. Much cleaner and you don't need a counter ... for loops give you that.
    i += 1
    if total[i] == 1:                    ### good adjustment for output
        amount = "time"
    else:
        amount = "times"
    results = "Dice rolled {}, {} {}".format(i + 1, total[i], amount)
    print(results)

