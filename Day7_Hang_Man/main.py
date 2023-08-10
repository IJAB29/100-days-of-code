import art
import words
import random

randWord = random.choice(words.word_list)
randNumHints = random.randint(1, int(round(len(randWord) / 2, 0)))
hintLocList = []
for i in range(randNumHints):
    hintLocList.append(random.randint(0, len(randWord)))

health = len(art.stages) - 1
guessWord = ""
text = ""
image = art.logo

for i in range(0, len(randWord)):
    if i in hintLocList:
        guessWord += randWord[i]
    else:
        guessWord += "_"

randWord = words.addSpace(randWord)
guessWord = words.addSpace(guessWord)

print(guessWord)
print(text)
print(image)

while guessWord != randWord and health != 0:
    randWord = list(randWord)
    guessWord = list(guessWord)

    letter = input("Guess a letter: ").lower()

    if letter in randWord:
        if letter in guessWord:
            text = f"You already guessed the letter {letter}."
            for i in range(0, len(randWord)):
                if randWord[i] == letter:
                    guessWord[i] = letter
        else:
            text = ""
            for i in range(0, len(randWord)):
                if randWord[i] == letter:
                    guessWord[i] = letter
    else:
        health -= 1
        text = f"You guessed {letter}, that's not in the word. You lost a life."

    image = art.stages[health]
    randWord = "".join(randWord)
    guessWord = "".join(guessWord)

    print(guessWord)
    print(text)
    print(image)

if guessWord == randWord:
    print("YOU WIN!")
else:
    print("YOU LOSE")
    print(f"The word was {randWord.replace(' ', '')}.")
