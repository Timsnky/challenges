#Challenge : https://www.coderbyte.com/editor/guest:Scale%20Balancing:JavaScript

class WeightBalancing(object):
    def __init__(self, weightList):
        self.weightList = weightList
        self.weights = weightList[0]
        self.weightOptions = weightList[1]
        print(weightList)
        weightList[1].sort()

    def balanceWeights(self):
        difference = (self.weights[0] - self.weights[1])
        if difference == 0:
            print("Weights already balanced")
            return

        selectedWeights = self.processWeights(difference)

        if(len(selectedWeights) == 0):
            print("Not Possible")
        else:
            self.toString(selectedWeights)

    def processWeights(self, difference):
        weightOptionsCopy = self.weightOptions.copy()

        selectedWeights = []

        for weight in weightOptionsCopy:
            if weight == abs(difference):
                selectedWeights.append(weight)
                return selectedWeights

        firstNumIndex = 0

        while firstNumIndex <= len(weightOptionsCopy) - 2:
            firstWeight = weightOptionsCopy[firstNumIndex]
            innerIndex = firstNumIndex

            while innerIndex + 1 <= len(weightOptionsCopy) - 1:
                secondWeight = weightOptionsCopy[firstNumIndex + 1]

                if firstWeight - secondWeight == difference or firstWeight + secondWeight == abs(difference):
                    selectedWeights.append(firstWeight)
                    selectedWeights.append(secondWeight)
                    selectedWeights.sort()
                    return selectedWeights

                innerIndex += 1

            firstNumIndex += 1

        return selectedWeights

    def toString(self, selectedWeights):
        index = 0
        outString = ''
        while index <= len(selectedWeights) - 1:
            if(index != len(selectedWeights) - 1):
                outString += str(selectedWeights[index]) + ","
            else:
                outString += str(selectedWeights[index])
            index += 1

        print(outString)

w = WeightBalancing([[3, 4], [1, 7, 2, 7]])
w.balanceWeights()
w = WeightBalancing([[5, 9], [1, 2, 6, 7]])
w.balanceWeights()
w = WeightBalancing([[13, 4], [1, 2, 3, 6, 14]])
w.balanceWeights()