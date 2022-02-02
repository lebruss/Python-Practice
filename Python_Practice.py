#Caleb James Russell
#Python practice

import random

characterNames = ['Thomas', 'Richard', 'Patrick', 'Robert', 'Seth', 'Parker', 'Sepp', 'Arvo', 'Kreeta', 'Hans', 'Greeta', 'Peeter', 'Pierre-Luigi', 'Khan']
familyNames = ['Hansson', 'Schmitt', 'de Groot', 'Jones', 'Blatter', 'Kivisaar']
party = []
partySize = random.randint(2,5)

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

#Party roster
print("ROSTER:")
print("ID   NAME    AGE     EXP")
print(". . . . .")
for i in party:
    print (i.id, i.name, i.familyName, i.age, i.exp)


#press any key to exit
print("\n Press any key to exit")
input()