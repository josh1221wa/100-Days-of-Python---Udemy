# Create a snake game
from operator import imod
import turtle
import time
from Snake import Snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# We turn the tracer off to get fluid animations instead of seeing each turtle object move one-by-one. The screen will only uodate itself when we manually run an update command
screen.tracer(0)   # Turn off animations in the turtle screen

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()