#Challenge :
# Lucky Alive Person In a Circle : Given n people standing in a circle where 1st is having sword,
#find the luckiest person in the circle, if from 1st soldier who is having a sword each have to
#kill the next soldier and handover the sword to next soldier, in turn, the soldier will kill the
#adjacent soldier and handover the sword to next soldier such that one soldier remains in this war
#who is not killed by anyone.

class LuckyPerson(object):
    def __init__(self, peopleCount):
        self.peopleCount = peopleCount
        self.peopleArray = list(range(1, self.peopleCount + 1))
        print(self.peopleArray)

    def getLuckyPerson(self):
        peopleArrayCopy = self.peopleArray.copy()

        withSword = True

        while (len(peopleArrayCopy) > 1):
            peoplArrayTemp = list()

            for person in peopleArrayCopy:
                if (withSword):
                    peoplArrayTemp.append(person)
                    withSword = False
                else:
                    withSword = True

            peopleArrayCopy = peoplArrayTemp.copy()
            print(peopleArrayCopy)

        print(peopleArrayCopy)

c = LuckyPerson(9)
c.getLuckyPerson()