from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x = -290, y = 270)
        self.write(arg = f"Level: {self.level}", align= "left", font = FONT)
    
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(arg = f"Level: {self.level}", align= "left", font = FONT)
    
    def game_over(self):
        self.home()
        self.write(arg = "GAME OVER", align= "center", font = FONT)
