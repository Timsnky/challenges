# 01/05/2018
# moveFromObstacle.py
# Move a sribbler robot while check presence of
# obstacle till its free

from Myro import *
init("simulator")

#Function move from box to perform the desired actions
def moveFromBox():
    while True:
        # Check presence of obstacle before moving
        brightValues = getBright()

        # If no sensor is close to obstacle then move forward
        # Else rotate based on sensor not close to obstacle
        if min(brightValues) > 200:
            forward(1, 0.5)
        else:
            # Get the sensor not closes to an obstacle
            brightSide = brightValues.index(max(brightValues[0], brightValues[2]))

            if brightSide == 0:
                turnLeft(1, 1)
            else:
                turnRight(1, 1)
            
readLight()