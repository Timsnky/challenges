#!/usr/bin/python

##Initilize the dictionary to store the answers from the user
answers = {}

##Get the input for the pluralNoun
answerInput = raw_input("Enter a plural noun:");
answers['pluralNoun'] = answerInput

##Get the input for the pluralNoun2
answerInput = raw_input("Enter another plural noun:");
answers['pluralNoun2'] = answerInput

##Get the input for the adjective
answerInput = raw_input("Enter an adjective:");
answers['adjective'] = answerInput

##Get the input for the noun
answerInput = raw_input("Enter a noun:");
answers['noun'] = answerInput

##Get the input for the noun2
answerInput = raw_input("Enter another noun:");
answers['noun2'] = answerInput

##Get the input for the noun3
answerInput = raw_input("Enter another noun:");
answers['noun3'] = answerInput

##Get the input for the animal
answerInput = raw_input("Enter an animal:");
answers['animal'] = answerInput

##Dislay the answers

print ("\t\t\tSPRING GARDEN\n")
print("\tPlanting a vegetable garden is not only fun,")
print("it also helps save " , answers['pluralNoun'], ". You will need a piece")
print("of " , answers['adjective'] , " land. You may need a " ,answers['noun'] ," to keep")
print("the ", answers['pluralNoun2'], " and " ,answers['noun2'], " out. As soon as")
print(answers['noun3'] , " is here you can go out there with your " , answers['animal'])
print("and plant all kinds of " , answers['pluralNoun'] , ". Then in a few")
print("months, you will hav corn on the " , answers['noun2'] , " and big,")
print(answers['adjective'] , " flowers.")
print("\t\tTHE END")