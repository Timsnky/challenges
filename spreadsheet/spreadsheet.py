def getSpreadsheetNotation(n):

    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    row = int(n / 702) + 1

    collumn = n % 702

    if collumn == 0:
        row = row - 1

    firstLetterIndex = int(collumn / 26)

    firstletterMod = collumn % 26

    firstletter = ""

    if firstletterMod == 0:
        firstletter = alphabets[25]
    elif firstLetterIndex > 0:
        firstletter = alphabets[firstLetterIndex - 1]

    secondLetterIndex = collumn % 26

    if secondLetterIndex == 0:
        secondletter = alphabets[25]
    else:
        secondletter = alphabets[secondLetterIndex - 1]

    return str(row) + firstletter + secondletter

print(getSpreadsheetNotation(27))