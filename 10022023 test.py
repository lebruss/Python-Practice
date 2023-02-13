import os
import random
import time

#clear the terminal screen (Operating System-agnostic)
def blankScreen():
    os.system('cls||clear')

#Menu
while True:
    blankScreen()
    print("1. People")
    def menu1():
        blankScreen()
        print("Menu option 1")
        input()
    choice = input()
    if choice == "1":
        menu1()
