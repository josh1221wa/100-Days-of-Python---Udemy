# Update the snake game - Continue from Day 21
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# We turn the tracer off to get fluid animations instead of seeing each turtle object move one-by-one. The screen will only uodate itself when we manually run an update command
screen.tracer(0)   # Turn off animations in the turtle screen

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # Make snake move
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_up()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()
    
    # Detect collision with tail
    # If head collides with any segment in tail:
        # Trigger game_over sequence
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()