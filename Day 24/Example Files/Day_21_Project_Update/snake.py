import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
    
    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle_obj = turtle.Turtle("square")
        turtle_obj.color("white")
        turtle_obj.penup()
        turtle_obj.goto(position)
        self.segments.append(turtle_obj)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)    # Make pieces disappear
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        # In this we make the segments from the back move to the position of the segment before it, and then we make the front segment move front by 20. This can be useful when turnings occur.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    