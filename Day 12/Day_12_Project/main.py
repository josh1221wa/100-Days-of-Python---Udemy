import random
from art import logo

def guess_number(chances, number):
    while chances>0:
        guess = int(input(f"You have {chances} attempts remaining to guess the number.\nMake a guess: "))
        if guess>number:
            print("Too high.\nGuess again.")
        elif guess<number:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {number}.")
            return
        chances-=1
    print("You've run out of guesses. You lose.")

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(0, 100)
if input("Choose a difficulty. Type 'easy' or 'hard': ")=='easy':
    chances = 10
else:
    chances = 5

guess_number(chances, number)
