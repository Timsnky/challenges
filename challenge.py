def getUniqueChars(firstString):
    firstStringList = []

    for char in firstString:
        if char not in firstStringList:
            firstStringList.append(char)

    return firstStringList

def compare(firstString, secondString):

    firstSet = list(firstString)
    firstSet.sort()

    secondSet = list(secondString)
    secondSet.sort()

    return  firstSet == secondSet

def armstrong(a):
    aList = list(a)

    aSum = 0
    for char in aList:
        aSum = aSum + (int(char) ** 3)

    if aSum == a:
        print("It is an ARMSTRONG number")
    else:
        print("It is NOT an ARMSTRONG number")





# print(compare("AAB", "ABB"))
# print(compare("BAC", "ABC"))
# print(compare("AABC", "BAC"))

armstrong(153)








