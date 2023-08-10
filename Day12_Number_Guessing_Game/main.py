import random


def check(randNum, guessNum):
    if guessNum == randNum:
        print(f"You got it! the answer was {randNum}")
        return True
    elif 0 < guessNum < randNum:
        print("Too low.")
        return False
    elif 100 >= guessNum > randNum:
        print("Too high.")
        return False
    else:
        print("Out of the range!")
        return False
    

randomNum = random.randint(1, 100)

print("I'm thinking of a number from 1 to 100")
numTurns = input("Choose a difficulty level 'normal' for 10 turns or 'hard' for 5 turns: ")
if numTurns == "normal":
    attempts = 10
else:
    attempts = 5

gameOver = False
while not gameOver:
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    gameOver = check(randomNum, guess)
    if not gameOver and attempts == 0:
        print(f"You ran out of attempts. Game Over.\nThe number was {randomNum}")
        gameOver = True
    elif not gameOver and attempts > 0:
        print("Guess again.")
