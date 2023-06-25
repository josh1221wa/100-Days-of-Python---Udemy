from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.fetch_highscore()
        self.penup()
        self.goto(x = 0, y = 280)
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(arg = f"Score : {self.score} High Score : {self.highscore}", move = False, align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.store_highscore(self.highscore)          
        self.score = 0
        self.write_score()

    def fetch_highscore(self):
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())

    def store_highscore(self, highscore):
        with open("data.txt", "w") as file:
            file.write(str(highscore))
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg = "GAME OVER", move = False, align = ALIGNMENT, font = FONT)
    
    def score_up(self):
        self.score += 1;
        self.clear()
        self.write_score()