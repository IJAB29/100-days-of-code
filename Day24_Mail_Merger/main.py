def readTexts(locLetter, locNames):
    with open(locLetter) as file:
        letter = file.read()

    with open(locNames) as file:
        names = file.read()
        names = names.split("\n")
    dic = {"names": names, "letter": letter}
    return dic


def writeLetters(textFiles, locOutput):
    for invitee in textFiles["names"]:
        with open(f"{locOutput}/{invitee}_letter.txt", "w") as file:
            file.write(textFiles["letter"].replace("[name]", invitee))


inputs = readTexts(locLetter="./Input/Letters/starting_letter.txt", locNames="./Input/Names/invited_names.txt")
writeLetters(inputs, locOutput="/Users/USER/PycharmProjects/Day24_Mail_Merger/Output/ReadyToSend")
