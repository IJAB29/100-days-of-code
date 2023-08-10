def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != "encode" and direction != "decode":
        print("Invalid input!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Enter your message:\n")
    shift = int(input("Enter the shift number:\n"))
    capital = input("Do you want to keep capitalization? 'yes' or 'no'\n")
    while capital != "yes" and capital != "no":
        print("Invalid input!")
        capital = input("Do you want to keep capitalization? 'yes' or 'no'\n")

    newText = ""
    shift %= 26

    if capital == "no":
        text = text.lower()
    if direction == "decode":
        shift *= -1
    for i in text:
        if ord(i) in range(97, 123):
            if ord(i) + shift >= 123:
                newCharVal = 97 + ((ord(i) + shift) - 123)
                newText += i.replace(i, chr(newCharVal))
            elif ord(i) + shift <= 96:
                newCharVal = 122 + ((ord(i) + shift) - 96)
                newText += i.replace(i, chr(newCharVal))
            else:
                newText += i.replace(i, chr(ord(i) + shift))
        elif ord(i) in range(65, 91):
            if ord(i) + shift >= 91:
                newCharVal = 65 + ((ord(i) + shift) - 91)
                newText += i.replace(i, chr(newCharVal))
            elif ord(i) + shift <= 64:
                newCharVal = 90 + ((ord(i) + shift) - 64)
                newText += i.replace(i, chr(newCharVal))
            else:
                newText += i.replace(i, chr(ord(i) + shift))
        else:
            newText += i
    print(f'The {direction}d message is "{newText}".')