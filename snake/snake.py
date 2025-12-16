from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE =20
UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            new_segments = Turtle("square")
            new_segments.color("white")
            new_segments.penup()
            new_segments.goto(position)
            self.segments.append(new_segments)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(90)
    def Down(self):
        if self.head.heading()!= UP:
            self.head.setheading(270)
    def Left(self):
        if self.head.heading()!=RIGHT :
            self.head.setheading(180)
    def Right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(0)
