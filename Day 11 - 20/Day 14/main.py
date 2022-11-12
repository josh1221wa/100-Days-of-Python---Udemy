# Higher Lower Game
import art
import game_data
import random
import os

def chooseB(A):
    notequal = False

    while not notequal:
        B = random.choice(game_data.data)
        if B != A:
            notequal = True
    return B


print(art.logo)

A = random.choice(game_data.data)
B = chooseB(A)

score = 0

win = True
while win:
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}\n{art.vs}\nAgainst B: {B['name']}, a {B['description']}, from {B['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")
    if (choice in "Aa" and A['follower_count'] > B['follower_count']) or (choice in "Bb" and B['follower_count'] > A['follower_count']):
        win = True
        score += 1
        os.system('cls')
        print(art.logo)
        print(f"You're right! Current score: {score}")
        A = B

        B = chooseB(A)

    else:
        win = False
        os.system('cls')
        print(f"Sorry, that's wrong. Final score: {score}")
