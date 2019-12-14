# https://app.codesignal.com/challenge/Dfq9AGTczotsS9hqF

class Locksmith:
    def __init__(self, itemCount, initialState):
        self.itemCount = itemCount
        self.initialState = initialState
        self.sortedState = self.sortAndReduce()

    def sortAndReduce(self):
        return  list(set(self.initialState.copy()))

    def multiplyNumbers(self, numbers):
        newList = []

        for item in numbers:
            newList.append(item * 10)

        return  newList



    def getLowestMotion(self):
        finalDict = {}

        for item in range(0, self.itemCount):
            moves = 0
            for stateItem in self.initialState:
                if item != stateItem:
                    minValue = min([item, stateItem])
                    maxValue = max([item, stateItem])

                    backward = abs (maxValue - minValue)
                    forward = (self.itemCount - maxValue) + minValue

                    moves = moves + min([backward, forward])

            finalDict[item] = moves

        print('-------- Start ---------')
        print("Item Count " + str(self.itemCount))
        print("Initial State " + str(self.initialState))
        print("Min Moves : " + str(min(finalDict.keys(), key=(lambda k: finalDict[k]))))
        print('---------- End ---------')

# s= Locksmith(10, [1])
# s.multiplyNumbers([1, 2, 3,4,5])

# smith = Locksmith(10, [2, 7, 1])
# smith.getLowestMotion()
# smith = Locksmith(3, [2, 0, 1, 2, 0, 1, 2])
# smith.getLowestMotion()
# smith = Locksmith(4, [1, 3])
# smith.getLowestMotion()
# smith = Locksmith(10, [7, 8, 9, 3, 3])
# smith.getLowestMotion()
# smith = Locksmith(100, [97, 98, 99, 0, 1])
# smith.getLowestMotion()
# smith = Locksmith(360, [178, 104, 21, 81, 330, 353, 299, 263, 221, 199, 124, 261, 66, 204, 244, 337, 224, 84, 352, 91])
# smith.getLowestMotion()
# smith = Locksmith(360, [45, 103, 44, 107, 41, 182, 14, 53, 181, 140, 186, 271, 189, 110, 78, 208, 354, 350, 70, 231])
# smith.getLowestMotion()
# smith = Locksmith(360, [46, 308, 85, 256, 216, 255, 289, 255, 100, 328, 138, 265, 49, 83, 320, 189, 56, 293, 326, 127])
# smith.getLowestMotion()
# smith = Locksmith(3, [0, 2, 0, 0, 0, 2, 2, 2, 1, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2, 0, 0, 1, 1, 1, 1, 0, 1, 0, 2, 2, 1, 0, 1, 0, 2, 1, 2, 2, 0, 0, 1, 2, 0, 0, 2, 2, 0, 1, 1, 2, 2, 0, 0, 0, 0, 1, 2, 1, 0, 0, 1, 0, 2, 2, 2, 2, 2, 0, 2, 1, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 2, 0, 0, 2, 1, 1, 1, 2, 2, 1, 1, 1])
# smith.getLowestMotion()
# smith = Locksmith(4, [3, 3, 0, 0, 2, 1, 2, 3, 0, 0, 2, 1, 2, 0, 0, 1, 3, 0, 0, 1, 1, 1, 0, 2, 0, 1, 0, 1, 3, 2, 2, 3, 1, 3, 0, 1, 0, 3, 2, 3, 2, 0, 3, 2, 0, 1, 2, 3, 0, 3, 2, 2, 3, 2, 0, 3, 0, 1, 3, 1, 2, 0, 3, 2, 1, 0, 3, 0, 0, 1, 0, 0, 3, 3, 0, 3, 3, 2, 0, 1, 3, 2, 1, 3, 0, 0, 2, 2, 2, 2, 0, 1, 2, 0, 3, 2, 2, 3, 3, 2])
# smith.getLowestMotion()
# smith = Locksmith(5, [2, 0, 2, 0, 2, 0, 1, 3, 3, 3, 4, 2, 2, 4, 1, 3, 4, 4, 2, 0, 0, 0, 0, 3, 0, 2, 2, 1, 0, 0, 4, 3, 3, 1, 4, 4, 3, 4, 4, 2, 4, 0, 0, 2, 4, 0, 3, 1, 2, 0, 1, 2, 0, 3, 3, 2, 0, 1, 3, 1, 4, 3, 1, 1, 3, 4, 2, 2, 3, 3, 0, 2, 3, 3, 2, 1, 0, 3, 4, 3, 4, 3, 4, 0, 3, 3, 0, 1, 1, 0, 0, 2, 2, 1, 4, 2, 1, 0, 3, 3])
# smith.getLowestMotion()


