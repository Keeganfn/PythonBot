import random
import re
userInput = input("na")
players = re.split("/", userInput )

playerNumber = len(players)

selection = random.randint(1, playerNumber)

print(players[selection] + " has been chosen")



