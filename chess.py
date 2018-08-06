#Challenge :  https://coderbyte.com/editor/guest:Eight%20Queens:JavaScript

import sys
import random


class Chess:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.initBoard()

    def initBoard(self):
        board = []
        row = 0

        while row < self.boardSize:
            collumn = 0
            boardRow = []
            while collumn < self.boardSize:
                boardRow.append(" ")
                collumn += 1

            board.append(boardRow)
            row += 1
        return board

    def clearBoard(self):
        for rowIndex, row in enumerate(self.board):
            for colIndex, column in enumerate(row):
                self.board[rowIndex][colIndex] = ' '

    def displayBoard(self):
        row = 0

        while row < self.boardSize * 2 + 1:
            collumn = 0
            rowString = ""

            while collumn < self.boardSize * 1:
                if (row % 2 == 0):
                    rowString += "+"
                    if (collumn < self.boardSize):
                        rowString += "---"
                else:
                    rowString += "| " + self.board[int((row - 1) / 2)][collumn] + " "

                collumn += 1

            if (row % 2 == 0):
                rowString += "+"
            else:
                rowString += "|"

            print(rowString)
            row += 1

    def underAttack(self, row, collumn):
        return len(self.checkUnderAttack(row, collumn)) != 0

    def checkUnderAttack(self, row, collumn):
        collumnIndex = 0

        while (collumnIndex < self.boardSize):
            if (self.board[row][collumnIndex] == "Q"):
                return [row, collumnIndex]

            collumnIndex += 1

        rowIndex = 0

        while (rowIndex < self.boardSize):
            if (self.board[rowIndex][collumn] == "Q"):
                return [rowIndex, collumn]

            rowIndex += 1

        rowIndex = row
        collumnIndex = collumn

        while (rowIndex >= 0 and collumnIndex < self.boardSize):
            if (self.board[rowIndex][collumnIndex] == "Q"):
                return [rowIndex, collumnIndex]

            rowIndex -= 1
            collumnIndex += 1

        rowIndex = row + 1
        collumnIndex = collumn - 1

        while (rowIndex < self.boardSize and collumnIndex >= 0):
            if (self.board[rowIndex][collumnIndex] == "Q"):
                return [rowIndex, collumnIndex]

            rowIndex += 1
            collumnIndex -= 1

        rowIndex = row
        collumnIndex = collumn

        while (rowIndex < self.boardSize and collumnIndex < self.boardSize):
            if (self.board[rowIndex][collumnIndex] == "Q"):
                return [rowIndex, collumnIndex]

            rowIndex += 1
            collumnIndex += 1

        rowIndex = row - 1
        collumnIndex = collumn - 1

        while (rowIndex >= 0 and collumnIndex >= 0):
            if (self.board[rowIndex][collumnIndex] == "Q"):
                return [rowIndex, collumnIndex]

            rowIndex -= 1
            collumnIndex -= 1

        return []

    def fillBoard(self, start=0):
        self.board[0][start] = "Q"
        self.displayBoard()
        row = 1
        attempts = 0
        forbbiddedColumn = None

        while (row < self.boardSize):
            collumn = 0
            noneFilled = True

            while (collumn < self.boardSize):
                if ((forbbiddedColumn == None
                     or (row != 0 and forbbiddedColumn < collumn)
                     or (row == 0 and (forbbiddedColumn < collumn or forbbiddedColumn == self.boardSize - 1)))
                    and not self.underAttack(row, collumn)):
                    self.board[row][collumn] = "Q"
                    noneFilled = False
                    break

                collumn += 1

            if (noneFilled):
                row -= 1
                forbbiddedColumn = self.getQueenLocation(row)
                if (row == 0):
                    attempts += 1
                if (attempts > self.boardSize):
                    raise ValueError("No viable solution")
            else:
                forbbiddedColumn = None
                row += 1

    def getQueenLocation(self, row):
        collumn = 0

        while (collumn < self.boardSize):
            if (self.board[row][collumn] == "Q"):
                self.board[row][collumn] = " "
                return collumn

            collumn += 1

        return None


c = Chess(8)
# c.fillBoard()
# c.displayBoard()

for i in range(0, c.boardSize):
    print("Simulating with Queen at position - " + str(i))
    c.fillBoard(i)
    c.displayBoard()
    c.clearBoard()
    print("Done simulating with Queen at position - " + str(i))
