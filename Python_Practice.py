#Caleb James Russell
#Python practice

import random

characterNames = ['Thomas', 'Richard', 'Patrick', 'Robert', 'Seth', 'Parker', 'Sepp', 'Arvo', 'Kreeta', 'Hans', 'Greeta', 'Peeter', 'Pierre-Luigi', 'Khan', 'Tanja']
familyNames = ['Hansson', 'Schmitt', 'de Groot', 'Jones', 'Blatter', 'Kivisaar', 'Starman', 'Kebabian', 'Young']
party = []
partySize = random.randint(2,6)
#party coordinates (Party starts at 0,0)
partyX = 0
partyY = 0
partyCoords = (str(partyX) + "," + str(partyY))

#define moving
def move_forward():
    pass

class Character:
    isPlayer = 0
    exp = 0

#User
player = Character()
player.isPlayer = 1
player.name = "Leb"
player.age = 24
#player.name = str(input("What is your name?"))
#player.age = input("What is your age?")
player.id = len(party) + 1
player.familyName = random.choice(familyNames)
party.append(player)

#debug partySize
#print("Party size: " + str(partySize))

#Make NPCs
while len(party) < partySize:
    newCharacter = Character()
    newCharacter.name = random.choice(characterNames)
    newCharacter.familyName = random.choice(familyNames)
    newCharacter.age = random.randint(15,62)
    newCharacter.id = len(party) + 1
    party.append(newCharacter)




#menu
while True:
    #Party roster
    print("ROSTER:")
    print("ID\tNAME\t\tAGE\tEXP")
    print(". . . . .")
    #print character stats
    for i in party:
        print (str(i.id) + "\t" + str(i.name) + " " + str(i.familyName) + "\t" + str(i.age) + "\t" + str(i.exp))

    #print party location
    print ("Your party is current located at " + partyCoords)
    print("1. Move forward")
    print("2. Exit")
    menuChoice = input()
    if menuChoice == 1:
        move_forward()
        print("Traveling forward...\n")
    if menuChoice == 2:
        break
    else:
        continue
#press any key to exit
print("\n Press any key to exit")
input()