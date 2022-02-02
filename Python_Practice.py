#Caleb James Russell
#Python practice

import random

characterNames = ['Thomas', 'Richard', 'Patrick', 'Robert', 'Seth', 'Parker', 'Sepp', 'Arvo', 'Kreeta', 'Hans']
party = []


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
party.append(player)

#Make NPC
newCharacter = Character()
newCharacter.name = random.choice(characterNames)
newCharacter.age = random.randint(15,62)
newCharacter.id = len(party) + 1
party.append(newCharacter)

#Party roster
print("ROSTER:")

print("ID   NAME    AGE     EXP")
print(". . . . .")
for i in party:
    print (i.id, i.name, i.age, i.exp)