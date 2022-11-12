from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x = 0, y = new_y)
    
    def collision(self, car_list):
        for i in car_list:
            if self.distance(i) < 24:
                return True
    
    def cross_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
    
    def reset(self):
        self.goto(STARTING_POSITION)
