import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇
hands = [rock, paper, scissors]
aiHand = random.randint(0, len(hands)-1)

yourHand = input("Choose your hand:\n0 = Rock\n1 = Paper\n2 = Scissors: ")
yourHand = int(yourHand)
if yourHand > 2:
    print("Choose from the given")
else:
    print(f"You chose:{hands[yourHand]}")
    print(f"AI chose:{hands[aiHand]}")
    if yourHand > aiHand:
        if aiHand == 0 and yourHand == 2:
            print("You lose.")
        else:
            print("You win!")
    elif yourHand < aiHand:
        if yourHand == 0 and aiHand == 2:
            print("You win!")
        else:
            print("You lose.")
    else:
        print("Draw!")