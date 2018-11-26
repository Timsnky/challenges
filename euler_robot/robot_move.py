# Robot Movement https://projecteuler.net/problem=208
# Track Location https://math.stackexchange.com/questions/1384994/rotate-a-point-on-a-circle-with-known-radius-and-position

import math
import time

class Robot:
    def __init__(self, movementAngle, x, y, xCenter, yCenter):
        """
        Initialize a robot object and define the required parameters that determine
        the starting location and motion behaviour
        :param movementAngle:
        :param x:
        :param y:
        :param xCenter:
        :param yCenter:
        """
        self.movementAngle = movementAngle
        self.x = x
        self.y = y
        self.xCenter = xCenter
        self.yCenter = yCenter

    def moveRobot(self, direction):
        """
        Move a robot a single step in a specific direction
        0 for anticlockwise and 1 for clockwise
        :param direction:
        """
        if direction == 0:
            angle = self.movementAngle
        else:
            angle = - self.movementAngle

        newPoint = self.getEndPoint(self.x, self.y, self.xCenter, self.yCenter, angle)

        self.x = newPoint[0]
        self.y = newPoint[1]

    def getEndPoint(self, xStart, yStart, xCenter, yCenter, movementAngle):
        """
        Get the next location on the robot path after it moves a single step in a specified
        angle
        :param xStart:
        :param yStart:
        :param xCenter:
        :param yCenter:
        :param movementAngle:
        :return:
        """
        sinAngle = math.sin(math.radians(movementAngle))
        cosAngle = math.cos(math.radians(movementAngle))

        xRadius = xStart - xCenter
        yRadius = yStart - yCenter

        xEnd = xCenter + (xRadius * cosAngle) - (yRadius * sinAngle)
        yEnd = yCenter + (xRadius * sinAngle) + (yRadius * cosAngle)

        xEnd = round(xEnd, 2)
        yEnd = round(yEnd, 2)

        if yEnd == 0:
            yEnd = abs(yEnd)
        if xEnd == 0:
            xEnd = abs(xEnd)

        return [xEnd, yEnd]

    def shiftRobotCenter(self):
        """
        Shift the center of motion of the robot in instances where the movement direction changes
        from clockwise to anti clockwise or the inverse
        """
        newCenter = self.getEndPoint(self.xCenter, self.yCenter, self.x, self.y, 180)

        self.xCenter = newCenter[0]
        self.yCenter = newCenter[1]


class RobotWalk:
    def __init__(self, maxMovements, movementAngle, x, y, xCenter, yCenter):
        """
        Initialize a robot walk class to perform the walking for a specified number of steps
        for a specific angle movement per step from the specified starting location and orientation
        :param maxMovements:
        :param movementAngle:
        :param x:
        :param y:
        :param xCenter:
        :param yCenter:
        """
        self.maxMovement = maxMovements
        self.movementAngle = movementAngle
        self.x = x
        self.y = y
        self.xCenter = xCenter
        self.yCenter = yCenter

    def evaluateMovement(self):
        """
        Evaluate the movement of the robot and determine the number of paths that take the robot
        back to its starting point after the set number of steps
        """
        startPoint = (self.x, self.y, self.xCenter, self.yCenter, None)
        reachedLocations = {startPoint: 1}
        startTime = time.time()

        for index in range(self.maxMovement):
            newReachedLocations = {}

            for location, ways in reachedLocations.items():
                clockwiseRobot = Robot(self.movementAngle, location[0], location[1], location[2], location[3])
                antiClockRobot = Robot(self.movementAngle, location[0], location[1], location[2], location[3])

                lastStep = location[4]

                if lastStep != None:
                    if lastStep == 0:
                        clockwiseRobot.shiftRobotCenter()

                    if lastStep == 1:
                        antiClockRobot.shiftRobotCenter()

                antiClockRobot.moveRobot(0)
                antiClockEnd = (antiClockRobot.x, antiClockRobot.y, antiClockRobot.xCenter, antiClockRobot.yCenter, 0)

                clockwiseRobot.moveRobot(1)
                clockEnd = (clockwiseRobot.x, clockwiseRobot.y, clockwiseRobot.xCenter, clockwiseRobot.yCenter, 1)

                newReachedLocations[clockEnd] = newReachedLocations.get(clockEnd, 0) + ways
                newReachedLocations[antiClockEnd] = newReachedLocations.get(antiClockEnd, 0) + ways

            reachedLocations = newReachedLocations
        paths = self.getPathCount(reachedLocations, startPoint)
        endTime = time.time()

        print("-------------- Final Verdict ------------------------------")
        print("Max Steps " + str(self.maxMovement))
        print("Correct Paths : " + str(paths))
        print("Total Ending Points : " + str(len(reachedLocations)))
        print("Time Taken : " + str(endTime - startTime))
        print("-----------------------------------------------------------")

    def getPathCount(self, reachedLocations, startPoint):
        """
        Get the count of the paths that end back to the starting point based on the final
        path locations dictionary after the movements are over
        :param reachedLocations:
        :param startPoint:
        :return:
        """
        count = 0
        for location, ways in reachedLocations.items():
            if (location[0] == startPoint[0] and location[1] == startPoint[1]):
                count = count + ways
        return count

# Evaluate the motion for a range of steps starting from 5 to 70
# We are only factoring in steps divisible by 5 since for the current
# task the other combination wont have any correct paths
for index in range(5, 70, 5):
    robot = RobotWalk(index, 72, 1, 0, 0, 0)
    robot.evaluateMovement()