import pandas as pd

def multiplyNumbers(numbers, multiplier):
    newList = []

    for item in numbers:
        newList.append(item * multiplier)

    return newList

print(multiplyNumbers([1, 2, 3, 4], 10))
