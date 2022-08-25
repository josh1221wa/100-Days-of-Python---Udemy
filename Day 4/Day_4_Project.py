import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

actions = [rock, paper, scissors]

ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
if ch>2:
    print("Invalid input. You lose.")
    exit()
print(actions[ch])

computer = random.randint(0, 2)
print("Computer chose: \n\n")
print(actions[computer])

winning = [[0, 2], [2, 1], [1, 0]]
if [ch, computer] in winning:
    print("You win!")
else:
    print("You lose!")
