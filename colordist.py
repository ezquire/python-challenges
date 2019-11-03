from collections import Counter
import random

'''1. create a dictionary of the colors and their counts
2. add up the weights aka counts (in this case its the size of the list)
3. pick a random number between 1 and sum of weights
4. iterate through the dictionary and subtract each item's weight from random number
5. if result is <= 0 break, select this item
6. else continue iterating and subtracting'''


def randcolor(colorlist):
    colorDict = Counter(colorlist)
    totalWeight = len(colorlist)
    num = random.randint(1, totalWeight)
    for color in colorDict:
        num -= colorDict[color]
        if num <= 0:
            return color
        


colorList = ["red", "green", "blue", "red"]
expected = Counter(colorList)
for color in expected:
    expected[color] = expected[color]/len(colorList)

actual = {"red": 0, "green": 0, "blue": 0}

for i in range(1000000):
    actual[randcolor(colorList)] += 1

for color in actual:
    actual[color] = actual[color]/1000000


print("Expected Distribution", dict(expected))
print("Actual Distribution", actual)
