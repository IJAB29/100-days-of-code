import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {r.letter: r.code for (i, r) in data.iterrows()}


def convert():
    word = input("Enter a word: ").upper()
    try:
        wordConverted = [phonetics[let] for let in word]
    except KeyError:
        print("Sorry, letters only please.")
        convert()
    else:
        print(wordConverted)


convert()
