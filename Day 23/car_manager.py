from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.movement_speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.loop_count = 0

    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        random_y = random.randint(-250, 250)
        car.goto(x = 300, y = random_y)
        self.car_list.append(car)
    
    def move_cars(self):
        for i in self.car_list:
            i.forward(self.movement_speed)
        
        for i in self.car_list:
            if i.xcor() < -320:
                self.car_list.remove(i)
                i.hideturtle()
    
    def increase_speed(self):
        self.movement_speed += MOVE_INCREMENT
