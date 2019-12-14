from Myro import *
init("simulator")


def readLight():
    midSensor = 1

    while True:
        #brightValues = getBright()
        brightValues = [5000, 5000, 5000]
        print(brightValues)

        if brightValues[midSensor] > 100:
            forward(1, 0.5)
        else:
            brightSide = brightValues.index(max(brightValues[0], brightValues[1]))

            if brightSide == 0:
                turnLeft(1, 0.5)
            else:
                turnRight(1, 0.5)