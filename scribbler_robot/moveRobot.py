# 01/05/2018
# moveRobot.py
# Move a sribbler robot upto a wall the turn back


from Myro import *
init("simulator")

# Function moveRobot to do the moving
def moveRobot():
    # Record number of seconds travelled
    timeTravelled = 0

    #Move robot forward till it stalls
    while not getStall():
        forward(1, 0.1)
        timeTravelled += 1

    #Move back to allow for rotation
    backward(1, 0.25)

    #Roate for approx 180 degrees
    turnLeft(1, 5)

    #Move back to starting point
    forward(1, timeTravelled * 0.1)
      
moveRobot()