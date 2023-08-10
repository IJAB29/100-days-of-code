import os
import art

clear = lambda: os.system('cls')
clear()


def bidInput():
    name = input("What is your name? ")
    amount = int(input("What is your bid? $"))
    bids[name] = amount
    return bids


def highestBid(a):
    highestAmt = 0
    for key, value in a.items():
        if value > highestAmt:
            highestAmt = value
            highestBidder = {key: highestAmt}
    return highestBidder


bids = {}
print(art.logo)
print("Welcome to the secret auction program.")
goAgain = True
while goAgain:
    bidInput()
    bidAgain = input("Are there any other bidders? 'yes' or 'no'\n").lower()
    while bidAgain != "yes" and bidAgain != "no":
        print("Invalid input!")
        bidAgain = input("Are there any other bidders? 'yes' or 'no'\n").lower()
    if bidAgain == "yes":
        clear()
    else:
        goAgain = False
        for key, value in highestBid(bids).items():
            print(f"The winner is {key} with a bid of ${value}.")
