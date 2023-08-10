import random
import art
import data

score = 0
gameOver = False
print(art.logo)
personA = random.choice(data.data)

while not gameOver:
    personB = random.choice(data.data)
    while personA == personB:
        personB = random.choice(data.data)

    print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}.")
    print(art.vs)
    print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}.")
    print(f"A followers: {personA['follower_count']}")
    print(f"B followers: {personB['follower_count']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #clear()
    print(art.logo)
    if data.guessCorrect(data.higher(personA, personB), guess):
        score += 1
        print(f"You're right! Current score: {score}")
        if data.higher(personA, personB) == "b":
            personA = personB
    else:
        gameOver = True
        print(f"Sorry, that's wrong. Final score: {score}")


