#merchant game
#caleb james russell
#march 11 2023

'''
you are a merchant who buys and sells things
player has money
player has a mode of transportation, which can be upgraded
there are different cities
each city has a market where you buy and sell things
different cities will have different prices for each item
You gotta make money
Maybe sometimes, an item will not be available in a city. It will then be valuable
Maybe there will be pirates who attack you while traveling
Hmm
'''

import time
import random
import os

#function: clear the terminal screen
def blankScreen():
    os.system('cls||clear')

name = input('What is your name?')

#literal string interpolation
print(f"Hello, {name}. Welcome to being a merchant")
input()
blankScreen()

currentCity = "Tallinn"

#menu functions
def inventory():
    blankScreen()
    print("Inventory")
    input()

#main menu
while True:
    blankScreen()
    print(f"1. Current city: {currentCity}")
    print(f"2. Visit market")
    print(f"3. Travel")
    print(f"4. Rest")
    print(f"5. Inventory")
    input = input()
    if input == "5":
        inventory()