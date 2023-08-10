############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import actions
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def BlackJack(cards):
    dealerHand = actions.deal(cards)["Dealer's Hand"]
    playerHand = actions.deal(cards)["Player's Hand"]

    print(art.logo)

    hitAgain = True
    while hitAgain:
        print(f"Your cards: {playerHand}")
        print(f"Dealer's cards: {dealerHand}")
        if actions.total(playerHand) >= 21:
            actions.gameOver(cards, playerHand, dealerHand)
            hitAgain = False
        else:
            if input("Get another card? 'yes' or 'no': ") == "no":
                actions.gameOver(cards, playerHand, dealerHand)
                hitAgain = False
            else:
                actions.hit(cards, playerHand)

    if input("Do you want to play again? 'yes' or 'no': ") == "yes":
        BlackJack(cards)


BlackJack(cards)