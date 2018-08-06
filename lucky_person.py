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