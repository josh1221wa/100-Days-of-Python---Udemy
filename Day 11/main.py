# Blackjack Project

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import art
import random
import os


def drawcard(user, cards):
    card = random.choice(cards)
    if card == 11 and sum(user)+11 > 21:
        card = 1
    user.append(card)


while True:
    player = []
    computer = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
        exit()
    else:
        os.system('cls')

    print(art.logo)
    for i in range(2):
        drawcard(player, cards)
        drawcard(computer, cards)

    print(f"\tYour cards: {player}, current score: {sum(player)}")
    print(f"\tComputer's first card: {computer[0]}")

    if 11 in computer and 10 in computer:
        print(f"\tYour final hand: {player}, final score: {sum(player)}")
        print(
            f"\tComputer's final hand: {computer}, final score: {sum(computer)}")

        print("Computer gets blackjack. You lose!")
        continue

    if 11 in player and 10 in player:
        print(f"\tYour final hand: {player}, final score: {sum(player)}")
        print(
            f"\tComputer's final hand: {computer}, final score: {sum(computer)}")

        print("You got a blackjack. You win!")
        continue

    pickNew = False
    if sum(player) < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        pickNew = True

    while (sum(player) < 21 and pickNew):
        pickNew = False
        player.append(random.choice(cards))
        print(f"\tYour cards: {player}, current score: {sum(player)}")
        print(f"\tComputer's first card: {computer[0]}")

        if sum(player) < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            pickNew = True

    while sum(computer) < 16:
        computer.append(random.choice(cards))

    print(f"\tYour final hand: {player}, final score: {sum(player)}")
    print(f"\tComputer's final hand: {computer}, final score: {sum(computer)}")

    if sum(player) > 21:
        print("You went over. You lose😭")
    elif sum(computer) > 21:
        print("Computer went over. You win!")
    elif sum(computer) > sum(player):
        print("You lose😢")
    elif sum(computer) == sum(player):
        print('Draw.')
    else:
        print("You win!")
