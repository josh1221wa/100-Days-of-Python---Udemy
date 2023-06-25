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

choice = input("You're at a crossroad. Do you go left or right? ").lower()
if choice == "left":
    choice = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat to come or 'swim' to swim across the lake. ").lower()

    if choice == "wait":
        choice = input(
            "You arive at the island unharmed. There is a house with 3 doors. One red, on yellow and one blue. Which color do you choose? ").lower()
        if choice == "yellow":
            print("Ypu find the treasure. You win!")
        elif choice == "red":
            print("You are burned by fire. You lose!")
        elif choice == "blue":
            print("You are eaten by beats. You lose!")
        else:
            print("You lose!")
    else:
        print("You are eaten by a trout. You lose!")
else:
    print("You fell into a hole. You lose!")
