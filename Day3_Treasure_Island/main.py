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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
decision1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
if decision1.lower() == "left":
    decision2 = input("You come into a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across\n")
    if decision2.lower() == "wait":
        decision3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n")
        if decision3.lower() == "red":
            print("You were eaten by a monster disguised as the door.\nGame over.")
        elif decision3.lower() == "yellow":
            print("You have obtained the treasure.\nYou win!")
        elif decision3.lower() == "blue":
            print("As you entered, you stepped on a trap and exploded.\nGame over.")
        else:
            print("You were idle for too long and was attacked by wild beasts.\nGame over.")
    elif decision2.lower() == "swim":
        print("You were attacked by a shark.\nGame over.")
    else:
        print("You were idle for too long and was attacked by wild beasts.\nGame over.")
elif decision1.lower() == "right":
    print("You fell into a hole.\nGame over.")
else:
    print("You were idle for too long and was attacked by wild beasts.\nGame over.")