import turtle
import random

turtle.TurtleScreen._RUNNING = True

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)  # Sets the screen dimensions
# Creates a window with a text input box
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -70

for color in colors:
    turtle_obj = turtle.Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(color)
    turtle_obj.goto(x, y)
    print(turtle_obj.pencolor())
    y += 30
    all_turtles.append(turtle_obj)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_obj in all_turtles:
        if turtle_obj.xcor() > 230:
            is_race_on = False

            winning_color = turtle_obj.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle_obj.forward(random_distance)

screen.bye()
