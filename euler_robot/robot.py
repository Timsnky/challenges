#Robot Movement https://projecteuler.net/problem=208
#Track Location https://math.stackexchange.com/questions/1384994/rotate-a-point-on-a-circle-with-known-radius-and-position

import math
import time

class RobotWalk:
    def __init__(self, maxMovements, movementAngle, x, y, xCenter, yCenter):
        self.maxMovement = maxMovements
        self.movementAngle = movementAngle
        self.x = x
        self.y = y
        self.xCenter = xCenter
        self.yCenter = yCenter

    def evaluateMovement(self):
        possiblePaths = 2 ** self.maxMovement
        startTime = time.time()
        index = 0
        correctPaths = 0
        wrongPaths = 0

        while index < possiblePaths:
            robot = Robot(self.movementAngle, self.x, self.y, self.xCenter, self.yCenter)
            pathList = self.getPathBinaryArray(index)

            robot = self.walkRobotOnPath(robot, pathList)

            if self.compareFinalPosition(robot.x, robot.y):
                binNum = format(index, '0' + str(self.maxMovement) + 'b')
                print(binNum)

                correctPaths = correctPaths + 1
            else:
                wrongPaths = wrongPaths + 1

            index = index + 1

        endTime = time.time()
        print("-------------- Final Verdict ------------------------------")
        print("Max Steps " + str(self.maxMovement) + " Correct Paths : " + str(correctPaths))
        print("Wrong Paths : " + str(wrongPaths))
        print("Total Paths : " + str(possiblePaths))
        print("Time Taken : " + str(endTime - startTime))
        print("-----------------------------------------------------------")

    def compareFinalPosition(self, xFinal, yFinal):
        return xFinal == self.x and yFinal == self.y

    def walkRobotOnPath(self, robot, pathList):
        previousStep = None
        stepTrace = {}
        index = 0

        for step in pathList:
            step = int(step)
            if previousStep != None and previousStep != step:
                robot.shiftRobotCenter()
            robot.moveRobot(step)
            previousStep = step
            stepTrace[index] = (robot.x, robot.y)
            index = index + 1

        return robot

    def getPathBinaryArray(self, number):
        binNum = format(number, '0' + str(self.maxMovement) + 'b')
        return list(binNum)

class Robot:
    def __init__(self, movementAngle, x, y, xCenter, yCenter):
        self.movementAngle = movementAngle
        self.x = x
        self.y = y
        self.xCenter = xCenter
        self.yCenter = yCenter

    def moveRobot(self, direction):
        if direction == 0:
            angle = self.movementAngle
        else:
            angle = - self.movementAngle

        newPoint = self.getEndPoint(self.x, self.y, self.xCenter, self.yCenter, angle)

        self.x = newPoint[0]
        self.y = newPoint[1]

    def getEndPoint(self, xStart, yStart, xCenter, yCenter, movementAngle):
        sinAngle = math.sin(math.radians(movementAngle))
        cosAngle = math.cos(math.radians(movementAngle))

        xRadius = xStart - xCenter
        yRadius = yStart - yCenter

        xEnd = xCenter + (xRadius * cosAngle) - (yRadius * sinAngle)
        yEnd = yCenter + (xRadius * sinAngle) + (yRadius * cosAngle)

        xEnd = round(xEnd, 2)
        yEnd = round(yEnd, 2)

        return [xEnd, yEnd]

    def shiftRobotCenter(self):
        newCenter = self.getEndPoint(self.xCenter, self.yCenter, self.x, self.y, 180)

        self.xCenter = newCenter[0]
        self.yCenter = newCenter[1]

robot = RobotWalk(10, 72, 1, 0, 0, 0)
robot.evaluateMovement()


