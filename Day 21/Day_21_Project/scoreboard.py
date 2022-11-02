from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 280)
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        self.write(arg = f"Score : {self.score}", move = False, align = ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER", move = False, align = ALIGNMENT, font = FONT)
    
    def score_up(self):
        self.score += 1;
        self.clear()
        self.write_score()