#!/usr/bin/python

from random import *

#Function to perform bubble sort
def bubbleSort( data ):
    dataChanged = True

    while(dataChanged):

        dataChanged = False

        for index in range(len(data) - 1):

            if data[index + 1] < data[index]:
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp
                dataChanged = True

    return data

originalData = []

for x in range(0, 9):
    originalData.insert(x, randint(1, 100))

bubbleData = bubbleSort(originalData)

