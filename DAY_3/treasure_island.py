print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad,where do you want to go? Type 'Left' or 'Right'\n")
choice1_lowercase = choice1.lower()
if choice1_lowercase == "left":
    print("You've come to a lake.There is an island in the middle of the lake.Type 'Wait' to wait for a bot.Type 'Swim' to swim across.")
    choice2= input("What you want to do Swim or Wait \n")
    choice2_lowercase = choice2.lower()
    if choice2_lowercase == "wait":
        choice3_lowercase = input("You arrive at the island unharmed.There is a house with 3 doors. One REd,One Yellow, and one Blue>Which colour do you choose\n").lower()
        if choice3_lowercase == "yellow":
            print("You found the teasure! You Win..!")
        elif choice3_lowercase == "red":
            print("IT's a Room full of fire. Game Over.")
        elif choice3_lowercase == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("YOu got attacked by an angry trout.Game Over")
else:
    print("You dell into a hole.Game Over.")